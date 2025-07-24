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
1. **Layered Requirements Design**
   - Core tier: Essential packages for basic functionality
   - Analysis tier: Advanced analytics and specialized tools
   - Development tier: Testing, code quality, and documentation tools
   - Separate tiers to prevent dependency hell and enable flexible installation

2. **Dependency Optimization**
   - Group compatible packages by functionality and stability
   - Specify minimum viable versions for maximum compatibility
   - Remove redundant or conflicting package specifications
   - Test installation order and dependency resolution

3. **Enterprise Standards**
   - Enforce Python 3.11+ compatibility across all packages
   - Document layered installation approaches
   - Provide clear upgrade paths for different use cases
   - Maintain backward compatibility where possible

## Implementation Protocol
- Create tiered requirements files with clear separation
- Test installation scenarios across different environments
- Update documentation with prominent version requirements
- Validate package functionality after restructuring
- Document troubleshooting patterns for common issues

## Success Metrics
- Successful installation across core/analysis/development tiers
- Elimination of dependency conflicts and version errors
- Clear documentation and installation guidance
- Python 3.11+ compatibility enforced throughout
- Scalable architecture supporting multiple deployment scenarios

Execute when requirements complexity requires systematic restructuring.

## Synapses (Embedded Connections)
- performance-optimization.instructions.md (0.91, applies, bidirectional) - "Performance optimization through dependency management"
- notebook-optimization.prompt.md (0.92, coordinates, bidirectional) - "Notebook environment optimization and compatibility"
- data-engineering.instructions.md (0.88, supports, bidirectional) - "Pipeline dependency management and optimization"
- enterprise-analytics.instructions.md (0.87, complies, forward) - "Enterprise environment compatibility standards"
- quality-assurance.instructions.md (0.90, validates, bidirectional) - "Quality standards for dependency management"
- data-security.instructions.md (0.85, secures, forward) - "Secure package management and vulnerability assessment"
- machine-learning.instructions.md (0.86, enables, bidirectional) - "ML library optimization and compatibility"
