# Interactive SPSS to Python Analysis Guide

**Version**: 2.0
**Date**: July 27, 2025
**Framework**: Alex's Bootstrap Learning Framework - Enhanced Multi-Step Analysis Workflow
**Enhancement**: Comprehensive Missing Data Analysis & Organized File Structure

## 🚀 New Multi-Step Analysis Workflow

**UPDATED**: This guide now includes a streamlined 3-step interactive analysis workflow with comprehensive missing data assessment and organized file management.

### 🎯 Quick Start - Multi-Step Workflow

For immediate analysis, use the new step-by-step scripts located in `scripts/`:

1. **Step 1**: Data Exploration - `python step1_explore_spss_data.py`
2. **Step 2**: Variable Selection - `python step2_variable_selection.py`
3. **Step 3**: Analysis Execution - `python step3_execute_analysis.py`

All results are automatically saved in `scripts/results/` for easy organization.

## How to Use This Guide

This manual provides two approaches:
1. **🔥 NEW: Interactive Multi-Step Scripts** - Automated workflow with missing data analysis
2. **📚 Traditional: Manual Analysis Prompts** - Custom notebook creation

**Your Data**: Throughout this guide, we'll assume your SPSS data file is in the `notebooks/` directory.

---

## Table of Contents

1. [🆕 Multi-Step Analysis Workflow](#multi-step-analysis-workflow)
2. [🎯 Missing Data Assessment](#missing-data-assessment)
3. [Getting Started with Your Data](#getting-started-with-your-data)
4. [Basic Descriptive Analysis](#basic-descriptive-analysis)
5. [Scale Reliability Assessment](#scale-reliability-assessment)
6. [Factor Analysis](#factor-analysis)
7. [Customer Satisfaction Driver Analysis](#customer-satisfaction-driver-analysis)
8. [Group Comparisons](#group-comparisons)
9. [Advanced Predictive Modeling](#advanced-predictive-modeling)
10. [Complete Survey Analysis Workflow](#complete-survey-analysis-workflow)
11. [Interactive Dashboard Creation](#interactive-dashboard-creation)
12. [📁 File Organization](#file-organization)

---

## 🆕 Multi-Step Analysis Workflow

### ✨ Enhanced Features:
- **Comprehensive Missing Data Analysis**: Pattern detection, mechanism assessment (MCAR/MAR/MNAR)
- **Variable Quality Assessment**: Automated categorization with missing data warnings
- **Interactive Configuration**: Step-by-step guided analysis setup
- **Organized Output**: All results saved in `scripts/results/` folder

### 🔧 Step 1: Data Exploration
**Script**: `step1_explore_spss_data.py`
**Purpose**: Comprehensive SPSS data exploration with missing data analysis

**Features**:
- Automatic SPSS file detection
- Variable type categorization (continuous, categorical, binary)
- **Enhanced Missing Data Analysis**:
  - Missing data patterns and mechanisms (MCAR/MAR/MNAR)
  - Completion rates by variable
  - Quality recommendations based on missingness
- Descriptive statistics with SPSS metadata preservation

**Output**: `scripts/results/spss_exploration_results.json`

### 🔧 Step 2: Variable Selection & Design
**Script**: `step2_variable_selection.py`
**Purpose**: Interactive variable selection with missing data quality warnings

**Features**:
- **Missing Data Quality Warnings**:
  - ⚠️ Visual indicators for high missingness (>15%)
  - Automated quality categorization (suitable/caution/exclude)
  - Data quality considerations in analysis planning
- Suggested analysis configurations
- Interactive configuration building
- Automated Step 3 script generation

**Output**: `scripts/results/analysis_configuration.json` + `step3_execute_analysis.py`

### 🔧 Step 3: Analysis Execution
**Script**: `step3_execute_analysis.py` (auto-generated)
**Purpose**: Execute selected analysis with missing data considerations

**Features**:
- Configuration-based analysis execution
- Missing data handling recommendations
- Results with data quality notes
- Export-ready outputs

**Output**: Analysis results in `scripts/results/`

---

## 🎯 Missing Data Assessment

### 📊 Comprehensive Missing Data Framework

The new workflow includes sophisticated missing data analysis:

#### **Missing Data Patterns**:
- **Complete**: Variables with no missing data
- **Monotone**: Predictable missing patterns
- **Non-monotone**: Complex missing patterns requiring investigation

#### **Missing Data Mechanisms**:
- **MCAR** (Missing Completely at Random): Safe for standard analysis
- **MAR** (Missing at Random): May require imputation
- **MNAR** (Missing Not at Random): Requires careful handling

#### **Quality Categorization**:
- **✅ Suitable** (<15% missing): Standard analysis recommended
- **⚠️ Caution** (15-29% missing): Consider imputation or sensitivity analysis
- **❌ Exclude** (≥30% missing): High risk, investigate before use

#### **Automated Recommendations**:
- Missing data handling strategies
- Variable inclusion warnings
- Analysis approach suggestions based on data quality

---

## Getting Started with Your Data

### Enhanced Data Import with Missing Data Analysis:
- SPSS file imported with all metadata preserved
- **Missing data pattern analysis and mechanism assessment**
- **Variable quality categorization with missingness warnings**
- **Data quality recommendations and caution flags**
- Variable summary with labels and measurement levels

### Quick Start Prompt:
```
"Run the multi-step SPSS analysis workflow starting with step1_explore_spss_data.py for comprehensive data exploration with missing data analysis."
```

### Traditional Manual Prompt:
```
"Please create a notebook cell to import my SPSS file and provide a comprehensive data overview including missing data analysis. I want to see the sample size, variable types, missing data patterns, mechanisms assessment, and data quality recommendations. Show me variables categorized by missing data quality (suitable/caution/exclude)."
```

### Expected Results:
- **Sample Information**: Total cases, complete cases, missing data summary
- **Missing Data Analysis**: Patterns, mechanisms, completion rates
- **Variable Quality Assessment**: Quality categorization with warnings
- **Data Quality Recommendations**: Handling strategies for missing data
- **Variable Summary**: All variables with labels, types, and quality indicators

---

## Basic Descriptive Analysis

### What You'll Get:
- Comprehensive descriptive statistics (mean, median, std dev, range)
- Frequency tables for categorical variables
- Distribution visualizations
- Outlier detection

### Prompt to Copy:
```
"Create notebook cells to perform descriptive analysis on my customer satisfaction survey data (DATA.sav). I need descriptive statistics for all numerical variables, frequency tables for categorical variables, and identify any outliers. Make it equivalent to running SPSS DESCRIPTIVES and FREQUENCIES commands."
```

### Expected Results:
- **Numerical Variables**: Mean, standard deviation, minimum, maximum, skewness, kurtosis
- **Categorical Variables**: Count and percentage for each category
- **Visualizations**: Histograms, box plots, and bar charts
- **Outlier Report**: Cases that fall outside normal ranges

---

## Scale Reliability Assessment

### What You'll Get:
- Cronbach's Alpha for each scale
- Item-total correlations
- "Alpha if item deleted" analysis
- Scale improvement recommendations

### Prompt to Copy:
```
"Please create notebook cells to analyze the reliability of my customer satisfaction scales. My satisfaction scale includes variables [sat_overall, sat_quality, sat_service, sat_value] and my loyalty scale includes [loy_recommend, loy_repurchase, loy_advocate]. Provide complete reliability analysis equivalent to SPSS RELIABILITY command with all statistics and recommendations."
```

*Note: Replace the variable names in brackets with your actual survey variable names*

### Expected Results:
- **Cronbach's Alpha Values**: For each scale (target: α ≥ 0.70)
- **Item Statistics**: Mean and standard deviation for each item
- **Item-Total Correlations**: How well each item correlates with the total scale
- **Reliability Improvement**: Which items, if any, should be removed to improve reliability
- **Scale Scoring**: New composite scale variables created from reliable items

---

## Factor Analysis

### What You'll Get:
- KMO and Bartlett's test results
- Factor structure with loadings
- Variance explained by each factor
- Factor score variables

### Prompt to Copy:
```
"Create notebook cells to perform exploratory factor analysis on my survey items [list your items here]. I want to understand the underlying factor structure. Include KMO test, Bartlett's test, factor loadings with rotation, and create factor scores. Make it equivalent to SPSS FACTOR analysis with varimax rotation."
```

### Expected Results:
- **Factorability Tests**: KMO > 0.6 and significant Bartlett's test
- **Number of Factors**: Eigenvalues > 1 rule and scree plot
- **Factor Loadings**: Items loading on each factor (>0.40 threshold)
- **Variance Explained**: Percentage of variance explained by each factor
- **Factor Scores**: New variables representing factor scores for each respondent

---

## Customer Satisfaction Driver Analysis

### What You'll Get:
- Ranked importance of satisfaction drivers
- Primary, secondary, and tertiary driver categories
- Business actionability assessment
- Performance vs. importance matrix

### Prompt to Copy:
```
"Please create notebook cells to perform customer satisfaction driver analysis using my DATA.sav file. I want to identify which factors drive overall satisfaction using machine learning techniques. Include feature importance rankings, driver categorization (primary/secondary/tertiary), and business recommendations. My satisfaction measure is [satisfaction_variable] and potential drivers include [list driver variables]."
```

### Expected Results:
- **Driver Importance Rankings**: Top 10 drivers ranked by statistical importance
- **Driver Categories**:
  - Primary Drivers (top 50% of importance)
  - Secondary Drivers (next 30% of importance)
  - Tertiary Drivers (remaining 20% of importance)
- **Business Impact**: Dollar impact estimates and action priorities
- **Performance Gaps**: Where to focus improvement efforts

---

## Group Comparisons

### What You'll Get:
- Statistical significance tests (t-tests, ANOVA)
- Effect sizes and practical significance
- Group means with confidence intervals
- Post-hoc analysis for multiple groups

### Prompt to Copy:
```
"Create notebook cells to compare customer satisfaction across different groups in my survey data. I want to compare satisfaction levels by [customer_type, region, tenure, etc.]. Include appropriate statistical tests (t-tests or ANOVA), effect sizes, and practical significance interpretation equivalent to SPSS COMPARE MEANS procedures."
```

### Expected Results:
- **Group Statistics**: Mean satisfaction for each group with sample sizes
- **Statistical Tests**: t-test results (2 groups) or ANOVA (3+ groups)
- **Effect Sizes**: Cohen's d or eta-squared values
- **Confidence Intervals**: 95% CI for group differences
- **Business Interpretation**: Which differences matter practically

---

## Advanced Predictive Modeling

### What You'll Get:
- Predictive models for customer behavior
- Variable importance in prediction
- Model accuracy metrics
- Customer risk scoring

### Prompt to Copy:
```
"Please create notebook cells to build predictive models for customer satisfaction and loyalty using my DATA.sav file. I want to predict [churn/satisfaction_level/recommendation] using available survey variables. Include model comparison, feature importance, and practical business applications beyond traditional SPSS capabilities."
```

### Expected Results:
- **Model Performance**: Accuracy, precision, recall, F1-score
- **Feature Importance**: Which variables best predict the outcome
- **Customer Scoring**: Risk scores for each customer
- **Business Rules**: Decision trees for customer segmentation
- **ROI Estimates**: Expected business value from model insights

---

## Complete Survey Analysis Workflow

### What You'll Get:
- End-to-end analysis from data import to business recommendations
- Executive summary with key findings
- Statistical appendix with detailed results
- Action plan with priorities

### Prompt to Copy:
```
"Create a complete customer satisfaction survey analysis workflow using my DATA.sav file. Start with data import and quality checks, then perform reliability analysis, descriptive statistics, driver analysis, group comparisons, and conclude with business recommendations. Format this as a comprehensive research report equivalent to a full SPSS analysis session."
```

### Expected Results:
- **Executive Summary**:
  - Overall satisfaction score and trend
  - Top 3 improvement opportunities
  - ROI estimates for recommended actions
- **Detailed Findings**:
  - Sample characteristics and data quality
  - Scale reliability and validity evidence
  - Satisfaction driver hierarchy
  - Segment performance comparisons
- **Business Recommendations**:
  - Prioritized action plan
  - Resource allocation suggestions
  - Expected impact estimates
- **Technical Appendix**: All statistical details and assumptions

---

## Interactive Dashboard Creation

### What You'll Get:
- Interactive satisfaction dashboard
- Real-time filtering capabilities
- Automated alert system
- Exportable executive reports

### Prompt to Copy:
```
"Please create notebook cells to build an interactive customer satisfaction dashboard using my DATA.sav file. Include satisfaction trends, driver analysis, segment comparisons, and alert systems. Make it suitable for executive presentation and ongoing monitoring beyond static SPSS output."
```

### Expected Results:
- **Executive Overview**: Key metrics with trend indicators
- **Driver Analysis Dashboard**: Interactive importance rankings
- **Segment Performance**: Filterable group comparisons
- **Alert System**: Automatic flags for satisfaction drops
- **Export Capabilities**: PDF reports and PowerPoint slides

---

## Advanced Analysis Requests

### Structural Equation Modeling
**Prompt**: *"Create notebook cells to perform structural equation modeling on my customer satisfaction data. I want to test the relationship between service quality dimensions, overall satisfaction, and customer loyalty using SEM techniques beyond SPSS capabilities."*

**Expected Results**: Path coefficients, model fit statistics, mediation analysis, theoretical model validation

### Longitudinal Analysis
**Prompt**: *"Analyze satisfaction trends over time using my panel data. Include time series analysis, satisfaction trajectory modeling, and churn prediction using advanced techniques not available in basic SPSS."*

**Expected Results**: Trend analysis, satisfaction lifecycle models, predictive alerts, seasonal patterns

### Text Analytics Integration
**Prompt**: *"Integrate open-ended survey responses with quantitative satisfaction data. Perform sentiment analysis on comments and link findings to numerical ratings using advanced text analytics."*

**Expected Results**: Sentiment scores, topic modeling, text-based driver analysis, integrated insights

---

## Tips for Effective Requests

### Be Specific About Your Variables
Instead of: *"Analyze my satisfaction data"*
Use: *"Analyze satisfaction using variables sat_overall, sat_quality, sat_service as my satisfaction scale"*

### Specify Your Business Context
Include: *"This is for a retail bank customer satisfaction survey with 500 respondents"*

### Request Interpretation
Add: *"Please include business interpretation and recommendations, not just statistical results"*

### Ask for Comparisons
Include: *"Compare these results to typical satisfaction survey benchmarks"*

### Request Visualizations
Add: *"Include publication-ready charts and graphs for executive presentation"*

---

## Sample Complete Request

```
"I have a customer satisfaction survey in SPSS format (DATA.sav) with 450 responses from retail customers. Please create a complete analysis notebook that includes:

1. Data import with quality assessment
2. Reliability analysis for satisfaction scale (sat_overall, sat_quality, sat_service, sat_value) and loyalty scale (loy_recommend, loy_repurchase)
3. Driver analysis to identify what drives overall satisfaction
4. Comparison of satisfaction by customer type (new vs. existing customers)
5. Predictive modeling to identify at-risk customers
6. Executive dashboard with key findings and recommendations

Format the results for business presentation with clear interpretations and action items. Include both statistical rigor and practical business value."
```

---

## Getting Help

### If You Need to Modify Requests:
- *"Please add correlation analysis to the previous notebook"*
- *"Can you create a simplified version suitable for non-technical stakeholders?"*
- *"Add benchmarking against industry standards"*

### If You Encounter Issues:
- *"The variable names in my file are different. Can you adapt the analysis?"*
- *"I need to handle missing data differently. Please modify the approach"*
- *"Can you explain the statistical assumptions and limitations?"*

### For Advanced Customization:
- *"Adapt this analysis for a B2B customer satisfaction survey"*
- *"Include multilevel modeling for hierarchical data structure"*
- *"Add machine learning techniques for customer segmentation"*

---

## 📁 File Organization

### 🎯 Organized Project Structure

The enhanced workflow uses an organized file structure to keep analysis outputs properly managed:

```
DATA-ANALYSIS/
├── scripts/                          # Analysis scripts
│   ├── results/                      # 🔥 All analysis outputs
│   │   ├── spss_exploration_results.json
│   │   ├── analysis_configuration.json
│   │   └── *.md                     # Generated reports
│   ├── step1_explore_spss_data.py   # Data exploration
│   ├── step2_variable_selection.py  # Variable selection
│   ├── step3_execute_analysis.py    # Analysis execution
│   └── generate_unified_report.py   # Comprehensive reporting
├── notebooks/                        # Jupyter notebooks
│   └── *.sav                        # SPSS data files
├── data/                            # Project data
└── docs/                            # Documentation
```

### 📋 Output File Management

#### **Step 1 Outputs** (`scripts/results/`):
- `spss_exploration_results.json` - Dataset overview and missing data analysis
- Console output with comprehensive data quality assessment

#### **Step 2 Outputs** (`scripts/results/`):
- `analysis_configuration.json` - Analysis configurations with quality warnings
- `step3_execute_analysis.py` - Auto-generated execution script
- Interactive guidance with missing data recommendations

#### **Step 3 Outputs** (`scripts/results/`):
- Analysis results with data quality notes
- Statistical outputs formatted for business interpretation
- Export-ready visualizations and tables

#### **Unified Reports** (`scripts/results/`):
- Comprehensive analysis reports (`.md` format)
- Executive summaries with business recommendations
- Statistical appendices with methodological notes

### ✅ Benefits of Organized Structure

1. **No Confusion**: All outputs contained within scripts folder
2. **Version Control**: Easy tracking of analysis iterations
3. **Self-Contained**: Scripts and outputs stay together
4. **Professional**: Clean, organized project structure
5. **Collaborative**: Clear file locations for team sharing

### 🔄 Migration Guide

If upgrading from previous versions:
1. **Automatic**: New scripts automatically use organized structure
2. **Legacy Files**: Previous outputs in `data/output/` can be moved to `scripts/results/`
3. **Notebooks**: Continue using existing notebook workflows
4. **Integration**: Organized scripts work alongside traditional notebooks

---

## 🚀 Quick Reference

### **For Immediate Analysis**:
```bash
cd scripts/
python step1_explore_spss_data.py    # Explore with missing data analysis
python step2_variable_selection.py   # Configure with quality warnings
python step3_execute_analysis.py     # Execute selected analysis
```

### **For Custom Notebooks**:
Use the traditional prompts throughout this guide to create custom analysis notebooks.

### **For Comprehensive Reports**:
```bash
python generate_unified_report.py    # Generate complete analysis report
```

### **Results Location**:
All outputs saved in: `scripts/results/`

---

*This guide combines traditional SPSS analysis capabilities with modern Python data science workflows, enhanced with comprehensive missing data analysis and organized file management for professional analysis workflows.*
