# SPSS Unified Reporting Script Architecture Guide

## 📋 Overview

This guide documents the methodology and architecture for creating unified reporting scripts for SPSS data analysis. The pattern established with `generate_unified_report.py` provides a template for future SPSS file analysis workflows.

## 🏗️ Script Architecture Pattern

### 1. Core Dependencies & Setup
```python
#!/usr/bin/env python3
"""
UNIFIED COMPREHENSIVE ANALYSIS REPORT GENERATOR
Consolidates ALL statistical analyses into a single executive-ready document
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pyreadstat        # Critical for SPSS .sav file loading
import datetime
from io import BytesIO
import base64
from matplotlib.patches import Circle

# Path configuration for standalone execution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```

### 2. SPSS Data Loading Pattern
```python
# Load and process SPSS data
print("🔄 Loading SPSS data and recreating analysis variables...")

# Read SPSS file with metadata preservation
spss_file_path = '../notebooks/[FILENAME].sav'
analysis_data, metadata = pyreadstat.read_sav(spss_file_path)

# Inspect data structure (for development)
print(f"📊 Dataset shape: {analysis_data.shape}")
print(f"📋 Variables: {list(analysis_data.columns)}")
print(f"🔍 Data types: {analysis_data.dtypes}")
```

### 3. Statistical Analysis Pipeline

#### A. Correlation Analysis
```python
# Calculate correlation matrix for key variables
correlation_matrix = analysis_data[['VAR1', 'VAR2', 'VAR3']].corr()

# Extract specific correlations
correlation_1 = correlation_matrix.loc['VAR1', 'VAR2']
correlation_2 = correlation_matrix.loc['VAR2', 'VAR3']
correlation_3 = correlation_matrix.loc['VAR1', 'VAR3']
```

#### B. Normality Testing
```python
# Perform normality tests for all continuous variables
normality_results = {}
for var in ['VAR1', 'VAR2', 'VAR3']:
    statistic, p_value = stats.shapiro(analysis_data[var])
    normality_results[var] = {'statistic': statistic, 'p_value': p_value}
```

#### C. Group Comparisons (T-tests)
```python
# Define groups based on categorical variables
group1 = analysis_data[analysis_data['GROUPVAR'] == 1]['OUTCOME']
group2 = analysis_data[analysis_data['GROUPVAR'] == 2]['OUTCOME']

# Test assumptions (equal variances)
levene_stat, levene_p = stats.levene(group1, group2)
equal_var = levene_p > 0.05

# Perform t-test
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=equal_var)

# Calculate effect size (Cohen's d)
pooled_std = np.sqrt(((len(group1)-1)*group1.var() +
                     (len(group2)-1)*group2.var()) /
                    (len(group1) + len(group2) - 2))
cohens_d = (group1.mean() - group2.mean()) / pooled_std
```

#### D. Effect Size Interpretation
```python
# Cohen's d interpretation
def interpret_cohens_d(d):
    if abs(d) < 0.2:
        return "Small"
    elif abs(d) < 0.5:
        return "Small to Medium"
    elif abs(d) < 0.8:
        return "Medium to Large"
    else:
        return "Large"
```

### 4. Visualization Pipeline

#### A. Chart Creation Pattern
```python
def create_visualizations():
    charts = []

    # 1. Correlation Matrix Heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, annot=True, mask=mask, cmap='RdYlBu_r',
                center=0, square=True, linewidths=0.5,
                cbar_kws={"shrink": .8}, fmt='.3f')
    plt.title('DATASET NAME - Correlation Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()

    # Save as base64 for embedding
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    img_data = base64.b64encode(buffer.getvalue()).decode()
    charts.append(('Correlation Analysis', img_data))
    plt.close()

    return charts
```

#### B. Multi-Panel Dashboard
```python
# 2. Comprehensive Analysis Dashboard
fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle('DATASET NAME - Analysis Dashboard', fontsize=16, fontweight='bold')

# Panel 1: Correlation heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0, ax=axes[0,0])
axes[0,0].set_title('Correlation Matrix')

# Panel 2-4: Scatter plots with correlations
axes[0,1].scatter(analysis_data['VAR1'], analysis_data['VAR2'], alpha=0.6, color='blue')
axes[0,1].set_xlabel('Variable 1')
axes[0,1].set_ylabel('Variable 2')
axes[0,1].set_title(f'VAR1 vs VAR2 (r={correlation_1:.3f})')

# Panel 5-6: Distribution plots
axes[2,0].hist(analysis_data['VAR1'], bins=20, alpha=0.7, color='skyblue')
axes[2,0].set_xlabel('Variable 1')
axes[2,0].set_ylabel('Frequency')
axes[2,0].set_title('Variable 1 Distribution')
```

### 5. Report Generation Template

#### A. Executive Summary Structure
```python
comprehensive_report = f'''# 📊 UNIFIED COMPREHENSIVE ANALYSIS REPORT
## [DATASET NAME] Analytics Excellence
### Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📋 EXECUTIVE SUMMARY

**Dataset:** [DATASET DESCRIPTION]
**Sample Size:** {len(analysis_data)} responses
**Data Completeness:** {(1 - analysis_data.isnull().sum().sum() / (len(analysis_data) * len(analysis_data.columns))) * 100:.1f}%
**Analysis Framework:** Scholar-Practitioner SPSS-Python Integration Excellence

### 🎯 Key Business Insights
• **Primary finding 1** (statistical details)
• **Primary finding 2** (statistical details)
• **Primary finding 3** (statistical details)
'''
```

#### B. Statistical Results Section
```python
## 🧪 ADVANCED STATISTICAL TESTING RESULTS

### Normality Assessment (Shapiro-Wilk Tests)
- **Variable 1:** W = {normality_results['VAR1']['statistic']:.4f}, p = {normality_results['VAR1']['p_value']:.3f}
- **Variable 2:** W = {normality_results['VAR2']['statistic']:.4f}, p = {normality_results['VAR2']['p_value']:.3f}

### Independent T-Tests Analysis
- **Group 1:** Mean = {group1.mean():.2f} (SD = {group1.std():.2f})
- **Group 2:** Mean = {group2.mean():.2f} (SD = {group2.std():.2f})
- **t-statistic:** {t_stat:.3f}
- **p-value:** {p_value:.3f}
- **Cohen's d:** {cohens_d:.3f} ({interpret_cohens_d(cohens_d)} effect size)
```

### 6. File Management Pattern

#### A. Output Directory Structure
```python
# Save unified comprehensive report to scripts/results/
report_filename = f"UNIFIED_ANALYSIS_{DATASET_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results'))
os.makedirs(results_dir, exist_ok=True)
file_path = os.path.join(results_dir, report_filename)
```

#### B. Return Metadata
```python
return {
    'filename': report_filename,
    'content': comprehensive_report,
    'charts_embedded': len(charts),
    'statistical_tests_included': test_count,
    'file_size_mb': len(comprehensive_report) / (1024*1024),
    'success': True
}
```

## 🔄 Customization Guidelines for New SPSS Files

### 1. Variable Identification
- Examine SPSS variable labels using `metadata.column_labels`
- Identify continuous vs categorical variables
- Map business concepts to variable names

### 2. Analysis Strategy
- **Descriptive**: Always include means, SDs, distributions
- **Correlational**: Focus on key business relationships
- **Inferential**: T-tests, ANOVA based on research questions
- **Effect Sizes**: Always calculate and interpret Cohen's d

### 3. Visualization Customization
- Adapt chart titles to business context
- Modify color schemes for brand alignment
- Adjust figure sizes based on variable count
- Include correlation values in scatter plots

### 4. Business Context Integration
- Customize executive summary for domain
- Align recommendations with organizational goals
- Include domain-specific interpretation
- Map statistical findings to business actions

## 📊 Template Checklist for New SPSS Scripts

### Pre-Development
- [ ] Examine SPSS file structure and variables
- [ ] Identify key research questions
- [ ] Determine appropriate statistical tests
- [ ] Plan visualization strategy

### Core Implementation
- [ ] SPSS data loading with metadata
- [ ] Variable selection and preprocessing
- [ ] Statistical analysis pipeline
- [ ] Visualization generation
- [ ] Report template customization

### Quality Assurance
- [ ] Test with sample data
- [ ] Validate statistical calculations
- [ ] Check visualization quality (300 DPI)
- [ ] Verify report formatting
- [ ] Test standalone execution

### Documentation
- [ ] Update script docstring
- [ ] Add usage examples
- [ ] Document variable mappings
- [ ] Include business context

## 🚀 Future Enhancement Opportunities

### Advanced Analytics
- **Machine Learning Integration**: Predictive modeling capabilities
- **Advanced SEM**: Full structural equation modeling with lavaan-style syntax
- **Multilevel Modeling**: Hierarchical data analysis
- **Time Series**: Longitudinal analysis capabilities

### Automation Features
- **Batch Processing**: Multiple SPSS files in sequence
- **Template Engine**: Dynamic report generation
- **Email Integration**: Automated distribution
- **Dashboard Updates**: Live data refresh

### Enterprise Features
- **Version Control**: Report versioning and comparison
- **Audit Trails**: Analysis reproducibility
- **Access Controls**: Secure data handling
- **Compliance Reporting**: Regulatory requirements

---

*This architecture guide provides the foundation for creating standardized, high-quality SPSS analysis scripts that maintain consistency while allowing for domain-specific customization.*
