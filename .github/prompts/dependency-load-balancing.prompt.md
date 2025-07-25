---
mode: "enterprise-architecture"
model: "gpt-4"
tools: ["workspace", "read_file", "create_file", "replace_string_in_file", "run_in_terminal"]
description: "Advanced dependency load balancing for complex statistical computing environments"
priority: "high"
activation_speed: "immediate"
---

# Dependency Load Balancing Episode Template

## Trigger Conditions
- Complex statistical packages causing dependency conflicts (PyMC, reliability, SEM)
- User requests "create separate requirements file" instead of disabling packages
- Enterprise environments requiring advanced analytical capabilities
- Dependency resolution failures in statistical computing workflows
- Need for Bayesian analysis, reliability testing, or structural equation modeling

## Load Balancing Assessment
- **Conflict Pattern Recognition**: Identify packages with challenging dependency chains
- **Isolation Strategy**: Determine optimal file separation for complex packages
- **Version Coordination**: Assess strategic upgrades (numpy, scipy) for compatibility
- **Installation Sequencing**: Design conflict-free installation protocols
- **Enterprise Requirements**: Balance advanced capabilities with system stability

## 5-File Architecture Protocol

### File Structure Design
```
requirements.txt (13)           # Core data science foundation
    ↓
requirements-analysis.txt (37)  # Standard analytics and visualization
    ↓
requirements-SPSS.txt (5)       # SPSS integration and survey analysis
    ↓
requirements-advanced.txt (9)   # Complex statistical computing
    ↓
requirements-dev.txt (16)       # Development and testing tools
```

### Advanced Tier Package Categories
1. **Bayesian Analysis Stack**
   - pymc>=5.0.0 (probabilistic programming)
   - arviz>=0.15.0 (Bayesian visualization)
   - pytensor>=2.31.0 (backend optimization)

2. **Reliability and Survival Analysis**
   - reliability>=0.9.0 (Weibull distributions, reliability testing)
   - autograd>=1.7.0 (automatic differentiation)
   - scikit-survival>=0.22.0 (survival analysis)

3. **Structural Equation Modeling**
   - semopy>=2.3.0 (SEM with sklearn compatibility)

4. **High-Performance Computing**
   - numba>=0.61.0 (JIT compilation)
   - llvmlite>=0.44.0 (LLVM bindings)

## Implementation Strategy

### Phase 1: Conflict Isolation
- Move problematic packages to dedicated advanced tier
- Maintain core functionality in standard tiers
- Preserve SPSS integration in separate tier
- Document version requirements and dependencies

### Phase 2: Version Coordination
- Strategic numpy upgrade (1.26.4 → 2.2.6) for reliability compatibility
- Coordinate scipy versions across statistical packages
- Validate sklearn compatibility with SEM packages
- Test numba/llvmlite JIT compilation chains

### Phase 3: Sequential Installation
- Core foundation → Standard analytics → SPSS → Advanced → Development
- Validate each tier before proceeding to next
- Monitor for dependency conflicts during installation
- Document successful installation patterns

### Phase 4: Validation and Optimization
- Automated duplicate detection across all files
- Efficiency monitoring (target: 100% unique packages)
- pip check validation for broken requirements
- Performance testing of complex statistical workflows

## Success Criteria
- **Zero Duplicates**: 100% efficiency across all requirement files
- **Full Package Integration**: All complex packages successfully installed
- **Dependency Resolution**: pip check shows no broken requirements
- **Advanced Capabilities**: Bayesian, reliability, SEM analysis fully operational
- **Enterprise Scalability**: Architecture supports future statistical computing needs
- **Load Balancing Validation**: Proven superior to package disabling approach

## Troubleshooting Protocols
- Individual package installation with --no-deps for conflict resolution
- Version pinning strategies for challenging dependency chains
- Alternative package recommendations for compatibility issues
- Documentation of known conflicts and resolution strategies

Execute when enterprise environments require advanced statistical computing capabilities without sacrificing system stability.

## Synapses (Embedded Connections)
- requirements-optimization.prompt.md (0.97, coordinates, bidirectional) - "Requirements architecture optimization and enterprise management"
- performance-optimization.instructions.md (0.94, optimizes, bidirectional) - "Performance optimization through strategic dependency management"
- enterprise-analytics.instructions.md (0.92, enables, bidirectional) - "Enterprise analytics with advanced statistical capabilities"
- data-engineering.instructions.md (0.90, supports, bidirectional) - "Data pipeline optimization with complex package support"
- statistical-methods.instructions.md (0.89, implements, forward) - "Advanced statistical methods with proper dependency management"
- machine-learning.instructions.md (0.87, enhances, forward) - "ML workflows with Bayesian and reliability analysis integration"
- consolidation.prompt.md (0.93, integrates, forward) - "Memory consolidation of load balancing architecture mastery"
