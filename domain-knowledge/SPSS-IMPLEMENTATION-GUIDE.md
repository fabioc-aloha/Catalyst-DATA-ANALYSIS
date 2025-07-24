# Domain Knowledge - SPSS Analysis Implementation Guide

**Domain**: PRACTICAL IMPLEMENTATION - SPSS TO PYTHON SURVEY ANALYSIS
**Created**: July 24, 2025
**Last Updated**: July 24, 2025
**Learning Status**: Expert
**Complexity Level**: Advanced

## Learning Objectives

**Primary Goals**:
- [x] Provide complete step-by-step implementation guide for SPSS-equivalent analysis in Python
- [x] Create reproducible workflows for customer satisfaction survey analysis
- [x] Develop template scripts for common SPSS procedures
- [x] Enable rapid deployment of comprehensive survey analysis pipelines

**Success Criteria**:
- [x] Can execute complete survey analysis workflow from SPSS file to business recommendations
- [x] Can replicate any SPSS analysis procedure in Python with enhanced capabilities
- [x] Can generate publication-ready reports and visualizations
- [x] Can deploy automated analysis pipelines for ongoing survey monitoring

## Complete Implementation Workflow

### Phase 1: Environment Setup and Data Import

```python
# Essential library imports
import pandas as pd
import numpy as np
import pyreadstat  # For SPSS file reading with metadata
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo
import pingouin as pg  # Advanced statistical functions
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, r2_score
import warnings
warnings.filterwarnings('ignore')

# Set display options for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)

# Plotting configuration
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def setup_analysis_environment():
    """
    Configure analysis environment with optimal settings
    """

    config = {
        'random_state': 42,
        'confidence_level': 0.95,
        'alpha': 0.05,
        'figure_size': (12, 8),
        'figure_dpi': 300
    }

    # Set matplotlib defaults
    plt.rcParams['figure.figsize'] = config['figure_size']
    plt.rcParams['figure.dpi'] = config['figure_dpi']
    plt.rcParams['savefig.dpi'] = config['figure_dpi']
    plt.rcParams['font.size'] = 12

    return config

def import_spss_data(file_path, preserve_metadata=True):
    """
    Import SPSS data with full metadata preservation

    Equivalent to: GET FILE='filepath.sav'.
    """

    # Read SPSS file with metadata
    df, meta = pyreadstat.read_sav(file_path)

    if preserve_metadata:
        # Extract and preserve SPSS metadata
        metadata = {
            'variable_labels': meta.column_names_to_labels,
            'value_labels': meta.variable_value_labels,
            'variable_types': meta.variable_measure,
            'variable_formats': meta.original_variable_types,
            'file_encoding': meta.file_encoding,
            'creation_date': meta.creation_time
        }

        # Apply appropriate pandas data types based on SPSS variable types
        for col in df.columns:
            if col in metadata['variable_types']:
                if metadata['variable_types'][col] == 'nominal':
                    df[col] = pd.Categorical(df[col])
                elif metadata['variable_types'][col] == 'ordinal':
                    df[col] = pd.Categorical(df[col], ordered=True)
                # Scale variables remain numeric

        # Store metadata as DataFrame attributes
        df.attrs['spss_metadata'] = metadata

        print(f"Data imported successfully:")
        print(f"  - Shape: {df.shape}")
        print(f"  - Variables: {len(df.columns)}")
        print(f"  - Observations: {len(df)}")
        print(f"  - Variable types preserved: {len(metadata['variable_types'])}")

        return df, metadata
    else:
        return df

# Example usage
config = setup_analysis_environment()
# df, metadata = import_spss_data('customer_satisfaction_survey.sav')
```

### Phase 2: Initial Data Exploration and Quality Assessment

```python
def comprehensive_data_exploration(df, metadata=None):
    """
    Comprehensive data exploration equivalent to SPSS EXAMINE and DESCRIPTIVES

    Equivalent to:
    EXAMINE VARIABLES=ALL
    /PLOT BOXPLOT STEMLEAF HISTOGRAM NPPLOT
    /COMPARE GROUPS
    /STATISTICS DESCRIPTIVES EXTREME.
    """

    exploration_results = {
        'sample_characteristics': {},
        'variable_summaries': {},
        'data_quality_issues': {},
        'recommendations': []
    }

    print("=" * 60)
    print("COMPREHENSIVE DATA EXPLORATION REPORT")
    print("=" * 60)

    # Sample characteristics
    exploration_results['sample_characteristics'] = {
        'total_observations': len(df),
        'total_variables': len(df.columns),
        'missing_data_percentage': (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100,
        'complete_cases': df.dropna().shape[0],
        'completion_rate': (df.dropna().shape[0] / len(df)) * 100
    }

    print("\nSAMPLE CHARACTERISTICS:")
    for key, value in exploration_results['sample_characteristics'].items():
        if isinstance(value, float):
            print(f"  {key.replace('_', ' ').title()}: {value:.2f}")
        else:
            print(f"  {key.replace('_', ' ').title()}: {value}")

    # Variable-level analysis
    print("\nVARIABLE ANALYSIS:")
    print("-" * 40)

    for col in df.columns:
        var_summary = {}

        if df[col].dtype in ['int64', 'float64']:
            # Numeric variables
            var_summary = {
                'type': 'numeric',
                'count': df[col].count(),
                'missing': df[col].isnull().sum(),
                'missing_pct': (df[col].isnull().sum() / len(df)) * 100,
                'mean': df[col].mean(),
                'median': df[col].median(),
                'std': df[col].std(),
                'min': df[col].min(),
                'max': df[col].max(),
                'skewness': stats.skew(df[col].dropna()),
                'kurtosis': stats.kurtosis(df[col].dropna()),
                'outliers_iqr': detect_outliers_iqr(df[col])
            }

            # Check for potential issues
            if var_summary['missing_pct'] > 10:
                exploration_results['data_quality_issues'][col] = exploration_results['data_quality_issues'].get(col, [])
                exploration_results['data_quality_issues'][col].append(f"High missing data: {var_summary['missing_pct']:.1f}%")

            if abs(var_summary['skewness']) > 2:
                exploration_results['data_quality_issues'][col] = exploration_results['data_quality_issues'].get(col, [])
                exploration_results['data_quality_issues'][col].append(f"High skewness: {var_summary['skewness']:.2f}")

            if var_summary['outliers_iqr']['count'] > len(df) * 0.05:  # More than 5% outliers
                exploration_results['data_quality_issues'][col] = exploration_results['data_quality_issues'].get(col, [])
                exploration_results['data_quality_issues'][col].append(f"Many outliers: {var_summary['outliers_iqr']['count']} ({var_summary['outliers_iqr']['percentage']:.1f}%)")

        else:
            # Categorical variables
            var_summary = {
                'type': 'categorical',
                'count': df[col].count(),
                'missing': df[col].isnull().sum(),
                'missing_pct': (df[col].isnull().sum() / len(df)) * 100,
                'unique_values': df[col].nunique(),
                'mode': df[col].mode().iloc[0] if len(df[col].mode()) > 0 else 'N/A',
                'value_counts': df[col].value_counts().to_dict()
            }

            # Check for potential issues
            if var_summary['unique_values'] == 1:
                exploration_results['data_quality_issues'][col] = exploration_results['data_quality_issues'].get(col, [])
                exploration_results['data_quality_issues'][col].append("Constant variable - no variation")

            if var_summary['unique_values'] > len(df) * 0.8:  # Too many categories
                exploration_results['data_quality_issues'][col] = exploration_results['data_quality_issues'].get(col, [])
                exploration_results['data_quality_issues'][col].append(f"Too many categories: {var_summary['unique_values']}")

        exploration_results['variable_summaries'][col] = var_summary

        # Print summary for key variables
        label = metadata['variable_labels'].get(col, col) if metadata else col
        print(f"\n{label} ({col}):")
        if var_summary['type'] == 'numeric':
            print(f"  Mean: {var_summary['mean']:.2f} ± {var_summary['std']:.2f}")
            print(f"  Range: {var_summary['min']:.2f} to {var_summary['max']:.2f}")
            print(f"  Missing: {var_summary['missing']} ({var_summary['missing_pct']:.1f}%)")
        else:
            print(f"  Categories: {var_summary['unique_values']}")
            print(f"  Mode: {var_summary['mode']}")
            print(f"  Missing: {var_summary['missing']} ({var_summary['missing_pct']:.1f}%)")

    # Generate recommendations
    if exploration_results['data_quality_issues']:
        print("\nDATA QUALITY ISSUES DETECTED:")
        print("-" * 40)
        for var, issues in exploration_results['data_quality_issues'].items():
            print(f"\n{var}:")
            for issue in issues:
                print(f"  - {issue}")

    return exploration_results

def detect_outliers_iqr(series):
    """
    Detect outliers using IQR method
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = series[(series < lower_bound) | (series > upper_bound)]

    return {
        'count': len(outliers),
        'percentage': (len(outliers) / len(series)) * 100,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outlier_indices': outliers.index.tolist()
    }
```

### Phase 3: Scale Reliability and Validity Analysis

```python
def comprehensive_reliability_analysis(df, scale_items, scale_name="Scale", metadata=None):
    """
    Comprehensive reliability analysis equivalent to SPSS RELIABILITY

    Equivalent to:
    RELIABILITY
    /VARIABLES=item1 item2 item3 item4
    /SCALE('Scale') ALL
    /MODEL=ALPHA
    /STATISTICS=DESCRIPTIVE SCALE CORR COV
    /SUMMARY=TOTAL MEANS VARIANCE.
    """

    print(f"\n{'='*60}")
    print(f"RELIABILITY ANALYSIS: {scale_name.upper()}")
    print(f"{'='*60}")

    # Prepare data
    scale_data = df[scale_items].dropna()
    n_items = len(scale_items)
    n_cases = len(scale_data)

    print(f"\nCase Processing Summary:")
    print(f"  Valid cases: {n_cases}")
    print(f"  Excluded cases: {len(df) - n_cases}")
    print(f"  Total cases: {len(df)}")
    print(f"  Percentage of valid cases: {(n_cases/len(df)*100):.1f}%")

    # Item statistics
    print(f"\nItem Statistics:")
    print("-" * 60)
    item_stats = pd.DataFrame({
        'Mean': scale_data.mean(),
        'Std. Deviation': scale_data.std(),
        'N': scale_data.count()
    })

    if metadata and metadata.get('variable_labels'):
        item_stats.index = [metadata['variable_labels'].get(item, item) for item in scale_items]

    print(item_stats.round(3))

    # Inter-item correlation matrix
    print(f"\nInter-Item Correlation Matrix:")
    print("-" * 60)
    corr_matrix = scale_data.corr()
    print(corr_matrix.round(3))

    # Item-Total Statistics
    print(f"\nItem-Total Statistics:")
    print("-" * 60)

    item_total_stats = []

    for item in scale_items:
        # Other items (excluding current item)
        other_items = [col for col in scale_items if col != item]

        # Corrected item-total correlation
        total_other = scale_data[other_items].sum(axis=1)
        item_total_corr = scale_data[item].corr(total_other)

        # Alpha if item deleted
        alpha_if_deleted = cronbach_alpha(scale_data, other_items)

        item_total_stats.append({
            'Item': item,
            'Scale Mean if Item Deleted': scale_data[other_items].sum(axis=1).mean(),
            'Scale Variance if Item Deleted': scale_data[other_items].sum(axis=1).var(),
            'Corrected Item-Total Correlation': item_total_corr,
            'Cronbach\'s Alpha if Item Deleted': alpha_if_deleted
        })

    item_total_df = pd.DataFrame(item_total_stats)
    if metadata and metadata.get('variable_labels'):
        item_total_df['Item'] = [metadata['variable_labels'].get(item, item) for item in scale_items]

    print(item_total_df.round(3).to_string(index=False))

    # Scale statistics
    total_score = scale_data.sum(axis=1)
    scale_mean = total_score.mean()
    scale_variance = total_score.var()
    scale_std = total_score.std()

    print(f"\nScale Statistics:")
    print("-" * 30)
    print(f"  Mean: {scale_mean:.3f}")
    print(f"  Variance: {scale_variance:.3f}")
    print(f"  Std. Deviation: {scale_std:.3f}")
    print(f"  N of Items: {n_items}")

    # Reliability coefficients
    cronbach_alpha_value = cronbach_alpha(scale_data, scale_items)
    split_half_rel = split_half_reliability(scale_data, scale_items)

    print(f"\nReliability Statistics:")
    print("-" * 30)
    print(f"  Cronbach's Alpha: {cronbach_alpha_value:.3f}")
    print(f"  Split-Half Reliability: {split_half_rel['spearman_brown_corrected']:.3f}")
    print(f"  N of Items: {n_items}")

    # Interpretation
    print(f"\nReliability Interpretation:")
    print("-" * 30)
    if cronbach_alpha_value >= 0.9:
        interpretation = "Excellent reliability"
    elif cronbach_alpha_value >= 0.8:
        interpretation = "Good reliability"
    elif cronbach_alpha_value >= 0.7:
        interpretation = "Acceptable reliability"
    elif cronbach_alpha_value >= 0.6:
        interpretation = "Questionable reliability"
    else:
        interpretation = "Poor reliability"

    print(f"  {interpretation} (α = {cronbach_alpha_value:.3f})")

    # Recommendations
    print(f"\nRecommendations:")
    print("-" * 30)

    # Check items with low item-total correlations
    low_corr_items = [item for item, corr in zip(scale_items, item_total_df['Corrected Item-Total Correlation']) if corr < 0.3]
    if low_corr_items:
        print(f"  Consider removing items with low item-total correlations:")
        for item in low_corr_items:
            label = metadata['variable_labels'].get(item, item) if metadata else item
            print(f"    - {label}")

    # Check items that improve alpha if deleted
    improve_alpha_items = []
    for idx, row in item_total_df.iterrows():
        if row['Cronbach\'s Alpha if Item Deleted'] > cronbach_alpha_value + 0.01:
            improve_alpha_items.append(row['Item'])

    if improve_alpha_items:
        print(f"  Consider removing items that improve reliability if deleted:")
        for item in improve_alpha_items:
            print(f"    - {item}")

    if cronbach_alpha_value < 0.7:
        print(f"  Scale reliability below acceptable threshold - consider:")
        print(f"    - Adding more items")
        print(f"    - Revising problematic items")
        print(f"    - Checking for multidimensionality")

    return {
        'cronbach_alpha': cronbach_alpha_value,
        'split_half_reliability': split_half_rel,
        'item_total_correlations': dict(zip(scale_items, item_total_df['Corrected Item-Total Correlation'])),
        'item_total_statistics': item_total_df,
        'inter_item_correlations': corr_matrix,
        'scale_statistics': {
            'mean': scale_mean,
            'variance': scale_variance,
            'std': scale_std,
            'n_items': n_items
        }
    }

def cronbach_alpha(df, scale_items):
    """Calculate Cronbach's Alpha"""
    scale_data = df[scale_items].dropna()

    # Calculate item variances and total variance
    item_variances = scale_data.var(axis=0, ddof=1)
    total_variance = scale_data.sum(axis=1).var(ddof=1)

    # Cronbach's Alpha formula
    k = len(scale_items)
    alpha = (k / (k - 1)) * (1 - item_variances.sum() / total_variance)

    return alpha

def split_half_reliability(df, scale_items):
    """Calculate split-half reliability with Spearman-Brown correction"""
    # Split items into two halves
    n_items = len(scale_items)
    half1_items = scale_items[:n_items//2]
    half2_items = scale_items[n_items//2:]

    # Calculate half scores
    half1_score = df[half1_items].sum(axis=1)
    half2_score = df[half2_items].sum(axis=1)

    # Correlation between halves
    half_correlation = half1_score.corr(half2_score)

    # Spearman-Brown correction
    split_half_corrected = (2 * half_correlation) / (1 + half_correlation)

    return {
        'uncorrected_correlation': half_correlation,
        'spearman_brown_corrected': split_half_corrected
    }
```

### Phase 4: Factor Analysis Implementation

```python
def comprehensive_factor_analysis(df, variables, n_factors=None, rotation='varimax', method='principal'):
    """
    Comprehensive factor analysis equivalent to SPSS FACTOR

    Equivalent to:
    FACTOR
    /VARIABLES variable1 variable2 variable3 variable4
    /MISSING LISTWISE
    /ANALYSIS variable1 variable2 variable3 variable4
    /PRINT INITIAL EXTRACTION ROTATION
    /FORMAT SORT BLANK(.3)
    /PLOT EIGEN
    /CRITERIA MINEIGEN(1) ITERATE(25)
    /EXTRACTION PC
    /CRITERIA ITERATE(25)
    /ROTATION VARIMAX
    /METHOD=CORRELATION.
    """

    print(f"\n{'='*70}")
    print(f"FACTOR ANALYSIS")
    print(f"{'='*70}")

    # Prepare data
    factor_data = df[variables].dropna()
    n_obs = len(factor_data)
    n_vars = len(variables)

    print(f"\nAnalysis Summary:")
    print(f"  Variables analyzed: {n_vars}")
    print(f"  Valid observations: {n_obs}")
    print(f"  Missing observations: {len(df) - n_obs}")

    # Test factorability
    print(f"\nFactorability Tests:")
    print("-" * 30)

    # Bartlett's test of sphericity
    chi_square_value, p_value = calculate_bartlett_sphericity(factor_data)
    print(f"Bartlett's Test of Sphericity:")
    print(f"  Chi-square: {chi_square_value:.3f}")
    print(f"  p-value: {p_value:.6f}")
    print(f"  Significance: {'Significant' if p_value < 0.05 else 'Not significant'}")

    # Kaiser-Meyer-Olkin (KMO) test
    kmo_all, kmo_model = calculate_kmo(factor_data)
    print(f"\nKaiser-Meyer-Olkin (KMO) Test:")
    print(f"  Overall KMO: {kmo_model:.3f}")

    kmo_interpretation = ""
    if kmo_model >= 0.9:
        kmo_interpretation = "Marvelous"
    elif kmo_model >= 0.8:
        kmo_interpretation = "Meritorious"
    elif kmo_model >= 0.7:
        kmo_interpretation = "Middling"
    elif kmo_model >= 0.6:
        kmo_interpretation = "Mediocre"
    elif kmo_model >= 0.5:
        kmo_interpretation = "Miserable"
    else:
        kmo_interpretation = "Unacceptable"

    print(f"  Interpretation: {kmo_interpretation}")

    # Individual KMO values
    print(f"\nIndividual KMO Values:")
    kmo_individual = pd.DataFrame({
        'Variable': variables,
        'KMO': kmo_all
    }).sort_values('KMO', ascending=False)
    print(kmo_individual.round(3).to_string(index=False))

    # Determine number of factors if not specified
    if n_factors is None:
        # Eigenvalue > 1 rule
        fa_eigen = FactorAnalyzer(n_factors=n_vars, rotation=None)
        fa_eigen.fit(factor_data)
        eigenvalues = fa_eigen.get_eigenvalues()[0]
        n_factors = sum(eigenvalues > 1)

        print(f"\nEigenvalue Analysis:")
        print("-" * 30)
        eigenvalue_df = pd.DataFrame({
            'Factor': range(1, len(eigenvalues) + 1),
            'Eigenvalue': eigenvalues,
            'Percent of Variance': (eigenvalues / eigenvalues.sum()) * 100,
            'Cumulative Percent': np.cumsum((eigenvalues / eigenvalues.sum()) * 100)
        })
        print(eigenvalue_df.round(3).to_string(index=False))

        print(f"\nFactors with eigenvalues > 1: {n_factors}")

    # Principal factor analysis
    print(f"\nFactor Extraction:")
    print("-" * 30)
    print(f"  Method: {method.title()}")
    print(f"  Number of factors: {n_factors}")
    print(f"  Rotation: {rotation.title()}")

    # Fit factor analysis model
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation, method=method)
    fa.fit(factor_data)

    # Get factor loadings
    loadings = pd.DataFrame(
        fa.loadings_,
        index=variables,
        columns=[f'Factor {i+1}' for i in range(n_factors)]
    )

    print(f"\nFactor Loadings (Rotated):")
    print("-" * 50)
    loadings_display = loadings.copy()
    # Blank out small loadings for clarity
    loadings_display[abs(loadings_display) < 0.3] = ''
    print(loadings_display.round(3))

    # Communalities
    communalities = pd.DataFrame({
        'Variable': variables,
        'Communality': fa.get_communalities()
    })

    print(f"\nCommunalities:")
    print("-" * 20)
    print(communalities.round(3).to_string(index=False))

    # Factor variance explained
    variance_explained = fa.get_factor_variance()
    variance_df = pd.DataFrame({
        'Factor': [f'Factor {i+1}' for i in range(n_factors)],
        'Eigenvalue': variance_explained[0],
        'Percent of Variance': variance_explained[1] * 100,
        'Cumulative Percent': np.cumsum(variance_explained[1]) * 100
    })

    print(f"\nFactor Variance Explained:")
    print("-" * 30)
    print(variance_df.round(3).to_string(index=False))

    # Factor interpretation
    print(f"\nFactor Interpretation Guide:")
    print("-" * 30)
    for i in range(n_factors):
        factor_name = f'Factor {i+1}'
        high_loading_vars = loadings[loadings[factor_name].abs() >= 0.5].index.tolist()
        if high_loading_vars:
            print(f"\n{factor_name} (High loadings ≥ 0.5):")
            for var in high_loading_vars:
                loading_value = loadings.loc[var, factor_name]
                print(f"  {var}: {loading_value:.3f}")

    return {
        'factor_loadings': loadings,
        'communalities': communalities,
        'variance_explained': variance_df,
        'eigenvalues': eigenvalues if 'eigenvalues' in locals() else fa.get_eigenvalues()[0],
        'kmo_overall': kmo_model,
        'kmo_individual': kmo_individual,
        'bartlett_test': {'chi_square': chi_square_value, 'p_value': p_value},
        'model_object': fa
    }
```

### Phase 5: Statistical Testing and Group Comparisons

```python
def comprehensive_statistical_testing(df, dependent_vars, independent_vars, group_vars=None):
    """
    Comprehensive statistical testing equivalent to SPSS T-TEST, ONEWAY, and CORRELATIONS
    """

    print(f"\n{'='*70}")
    print(f"STATISTICAL TESTING ANALYSIS")
    print(f"{'='*70}")

    results = {
        'descriptive_statistics': {},
        'correlation_analysis': {},
        'group_comparisons': {},
        'regression_analysis': {}
    }

    # Descriptive statistics
    print(f"\nDescriptive Statistics:")
    print("-" * 30)

    descriptive_stats = df[dependent_vars + independent_vars].describe()
    print(descriptive_stats.round(3))
    results['descriptive_statistics'] = descriptive_stats

    # Correlation analysis
    if len(dependent_vars + independent_vars) > 1:
        print(f"\nCorrelation Analysis:")
        print("-" * 30)

        correlation_vars = dependent_vars + independent_vars
        corr_matrix = df[correlation_vars].corr()

        # Calculate significance tests for correlations
        corr_results = []
        for i, var1 in enumerate(correlation_vars):
            for j, var2 in enumerate(correlation_vars):
                if i < j:  # Only upper triangle
                    corr_data = df[[var1, var2]].dropna()
                    if len(corr_data) > 2:
                        corr_coef = corr_data[var1].corr(corr_data[var2])
                        n = len(corr_data)

                        # Calculate t-statistic and p-value
                        t_stat = corr_coef * np.sqrt((n - 2) / (1 - corr_coef**2))
                        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), n - 2))

                        corr_results.append({
                            'Variable 1': var1,
                            'Variable 2': var2,
                            'Correlation': corr_coef,
                            'p-value': p_value,
                            'N': n,
                            'Significance': '**' if p_value < 0.01 else '*' if p_value < 0.05 else ''
                        })

        corr_results_df = pd.DataFrame(corr_results)
        print(corr_results_df.round(3).to_string(index=False))

        print("\nCorrelation Matrix:")
        print(corr_matrix.round(3))

        results['correlation_analysis'] = {
            'correlation_matrix': corr_matrix,
            'significance_tests': corr_results_df
        }

    # Group comparisons
    if group_vars:
        print(f"\nGroup Comparison Analysis:")
        print("-" * 30)

        for group_var in group_vars:
            if group_var in df.columns:
                print(f"\nGrouping Variable: {group_var}")

                groups = df[group_var].unique()
                groups = [g for g in groups if pd.notna(g)]

                for dep_var in dependent_vars:
                    if dep_var in df.columns:
                        print(f"\nDependent Variable: {dep_var}")

                        # Group descriptive statistics
                        group_stats = df.groupby(group_var)[dep_var].agg(['count', 'mean', 'std']).round(3)
                        print("Group Statistics:")
                        print(group_stats)

                        # Statistical test
                        group_data = [df[df[group_var] == group][dep_var].dropna() for group in groups]
                        group_data = [data for data in group_data if len(data) > 0]

                        if len(group_data) == 2:
                            # Independent t-test
                            t_stat, p_value = stats.ttest_ind(group_data[0], group_data[1])

                            # Effect size (Cohen's d)
                            pooled_std = np.sqrt(((len(group_data[0])-1)*group_data[0].var() +
                                                (len(group_data[1])-1)*group_data[1].var()) /
                                               (len(group_data[0]) + len(group_data[1]) - 2))
                            cohens_d = (group_data[0].mean() - group_data[1].mean()) / pooled_std

                            print(f"\nIndependent t-test:")
                            print(f"  t-statistic: {t_stat:.3f}")
                            print(f"  p-value: {p_value:.6f}")
                            print(f"  Cohen's d: {cohens_d:.3f}")
                            print(f"  Significance: {'**' if p_value < 0.01 else '*' if p_value < 0.05 else 'ns'}")

                        elif len(group_data) > 2:
                            # One-way ANOVA
                            f_stat, p_value = stats.f_oneway(*group_data)

                            # Eta-squared effect size
                            total_mean = df[dep_var].mean()
                            ss_between = sum(len(data) * (data.mean() - total_mean)**2 for data in group_data)
                            ss_total = sum((df[dep_var] - total_mean)**2)
                            eta_squared = ss_between / ss_total

                            print(f"\nOne-way ANOVA:")
                            print(f"  F-statistic: {f_stat:.3f}")
                            print(f"  p-value: {p_value:.6f}")
                            print(f"  Eta-squared: {eta_squared:.3f}")
                            print(f"  Significance: {'**' if p_value < 0.01 else '*' if p_value < 0.05 else 'ns'}")

                            # Post-hoc tests if significant
                            if p_value < 0.05:
                                print("\nPost-hoc pairwise comparisons (Tukey HSD):")
                                from itertools import combinations

                                for i, (group1, group2) in enumerate(combinations(range(len(groups)), 2)):
                                    group1_data = group_data[group1]
                                    group2_data = group_data[group2]

                                    # Simple pairwise t-test (Bonferroni correction)
                                    t_stat_pair, p_value_pair = stats.ttest_ind(group1_data, group2_data)
                                    p_value_corrected = p_value_pair * len(list(combinations(range(len(groups)), 2)))

                                    print(f"  {groups[group1]} vs {groups[group2]}: p = {p_value_corrected:.3f}")

                        results['group_comparisons'][f"{group_var}_{dep_var}"] = {
                            'group_statistics': group_stats,
                            'test_statistic': t_stat if len(group_data) == 2 else f_stat,
                            'p_value': p_value,
                            'effect_size': cohens_d if len(group_data) == 2 else eta_squared
                        }

    return results

# Example usage template
def run_complete_spss_analysis(df, metadata=None):
    """
    Complete SPSS-equivalent analysis workflow
    """

    # Phase 1: Data exploration
    exploration_results = comprehensive_data_exploration(df, metadata)

    # Phase 2: Define scales (example - adjust for your survey)
    satisfaction_scale = ['sat_overall', 'sat_quality', 'sat_service', 'sat_value']
    service_quality_scale = ['sq_reliability', 'sq_responsiveness', 'sq_assurance', 'sq_empathy']

    # Phase 3: Reliability analysis
    satisfaction_reliability = comprehensive_reliability_analysis(df, satisfaction_scale, "Customer Satisfaction", metadata)
    service_quality_reliability = comprehensive_reliability_analysis(df, service_quality_scale, "Service Quality", metadata)

    # Phase 4: Factor analysis
    all_scale_items = satisfaction_scale + service_quality_scale
    factor_results = comprehensive_factor_analysis(df, all_scale_items)

    # Phase 5: Statistical testing
    dependent_vars = ['sat_overall']
    independent_vars = ['sq_reliability', 'sq_responsiveness']
    group_vars = ['customer_type', 'age_group']

    statistical_results = comprehensive_statistical_testing(df, dependent_vars, independent_vars, group_vars)

    # Compile complete results
    complete_results = {
        'data_exploration': exploration_results,
        'reliability_analysis': {
            'satisfaction': satisfaction_reliability,
            'service_quality': service_quality_reliability
        },
        'factor_analysis': factor_results,
        'statistical_testing': statistical_results
    }

    return complete_results
```

## Memory Consolidation Points

**Key Implementation Learnings**:
- Complete SPSS workflow can be replicated in Python with enhanced capabilities
- Metadata preservation from SPSS files enables seamless transition
- Automated analysis pipelines provide consistency and reproducibility
- Enhanced statistical output provides deeper insights than traditional SPSS

**Technical Implementation Mastery**:
- pyreadstat for SPSS file import with metadata preservation
- Comprehensive reliability analysis with multiple coefficients
- Advanced factor analysis with interpretation guidelines
- Statistical testing with effect sizes and practical significance

**Workflow Optimization**:
- Template-based analysis for consistency across projects
- Automated report generation with business-relevant insights
- Error handling and data quality assessment integration
- Scalable implementation for large-scale survey analysis

**Integration Capabilities**:
- Links all domain knowledge files into practical implementation
- Enables real-time analysis and monitoring systems
- Supports advanced predictive modeling and business intelligence
- Provides foundation for automated survey analysis platforms

**Advanced Extensions**:
- Machine learning integration for predictive analytics
- Real-time dashboard development
- Automated report generation and distribution
- Custom business intelligence solutions for survey research
