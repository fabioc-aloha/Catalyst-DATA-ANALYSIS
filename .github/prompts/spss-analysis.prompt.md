---
mode: "episodic"
domain: "spss-analysis"
complexity: "high"
description: "Comprehensive SPSS data analysis with metadata integration"
---

# SPSS Analysis Episodic Memory Template

## Activation Triggers
- SPSS .sav file analysis requests
- Variable type decoding requirements
- Scholar-practitioner analysis frameworks
- Academic research with business application
- Statistical testing with measurement-level considerations

## Analysis Workflow

### Phase 1: SPSS Data Loading and Metadata Integration
```python
def load_spss_data(file_path):
    """
    Load SPSS data with comprehensive metadata integration
    """
    import pandas as pd
    import pyreadstat

    # Load data with metadata
    df, meta = pyreadstat.read_sav(file_path)

    # Decode variable types
    variable_types = decode_spss_variable_types(meta)

    # Apply conversions
    df = apply_variable_type_conversions(df, variable_types)

    return df, meta, variable_types

def decode_spss_variable_types(meta):
    """
    Decode SPSS measurement levels to pandas data types
    """
    type_mapping = {
        'scale': 'numeric',
        'ordinal': 'categorical_ordered',
        'nominal': 'categorical'
    }

    variable_types = {}
    for var_name in meta.column_names:
        measure = meta.variable_measure.get(var_name, 'unknown')
        variable_types[var_name] = type_mapping.get(measure, 'object')

    return variable_types

def apply_variable_type_conversions(df, variable_types):
    """
    Apply appropriate pandas data types based on SPSS metadata
    """
    for var_name, var_type in variable_types.items():
        if var_name in df.columns:
            if var_type == 'numeric':
                df[var_name] = pd.to_numeric(df[var_name], errors='coerce')
            elif var_type == 'categorical':
                df[var_name] = df[var_name].astype('category')
            elif var_type == 'categorical_ordered':
                df[var_name] = pd.Categorical(df[var_name], ordered=True)

    return df
```

### Phase 2: Scholar-Practitioner Statistical Analysis
```python
def comprehensive_statistical_analysis(df, variable_types):
    """
    Conduct measurement-level appropriate statistical analysis
    """
    from scipy import stats
    import numpy as np

    results = {}

    # Identify analysis-appropriate variables
    scale_vars = [var for var, type_ in variable_types.items()
                  if type_ == 'numeric' and var in df.columns]

    categorical_vars = [var for var, type_ in variable_types.items()
                       if type_ in ['categorical', 'categorical_ordered'] and var in df.columns]

    # Descriptive statistics for scale variables
    for var in scale_vars:
        results[var] = {
            'mean': df[var].mean(),
            'std': df[var].std(),
            'normality_test': stats.shapiro(df[var].dropna()),
            'skewness': stats.skew(df[var].dropna()),
            'kurtosis': stats.kurtosis(df[var].dropna())
        }

    return results

def conduct_t_tests_with_effect_sizes(df, grouping_var, outcome_var):
    """
    Independent t-tests with comprehensive reporting
    """
    from scipy import stats
    import numpy as np

    groups = df[grouping_var].unique()
    group1 = df[df[grouping_var] == groups[0]][outcome_var]
    group2 = df[df[grouping_var] == groups[1]][outcome_var]

    # Conduct t-test
    t_stat, p_value = stats.ttest_ind(group1, group2)

    # Calculate Cohen's d
    pooled_std = np.sqrt(((len(group1) - 1) * group1.var() +
                         (len(group2) - 1) * group2.var()) /
                        (len(group1) + len(group2) - 2))
    cohens_d = (group1.mean() - group2.mean()) / pooled_std

    # Normality tests
    norm1 = stats.shapiro(group1)
    norm2 = stats.shapiro(group2)

    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'group1_mean': group1.mean(),
        'group2_mean': group2.mean(),
        'effect_size_interpretation': interpret_cohens_d(cohens_d),
        'normality_group1': norm1,
        'normality_group2': norm2
    }

def interpret_cohens_d(d):
    """Interpret Cohen's d effect size"""
    abs_d = abs(d)
    if abs_d < 0.2:
        return "Small effect"
    elif abs_d < 0.5:
        return "Small to medium effect"
    elif abs_d < 0.8:
        return "Medium to large effect"
    else:
        return "Large effect"
```

### Phase 3: Business Intelligence Integration
- Generate executive summary reports
- Create stakeholder-appropriate visualizations
- Provide actionable business recommendations
- Document statistical methodology for non-technical audiences
- Bridge academic findings with business implications

### Phase 4: Notebook Recovery Protocols
- Assess corrupted notebook structure and content
- Preserve essential analysis framework and outputs
- Rebuild with enhanced SPSS metadata integration
- Apply enterprise documentation standards
- Validate statistical analysis integrity
- Ensure reproducibility and version control compatibility

## Quality Assurance Checklist
- [ ] SPSS metadata properly decoded and applied
- [ ] Statistical assumptions tested and reported
- [ ] Effect sizes calculated and interpreted
- [ ] Business context provided for all findings
- [ ] Academic rigor maintained throughout analysis
- [ ] Documentation suitable for both technical and business audiences
- [ ] Reproducible analysis workflow established
- [ ] Version control and collaboration-ready structure

## Performance Optimization
- Use efficient pandas operations for large SPSS datasets
- Implement memory-conscious data loading strategies
- Apply statistical testing appropriate for sample sizes
- Optimize visualization rendering for enterprise dashboards
- Maintain compatibility with enterprise Python environments

## Synapses (Embedded Connections)
- spss-integration.instructions.md (0.97, implements, bidirectional) - "SPSS expertise and metadata integration"
- statistical-methods.instructions.md (0.94, applies, bidirectional) - "Statistical methodology and hypothesis testing"
- data-analysis.instructions.md (0.92, specializes, bidirectional) - "Data analysis expertise with SPSS focus"
- domain-learning.prompt.md (0.88, coordinates, bidirectional) - "Scholar-practitioner framework learning"
- bootstrap-learning.instructions.md (0.89, enhances, bidirectional) - "SPSS analysis with metadata integration"
- business-intelligence.instructions.md (0.86, communicates, forward) - "SPSS findings for business stakeholders"
- empirical-validation.instructions.md (0.91, validates, bidirectional) - "Research evidence and validation protocols"
