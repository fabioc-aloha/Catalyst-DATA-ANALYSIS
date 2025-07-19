---
mode: "agent"
model: "gpt-4"
tools: ["workspace", "run_in_terminal", "read_file", "create_file"]
description: "Advanced statistical analysis and interpretation workflow"
complexity: "high"
estimated_time: "45-90 minutes"
requires_validation: true
---

# Statistical Analysis Episode Template

## Phase 1: Analysis Planning and Assumptions
- Define research questions and hypotheses clearly
- Select appropriate statistical tests based on data characteristics
- Check sample size requirements and power considerations
- Validate statistical assumptions systematically
- Plan for multiple comparison corrections if needed

## Phase 2: Descriptive and Inferential Statistics
- Generate comprehensive descriptive statistics
- Conduct appropriate hypothesis tests
- Calculate effect sizes and confidence intervals
- Apply robust methods for non-normal distributions
- Document all statistical decisions and rationale

## Phase 3: Advanced Modeling
- Implement regression analysis with diagnostic checking
- Apply multivariate statistical methods as appropriate
- Use machine learning approaches for prediction
- Validate models using cross-validation techniques
- Assess model performance and generalizability

## Phase 4: Results Interpretation and Reporting
- Interpret statistical results in practical context
- Generate publication-quality tables and figures
- Write clear statistical summaries for different audiences
- Provide actionable recommendations based on findings
- Document limitations and areas for future research

## Implementation Steps
1. Activate statistical environment: ${workspaceFolder}/.venv
2. Load and prepare data for analysis
3. Execute planned statistical procedures
4. Validate results and check assumptions
5. Generate comprehensive analytical report

Use advanced statistical libraries from ${workspaceFolder}/.venv
