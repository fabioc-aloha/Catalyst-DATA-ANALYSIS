---
workflow_type: "unified_spss_reporting"
complexity_level: "high"
business_domain: "SPSS analysis, enterprise reporting, statistical automation"
execution_context: "standalone script generation for SPSS data analysis"
---

# Unified SPSS Reporting Script Generation Workflow

## Executive Summary Generation Protocol

**Objective**: Create standalone, reusable Python scripts that transform SPSS datasets into comprehensive business reports with embedded visualizations and strategic insights.

**Core Architecture Framework**:
- Template-based customizable script generation
- Complete statistical analysis pipeline automation
- Professional-grade visualization with base64 embedding
- Executive-ready reporting with business intelligence integration
- Domain-agnostic framework adaptable to any SPSS dataset

## Phase 1: Dataset Assessment and Template Selection

### SPSS Data Structure Analysis
```python
def assess_spss_dataset(spss_file_path):
    """Comprehensive assessment of SPSS dataset for template customization"""
    
    # Load with metadata preservation
    data, metadata = pyreadstat.read_sav(spss_file_path)
    
    assessment = {
        'shape': data.shape,
        'variables': list(data.columns),
        'data_types': data.dtypes.to_dict(),
        'missing_patterns': data.isnull().sum().to_dict(),
        'categorical_vars': [col for col in data.columns if data[col].dtype == 'object'],
        'continuous_vars': [col for col in data.columns if data[col].dtype in ['int64', 'float64']],
        'metadata': {
            'variable_labels': metadata.variable_labels if metadata.variable_labels else {},
            'value_labels': metadata.value_labels if metadata.value_labels else {}
        }
    }
    
    return data, assessment

# Business context identification
def identify_business_context(assessment):
    """Identify likely business domain and analysis focus"""
    
    variable_patterns = {
        'satisfaction': ['satisfaction', 'sat', 'happy', 'pleased'],
        'performance': ['performance', 'rating', 'score', 'evaluation'],
        'demographics': ['age', 'gender', 'income', 'education'],
        'behavior': ['usage', 'frequency', 'purchase', 'visit']
    }
    
    # Pattern matching logic for domain identification
    context = analyze_variable_patterns(assessment['variables'], variable_patterns)
    return context
```

**Template Selection Criteria**:
- Business domain (satisfaction, performance, demographic, behavioral)
- Analysis complexity (exploratory, confirmatory, predictive)
- Stakeholder audience (executive, technical, operational)
- Reporting frequency (one-time, recurring, real-time)

## Phase 2: Script Generation and Customization

### Core Template Structure
```python
#!/usr/bin/env python3
"""
UNIFIED COMPREHENSIVE ANALYSIS REPORT GENERATOR
Customized for: [DOMAIN_SPECIFIC_CONTEXT]
Generated: [TIMESTAMP]
"""

# ==================== CUSTOMIZATION SECTION ====================
# Modify these variables for your specific dataset and business context

DATASET_NAME = "[BUSINESS_SPECIFIC_NAME]"
SPSS_FILENAME = "[DATA_FILE.sav]"
ANALYSIS_TITLE = "[Domain-Specific Analysis Title]"
BUSINESS_DOMAIN = "[Industry/Department]"

# Variable mapping (customize based on your SPSS variables)
KEY_VARIABLES = ['Variable1', 'Variable2', 'Variable3']  # Main analysis variables
GROUPING_VARIABLE = 'CategoricalVariable'  # For group comparisons
OUTCOME_VARIABLE = 'PrimaryOutcome'  # Main dependent variable

# Business insights template (customize for your domain)
KEY_INSIGHTS_TEMPLATE = [
    "Domain-specific insight template 1",
    "Business interpretation framework 2", 
    "Strategic recommendation pattern 3"
]

# ==================== EXECUTION SECTION ====================
# Standard execution - no modifications needed below this line
```

**Statistical Pipeline Architecture**:
1. **Data Loading**: pyreadstat with metadata preservation
2. **Validation**: Variable existence and data quality checks
3. **Analysis**: Correlations, normality tests, group comparisons, effect sizes
4. **Visualization**: High-resolution charts with base64 embedding
5. **Reporting**: Markdown generation with embedded visuals and insights

## Phase 3: Quality Assurance and Validation

### Script Validation Protocol
```python
def validate_generated_script(script_path, test_data_path):
    """Comprehensive validation of generated unified reporting script"""
    
    validation_results = {
        'syntax_check': check_python_syntax(script_path),
        'dependency_validation': validate_imports(script_path),
        'execution_test': test_script_execution(script_path, test_data_path),
        'output_validation': validate_report_generation(script_path),
        'quality_metrics': assess_report_quality(script_path)
    }
    
    return validation_results
```

**Quality Standards Enforcement**:
- ✅ Standalone execution capability (no external dependencies)
- ✅ Error handling for missing variables or data issues
- ✅ Professional visualization quality (300 DPI resolution)
- ✅ Complete statistical reporting with interpretation
- ✅ Business-ready insights and recommendations
- ✅ Comprehensive documentation and methodology

## Phase 4: Business Intelligence Integration

### Executive Summary Generation
```python
def generate_executive_summary(analysis_results, business_context):
    """Create executive-level summary with strategic recommendations"""
    
    summary_components = {
        'key_findings': extract_primary_insights(analysis_results),
        'business_impact': quantify_business_implications(analysis_results),
        'recommendations': generate_strategic_actions(analysis_results),
        'confidence_levels': assess_finding_confidence(analysis_results),
        'next_steps': propose_follow_up_actions(analysis_results)
    }
    
    return format_executive_summary(summary_components)
```

**Strategic Framework Integration**:
- Performance vs. Importance quadrant analysis
- Driver hierarchy with business impact estimation
- Segment-specific insights and recommendations
- ROI projections for recommended actions
- Risk assessment and mitigation strategies

## Phase 5: Template Library Management

### Reusable Template Catalog
```python
# Domain-specific template variations
TEMPLATE_LIBRARY = {
    'customer_satisfaction': {
        'variables': ['overall_sat', 'service_quality', 'value_perception'],
        'analyses': ['driver_analysis', 'segment_comparison', 'loyalty_prediction'],
        'insights': ['satisfaction_drivers', 'improvement_priorities', 'retention_risk']
    },
    'employee_engagement': {
        'variables': ['engagement_score', 'job_satisfaction', 'intention_to_stay'],
        'analyses': ['factor_analysis', 'manager_comparison', 'tenure_analysis'],
        'insights': ['engagement_drivers', 'manager_effectiveness', 'retention_strategy']
    },
    'market_research': {
        'variables': ['brand_preference', 'purchase_intent', 'price_sensitivity'],
        'analyses': ['brand_positioning', 'price_elasticity', 'segment_profiling'],
        'insights': ['market_opportunities', 'competitive_advantages', 'pricing_strategy']
    }
}
```

**Template Maintenance Protocol**:
- Version control for template evolution
- Usage analytics and optimization feedback
- Domain expert validation and enhancement
- Automated testing and quality assurance
- Documentation updates and examples

## Success Metrics and Optimization

### Performance Indicators
- **Efficiency**: Script generation time < 5 minutes
- **Accuracy**: >95% successful execution on diverse datasets
- **Quality**: Executive satisfaction rating > 4.5/5.0
- **Adoption**: Template usage across multiple business units
- **Innovation**: Regular enhancement with new statistical methods

### Continuous Improvement Framework
- Regular template updates based on user feedback
- Integration of new statistical methods and visualizations
- Business domain expansion and specialization
- Automation enhancements for recurring analyses
- Integration with enterprise data platforms and workflows

This unified reporting framework ensures consistent, high-quality analysis across all SPSS datasets while maintaining flexibility for domain-specific requirements and business contexts.
