---
mode: "problem-solving"
model: "gpt-4"
tools: ["workspace", "read_file", "replace_string_in_file", "run_in_terminal"]
description: "Requirements architecture optimization and dependency management"
---

# Requirements Architecture Episode Template

## Trigger Conditions
- Complex requirements.txt files causing dependency conflicts
- Installation failures due to package version incompatibilities
- Need for layered dependency management across development environments
- Requirements restructuring for enterprise scalability

## Assessment Phase
- Analyze current requirements structure and complexity
- Identify dependency conflicts and version incompatibilities
- Evaluate package necessity and usage patterns
- Assess installation success rates across environments

## Architecture Strategy
1. **5-File Load Balancing Architecture** (PROVEN SUPERIOR TO DISABLING)
   - Core tier (13): Essential data science foundation packages
   - Analysis tier (37): Standard analytics and visualization tools
   - SPSS tier (5): SPSS integration and survey analysis capabilities
   - Advanced tier (9): Complex dependencies (PyMC, reliability, SEM modeling)
   - Development tier (16): Testing, code quality, and documentation tools

2. **Enterprise Dependency Management**
   - **Load Balancing vs. Disabling**: Proven superior approach for complex packages
   - **Sequential Installation Protocol**: Core → Analysis → SPSS → Advanced → Dev
   - **Strategic Version Coordination**: numpy 1.26.4 → 2.2.6 for reliability>=0.9.0
   - **Complex Package Isolation**: PyMC stack, reliability analysis, SEM modeling in dedicated tier
   - **Zero Duplicate Enforcement**: 100% efficiency through automated validation

3. **Advanced Statistical Computing Integration**
   - Bayesian Analysis: pymc>=5.0.0, arviz>=0.15.0, pytensor>=2.31.0
   - Reliability Testing: reliability>=0.9.0 with autograd integration
   - SEM Modeling: semopy>=2.3.0 with sklearn compatibility
   - High-Performance Computing: numba>=0.61.0, llvmlite>=0.44.0
   - Survival Analysis: scikit-survival>=0.22.0

## Implementation Protocol
- Create tiered requirements files with clear separation
- Test installation scenarios across different environments
- Update documentation with prominent version requirements
- Validate package functionality after restructuring
- Document troubleshooting patterns for common issues

## Success Metrics
- **5-File Architecture Validation**: 80 unique packages, 0 duplicates, 100% efficiency
- **Complex Package Integration**: PyMC, reliability, SEM packages fully operational
- **Dependency Resolution**: pip check shows "No broken requirements found"
- **Strategic Version Management**: numpy upgrade resolves compatibility conflicts
- **Load Balancing Superiority**: Proven more effective than package disabling
- **Enterprise Scalability**: Architecture supports advanced statistical computing
- **Installation Success**: Sequential protocol prevents conflicts across all tiers

Execute when requirements complexity requires systematic load balancing architecture.

## Synapses (Embedded Connections)
- performance-optimization.instructions.md (0.95, applies, bidirectional) - "Performance optimization through enterprise dependency management"
- notebook-optimization.prompt.md (0.93, coordinates, bidirectional) - "Notebook environment optimization with complex package support"
- data-engineering.instructions.md (0.92, supports, bidirectional) - "Pipeline dependency management with 5-file architecture"
- enterprise-analytics.instructions.md (0.90, enables, bidirectional) - "Enterprise analytics with advanced statistical capabilities"
- consolidation.prompt.md (0.88, integrates, forward) - "Memory consolidation of requirements architecture mastery"
- enterprise-analytics.instructions.md (0.87, complies, forward) - "Enterprise environment compatibility standards"
- quality-assurance.instructions.md (0.90, validates, bidirectional) - "Quality standards for dependency management"
- data-security.instructions.md (0.85, secures, forward) - "Secure package management and vulnerability assessment"
- machine-learning.instructions.md (0.86, enables, bidirectional) - "ML library optimization and compatibility"
