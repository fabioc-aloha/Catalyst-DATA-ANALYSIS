# Configuration Guide

## Overview

The Enterprise Data Analysis Cognitive Architecture uses a multi-layered configuration system that supports development, testing, and production environments with enterprise-grade security and compliance standards.

## Configuration Hierarchy

```
Configuration Priority (highest to lowest):
1. Environment Variables (.env)
2. Configuration Files (config/*.yaml)
3. Default Settings (hardcoded)
4. Command Line Arguments
```

## Environment Configuration

### `.env` File Configuration

Create a `.env` file in your project root:

```bash
# ===================================
# ENVIRONMENT SETTINGS
# ===================================
DATA_ANALYSIS_ENV=development  # development, testing, production
LOG_LEVEL=INFO                 # DEBUG, INFO, WARNING, ERROR, CRITICAL
DEBUG_MODE=true                # Enable debug features

# ===================================
# STATISTICAL ANALYSIS DEFAULTS
# ===================================
DEFAULT_ALPHA=0.05            # Default significance level
DEFAULT_POWER=0.80            # Default statistical power
DEFAULT_EFFECT_SIZE=0.5       # Default effect size for power calculations
CONFIDENCE_LEVEL=0.95         # Default confidence level

# ===================================
# DATA PROCESSING SETTINGS
# ===================================
MAX_MEMORY_GB=8               # Maximum memory usage in GB
CHUNK_SIZE=10000              # Default chunk size for large datasets
PARALLEL_JOBS=-1              # Number of parallel jobs (-1 = all cores)
RANDOM_SEED=42                # Default random seed for reproducibility

# ===================================
# VISUALIZATION SETTINGS
# ===================================
PLOT_STYLE=publication        # publication, presentation, web
DPI=300                       # Default DPI for exports
FIGURE_SIZE_WIDTH=10          # Default figure width
FIGURE_SIZE_HEIGHT=6          # Default figure height
COLOR_PALETTE=viridis         # Default color palette

# ===================================
# FILE HANDLING
# ===================================
DEFAULT_ENCODING=utf-8        # Default file encoding
MAX_FILE_SIZE_MB=1000        # Maximum file size for processing
TEMP_DIR=./temp              # Temporary directory for processing
CACHE_DIR=./cache            # Cache directory for processed data

# ===================================
# SECURITY SETTINGS
# ===================================
ENABLE_DATA_MASKING=true     # Enable automatic PII masking
AUDIT_LOGGING=true           # Enable audit logging
ENCRYPTION_KEY_PATH=./keys/  # Path to encryption keys
SESSION_TIMEOUT=3600         # Session timeout in seconds

# ===================================
# DATABASE CONNECTIONS
# ===================================
# DATABASE_URL=postgresql://user:pass@host:port/db
# MONGODB_URL=mongodb://user:pass@host:port/db
# REDIS_URL=redis://host:port/db

# ===================================
# ENTERPRISE INTEGRATION
# ===================================
ENTERPRISE_MODE=true         # Enable enterprise features
COMPLIANCE_LEVEL=strict      # strict, moderate, basic
DATA_RETENTION_DAYS=2555     # 7 years default retention
GDPR_COMPLIANCE=true         # Enable GDPR compliance features
HIPAA_COMPLIANCE=false       # Enable HIPAA compliance features
```

### Environment-Specific Configurations

#### Development Environment
```bash
DATA_ANALYSIS_ENV=development
LOG_LEVEL=DEBUG
DEBUG_MODE=true
ENABLE_DATA_MASKING=false
PARALLEL_JOBS=2
MAX_MEMORY_GB=4
```

#### Testing Environment
```bash
DATA_ANALYSIS_ENV=testing
LOG_LEVEL=INFO
DEBUG_MODE=false
ENABLE_DATA_MASKING=true
PARALLEL_JOBS=1
MAX_MEMORY_GB=2
RANDOM_SEED=42
```

#### Production Environment
```bash
DATA_ANALYSIS_ENV=production
LOG_LEVEL=WARNING
DEBUG_MODE=false
ENABLE_DATA_MASKING=true
AUDIT_LOGGING=true
ENCRYPTION_KEY_PATH=/secure/keys/
COMPLIANCE_LEVEL=strict
SESSION_TIMEOUT=1800
```

## Configuration Files

### Analysis Configuration (`config/analysis_config.yaml`)

```yaml
# Statistical Analysis Configuration
statistical_analysis:
  default_tests:
    normality: 
      - shapiro_wilk
      - kolmogorov_smirnov
    homoscedasticity:
      - levene
      - bartlett
    independence:
      - durbin_watson
  
  multiple_comparisons:
    correction_method: bonferroni  # bonferroni, fdr_bh, holm
    family_wise_error_rate: 0.05
  
  effect_sizes:
    enable: true
    methods:
      - cohens_d
      - eta_squared
      - cramers_v
  
  power_analysis:
    enable: true
    minimum_power: 0.80
    alpha_level: 0.05

# Data Quality Configuration
data_quality:
  missing_data:
    threshold_warning: 0.05      # Warn if >5% missing
    threshold_error: 0.20        # Error if >20% missing
    imputation_methods:
      - mean
      - median
      - mode
      - forward_fill
      - backward_fill
  
  outlier_detection:
    methods:
      - iqr
      - z_score
      - isolation_forest
    z_score_threshold: 3
    iqr_multiplier: 1.5
  
  validation_rules:
    enable: true
    check_duplicates: true
    check_data_types: true
    check_value_ranges: true

# Machine Learning Configuration
machine_learning:
  model_selection:
    cross_validation:
      cv_folds: 5
      stratified: true
      shuffle: true
    
    hyperparameter_tuning:
      method: grid_search  # grid_search, random_search, bayesian
      n_iter: 100
      scoring: accuracy
    
    feature_selection:
      enable: true
      methods:
        - variance_threshold
        - univariate_selection
        - recursive_feature_elimination
  
  model_evaluation:
    metrics:
      classification:
        - accuracy
        - precision
        - recall
        - f1_score
        - roc_auc
      regression:
        - rmse
        - mae
        - r2_score
        - mape
    
    validation_strategy: train_test_split  # train_test_split, cross_validation
    test_size: 0.2
    validation_size: 0.2
```

### Visualization Configuration (`config/visualization_config.yaml`)

```yaml
# Publication Settings
publication:
  style: seaborn-v0_8-whitegrid
  figure_size: [10, 6]
  dpi: 300
  font_family: serif
  font_size: 12
  title_size: 14
  label_size: 12
  tick_size: 10
  legend_size: 10
  
  colors:
    primary: "#1f77b4"
    secondary: "#ff7f0e"
    accent: "#2ca02c"
    palette: viridis
  
  export_formats:
    - png
    - pdf
    - svg

# Interactive Dashboards
dashboards:
  plotly_theme: plotly_white
  height: 600
  width: 800
  margin:
    l: 50
    r: 50
    t: 50
    b: 50
  
  colors:
    background: "#ffffff"
    grid: "#e5e5e5"
    text: "#2e2e2e"
  
  animations:
    enable: true
    duration: 500
    easing: cubic-in-out

# Chart Specific Settings
charts:
  histogram:
    bins: auto
    density: false
    alpha: 0.7
  
  scatter:
    size: 50
    alpha: 0.6
    edge_color: black
    edge_width: 0.5
  
  heatmap:
    annot: true
    cmap: viridis
    center: 0
    square: true
  
  boxplot:
    show_means: true
    mean_marker: diamond
    outlier_marker: circle
    whiskers: 1.5
```

### Logging Configuration (`config/logging_config.yaml`)

```yaml
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    datefmt: "%Y-%m-%d %H:%M:%S"
  
  detailed:
    format: "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s"
    datefmt: "%Y-%m-%d %H:%M:%S"
  
  json:
    format: '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: standard
    stream: ext://sys.stdout
  
  file:
    class: logging.handlers.RotatingFileHandler
    level: DEBUG
    formatter: detailed
    filename: logs/data_analysis.log
    maxBytes: 10485760  # 10MB
    backupCount: 5
  
  audit:
    class: logging.handlers.RotatingFileHandler
    level: INFO
    formatter: json
    filename: logs/audit.log
    maxBytes: 10485760
    backupCount: 10

loggers:
  data_analysis:
    level: DEBUG
    handlers: [console, file]
    propagate: false
  
  audit:
    level: INFO
    handlers: [audit]
    propagate: false
  
  security:
    level: WARNING
    handlers: [console, file, audit]
    propagate: false

root:
  level: INFO
  handlers: [console, file]
```

## Cognitive Architecture Configuration

### Memory System Settings

```yaml
# .github/config/cognitive_config.yaml
cognitive_architecture:
  working_memory:
    capacity: 4
    rules:
      - name: enterprise_analytics
        priority: high
        activation_pattern: "**/*enterprise*,**/*business*"
      - name: data_governance
        priority: high
        activation_pattern: "**/*governance*,**/*compliance*"
      - name: business_intelligence
        priority: high
        activation_pattern: "**/*bi*,**/*dashboard*,**/*report*"
      - name: scalable_performance
        priority: high
        activation_pattern: "**/*performance*,**/*scale*,**/*big-data*"
  
  long_term_memory:
    procedural_memory:
      path: ".github/instructions/"
      format: "markdown"
      activation_speed: "immediate"
    
    episodic_memory:
      path: ".github/prompts/"
      format: "markdown"
      activation_speed: "contextual"
  
  consolidation:
    auto_trigger_threshold: 4
    consolidation_frequency: "weekly"
    backup_enabled: true
    version_control: true
```

## Security Configuration

### Data Protection Settings

```yaml
# config/security_config.yaml
security:
  data_protection:
    encryption:
      enable: true
      algorithm: AES256
      key_rotation_days: 90
    
    pii_detection:
      enable: true
      patterns:
        - email
        - phone
        - ssn
        - credit_card
      masking_character: "*"
    
    data_masking:
      enable: true
      methods:
        - randomization
        - substitution
        - shuffling
        - nulling
  
  access_control:
    authentication:
      method: multi_factor
      session_timeout: 3600
      max_failed_attempts: 3
    
    authorization:
      role_based: true
      principle_least_privilege: true
      audit_all_access: true
  
  audit:
    enable: true
    log_level: detailed
    retention_days: 2555  # 7 years
    real_time_monitoring: true
```

## Performance Configuration

### Resource Management

```yaml
# config/performance_config.yaml
performance:
  memory_management:
    max_memory_gb: 8
    gc_threshold: 0.8
    chunk_processing: true
    chunk_size: 10000
  
  parallel_processing:
    enable: true
    max_workers: -1  # Use all available cores
    backend: threading  # threading, multiprocessing
  
  caching:
    enable: true
    cache_size_mb: 512
    cache_ttl_hours: 24
    cache_directory: "./cache"
  
  optimization:
    lazy_loading: true
    data_compression: true
    index_optimization: true
    query_optimization: true
```

## Advanced Configuration

### Custom Configuration Loading

```python
# config/config_loader.py
import os
import yaml
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    """Enterprise configuration management"""
    
    def __init__(self):
        self.config = {}
        self.load_all_configs()
    
    def load_all_configs(self):
        """Load all configuration files"""
        config_dir = Path("config")
        
        # Load YAML configurations
        for config_file in config_dir.glob("*.yaml"):
            with open(config_file) as f:
                config_name = config_file.stem
                self.config[config_name] = yaml.safe_load(f)
        
        # Override with environment variables
        self.apply_env_overrides()
    
    def apply_env_overrides(self):
        """Apply environment variable overrides"""
        env_mappings = {
            'DATA_ANALYSIS_ENV': 'environment.mode',
            'LOG_LEVEL': 'logging.level',
            'DEFAULT_ALPHA': 'statistical_analysis.alpha',
            'MAX_MEMORY_GB': 'performance.memory_management.max_memory_gb'
        }
        
        for env_var, config_path in env_mappings.items():
            if os.getenv(env_var):
                self.set_nested_config(config_path, os.getenv(env_var))
    
    def get(self, config_path: str, default: Any = None) -> Any:
        """Get configuration value using dot notation"""
        keys = config_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set_nested_config(self, config_path: str, value: Any):
        """Set configuration value using dot notation"""
        keys = config_path.split('.')
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = value

# Global configuration instance
config = ConfigManager()
```

## Configuration Validation

### Validation Rules

```python
# config/validator.py
from typing import Dict, List, Any
import os

class ConfigValidator:
    """Validate configuration settings"""
    
    @staticmethod
    def validate_statistical_config(config: Dict) -> List[str]:
        """Validate statistical analysis configuration"""
        errors = []
        
        alpha = config.get('DEFAULT_ALPHA', 0.05)
        if not 0 < alpha < 1:
            errors.append("DEFAULT_ALPHA must be between 0 and 1")
        
        power = config.get('DEFAULT_POWER', 0.80)
        if not 0 < power < 1:
            errors.append("DEFAULT_POWER must be between 0 and 1")
        
        return errors
    
    @staticmethod
    def validate_security_config(config: Dict) -> List[str]:
        """Validate security configuration"""
        errors = []
        
        if config.get('ENTERPRISE_MODE') and not config.get('AUDIT_LOGGING'):
            errors.append("AUDIT_LOGGING must be enabled in enterprise mode")
        
        if config.get('GDPR_COMPLIANCE') and not config.get('ENABLE_DATA_MASKING'):
            errors.append("DATA_MASKING must be enabled for GDPR compliance")
        
        return errors
    
    @staticmethod
    def validate_all(config: Dict) -> List[str]:
        """Validate all configuration settings"""
        errors = []
        errors.extend(ConfigValidator.validate_statistical_config(config))
        errors.extend(ConfigValidator.validate_security_config(config))
        return errors
```

## Environment Setup Scripts

### Development Setup

```bash
#!/bin/bash
# scripts/setup_dev.sh

echo "Setting up development environment..."

# Copy development environment template
cp config/env_templates/.env.development .env

# Install development dependencies
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install

# Create directories
mkdir -p logs cache temp data/raw data/processed

echo "Development environment setup complete!"
```

### Production Setup

```bash
#!/bin/bash
# scripts/setup_prod.sh

echo "Setting up production environment..."

# Copy production environment template
cp config/env_templates/.env.production .env

# Install production dependencies
pip install -r requirements.txt

# Set secure permissions
chmod 600 .env
chmod 700 logs/
chmod 700 cache/

# Generate encryption keys
python scripts/generate_keys.py

echo "Production environment setup complete!"
echo "Please review .env file and update sensitive values"
```

This comprehensive configuration system provides enterprise-grade flexibility while maintaining security and compliance standards. All settings can be easily adjusted for different environments and use cases.
