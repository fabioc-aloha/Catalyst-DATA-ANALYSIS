# How to Create SPSS Analysis Scripts - Step-by-Step Example

## 🎯 Scenario: Analyzing a New Employee Survey Dataset

Let's say you have a new SPSS file called `employee_survey.sav` with variables for job satisfaction, performance ratings, and tenure.

### Step 1: Copy the Template
```bash
cd scripts/
cp spss_report_template.py employee_survey_analysis.py
```

### Step 2: Customize the Variables
Edit `employee_survey_analysis.py` and update the customization section:

```python
# ==================== CUSTOMIZATION SECTION ====================
DATASET_NAME = "EMPLOYEE_SURVEY_2025"
SPSS_FILENAME = "employee_survey.sav"
KEY_VARIABLES = ['JobSatisfaction', 'PerformanceRating', 'Tenure']
GROUPING_VARIABLE = 'Department'
OUTCOME_VARIABLE = 'JobSatisfaction'

# Business context customization
ANALYSIS_TITLE = "Employee Satisfaction and Performance Analysis"
BUSINESS_DOMAIN = "Human Resources"
KEY_INSIGHTS_TEMPLATE = [
    "Job satisfaction correlates strongly with performance ratings",
    "Department differences impact employee satisfaction levels",
    "Tenure shows significant relationship with job satisfaction"
]
```

### Step 3: Run the Analysis
```bash
python employee_survey_analysis.py
```

### Step 4: Review Generated Report
The script will create: `scripts/results/UNIFIED_ANALYSIS_EMPLOYEE_SURVEY_2025_YYYYMMDD_HHMMSS.md`

## 🔧 Common Customizations

### For Different Variable Types
```python
# Continuous variables for correlation analysis
KEY_VARIABLES = ['Satisfaction', 'Performance', 'Engagement', 'Stress']

# Categorical grouping variable
GROUPING_VARIABLE = 'JobLevel'  # 1=Junior, 2=Senior, 3=Manager

# Outcome for group comparisons
OUTCOME_VARIABLE = 'Satisfaction'
```

### For Different Business Domains

#### Healthcare Analysis
```python
ANALYSIS_TITLE = "Patient Satisfaction and Care Quality Analysis"
BUSINESS_DOMAIN = "Healthcare"
KEY_VARIABLES = ['PatientSatisfaction', 'CareQuality', 'WaitTime']
```

#### Marketing Analysis
```python
ANALYSIS_TITLE = "Customer Experience and Purchase Intent Analysis"
BUSINESS_DOMAIN = "Marketing"
KEY_VARIABLES = ['CustomerSat', 'PurchaseIntent', 'BrandLoyalty']
```

#### Education Analysis
```python
ANALYSIS_TITLE = "Student Performance and Engagement Analysis"
BUSINESS_DOMAIN = "Education"
KEY_VARIABLES = ['GPA', 'Engagement', 'StudyHours']
```

## 📊 What the Template Automatically Generates

### Statistical Analyses
- ✅ Descriptive statistics for all variables
- ✅ Correlation matrix with significance testing
- ✅ Normality testing (Shapiro-Wilk)
- ✅ Independent t-tests with effect sizes
- ✅ Levene's test for equal variances

### Visualizations
- ✅ Correlation heatmap (high-resolution PNG)
- ✅ Multi-panel analysis dashboard
- ✅ Scatter plots with correlation values
- ✅ Distribution histograms

### Report Sections
- ✅ Executive summary with business insights
- ✅ Dataset overview and quality assessment
- ✅ Statistical results with interpretation
- ✅ Strategic recommendations framework
- ✅ Methodology documentation

## 🚀 Advanced Customizations

### Adding Custom Statistical Tests
```python
# Add ANOVA for multiple groups
from scipy.stats import f_oneway

if len(unique_groups) > 2:
    group_data = [analysis_data[analysis_data[GROUPING_VARIABLE] == group][OUTCOME_VARIABLE]
                  for group in unique_groups]
    f_stat, p_value = f_oneway(*group_data)
    print(f"📊 ANOVA: F = {f_stat:.3f}, p = {p_value:.3f}")
```

### Custom Visualizations
```python
# Add box plots for group comparisons
fig, ax = plt.subplots(figsize=(10, 6))
analysis_data.boxplot(column=OUTCOME_VARIABLE, by=GROUPING_VARIABLE, ax=ax)
plt.title(f'{OUTCOME_VARIABLE} by {GROUPING_VARIABLE}')
plt.suptitle('')  # Remove default title
```

### Business-Specific Insights
```python
# Custom insight generation based on correlations
insights = []
for key, value in correlations.items():
    if abs(value) > 0.5:
        var1, var2 = key.split('_to_')
        direction = "positively" if value > 0 else "negatively"
        insights.append(f"Strong correlation: {var1} relates {direction} to {var2} (r={value:.3f})")

KEY_INSIGHTS_TEMPLATE = insights[:3]  # Use top 3 correlations
```

## 📋 Quality Checklist

Before running your customized script:

- [ ] ✅ Updated all variable names to match your SPSS file
- [ ] ✅ Verified SPSS file path is correct
- [ ] ✅ Customized business context (title, domain, insights)
- [ ] ✅ Tested with a small subset of data first
- [ ] ✅ Reviewed variable types (continuous vs categorical)
- [ ] ✅ Confirmed grouping variables have appropriate values

## 🎯 Results You'll Get

Running the template with your customizations will generate:

1. **Console Output**: Real-time progress and statistical results
2. **Comprehensive Report**: ~1-2MB Markdown file with embedded charts
3. **High-Quality Visualizations**: 300 DPI PNG images embedded in report
4. **Business Insights**: Domain-specific interpretation and recommendations
5. **Statistical Rigor**: All analyses include assumption testing and effect sizes

This approach ensures consistency while allowing for domain-specific customization!
