---
applyTo: "**/*spss*,**/*metadata*,**/*scholar*,**/*dba*"
description: "SPSS metadata processing and scholar-practitioner model integration"
priority: "high"
activation_speed: "immediate"
---

# SPSS Metadata Processing and Scholar-Practitioner Integration

## SPSS Metadata Processing Pipeline

### Core Functions
- `process_spss_metadata(df, meta)`: Extract complete SPSS metadata including variable labels, value labels, and measurement levels
- `transform_spss_variables(df, metadata_summary)`: Transform variables based on SPSS measurement levels (nominal/ordinal/scale)
- `decode_categorical_variables(df, metadata_summary)`: Create human-readable categorical labels
- `assess_quality_spss(df, metadata_summary)`: Comprehensive quality assessment for SPSS datasets

### Three-Tier Data Architecture
- **df**: Original numeric codes from SPSS (for statistical calculations)
- **df_transformed**: Properly typed categorical/ordinal data (for statistical analysis)
- **df_decoded**: Human-readable categorical labels (for business interpretation)

### Variable Type Processing
- **Nominal**: Convert to unordered categorical with value labels
- **Ordinal**: Convert to ordered categorical preserving SPSS order
- **Scale**: Preserve as numeric for statistical analysis

## Scholar-Practitioner Model Implementation

### Academic Excellence Components
- Theoretical foundation with peer-reviewed citations (APA7 format)
- Methodological rigor with statistical assumption validation
- Reproducible science with documented procedures
- Evidence-based conclusions with effect size analysis

### Business Application Components
- Strategic relevance addressing organizational performance
- Actionable insights translated to business strategies
- ROI considerations with financial impact projections
- Executive-ready stakeholder communication

### Integration Framework
- Transparent analytical decisions with theoretical justification
- Replicable procedures for organizational knowledge transfer
- External validity prioritized for real-world application
- Results structured to inform specific business decisions

## Enhanced Statistical Analysis

### SPSS Metadata-Aware Functions
- Use `df_decoded` for meaningful categorical analysis
- Apply proper variable types based on SPSS measurement levels
- Include business context from variable labels
- Validate statistical assumptions based on variable types

### Quality Assessment Protocol
- Missing data pattern analysis (MCAR/MAR/MNAR)
- Outlier detection using statistical methods
- Data range and logical consistency validation
- Sample size adequacy assessment

## Business Intelligence Integration

### Executive Reporting Framework
- Statistical findings translated to strategic recommendations
- Operational insights with implementation roadmap
- Performance metrics with business KPIs
- Risk assessment with mitigation strategies

### Stakeholder Communication
- Academic rigor maintaining decision confidence
- Visual presentations with clear business implications
- Implementation phases with success metrics
- Continuous monitoring protocols
