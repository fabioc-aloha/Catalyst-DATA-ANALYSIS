# Scripts Directory

This directory contains standalone Python scripts for automated analysis and reporting.

## 📊 Available Scripts

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
