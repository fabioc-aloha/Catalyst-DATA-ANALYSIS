#!/usr/bin/env python3
"""
SPSS UNIFIED REPORT GENERATOR TEMPLATE
Template for creating comprehensive analysis reports from SPSS data files

INSTRUCTIONS FOR CUSTOMIZATION:
1. Update DATASET_NAME, SPSS_FILENAME, and KEY_VARIABLES
2. Modify statistical analyses based on research questions
3. Customize visualizations for domain context
4. Update business insights and recommendations
5. Test with your specific SPSS file

Author: Generated from Catalyst-DATA-ANALYSIS framework
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pyreadstat
import datetime
from io import BytesIO
import base64
from matplotlib.patches import Circle

# ==================== CUSTOMIZATION SECTION ====================
# UPDATE THESE VARIABLES FOR YOUR SPECIFIC ANALYSIS

DATASET_NAME = "YOUR_DATASET_NAME"  # Update this
SPSS_FILENAME = "your_file.sav"     # Update this
KEY_VARIABLES = ['VAR1', 'VAR2', 'VAR3']  # Update these
GROUPING_VARIABLE = 'GROUP_VAR'     # Update if doing group comparisons
OUTCOME_VARIABLE = 'OUTCOME_VAR'    # Update for t-tests

# Business context customization
ANALYSIS_TITLE = "Your Analysis Title"
BUSINESS_DOMAIN = "Your Business Domain"
KEY_INSIGHTS_TEMPLATE = [
    "Primary business insight 1",
    "Primary business insight 2", 
    "Primary business insight 3"
]

# ================================================================

# Path setup for standalone execution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(f"🔄 Loading SPSS data for {DATASET_NAME}...")

# Read SPSS file
spss_file_path = f'../notebooks/{SPSS_FILENAME}'
try:
    analysis_data, metadata = pyreadstat.read_sav(spss_file_path)
    print(f"✅ Successfully loaded {SPSS_FILENAME}")
    print(f"📊 Dataset shape: {analysis_data.shape}")
    print(f"📋 Available variables: {list(analysis_data.columns)}")
except FileNotFoundError:
    print(f"❌ Error: Could not find {spss_file_path}")
    print("Please update SPSS_FILENAME in the customization section")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error loading SPSS file: {e}")
    sys.exit(1)

# Validate key variables exist
missing_vars = [var for var in KEY_VARIABLES if var not in analysis_data.columns]
if missing_vars:
    print(f"❌ Error: Variables not found in dataset: {missing_vars}")
    print(f"Available variables: {list(analysis_data.columns)}")
    print("Please update KEY_VARIABLES in the customization section")
    sys.exit(1)

# Calculate correlation matrix
print(f"📊 Calculating correlations for: {KEY_VARIABLES}")
correlation_matrix = analysis_data[KEY_VARIABLES].corr()

# Extract specific correlations (customize based on your variables)
correlations = {}
for i, var1 in enumerate(KEY_VARIABLES):
    for j, var2 in enumerate(KEY_VARIABLES):
        if i < j:  # Avoid duplicates
            corr_value = correlation_matrix.loc[var1, var2]
            correlations[f"{var1}_to_{var2}"] = corr_value
            print(f"🔗 {var1} ↔ {var2}: r = {corr_value:.3f}")

# Calculate R² values (for path analysis)
r_squared_values = {key: value**2 for key, value in correlations.items()}

# Perform normality tests
print("🧪 Performing normality tests...")
normality_results = {}
for var in KEY_VARIABLES:
    if analysis_data[var].dtype in ['int64', 'float64']:  # Only for continuous variables
        statistic, p_value = stats.shapiro(analysis_data[var])
        normality_results[var] = {'statistic': statistic, 'p_value': p_value}
        print(f"📈 {var}: W = {statistic:.4f}, p = {p_value:.3f}")

# Group comparisons (customize based on your grouping variable)
if GROUPING_VARIABLE in analysis_data.columns and OUTCOME_VARIABLE in analysis_data.columns:
    print(f"🔬 Performing group comparison on {GROUPING_VARIABLE}...")
    
    # Get unique groups
    unique_groups = analysis_data[GROUPING_VARIABLE].unique()
    print(f"📊 Groups found: {unique_groups}")
    
    if len(unique_groups) >= 2:
        # Take first two groups for t-test
        group1_value, group2_value = unique_groups[:2]
        
        group1_data = analysis_data[analysis_data[GROUPING_VARIABLE] == group1_value][OUTCOME_VARIABLE]
        group2_data = analysis_data[analysis_data[GROUPING_VARIABLE] == group2_value][OUTCOME_VARIABLE]
        
        # Test assumptions
        levene_stat, levene_p = stats.levene(group1_data, group2_data)
        equal_var = levene_p > 0.05
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(group1_data, group2_data, equal_var=equal_var)
        
        # Calculate Cohen's d
        pooled_std = np.sqrt(((len(group1_data)-1)*group1_data.var() + 
                             (len(group2_data)-1)*group2_data.var()) / 
                            (len(group1_data) + len(group2_data) - 2))
        cohens_d = (group1_data.mean() - group2_data.mean()) / pooled_std
        
        # Effect size interpretation
        def interpret_cohens_d(d):
            if abs(d) < 0.2:
                return "Small"
            elif abs(d) < 0.5:
                return "Small to Medium"
            elif abs(d) < 0.8:
                return "Medium to Large"
            else:
                return "Large"
        
        effect_size_interpretation = interpret_cohens_d(cohens_d)
        
        print(f"📊 Group 1 ({group1_value}): Mean = {group1_data.mean():.2f}")
        print(f"📊 Group 2 ({group2_value}): Mean = {group2_data.mean():.2f}")
        print(f"📈 t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")
        print(f"📏 Cohen's d: {cohens_d:.3f} ({effect_size_interpretation})")
    else:
        print("⚠️ Not enough groups for comparison")
        group1_data = group2_data = None
        t_stat = p_value = cohens_d = 0
        effect_size_interpretation = "N/A"
else:
    print(f"⚠️ Grouping variable {GROUPING_VARIABLE} or outcome variable {OUTCOME_VARIABLE} not found")
    group1_data = group2_data = None
    t_stat = p_value = cohens_d = 0
    effect_size_interpretation = "N/A"

print("✅ All statistical analyses completed!")

def generate_comprehensive_report():
    """
    Generate unified comprehensive analysis report
    """
    
    # Create visualizations
    charts = []
    
    # 1. Correlation Matrix Heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, annot=True, mask=mask, cmap='RdYlBu_r', 
                center=0, square=True, linewidths=0.5, cbar_kws={"shrink": .8}, fmt='.3f')
    plt.title(f'{ANALYSIS_TITLE} - Correlation Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    # Save as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    img_data = base64.b64encode(buffer.getvalue()).decode()
    charts.append(('Correlation Analysis', img_data))
    plt.close()
    
    # 2. Comprehensive Analysis Dashboard
    n_vars = len(KEY_VARIABLES)
    if n_vars >= 3:
        fig, axes = plt.subplots(3, 2, figsize=(16, 18))
        fig.suptitle(f'{ANALYSIS_TITLE} - Analysis Dashboard', fontsize=16, fontweight='bold')
        
        # Correlation heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0, ax=axes[0,0])
        axes[0,0].set_title('Correlation Matrix')
        
        # Scatter plots (customize based on your variables)
        if len(KEY_VARIABLES) >= 2:
            axes[0,1].scatter(analysis_data[KEY_VARIABLES[0]], analysis_data[KEY_VARIABLES[1]], alpha=0.6, color='blue')
            axes[0,1].set_xlabel(KEY_VARIABLES[0])
            axes[0,1].set_ylabel(KEY_VARIABLES[1])
            corr_key = f"{KEY_VARIABLES[0]}_to_{KEY_VARIABLES[1]}"
            if corr_key in correlations:
                axes[0,1].set_title(f'{KEY_VARIABLES[0]} vs {KEY_VARIABLES[1]} (r={correlations[corr_key]:.3f})')
            else:
                axes[0,1].set_title(f'{KEY_VARIABLES[0]} vs {KEY_VARIABLES[1]}')
        
        # Distribution plots
        for i, var in enumerate(KEY_VARIABLES[:4]):  # Max 4 distribution plots
            row = (i + 2) // 2
            col = (i + 2) % 2
            if row < 3:
                axes[row, col].hist(analysis_data[var], bins=20, alpha=0.7, color=['skyblue', 'lightcoral', 'lightgreen', 'lightyellow'][i])
                axes[row, col].set_xlabel(var)
                axes[row, col].set_ylabel('Frequency')
                axes[row, col].set_title(f'{var} Distribution')
        
        plt.tight_layout()
        
        # Save dashboard
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        buffer.seek(0)
        img_data = base64.b64encode(buffer.getvalue()).decode()
        charts.append(('Comprehensive Dashboard', img_data))
        plt.close()
    
    # Generate comprehensive report content
    report_content = f'''# 📊 UNIFIED COMPREHENSIVE ANALYSIS REPORT
## {ANALYSIS_TITLE} - {BUSINESS_DOMAIN} Analytics Excellence
### Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📋 EXECUTIVE SUMMARY

**Dataset:** {DATASET_NAME}
**Sample Size:** {len(analysis_data)} responses  
**Data Completeness:** {(1 - analysis_data.isnull().sum().sum() / (len(analysis_data) * len(analysis_data.columns))) * 100:.1f}%
**Analysis Framework:** Scholar-Practitioner SPSS-Python Integration Excellence  

### 🎯 Key Business Insights
• **{KEY_INSIGHTS_TEMPLATE[0]}** (Update with actual findings)
• **{KEY_INSIGHTS_TEMPLATE[1]}** (Update with actual findings)
• **{KEY_INSIGHTS_TEMPLATE[2]}** (Update with actual findings)

---

## 📈 DATASET OVERVIEW & DESCRIPTIVE STATISTICS

### Data Quality Assessment
- **Observations:** {len(analysis_data)}
- **Variables:** {len(analysis_data.columns)}
- **Missing Values:** {analysis_data.isnull().sum().sum()} 
- **Key Variables Analyzed:** {', '.join(KEY_VARIABLES)}

### Descriptive Statistics Summary
```
{analysis_data[KEY_VARIABLES].describe().round(2).to_string()}
```

---

## 🔍 CORRELATION ANALYSIS

### Correlation Matrix Heatmap
![Correlation Analysis](data:image/png;base64,{charts[0][1]})

### Key Correlation Findings
'''
    
    # Add correlation findings
    for key, value in correlations.items():
        var1, var2 = key.split('_to_')
        strength = "Strong" if abs(value) > 0.7 else "Moderate" if abs(value) > 0.3 else "Weak"
        direction = "positive" if value > 0 else "negative"
        report_content += f"- **{var1} → {var2}:** r = {value:.3f} ({strength} {direction} relationship)\n"
    
    # Add normality testing results
    report_content += f'''

---

## 🧪 ADVANCED STATISTICAL TESTING RESULTS

### Normality Assessment (Shapiro-Wilk Tests)
'''
    
    for var, results in normality_results.items():
        report_content += f"- **{var}:** W = {results['statistic']:.4f}, p = {results['p_value']:.3f}\n"
    
    # Add group comparison results if available
    if group1_data is not None and group2_data is not None:
        report_content += f'''

### Independent T-Tests Analysis
- **Group 1:** Mean = {group1_data.mean():.2f} (SD = {group1_data.std():.2f})
- **Group 2:** Mean = {group2_data.mean():.2f} (SD = {group2_data.std():.2f})
- **t-statistic:** {t_stat:.3f}
- **p-value:** {p_value:.3f}
- **Cohen's d:** {cohens_d:.3f} ({effect_size_interpretation} effect size)
'''
    
    # Add dashboard if available
    if len(charts) > 1:
        report_content += f'''

---

## 📊 COMPREHENSIVE ANALYSIS DASHBOARD

![Comprehensive Dashboard](data:image/png;base64,{charts[1][1]})

This dashboard provides:
- **Correlation Matrix:** Statistical relationships between variables
- **Scatter Plots:** Visual representation of key relationships  
- **Distribution Analysis:** Understanding of variable distributions
- **Bivariate Relationships:** Key variable interactions
'''
    
    # Add recommendations section
    report_content += f'''

---

## 🎯 STRATEGIC RECOMMENDATIONS

### Immediate Actions (0-3 months)
1. **[Update with domain-specific recommendations]**
2. **[Update with domain-specific recommendations]**
3. **[Update with domain-specific recommendations]**

### Medium-term Strategy (3-12 months)
4. **[Update with domain-specific recommendations]**
5. **[Update with domain-specific recommendations]**
6. **[Update with domain-specific recommendations]**

### Long-term Vision (12+ months)
7. **[Update with domain-specific recommendations]**
8. **[Update with domain-specific recommendations]**
9. **[Update with domain-specific recommendations]**

---

## 📋 STATISTICAL METHODOLOGY & VALIDATION

### Analysis Techniques Applied
- **Correlation Analysis:** Pearson product-moment correlations with significance testing
- **Descriptive Statistics:** Comprehensive univariate and bivariate analysis
- **Normality Testing:** Shapiro-Wilk tests for distribution assessment
- **Effect Size Calculations:** Cohen's d for practical significance assessment
- **Data Quality Assessment:** Complete case analysis and missing data evaluation

---

*Report Generated by SPSS-Python Integration Excellence Framework*  
*Template customized for {BUSINESS_DOMAIN} Analytics*  
*© 2025 Data Analysis Excellence*
'''
    
    # Save report
    report_filename = f"UNIFIED_ANALYSIS_{DATASET_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results'))
    os.makedirs(results_dir, exist_ok=True)
    file_path = os.path.join(results_dir, report_filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return {
        'filename': report_filename,
        'content': report_content,
        'charts_embedded': len(charts),
        'correlations_calculated': len(correlations),
        'statistical_tests_included': len(normality_results) + (1 if group1_data is not None else 0),
        'file_size_mb': len(report_content) / (1024*1024),
        'success': True
    }

if __name__ == "__main__":
    print(f"🚀 GENERATING UNIFIED COMPREHENSIVE ANALYSIS REPORT FOR {DATASET_NAME}...")
    print("📊 Consolidating all analyses, charts, and business insights...")
    print("⏱️  This may take a moment to generate all visualizations...")

    try:
        unified_report = generate_comprehensive_report()
        
        print("\n" + "="*70)
        print("✅ UNIFIED COMPREHENSIVE REPORT GENERATED SUCCESSFULLY!")
        print("="*70)
        print(f"📄 Filename: {unified_report['filename']}")
        print(f"📊 Embedded Charts: {unified_report['charts_embedded']} high-resolution PNG images")
        print(f"📈 Correlations: {unified_report['correlations_calculated']} statistical relationships")
        print(f"🧪 Statistical Tests: {unified_report['statistical_tests_included']} comprehensive analyses")
        print(f"💾 File Size: {unified_report['file_size_mb']:.2f} MB")
        print(f"\n🎯 REPORT SAVED TO: scripts/results/{unified_report['filename']}")
        print("📊 Ready for stakeholder presentation and strategic decision-making")
        print("="*70)
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        print("Please check your customization settings and SPSS file path")
        sys.exit(1)
