---
mode: "workflow"
model: "gpt-4"
tools: ["workspace", "read_file", "run_notebook_cell", "get_python_environment_details"]
description: "Enterprise data preprocessing and quality assurance workflows"
---

# Data Cleaning Episode Template

## Data Quality Assessment Workflow
- Perform comprehensive data profiling and summary statistics
- Identify missing data patterns (MCAR, MAR, MNAR) and implications
- Detect outliers using statistical methods and domain knowledge
- Assess data consistency, validity, and integrity constraints
- Document data quality issues with severity and business impact

## Missing Data Handling Strategy
- Analyze missing data mechanisms and patterns
- Implement appropriate imputation methods based on data type
- Use multiple imputation for uncertainty quantification
- Validate imputation quality with cross-validation
- Document imputation decisions and assumptions

## Outlier Detection and Treatment
- Apply multiple outlier detection methods (statistical, ML-based)
- Investigate outliers for data entry errors vs. legitimate values
- Implement domain-appropriate outlier treatment strategies
- Document outlier handling decisions with business justification
- Validate treatment impact on downstream analysis

## Data Transformation and Standardization
- Apply appropriate scaling and normalization techniques
- Handle categorical data encoding and high-cardinality variables
- Implement feature engineering for analytical requirements
- Standardize data formats and naming conventions
- Create reproducible transformation pipelines

Execute for enterprise-grade data preprocessing with full documentation.
