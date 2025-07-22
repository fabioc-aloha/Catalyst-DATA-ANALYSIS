---
applyTo: "**/*.py,**/*.ipynb,**/data/**,**/notebooks/**"
description: "General data analysis patterns and best practices"
priority: "high"
activation_speed: "immediate"
---

# Data Analysis Procedural Memory

## Data Loading and Initial Inspection
- Use pandas.read_spss() or pyreadstat.read_sav() for SPSS files
- Perform initial data inspection with .info(), .describe(), .head()
- Check for missing values, duplicates, and data type consistency
- Document data source, collection method, and variable definitions
- Create data dictionaries for complex datasets

## SPSS Metadata Integration and Variable Type Decoding
- Preserve SPSS metadata during data loading with pyreadstat
- Decode measurement levels (scale, ordinal, nominal) from meta.variable_measure
- Apply appropriate pandas data types based on SPSS variable types
- Convert categorical variables with proper ordering for ordinal data
- Maintain SPSS value labels for enhanced data interpretation
- Document variable transformations and measurement level assignments

## Data Quality Assessment
- Identify and handle missing data patterns (MCAR, MAR, MNAR)
- Detect and address outliers using statistical methods
- Validate data ranges and logical consistency
- Check for multicollinearity in predictive variables
- Assess sample size adequacy for planned analyses

## Reproducible Analysis Workflow
- Use consistent naming conventions for variables and files
- Set random seeds for reproducible results
- Version control data processing scripts
- Document all analysis decisions and assumptions
- Create automated data processing pipelines

## Statistical Best Practices
- Choose appropriate statistical tests based on data type and distribution
- Check statistical assumptions before applying tests
- Use appropriate effect size measures alongside p-values
- Apply multiple comparison corrections when necessary
- Report confidence intervals and practical significance

## Scholar-Practitioner Statistical Analysis Framework
- Bridge academic rigor with business application requirements
- Conduct comprehensive assumption testing (normality, homogeneity of variance)
- Calculate and interpret effect sizes (Cohen's d, eta-squared) for practical significance
- Provide business context and actionable insights from statistical results
- Document statistical methodology and interpretation for stakeholder communication
- Apply measurement-level appropriate statistical tests based on SPSS metadata

## Code Organization and Documentation
- Structure notebooks with clear markdown sections
- Use functions for repeated analysis tasks
- Create reusable utility modules for common operations
- Include detailed comments explaining analysis rationale
- Generate automated reports with results and interpretations

## Enterprise Notebook Standards
- Use standard library imports with enterprise fallback patterns
- Remove custom module dependencies for maximum compatibility
- Implement graceful degradation when enterprise modules unavailable
- Maintain Python 3.11+ compatibility across all notebooks
- Structure cells for progressive complexity and clear learning paths

## Notebook Recovery and Optimization Protocols
- Implement clean rebuilding strategies for corrupted analysis notebooks
- Preserve essential analysis framework while removing display artifacts
- Enhance SPSS data loading with comprehensive metadata integration
- Apply enterprise documentation standards with result-driven updates
- Maintain statistical rigor while ensuring business applicability
- Create reproducible analysis templates for scholar-practitioner workflows

## Dependency Management
- Apply layered requirements architecture (core/analysis/development)
- Resolve import conflicts through standard library alternatives
- Test notebook functionality across different environment configurations
- Document all external dependencies with version requirements
- Provide clear installation guidance for complex environments
