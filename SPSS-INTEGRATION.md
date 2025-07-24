# SPSS to Python Integration Manual

**Version**: 1.0
**Date**: July 24, 2025
**Framework**: Alex's Bootstrap Learning Framework - NEWBORN Enhanced Data Analysis

## Table of Contents

1. [Quick Start Guide](#quick-start-guide)
2. [SPSS File Import and Setup](#spss-file-import-and-setup)
3. [Common SPSS Procedures in Python](#common-spss-procedures-in-python)
4. [Customer Satisfaction Survey Analysis](#customer-satisfaction-survey-analysis)
5. [Advanced Analytics Beyond SPSS](#advanced-analytics-beyond-spss)
6. [Troubleshooting and Best Practices](#troubleshooting-and-best-practices)
7. [Resources and Further Learning](#resources-and-further-learning)

---

## Quick Start Guide

### Prerequisites

Ensure you have Python 3.8+ and the following packages installed:

```bash
pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn
pip install pyreadstat factor-analyzer pingouin semopy
```

### 5-Minute SPSS File Analysis

```python
# Import essential libraries
import pandas as pd
import pyreadstat
from scipy import stats
import numpy as np

# 1. Import SPSS file with metadata
df, meta = pyreadstat.read_sav('your_survey_data.sav')
print(f"Data shape: {df.shape}")

# 2. Quick descriptive analysis (equivalent to SPSS DESCRIPTIVES)
print("\nDescriptive Statistics:")
print(df.describe())

# 3. Reliability analysis (equivalent to SPSS RELIABILITY)
# Define your scale items
satisfaction_items = ['sat1', 'sat2', 'sat3', 'sat4']  # Replace with your variables

def cronbach_alpha(df, items):
    """Calculate Cronbach's Alpha"""
    item_data = df[items].dropna()
    item_variances = item_data.var(axis=0, ddof=1)
    total_variance = item_data.sum(axis=1).var(ddof=1)
    k = len(items)
    alpha = (k / (k - 1)) * (1 - item_variances.sum() / total_variance)
    return alpha

alpha = cronbach_alpha(df, satisfaction_items)
print(f"\nCronbach's Alpha: {alpha:.3f}")

# 4. Basic correlation analysis (equivalent to SPSS CORRELATIONS)
correlation_matrix = df[satisfaction_items].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix.round(3))
```

---

## SPSS File Import and Setup

### Complete Data Import with Metadata Preservation

```python
import pandas as pd
import pyreadstat
import numpy as np

def import_spss_with_metadata(file_path):
    """
    Import SPSS file preserving all metadata
    Equivalent to: GET FILE='filepath.sav'
    """

    # Read SPSS file
    df, meta = pyreadstat.read_sav(file_path)

    # Preserve metadata
    metadata = {
        'variable_labels': meta.column_names_to_labels,
        'value_labels': meta.variable_value_labels,
        'variable_types': meta.variable_measure,
        'missing_values': meta.missing_ranges
    }

    # Apply appropriate data types
    for col in df.columns:
        if col in metadata['variable_types']:
            if metadata['variable_types'][col] == 'nominal':
                df[col] = pd.Categorical(df[col])
            elif metadata['variable_types'][col] == 'ordinal':
                df[col] = pd.Categorical(df[col], ordered=True)

    # Store metadata in DataFrame attributes
    df.attrs['spss_metadata'] = metadata

    return df, metadata

# Usage
df, metadata = import_spss_with_metadata('customer_survey.sav')

# Access variable labels
print("Variable Labels:")
for var, label in metadata['variable_labels'].items():
    print(f"  {var}: {label}")
```

### Data Quality Check (SPSS EXAMINE equivalent)

```python
def examine_data(df, variables=None):
    """
    Comprehensive data examination
    Equivalent to: EXAMINE VARIABLES=ALL /PLOT BOXPLOT HISTOGRAM
    """

    if variables is None:
        variables = df.select_dtypes(include=[np.number]).columns.tolist()

    results = {}

    for var in variables:
        if var in df.columns:
            data = df[var].dropna()

            results[var] = {
                'count': len(data),
                'missing': df[var].isnull().sum(),
                'mean': data.mean(),
                'median': data.median(),
                'std': data.std(),
                'min': data.min(),
                'max': data.max(),
                'skewness': stats.skew(data),
                'kurtosis': stats.kurtosis(data),
                'outliers_count': len(data[(data < data.quantile(0.25) - 1.5 * (data.quantile(0.75) - data.quantile(0.25))) |
                                          (data > data.quantile(0.75) + 1.5 * (data.quantile(0.75) - data.quantile(0.25)))])
            }

    return pd.DataFrame(results).T

# Usage
examination_results = examine_data(df)
print(examination_results.round(3))
```

---

## Common SPSS Procedures in Python

### 1. Descriptive Statistics

| SPSS Command | Python Equivalent | Notes |
|--------------|-------------------|-------|
| `DESCRIPTIVES VARIABLES=var1 var2` | `df[['var1', 'var2']].describe()` | Enhanced with additional statistics |
| `FREQUENCIES VARIABLES=var1` | `df['var1'].value_counts()` | Include missing value counts |
| `CROSSTABS TABLES=var1 BY var2` | `pd.crosstab(df['var1'], df['var2'])` | Add chi-square test |

```python
# SPSS: DESCRIPTIVES VARIABLES=satisfaction quality service
descriptive_stats = df[['satisfaction', 'quality', 'service']].describe()
print(descriptive_stats)

# SPSS: FREQUENCIES VARIABLES=customer_type
frequency_table = df['customer_type'].value_counts(dropna=False)
print(frequency_table)

# SPSS: CROSSTABS TABLES=customer_type BY satisfaction_level
crosstab = pd.crosstab(df['customer_type'], df['satisfaction_level'], margins=True)
print(crosstab)
```

### 2. Reliability Analysis

```python
def spss_reliability_analysis(df, scale_items, scale_name="Scale"):
    """
    Complete reliability analysis equivalent to SPSS RELIABILITY

    SPSS Equivalent:
    RELIABILITY
    /VARIABLES=item1 item2 item3 item4
    /SCALE('Scale Name') ALL
    /MODEL=ALPHA
    /STATISTICS=DESCRIPTIVE SCALE CORR
    /SUMMARY=TOTAL MEANS VARIANCE
    """

    print(f"\nRELIABILITY ANALYSIS: {scale_name}")
    print("=" * 50)

    # Case processing summary
    scale_data = df[scale_items].dropna()
    valid_cases = len(scale_data)
    total_cases = len(df)

    print(f"Case Processing Summary:")
    print(f"  Valid cases: {valid_cases} ({valid_cases/total_cases*100:.1f}%)")
    print(f"  Excluded: {total_cases - valid_cases} ({(total_cases-valid_cases)/total_cases*100:.1f}%)")

    # Item statistics
    print(f"\nItem Statistics:")
    item_stats = pd.DataFrame({
        'Mean': scale_data.mean(),
        'Std. Deviation': scale_data.std(),
        'N': scale_data.count()
    })
    print(item_stats.round(3))

    # Inter-item correlations
    print(f"\nInter-Item Correlation Matrix:")
    corr_matrix = scale_data.corr()
    print(corr_matrix.round(3))

    # Item-total statistics
    print(f"\nItem-Total Statistics:")
    item_total_stats = []

    for item in scale_items:
        other_items = [col for col in scale_items if col != item]
        total_other = scale_data[other_items].sum(axis=1)

        # Corrected item-total correlation
        item_total_corr = scale_data[item].corr(total_other)

        # Alpha if item deleted
        alpha_if_deleted = cronbach_alpha(scale_data, other_items)

        item_total_stats.append({
            'Item': item,
            'Corrected Item-Total Correlation': item_total_corr,
            'Cronbach\'s Alpha if Item Deleted': alpha_if_deleted
        })

    item_total_df = pd.DataFrame(item_total_stats)
    print(item_total_df.round(3).to_string(index=False))

    # Scale statistics
    total_score = scale_data.sum(axis=1)
    cronbach_alpha_value = cronbach_alpha(scale_data, scale_items)

    print(f"\nScale Statistics:")
    print(f"  Mean: {total_score.mean():.3f}")
    print(f"  Variance: {total_score.var():.3f}")
    print(f"  Std. Deviation: {total_score.std():.3f}")
    print(f"  N of Items: {len(scale_items)}")
    print(f"  Cronbach's Alpha: {cronbach_alpha_value:.3f}")

    return cronbach_alpha_value, item_total_df

def cronbach_alpha(df, items):
    """Calculate Cronbach's Alpha"""
    item_data = df[items].dropna()
    item_variances = item_data.var(axis=0, ddof=1)
    total_variance = item_data.sum(axis=1).var(ddof=1)
    k = len(items)
    alpha = (k / (k - 1)) * (1 - item_variances.sum() / total_variance)
    return alpha

# Usage
satisfaction_items = ['sat_overall', 'sat_quality', 'sat_service', 'sat_value']
alpha, item_stats = spss_reliability_analysis(df, satisfaction_items, "Customer Satisfaction")
```

### 3. Factor Analysis

```python
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo

def spss_factor_analysis(df, variables, n_factors=None, rotation='varimax'):
    """
    Factor analysis equivalent to SPSS FACTOR

    SPSS Equivalent:
    FACTOR
    /VARIABLES var1 var2 var3 var4
    /MISSING LISTWISE
    /ANALYSIS var1 var2 var3 var4
    /PRINT INITIAL EXTRACTION ROTATION
    /CRITERIA MINEIGEN(1) ITERATE(25)
    /EXTRACTION PC
    /ROTATION VARIMAX
    """

    print("FACTOR ANALYSIS")
    print("=" * 50)

    # Prepare data
    factor_data = df[variables].dropna()

    # KMO and Bartlett's test
    chi_square, p_value = calculate_bartlett_sphericity(factor_data)
    kmo_all, kmo_model = calculate_kmo(factor_data)

    print(f"KMO and Bartlett's Test:")
    print(f"  Kaiser-Meyer-Olkin Measure: {kmo_model:.3f}")
    print(f"  Bartlett's Test of Sphericity:")
    print(f"    Chi-square: {chi_square:.3f}")
    print(f"    p-value: {p_value:.6f}")

    # Determine factors if not specified
    if n_factors is None:
        fa_eigen = FactorAnalyzer(n_factors=len(variables), rotation=None)
        fa_eigen.fit(factor_data)
        eigenvalues = fa_eigen.get_eigenvalues()[0]
        n_factors = sum(eigenvalues > 1)
        print(f"\nFactors with eigenvalues > 1: {n_factors}")

    # Factor analysis
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation)
    fa.fit(factor_data)

    # Factor loadings
    loadings = pd.DataFrame(
        fa.loadings_,
        index=variables,
        columns=[f'Factor{i+1}' for i in range(n_factors)]
    )

    print(f"\nRotated Factor Loadings:")
    loadings_display = loadings.copy()
    loadings_display[abs(loadings_display) < 0.3] = ''  # Suppress small loadings
    print(loadings_display.round(3))

    # Communalities
    communalities = pd.DataFrame({
        'Variable': variables,
        'Communality': fa.get_communalities()
    })

    print(f"\nCommunalities:")
    print(communalities.round(3).to_string(index=False))

    # Variance explained
    variance_explained = fa.get_factor_variance()
    variance_df = pd.DataFrame({
        'Factor': [f'Factor{i+1}' for i in range(n_factors)],
        'Eigenvalue': variance_explained[0],
        '% of Variance': variance_explained[1] * 100,
        'Cumulative %': np.cumsum(variance_explained[1]) * 100
    })

    print(f"\nTotal Variance Explained:")
    print(variance_df.round(3).to_string(index=False))

    return loadings, communalities, variance_df

# Usage
factor_vars = ['item1', 'item2', 'item3', 'item4', 'item5']
loadings, communalities, variance = spss_factor_analysis(df, factor_vars)
```

### 4. Statistical Tests

```python
# T-Test (SPSS: T-TEST)
def independent_samples_ttest(df, test_var, group_var):
    """
    Independent samples t-test
    SPSS: T-TEST GROUPS=group_var(1 2) /VARIABLES=test_var
    """
    groups = df[group_var].unique()
    if len(groups) == 2:
        group1_data = df[df[group_var] == groups[0]][test_var].dropna()
        group2_data = df[df[group_var] == groups[1]][test_var].dropna()

        # Levene's test for equal variances
        levene_stat, levene_p = stats.levene(group1_data, group2_data)

        # T-test
        if levene_p > 0.05:  # Equal variances
            t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
            equal_var = True
        else:  # Unequal variances
            t_stat, p_value = stats.ttest_ind(group1_data, group2_data, equal_var=False)
            equal_var = False

        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(group1_data)-1)*group1_data.var() +
                            (len(group2_data)-1)*group2_data.var()) /
                           (len(group1_data) + len(group2_data) - 2))
        cohens_d = (group1_data.mean() - group2_data.mean()) / pooled_std

        print(f"Independent Samples T-Test: {test_var} by {group_var}")
        print(f"Levene's Test: F = {levene_stat:.3f}, p = {levene_p:.3f}")
        print(f"Equal variances {'assumed' if equal_var else 'not assumed'}")
        print(f"t = {t_stat:.3f}, df = {len(group1_data) + len(group2_data) - 2}")
        print(f"p-value (2-tailed) = {p_value:.3f}")
        print(f"Cohen's d = {cohens_d:.3f}")

        return {'t_statistic': t_stat, 'p_value': p_value, 'cohens_d': cohens_d}

# One-Way ANOVA (SPSS: ONEWAY)
def oneway_anova(df, dependent_var, factor_var):
    """
    One-way ANOVA
    SPSS: ONEWAY dependent_var BY factor_var /POSTHOC=TUKEY
    """
    groups = [df[df[factor_var] == group][dependent_var].dropna()
             for group in df[factor_var].unique() if pd.notna(group)]

    # ANOVA
    f_stat, p_value = stats.f_oneway(*groups)

    print(f"One-Way ANOVA: {dependent_var} by {factor_var}")
    print(f"F = {f_stat:.3f}, p = {p_value:.3f}")

    return {'f_statistic': f_stat, 'p_value': p_value}

# Correlation Analysis (SPSS: CORRELATIONS)
def correlation_analysis(df, variables):
    """
    Correlation analysis with significance tests
    SPSS: CORRELATIONS /VARIABLES=var1 var2 var3 /PRINT=TWOTAIL NOSIG
    """
    corr_matrix = df[variables].corr()

    # Calculate significance
    n = len(df[variables].dropna())
    significance_matrix = corr_matrix.copy()

    for i, var1 in enumerate(variables):
        for j, var2 in enumerate(variables):
            if i != j:
                corr = corr_matrix.loc[var1, var2]
                t_stat = corr * np.sqrt((n - 2) / (1 - corr**2))
                p_value = 2 * (1 - stats.t.cdf(abs(t_stat), n - 2))
                significance_matrix.loc[var1, var2] = p_value

    print("Correlation Matrix:")
    print(corr_matrix.round(3))
    print("\nSignificance (2-tailed):")
    print(significance_matrix.round(3))

    return corr_matrix, significance_matrix
```

---

## Customer Satisfaction Survey Analysis

### Complete Survey Analysis Workflow

```python
def complete_satisfaction_analysis(df, metadata=None):
    """
    Complete customer satisfaction survey analysis workflow
    Equivalent to a comprehensive SPSS analysis session
    """

    print("CUSTOMER SATISFACTION SURVEY ANALYSIS")
    print("=" * 60)

    # 1. Sample characteristics
    print("\n1. SAMPLE CHARACTERISTICS")
    print("-" * 30)
    print(f"Total responses: {len(df)}")
    print(f"Complete cases: {df.dropna().shape[0]}")
    print(f"Completion rate: {(df.dropna().shape[0] / len(df)) * 100:.1f}%")

    # 2. Scale reliability analysis
    print("\n2. SCALE RELIABILITY ANALYSIS")
    print("-" * 30)

    # Define scale items (adjust for your survey)
    satisfaction_scale = ['sat_overall', 'sat_quality', 'sat_service', 'sat_value']
    loyalty_scale = ['loy_recommend', 'loy_repurchase', 'loy_advocate']

    if all(item in df.columns for item in satisfaction_scale):
        sat_alpha, _ = spss_reliability_analysis(df, satisfaction_scale, "Customer Satisfaction")

    if all(item in df.columns for item in loyalty_scale):
        loy_alpha, _ = spss_reliability_analysis(df, loyalty_scale, "Customer Loyalty")

    # 3. Descriptive statistics
    print("\n3. DESCRIPTIVE STATISTICS")
    print("-" * 30)

    # Scale scores
    if all(item in df.columns for item in satisfaction_scale):
        df['satisfaction_score'] = df[satisfaction_scale].mean(axis=1)
        print(f"Satisfaction Scale (α = {sat_alpha:.3f}):")
        print(f"  Mean: {df['satisfaction_score'].mean():.2f}")
        print(f"  Std: {df['satisfaction_score'].std():.2f}")
        print(f"  Range: {df['satisfaction_score'].min():.2f} - {df['satisfaction_score'].max():.2f}")

    # 4. Driver analysis
    print("\n4. SATISFACTION DRIVER ANALYSIS")
    print("-" * 30)

    # Define predictor variables
    predictor_vars = [col for col in df.columns if any(x in col.lower() for x in ['quality', 'service', 'price', 'staff'])]

    if predictor_vars and 'satisfaction_score' in df.columns:
        driver_results = satisfaction_driver_analysis(df, predictor_vars, 'satisfaction_score')

        print("Top 5 Satisfaction Drivers:")
        for idx, row in driver_results['top_5_drivers'].iterrows():
            print(f"  {idx+1}. {row['variable']}: {row['importance_pct']:.1f}% ({row['driver_category']})")

    # 5. Group comparisons
    print("\n5. GROUP COMPARISONS")
    print("-" * 30)

    # Compare satisfaction by customer segments
    group_vars = [col for col in df.columns if any(x in col.lower() for x in ['type', 'segment', 'group', 'category'])]

    for group_var in group_vars[:2]:  # Limit to first 2 grouping variables
        if group_var in df.columns and 'satisfaction_score' in df.columns:
            print(f"\nSatisfaction by {group_var}:")
            group_means = df.groupby(group_var)['satisfaction_score'].agg(['count', 'mean', 'std'])
            print(group_means.round(3))

            # Statistical test
            if df[group_var].nunique() == 2:
                ttest_results = independent_samples_ttest(df, 'satisfaction_score', group_var)
            elif df[group_var].nunique() > 2:
                anova_results = oneway_anova(df, 'satisfaction_score', group_var)

    return df

def satisfaction_driver_analysis(df, predictor_vars, satisfaction_var):
    """
    Satisfaction driver analysis using Random Forest
    """
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score

    # Prepare data
    X = df[predictor_vars].dropna()
    y = df.loc[X.index, satisfaction_var]

    # Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X, y)

    # Feature importance
    importance_scores = pd.DataFrame({
        'variable': X.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)

    # Calculate percentages and categories
    total_importance = importance_scores['importance'].sum()
    importance_scores['importance_pct'] = importance_scores['importance'] / total_importance * 100
    importance_scores['cumulative_pct'] = importance_scores['importance_pct'].cumsum()

    # Categorize drivers
    def categorize_driver(row):
        if row['cumulative_pct'] <= 50:
            return 'Primary Driver'
        elif row['cumulative_pct'] <= 80:
            return 'Secondary Driver'
        else:
            return 'Tertiary Driver'

    importance_scores['driver_category'] = importance_scores.apply(categorize_driver, axis=1)

    # Model performance
    predictions = rf_model.predict(X)
    r2 = r2_score(y, predictions)

    return {
        'driver_importance': importance_scores,
        'top_5_drivers': importance_scores.head(5),
        'model_r2': r2,
        'model_object': rf_model
    }

# Usage
results = complete_satisfaction_analysis(df, metadata)
```

---

## Advanced Analytics Beyond SPSS

### 1. Machine Learning Integration

```python
# Predictive satisfaction modeling
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def satisfaction_prediction_model(df, satisfaction_var, predictor_vars):
    """
    Build predictive model for customer satisfaction
    Goes beyond traditional SPSS capabilities
    """

    # Create binary satisfaction target
    satisfaction_threshold = df[satisfaction_var].median()
    df['high_satisfaction'] = (df[satisfaction_var] > satisfaction_threshold).astype(int)

    # Prepare data
    X = df[predictor_vars].dropna()
    y = df.loc[X.index, 'high_satisfaction']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Predictions
    y_pred = rf_classifier.predict(X_test)

    print("Satisfaction Prediction Model Results:")
    print(classification_report(y_test, y_pred))

    return rf_classifier

# Real-time satisfaction monitoring
def create_satisfaction_dashboard_data(df, time_var='survey_date'):
    """
    Prepare data for real-time satisfaction monitoring
    Advanced capability beyond SPSS
    """

    df[time_var] = pd.to_datetime(df[time_var])

    # Weekly trends
    df['week'] = df[time_var].dt.to_period('W')
    weekly_satisfaction = df.groupby('week')['satisfaction_score'].agg(['mean', 'count', 'std'])

    # Recent trend analysis
    recent_weeks = weekly_satisfaction.tail(8)
    trend_slope = np.polyfit(range(len(recent_weeks)), recent_weeks['mean'], 1)[0]

    dashboard_data = {
        'current_satisfaction': df['satisfaction_score'].tail(100).mean(),
        'weekly_trends': weekly_satisfaction,
        'trend_direction': 'Improving' if trend_slope > 0 else 'Declining',
        'alert_level': 'High' if trend_slope < -0.1 else 'Normal'
    }

    return dashboard_data
```

### 2. Structural Equation Modeling

```python
# Basic SEM setup (requires semopy)
try:
    import semopy

    def satisfaction_sem_model(df):
        """
        Structural Equation Model for satisfaction
        Advanced technique beyond SPSS capabilities
        """

        model_spec = """
        # Measurement model
        ServiceQuality =~ sq_reliability + sq_responsiveness + sq_assurance
        Satisfaction =~ sat_overall + sat_quality + sat_service
        Loyalty =~ loy_recommend + loy_repurchase + loy_advocate

        # Structural model
        Satisfaction ~ ServiceQuality
        Loyalty ~ Satisfaction + ServiceQuality
        """

        model = semopy.Model(model_spec)
        results = model.fit(df)

        print("SEM Model Fit Statistics:")
        fit_stats = semopy.calc_stats(model)
        print(fit_stats)

        return model, results

except ImportError:
    print("semopy not available. Install with: pip install semopy")
```

---

## Troubleshooting and Best Practices

### Common Issues and Solutions

#### 1. SPSS File Import Issues

**Problem**: Cannot read SPSS file or missing metadata
```python
# Solution: Try different encoding
df, meta = pyreadstat.read_sav('file.sav', encoding='utf-8')

# Alternative: Use different SPSS reader
import pandas as pd
df = pd.read_spss('file.sav')  # Basic import without metadata
```

#### 2. Missing Data Handling

**Problem**: Different missing data handling than SPSS
```python
# SPSS MISSING VALUES treatment
# Python equivalent with explicit missing value codes
df = df.replace([99, 999, -99], np.nan)  # Define missing value codes
df = df.replace([' ', ''], np.nan)  # Handle string missing values

# Listwise deletion (SPSS default)
df_complete = df.dropna()

# Pairwise deletion for correlations
correlation_matrix = df.corr(min_periods=1)
```

#### 3. Variable Type Conversion

**Problem**: SPSS variable types not preserved
```python
# Convert to appropriate pandas types
def convert_spss_types(df, metadata):
    """Convert variables based on SPSS measurement levels"""

    if 'variable_types' in metadata:
        for var, var_type in metadata['variable_types'].items():
            if var in df.columns:
                if var_type == 'nominal':
                    df[var] = pd.Categorical(df[var])
                elif var_type == 'ordinal':
                    # Preserve order if value labels exist
                    if var in metadata.get('value_labels', {}):
                        categories = list(metadata['value_labels'][var].values())
                        df[var] = pd.Categorical(df[var], categories=categories, ordered=True)
                    else:
                        df[var] = pd.Categorical(df[var], ordered=True)

    return df
```

### Best Practices

#### 1. Reproducible Analysis

```python
# Set random seeds for reproducibility
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# Document analysis decisions
analysis_log = {
    'date': '2025-07-24',
    'analyst': 'Your Name',
    'data_file': 'customer_survey_2025.sav',
    'sample_size': len(df),
    'missing_data_treatment': 'listwise deletion',
    'significance_level': 0.05,
    'scale_reliability_threshold': 0.7
}
```

#### 2. Code Documentation

```python
def analyze_satisfaction_survey(df, config=None):
    """
    Comprehensive customer satisfaction survey analysis

    Parameters:
    -----------
    df : pandas.DataFrame
        Survey data with satisfaction and predictor variables
    config : dict, optional
        Analysis configuration parameters

    Returns:
    --------
    dict
        Analysis results including reliability, descriptives, and drivers

    Example:
    --------
    >>> results = analyze_satisfaction_survey(df)
    >>> print(f"Satisfaction reliability: {results['reliability']['satisfaction']:.3f}")
    """

    if config is None:
        config = {
            'satisfaction_items': ['sat_overall', 'sat_quality', 'sat_service'],
            'driver_variables': ['sq_reliability', 'sq_responsiveness'],
            'group_variables': ['customer_type', 'region']
        }

    # Analysis implementation here
    pass
```

#### 3. Error Handling

```python
def safe_cronbach_alpha(df, items):
    """Calculate Cronbach's Alpha with error handling"""

    try:
        # Check if all items exist
        missing_items = [item for item in items if item not in df.columns]
        if missing_items:
            print(f"Warning: Missing items {missing_items}")
            items = [item for item in items if item in df.columns]

        # Check minimum number of items
        if len(items) < 2:
            print("Error: Need at least 2 items for reliability analysis")
            return None

        # Calculate alpha
        item_data = df[items].dropna()
        if len(item_data) < 10:
            print("Warning: Small sample size for reliability analysis")

        return cronbach_alpha(item_data, items)

    except Exception as e:
        print(f"Error calculating Cronbach's Alpha: {e}")
        return None
```

---

## Resources and Further Learning

### Essential Documentation

1. **Domain Knowledge Files** (in `/domain-knowledge/` folder):
   - `SPSS-PYTHON-EQUIVALENTS.md` - Complete procedure mapping
   - `CUSTOMER-SATISFACTION-METHODOLOGIES.md` - Advanced survey analysis
   - `SCALE-DEVELOPMENT-VALIDATION.md` - Psychometric analysis
   - `STRUCTURAL-EQUATION-MODELING.md` - Advanced SEM techniques
   - `SPSS-IMPLEMENTATION-GUIDE.md` - Step-by-step implementations

### Python Libraries Documentation

1. **Core Libraries**:
   - [pandas](https://pandas.pydata.org/docs/) - Data manipulation
   - [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) - Statistical functions
   - [statsmodels](https://www.statsmodels.org/stable/) - Statistical modeling

2. **Specialized Libraries**:
   - [pyreadstat](https://pyreadstat.readthedocs.io/) - SPSS file reading
   - [factor-analyzer](https://factor-analyzer.readthedocs.io/) - Factor analysis
   - [pingouin](https://pingouin-stats.org/) - Advanced statistics
   - [semopy](https://semopy.com/) - Structural equation modeling

### Sample Analysis Templates

#### Quick Reliability Check
```python
# Template for quick scale reliability assessment
def quick_reliability_check(df, scale_items):
    alpha = cronbach_alpha(df, scale_items)
    n_items = len(scale_items)
    valid_cases = df[scale_items].dropna().shape[0]

    print(f"Scale Reliability Summary:")
    print(f"  Items: {n_items}")
    print(f"  Valid cases: {valid_cases}")
    print(f"  Cronbach's α: {alpha:.3f}")
    print(f"  Interpretation: {'Acceptable' if alpha >= 0.7 else 'Below threshold'}")

    return alpha
```

#### Quick Driver Analysis
```python
# Template for satisfaction driver identification
def quick_driver_analysis(df, satisfaction_var, predictor_vars):
    from sklearn.ensemble import RandomForestRegressor

    X = df[predictor_vars].dropna()
    y = df.loc[X.index, satisfaction_var]

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X, y)

    drivers = pd.DataFrame({
        'Variable': X.columns,
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False)

    print("Top 5 Satisfaction Drivers:")
    for idx, row in drivers.head(5).iterrows():
        print(f"  {row['Variable']}: {row['Importance']:.3f}")

    return drivers
```

### Getting Help

1. **Check the domain knowledge files** for comprehensive examples
2. **Review error messages** carefully - most issues are data-related
3. **Use Python's help system**: `help(function_name)` or `function_name?` in Jupyter
4. **Test with small data samples** before running on full dataset

---

**End of SPSS Integration Manual**

This manual provides the foundation for transitioning from SPSS to Python for customer satisfaction survey analysis. For advanced techniques and comprehensive examples, refer to the domain knowledge files in the `/domain-knowledge/` folder.
