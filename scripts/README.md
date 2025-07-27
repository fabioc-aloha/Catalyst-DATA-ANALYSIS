# Scripts Directory

This directory contains standalone Python scripts for automated analysis and reporting, featuring an enhanced **Multi-Step SPSS Analysis Workflow** with comprehensive missing data analysis.

## � Multi-Step SPSS Analysis Workflow (Enhanced)

### **Interactive 3-Step Analysis Process**

The enhanced workflow provides a guided, interactive approach to SPSS analysis with sophisticated missing data assessment:

#### **Step 1: Data Exploration** (`step1_explore_spss_data.py`)
**Purpose**: Comprehensive SPSS data exploration with advanced missing data analysis

**Enhanced Features**:
- 🎯 **Automatic SPSS file detection** from notebooks directory
- �📊 **Variable type categorization** (continuous, categorical, binary)
- 🔍 **Missing Data Pattern Analysis**: MCAR, MAR, MNAR detection
- 📈 **Completion Rate Assessment** with quality recommendations
- ⚠️ **Quality Categorization**: Suitable/Caution/Exclude based on missingness
- 🏷️ **SPSS Metadata Preservation**: Labels, value labels, measurement levels

**Output**: `./results/spss_exploration_results.json`

#### **Step 2: Variable Selection** (`step2_variable_selection.py`)
**Purpose**: Interactive variable selection with missing data quality warnings

**Enhanced Features**:
- ⚠️ **Visual Quality Indicators**: High missingness warnings (>15%)
- 🎯 **Automated Quality Assessment**: Three-tier system (suitable/caution/exclude)
- 🛠️ **Interactive Configuration Builder**: Guided analysis setup
- 📋 **Suggested Analysis Patterns**: Based on variable types and quality
- 🤖 **Dynamic Script Generation**: Auto-creates customized Step 3 script
- 💡 **Missing Data Recommendations**: Analysis approach suggestions

**Output**: `./results/analysis_configuration.json` + `step3_execute_analysis.py`

#### **Step 3: Analysis Execution** (`step3_execute_analysis.py`)
**Purpose**: Execute configured analysis with missing data considerations (auto-generated)

**Enhanced Features**:
- ⚙️ **Configuration-Driven Execution**: Based on Step 2 selections
- 🎯 **Missing Data Handling**: Quality-based analysis approaches
- 📊 **Statistical Analysis**: With data quality notes and warnings
- 📈 **Professional Formatting**: Export-ready results
- 📝 **Methodological Notes**: Missing data handling documentation

**Output**: Analysis results in `./results/`

---

## 📊 Standalone Analysis Scripts

### `generate_unified_report.py`
**Purpose**: Generates a comprehensive unified analysis report consolidating ALL statistical analyses from the SPSS dataset.

**Features**:
- ✅ Independent execution (no notebook dependencies)
- ✅ Complete statistical analysis recreation
- ✅ High-resolution embedded visualizations
- ✅ Executive-ready markdown report
- ✅ Microsoft GCX framework alignment

### `spss_report_template.py`
**Purpose**: Template script for creating unified reports from any SPSS (.sav) file.

**Features**:
- ✅ Customizable for any SPSS dataset
- ✅ Automated variable detection and validation
- ✅ Flexible statistical analysis pipeline
- ✅ Domain-specific customization options
- ✅ Error handling and validation

**Quick Setup**:
1. Update `DATASET_NAME`, `SPSS_FILENAME`, and `KEY_VARIABLES`
2. Customize business context variables
3. Run the script to generate your analysis

### `SPSS_UNIFIED_REPORTING_GUIDE.md`
**Purpose**: Comprehensive architecture guide for creating SPSS analysis scripts.

**Contents**:
- ✅ Script architecture patterns
- ✅ Statistical analysis pipeline
- ✅ Visualization best practices
- ✅ Customization guidelines
- ✅ Quality assurance checklist

**Usage**:
```bash
# From the scripts directory
cd scripts
..\.venv\Scripts\python.exe generate_unified_report.py

# Or from the project root
.venv\Scripts\python.exe scripts\generate_unified_report.py

# For new SPSS files, use the template:
# 1. Copy spss_report_template.py to new_analysis.py
# 2. Update customization variables
# 3. Run: python new_analysis.py
```

**Requirements**:
- SPSS data file: `../notebooks/DBA 710 Multiple Stores.sav`
- Python virtual environment with data analysis packages
- Output directory: `scripts/results/` (within scripts folder)

**Output**:
- **Location**: `scripts/results/` directory
- Comprehensive markdown report with embedded PNG charts
- File size: ~1.2MB
- Contains: correlations, t-tests, SEM analysis, business recommendations

**Analysis Included**:
- Descriptive statistics and data quality assessment
- Correlation analysis with significance testing
- Normality testing (Shapiro-Wilk)
- Independent t-tests with effect sizes (Cohen's d)
- Levene's test for equal variances
- Structural Equation Modeling (SEM) with R² calculations
- Strategic business recommendations
- Technical methodology documentation

## 🚀 Running Scripts

All scripts are designed to be run from the scripts directory or project root using the virtual environment Python interpreter.

## 📁 Directory Structure
```
scripts/
├── README.md                    # This file
├── generate_unified_report.py   # Unified report generator
└── (future automation scripts)
```
