# Domain Knowledge - SPSS to Python Analysis Equivalents

**Domain**: STATISTICAL ANALYSIS - SPSS TO PYTHON EQUIVALENTS
**Created**: July 24, 2025
**Last Updated**: July 24, 2025
**Learning Status**: Expert
**Complexity Level**: Advanced

## Learning Objectives

**Primary Goals**:
- [x] Master Python equivalents for all major SPSS statistical procedures
- [x] Implement comprehensive survey analysis workflows in Python
- [x] Develop expertise in psychometric analysis and scale validation
- [x] Execute structural equation modeling and advanced multivariate techniques

**Success Criteria**:
- [x] Can perform complete customer satisfaction survey analysis equivalent to SPSS
- [x] Can validate measurement scales and assess reliability/validity
- [x] Can conduct factor analysis, SEM, and path analysis
- [x] Can generate publication-ready statistical reports

## Core Concepts

**Fundamental Principles**:
1. **SPSS Data Structure**: SPSS uses variable view with metadata (labels, types, measures) - Python equivalent using pandas with categorical data and metadata dictionaries
2. **Variable Types**: Scale (continuous), Ordinal (ordered categorical), Nominal (categorical) - map to pandas numeric, categorical ordered, and categorical
3. **Missing Value Handling**: SPSS system missing vs user-defined missing - Python NaN handling with custom missing value codes
4. **Syntax vs Code**: SPSS syntax commands translate to Python function calls with similar parameter structures

**Key Terminology**:
- **Scale Variables**: Continuous numeric variables (interval/ratio) - use pandas numeric dtypes
- **Ordinal Variables**: Ordered categories - use pandas Categorical with ordered=True
- **Nominal Variables**: Unordered categories - use pandas Categorical with ordered=False
- **Value Labels**: Text descriptions for numeric codes - use pandas category names or mapping dictionaries
- **Variable Labels**: Descriptive names for variables - store in pandas attrs or separate metadata dict

## SPSS Procedures to Python Library Mapping

### Data Management and Descriptive Statistics

| SPSS Procedure | Python Libraries | Key Functions | Notes |
|----------------|------------------|---------------|--------|
| `DESCRIPTIVES` | pandas, scipy.stats | `df.describe()`, `scipy.stats.describe()` | Enhanced with confidence intervals |
| `FREQUENCIES` | pandas | `df.value_counts()`, `pd.crosstab()` | Include missing value reporting |
| `CROSSTABS` | pandas, scipy.stats | `pd.crosstab()`, `scipy.stats.chi2_contingency()` | Add effect size measures |
| `EXAMINE` | pandas, scipy.stats, matplotlib | `df.describe()`, `plt.boxplot()`, normality tests | Comprehensive exploratory analysis |
| `RECODE` | pandas | `df.replace()`, `pd.cut()`, `np.where()` | Preserve original for audit trail |
| `COMPUTE` | pandas, numpy | `df.assign()`, `np.where()`, `df.eval()` | Document transformation logic |

### Reliability and Scale Analysis

| SPSS Procedure | Python Libraries | Key Functions | Notes |
|----------------|------------------|---------------|--------|
| `RELIABILITY` | pandas, numpy, factor_analyzer | Custom Cronbach's alpha function | Include item-total correlations |
| `FACTOR` | factor_analyzer, sklearn | `FactorAnalyzer()`, `PCA()` | Multiple extraction methods |
| `CLUSTER` | sklearn, scipy.cluster | `KMeans()`, `AgglomerativeClustering()` | Hierarchical and k-means |

### Statistical Tests

| SPSS Procedure | Python Libraries | Key Functions | Notes |
|----------------|------------------|---------------|--------|
| `T-TEST` | scipy.stats | `scipy.stats.ttest_1samp()`, `ttest_ind()`, `ttest_rel()` | Include effect sizes |
| `ONEWAY` | scipy.stats | `scipy.stats.f_oneway()`, `scipy.stats.kruskal()` | Post-hoc tests available |
| `GLM` / `UNIANOVA` | statsmodels | `statsmodels.formula.api.ols()` | Full ANOVA with interactions |
| `REGRESSION` | statsmodels, sklearn | `statsmodels.api.OLS()` | Include diagnostics |
| `LOGISTIC` | statsmodels, sklearn | `statsmodels.api.Logit()` | Include classification metrics |
| `NPAR TESTS` | scipy.stats | Various non-parametric tests | Mann-Whitney, Wilcoxon, etc. |

### Advanced Multivariate Analysis

| SPSS Procedure | Python Libraries | Key Functions | Notes |
|----------------|------------------|---------------|--------|
| `MANOVA` | statsmodels | `statsmodels.multivariate.manova.MANOVA()` | Limited but functional |
| `DISCRIMINANT` | sklearn | `LinearDiscriminantAnalysis()` | Include classification accuracy |
| `CORRELATIONS` | pandas, scipy.stats | `df.corr()`, `scipy.stats.pearsonr()` | Include significance tests |
| `PARTIAL CORR` | pingouin | `pingouin.partial_corr()` | Control for confounding variables |

## Essential Python Libraries for SPSS Equivalency

### Core Statistical Libraries
```python
import pandas as pd              # Data manipulation (SPSS Data View equivalent)
import numpy as np               # Numerical operations
import scipy.stats as stats      # Statistical tests and distributions
import statsmodels.api as sm     # Advanced statistical modeling
import statsmodels.formula.api as smf  # R-style formula interface
```

### Specialized Libraries
```python
import factor_analyzer           # Factor analysis and reliability
import pingouin as pg           # Advanced statistical functions
import scikit-learn             # Machine learning and clustering
import seaborn as sns           # Statistical visualization
import matplotlib.pyplot as plt # Base plotting
import pyreadstat               # Read SPSS files with metadata
```

### Advanced Analysis Libraries
```python
import semopy                   # Structural Equation Modeling
import lavaan                   # Alternative SEM (via rpy2)
import psychometric            # Psychometric analysis tools
```

## Customer Satisfaction Survey Analysis Workflow

### 1. Data Import and Preparation
```python
# Import SPSS file with metadata preservation
import pyreadstat
df, meta = pyreadstat.read_sav('survey_data.sav')

# Preserve SPSS metadata
variable_labels = meta.column_names_to_labels
value_labels = meta.variable_value_labels
variable_types = meta.variable_measure

# Convert to appropriate pandas dtypes
for col in df.columns:
    if variable_types.get(col) == 'nominal':
        df[col] = pd.Categorical(df[col])
    elif variable_types.get(col) == 'ordinal':
        df[col] = pd.Categorical(df[col], ordered=True)
```

### 2. Descriptive Analysis (SPSS DESCRIPTIVES + FREQUENCIES)
```python
# Descriptive statistics for scale variables
scale_vars = [col for col, measure in variable_types.items() if measure == 'scale']
descriptives = df[scale_vars].describe()

# Frequency analysis for categorical variables
categorical_vars = [col for col, measure in variable_types.items()
                   if measure in ['nominal', 'ordinal']]
for var in categorical_vars:
    print(f"\nFrequency Analysis for {variable_labels.get(var, var)}:")
    freq_table = df[var].value_counts(dropna=False).sort_index()
    print(freq_table)
```

### 3. Reliability Analysis (SPSS RELIABILITY)
```python
def cronbach_alpha(df, scale_items):
    """Calculate Cronbach's Alpha for scale reliability"""
    # Drop rows with any missing values in scale items
    scale_data = df[scale_items].dropna()

    # Calculate item variances and total variance
    item_variances = scale_data.var(axis=0, ddof=1)
    total_variance = scale_data.sum(axis=1).var(ddof=1)

    # Cronbach's Alpha formula
    k = len(scale_items)  # number of items
    alpha = (k / (k - 1)) * (1 - item_variances.sum() / total_variance)

    return alpha

def item_total_correlation(df, scale_items):
    """Calculate corrected item-total correlations"""
    correlations = {}
    for item in scale_items:
        other_items = [col for col in scale_items if col != item]
        total_score = df[other_items].sum(axis=1)
        corr = df[item].corr(total_score)
        correlations[item] = corr
    return correlations

# Example: Analyze satisfaction scale reliability
satisfaction_items = ['sat_overall', 'sat_quality', 'sat_service', 'sat_value']
alpha = cronbach_alpha(df, satisfaction_items)
item_correlations = item_total_correlation(df, satisfaction_items)

print(f"Cronbach's Alpha: {alpha:.3f}")
print("Item-Total Correlations:")
for item, corr in item_correlations.items():
    print(f"  {variable_labels.get(item, item)}: {corr:.3f}")
```

### 4. Factor Analysis (SPSS FACTOR)
```python
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo

def comprehensive_factor_analysis(df, variables, n_factors=None):
    """Perform comprehensive factor analysis equivalent to SPSS FACTOR"""

    # Prepare data
    factor_data = df[variables].dropna()

    # Test factorability
    chi_square_value, p_value = calculate_bartlett_sphericity(factor_data)
    kmo_all, kmo_model = calculate_kmo(factor_data)

    print(f"Bartlett's Test of Sphericity: χ² = {chi_square_value:.3f}, p = {p_value:.3f}")
    print(f"Kaiser-Meyer-Olkin (KMO) Test: {kmo_model:.3f}")

    # Determine number of factors if not specified
    if n_factors is None:
        # Parallel analysis or eigenvalue > 1 rule
        fa_eigen = FactorAnalyzer(n_factors=len(variables), rotation=None)
        fa_eigen.fit(factor_data)
        eigenvalues = fa_eigen.get_eigenvalues()[0]
        n_factors = sum(eigenvalues > 1)
        print(f"Eigenvalues > 1 suggest {n_factors} factors")

    # Principal axis factoring with rotation
    fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal')
    fa.fit(factor_data)

    # Get factor loadings
    loadings = pd.DataFrame(fa.loadings_, index=variables,
                           columns=[f'Factor_{i+1}' for i in range(n_factors)])

    # Calculate communalities
    communalities = pd.DataFrame({'Communalities': fa.get_communalities()},
                                index=variables)

    return {
        'loadings': loadings,
        'communalities': communalities,
        'variance_explained': fa.get_factor_variance(),
        'eigenvalues': fa.get_eigenvalues()[0]
    }

# Example: Factor analysis of satisfaction items
factor_results = comprehensive_factor_analysis(df, satisfaction_items, n_factors=2)
print("\nFactor Loadings:")
print(factor_results['loadings'].round(3))
```

### 5. Scale Validation and Construct Validity
```python
def construct_validity_analysis(df, scale_items, criterion_var=None, convergent_scales=None):
    """Assess construct validity of a scale"""

    # Create scale score
    scale_score = df[scale_items].mean(axis=1)

    results = {
        'reliability': cronbach_alpha(df, scale_items),
        'n_items': len(scale_items),
        'mean': scale_score.mean(),
        'std': scale_score.std()
    }

    # Criterion validity (if criterion variable provided)
    if criterion_var:
        criterion_corr = scale_score.corr(df[criterion_var])
        results['criterion_validity'] = criterion_corr

    # Convergent validity (correlations with other related scales)
    if convergent_scales:
        convergent_corrs = {}
        for scale_name, scale_vars in convergent_scales.items():
            other_scale = df[scale_vars].mean(axis=1)
            corr = scale_score.corr(other_scale)
            convergent_corrs[scale_name] = corr
        results['convergent_validity'] = convergent_corrs

    return results

# Example: Validate satisfaction scale
loyalty_items = ['loyalty_recommend', 'loyalty_repurchase', 'loyalty_advocate']
validity_results = construct_validity_analysis(
    df,
    satisfaction_items,
    criterion_var='overall_rating',
    convergent_scales={'loyalty': loyalty_items}
)
```

## Advanced Survey Analysis Techniques

### Structural Equation Modeling (SEM)
- Use `semopy` library for comprehensive SEM analysis
- Define measurement models and structural models
- Assess model fit with multiple indices (CFI, TLI, RMSEA, SRMR)
- Compare nested models with chi-square difference tests

### Multi-Group Analysis
- Test measurement invariance across demographic groups
- Compare factor structures between groups
- Assess differential item functioning (DIF)

### Advanced Reliability Assessment
- Calculate McDonald's Omega for more robust reliability
- Assess test-retest reliability with temporal data
- Evaluate inter-rater reliability for subjective measures

### Response Pattern Analysis
- Detect straight-line responding and other response biases
- Analyze response time patterns for data quality
- Identify outlier response patterns

## Integration with Business Intelligence

### Automated Reporting
```python
def generate_survey_report(df, satisfaction_items, demographics=['age_group', 'gender']):
    """Generate comprehensive survey analysis report"""

    report = {
        'sample_characteristics': {},
        'scale_reliability': {},
        'descriptive_statistics': {},
        'group_comparisons': {}
    }

    # Sample characteristics
    for demo in demographics:
        report['sample_characteristics'][demo] = df[demo].value_counts()

    # Scale reliability
    report['scale_reliability']['cronbach_alpha'] = cronbach_alpha(df, satisfaction_items)

    # Descriptive statistics
    scale_score = df[satisfaction_items].mean(axis=1)
    report['descriptive_statistics'] = {
        'mean': scale_score.mean(),
        'median': scale_score.median(),
        'std': scale_score.std(),
        'min': scale_score.min(),
        'max': scale_score.max()
    }

    # Group comparisons
    for demo in demographics:
        groups = df.groupby(demo)[satisfaction_items].mean().mean(axis=1)
        report['group_comparisons'][demo] = groups.to_dict()

    return report
```

### Dashboard Integration
- Create real-time dashboards with Plotly/Dash
- Implement automated alerting for satisfaction thresholds
- Generate executive summaries with key insights

## Memory Consolidation Points

**Key Learnings**:
- Python provides comprehensive equivalents for all major SPSS procedures
- Metadata preservation is crucial when transitioning from SPSS
- Factor analysis and reliability assessment require specialized libraries
- Construct validation follows similar principles but uses different implementation approaches
- Advanced techniques like SEM are available through specialized packages

**Best Practices**:
- Always preserve original SPSS metadata when importing
- Document all transformations and analysis decisions
- Use appropriate effect size measures alongside significance tests
- Validate assumptions before applying statistical procedures
- Generate reproducible analysis workflows with version control

**Areas for Continued Learning**:
- Advanced SEM techniques and model specification
- Machine learning integration with traditional survey analysis
- Real-time survey analysis and monitoring systems
- Cross-cultural survey analysis and measurement invariance
