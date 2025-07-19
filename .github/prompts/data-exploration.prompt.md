---
mode: "agent"
model: "gpt-4"
tools: ["workspace", "run_in_terminal", "read_file", "create_file"]
description: "Systematic exploratory data analysis workflow"
complexity: "medium"
estimated_time: "30-60 minutes"
---

# Exploratory Data Analysis Episode Template

## Phase 1: Data Import and Initial Assessment
- Load SPSS .sav files using pyreadstat with metadata preservation
- Examine dataset structure, dimensions, and variable types
- Review variable labels, value labels, and missing value patterns
- Create comprehensive data dictionary and codebook
- Document data source and collection methodology

## Phase 2: Univariate Analysis
- Generate descriptive statistics for all variables
- Create appropriate visualizations (histograms, box plots, bar charts)
- Assess distributions and identify potential transformations
- Detect outliers using statistical methods (IQR, z-scores)
- Document unusual patterns or data quality issues

## Phase 3: Bivariate and Multivariate Exploration
- Create correlation matrices and heatmaps
- Generate cross-tabulations for categorical variables
- Explore relationships using scatter plots and regression lines
- Identify potential confounding variables
- Assess patterns of missing data across variables

## Phase 4: Hypothesis Generation and Analysis Planning
- Formulate research questions based on data exploration
- Identify appropriate statistical tests and modeling approaches
- Plan additional data collection or transformation needs
- Document assumptions and limitations
- Create analysis roadmap for subsequent investigations

## Implementation Steps
1. Configure Python environment: ${workspaceFolder}/.venv
2. Load data with metadata preservation
3. Generate comprehensive summary statistics
4. Create systematic visualization suite
5. Document findings and next steps

Use sophisticated analytics tools from ${workspaceFolder}/.venv
