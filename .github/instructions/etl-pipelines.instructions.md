---
applyTo: "**/*etl*,**/*pipeline*,**/*extract*,**/*transform*,**/*load*"
description: "Extract-Transform-Load automation, data integration workflows"
---

# ETL Pipelines Procedural Memory

## ETL Architecture Design
- Design modular ETL components with clear separation of concerns
- Implement configuration-driven pipelines for flexibility
- Use standardized data formats and schemas across pipelines
- Establish data lineage tracking from source to destination
- Create comprehensive logging and audit trails

## Extract Phase Best Practices
- Implement incremental extraction strategies to minimize data transfer
- Use appropriate connection pooling and timeout configurations
- Handle source system unavailability with retry mechanisms
- Implement data sampling for large datasets during development
- Monitor extraction performance and optimize query patterns

## Transform Phase Optimization
- Apply transformations in logical order for efficiency
- Use vectorized operations for large-scale data processing
- Implement data validation and quality checks at each step
- Handle schema evolution and backward compatibility
- Create reusable transformation functions and modules

## Load Phase Implementation
- Use appropriate loading strategies (bulk insert, upsert, streaming)
- Implement transaction management for data consistency
- Handle target system constraints and capacity limitations
- Create rollback procedures for failed loads
- Monitor load performance and optimize batch sizes

## Pipeline Orchestration
- Use workflow management tools for complex dependencies
- Implement proper error handling and notification systems
- Create monitoring dashboards for pipeline health
- Establish data freshness and quality SLAs
- Design disaster recovery and backup procedures
