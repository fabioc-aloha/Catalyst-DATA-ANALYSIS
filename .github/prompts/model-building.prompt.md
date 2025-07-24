---
mode: "workflow"
model: "gpt-4"
tools: ["workspace", "read_file", "run_notebook_cell", "semantic_search"]
description: "Predictive model development and optimization workflows"
---

# Model Building Episode Template

## Model Development Workflow
- Define clear business objectives and success metrics
- Perform comprehensive exploratory data analysis
- Engineer features based on domain knowledge and statistical analysis
- Split data appropriately for training, validation, and testing
- Establish baseline models for performance comparison

## Model Selection and Training
- Compare multiple algorithms suitable for the problem type
- Implement proper cross-validation strategies
- Tune hyperparameters using systematic search methods
- Apply regularization techniques to prevent overfitting
- Ensure reproducibility with proper random seed management

## Model Evaluation and Validation
- Use appropriate evaluation metrics for the business context
- Implement statistical significance testing for model comparison
- Assess model fairness and bias across different groups
- Validate model assumptions and check for violations
- Create comprehensive model documentation and interpretation

## Model Deployment Preparation
- Create model serialization and versioning procedures
- Implement model monitoring and drift detection systems
- Design A/B testing frameworks for model validation
- Establish rollback procedures for model failures
- Document model limitations and appropriate use cases

Execute for enterprise-grade predictive model development with full MLOps integration.

## Synapses (Embedded Connections)
- machine-learning.instructions.md (0.96, implements, bidirectional) - "ML expertise and algorithm selection"
- feature-engineering.prompt.md (0.92, builds_on, forward) - "Engineered features for model input"
- statistical-methods.instructions.md (0.89, validates, bidirectional) - "Statistical foundation for model assessment"
- model-validation.prompt.md (0.95, leads_to, forward) - "Model evaluation and validation protocols"
- business-insights.prompt.md (0.85, serves, forward) - "Models support business decision-making"
- data-governance.instructions.md (0.88, complies, forward) - "Model governance and ethical AI standards"
- performance-optimization.instructions.md (0.87, optimizes, bidirectional) - "Model performance and scalability"
