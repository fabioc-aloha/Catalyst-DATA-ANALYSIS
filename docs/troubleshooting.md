# Troubleshooting Guide

## Overview

This guide helps you diagnose and resolve common issues when working with the Enterprise Data Analysis Cognitive Architecture. Issues are organized by category with step-by-step solutions.

## General Troubleshooting Process

### 1. Information Gathering

Before troubleshooting, collect the following information:

```python
# System Information Script
import sys
import platform
import pandas as pd
import numpy as np
import psutil
from src.utils.system_info import SystemInfo

def collect_system_info():
    """Collect comprehensive system information"""
    info = {
        'python_version': sys.version,
        'platform': platform.platform(),
        'processor': platform.processor(),
        'memory_total': f"{psutil.virtual_memory().total / 1024**3:.1f} GB",
        'memory_available': f"{psutil.virtual_memory().available / 1024**3:.1f} GB",
        'pandas_version': pd.__version__,
        'numpy_version': np.__version__,
        'environment': SystemInfo.get_environment_info()
    }
    
    print("System Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    return info

# Run system info collection
system_info = collect_system_info()
```

### 2. Error Log Analysis

```python
# Log Analysis Tool
import re
from datetime import datetime
from typing import List, Dict

class LogAnalyzer:
    """Analyze system logs for troubleshooting"""
    
    def __init__(self, log_file_path: str = "logs/system.log"):
        self.log_file_path = log_file_path
        self.error_patterns = {
            'memory_error': r'MemoryError|out of memory|memory allocation',
            'file_error': r'FileNotFoundError|PermissionError|No such file',
            'data_error': r'ValueError|TypeError|KeyError',
            'connection_error': r'ConnectionError|TimeoutError|ConnectionRefused',
            'import_error': r'ImportError|ModuleNotFoundError'
        }
    
    def analyze_recent_errors(self, hours: int = 24) -> Dict[str, List[str]]:
        """Analyze recent errors in logs"""
        try:
            with open(self.log_file_path, 'r') as f:
                logs = f.readlines()
        except FileNotFoundError:
            return {"error": ["Log file not found"]}
        
        recent_errors = {}
        for error_type, pattern in self.error_patterns.items():
            matching_logs = [
                log.strip() for log in logs 
                if re.search(pattern, log, re.IGNORECASE)
            ]
            if matching_logs:
                recent_errors[error_type] = matching_logs[-5:]  # Last 5 occurrences
        
        return recent_errors
    
    def get_error_summary(self) -> str:
        """Get summary of errors for troubleshooting"""
        errors = self.analyze_recent_errors()
        
        if not errors:
            return "No recent errors found in logs."
        
        summary = "Recent Error Summary:\n"
        for error_type, error_list in errors.items():
            summary += f"\n{error_type.upper()}:\n"
            for error in error_list:
                summary += f"  - {error}\n"
        
        return summary

# Usage
analyzer = LogAnalyzer()
print(analyzer.get_error_summary())
```

## Installation Issues

### Issue 1: Package Installation Failures

**Symptoms:**
- `pip install` commands fail
- Missing dependencies errors
- Version conflicts

**Solutions:**

```bash
# 1. Update pip and setuptools
python -m pip install --upgrade pip setuptools wheel

# 2. Clear pip cache
pip cache purge

# 3. Install with verbose output for debugging
pip install -v package_name

# 4. Use specific package versions
pip install pandas==2.3.1 numpy==2.3.1

# 5. Install from different source
pip install --index-url https://pypi.org/simple/ package_name
```

**Advanced Solutions:**

```python
# Dependency Resolution Script
import subprocess
import sys
from typing import List

def resolve_dependencies(requirements_file: str = "requirements.txt") -> None:
    """Resolve dependency conflicts"""
    
    print("Analyzing dependency conflicts...")
    
    # Check for conflicts using pipdeptree
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pipdeptree", "--warn", "conflict"],
            capture_output=True,
            text=True
        )
        
        if "conflicts" in result.stdout.lower():
            print("Dependency conflicts found:")
            print(result.stdout)
            
            # Suggest resolution
            print("\nResolution suggestions:")
            print("1. Create fresh virtual environment")
            print("2. Install packages one by one")
            print("3. Use pip-tools to resolve dependencies")
        else:
            print("No dependency conflicts detected")
            
    except FileNotFoundError:
        print("Install pipdeptree for dependency analysis:")
        print("pip install pipdeptree")

# Usage
resolve_dependencies()
```

### Issue 2: Virtual Environment Problems

**Symptoms:**
- Commands not found after activation
- Wrong Python version
- Package not found errors

**Solutions:**

```bash
# 1. Recreate virtual environment
deactivate  # if currently activated
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/macOS

# 2. Verify environment
where python  # Windows
which python  # Unix/macOS
python --version

# 3. Verify pip location
where pip    # Windows  
which pip    # Unix/macOS

# 4. Reinstall packages
pip install -r requirements.txt
```

### Issue 3: SPSS File Reading Issues

**Symptoms:**
- `pyreadstat` installation fails
- SPSS files won't load
- Encoding errors

**Solutions:**

```python
# SPSS Troubleshooting Script
import os
import sys
from pathlib import Path

def diagnose_spss_issues():
    """Diagnose SPSS file reading issues"""
    
    print("SPSS Diagnostics:")
    
    # Check pyreadstat installation
    try:
        import pyreadstat
        print(f"✓ pyreadstat version: {pyreadstat.__version__}")
    except ImportError:
        print("✗ pyreadstat not installed")
        print("Install with: pip install pyreadstat")
        return
    
    # Check for common file issues
    test_files = [
        "test_data.sav",
        "survey_data.sav", 
        "data/sample.sav"
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            try:
                data, meta = pyreadstat.read_sav(file_path)
                print(f"✓ Successfully read {file_path}")
                print(f"  Shape: {data.shape}")
                print(f"  Variables: {len(meta.column_names)}")
            except Exception as e:
                print(f"✗ Error reading {file_path}: {str(e)}")
                print("  Try different encoding or check file integrity")

# Alternative SPSS reading methods
def try_alternative_spss_readers(file_path: str):
    """Try different methods to read SPSS files"""
    
    methods = [
        ("pyreadstat", lambda f: pyreadstat.read_sav(f)),
        ("pandas", lambda f: pd.read_spss(f)),
    ]
    
    for method_name, method_func in methods:
        try:
            data = method_func(file_path)
            print(f"✓ {method_name} successfully read the file")
            return data
        except Exception as e:
            print(f"✗ {method_name} failed: {str(e)}")
    
    return None

# Usage
diagnose_spss_issues()
```

## Data Loading Issues

### Issue 1: File Format Detection Failures

**Symptoms:**
- "Unsupported file format" errors
- Incorrect data parsing
- Missing columns or data

**Solutions:**

```python
# File Format Diagnostic Tool
import pandas as pd
import chardet
from pathlib import Path

class FileFormatDiagnostic:
    """Diagnose file format and encoding issues"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.results = {}
    
    def diagnose_encoding(self) -> str:
        """Detect file encoding"""
        try:
            with open(self.file_path, 'rb') as f:
                raw_data = f.read(10000)  # Read first 10KB
                result = chardet.detect(raw_data)
                confidence = result['confidence']
                encoding = result['encoding']
                
                print(f"Detected encoding: {encoding} (confidence: {confidence:.2f})")
                
                if confidence < 0.8:
                    print("Low confidence in encoding detection. Try:")
                    print("- utf-8")
                    print("- latin-1") 
                    print("- cp1252")
                
                return encoding
        except Exception as e:
            print(f"Encoding detection failed: {e}")
            return 'utf-8'
    
    def test_csv_reading(self) -> bool:
        """Test different CSV reading approaches"""
        encoding = self.diagnose_encoding()
        
        # Test different separators and parameters
        test_configs = [
            {'sep': ',', 'encoding': encoding},
            {'sep': ';', 'encoding': encoding},
            {'sep': '\t', 'encoding': encoding},
            {'sep': ',', 'encoding': 'utf-8'},
            {'sep': ',', 'encoding': 'latin-1'},
            {'sep': ',', 'encoding': 'cp1252'},
        ]
        
        for i, config in enumerate(test_configs):
            try:
                df = pd.read_csv(self.file_path, nrows=5, **config)
                print(f"✓ Config {i+1} successful: {config}")
                print(f"  Shape: {df.shape}")
                print(f"  Columns: {list(df.columns)}")
                return True
            except Exception as e:
                print(f"✗ Config {i+1} failed: {config} - {str(e)}")
        
        return False
    
    def suggest_pandas_options(self) -> Dict[str, Any]:
        """Suggest pandas reading options"""
        suggestions = {
            'encoding': self.diagnose_encoding(),
            'low_memory': False,  # For mixed types
            'dtype': 'object',    # Prevent type inference issues
            'keep_default_na': False,  # Preserve empty strings
            'na_values': ['', 'NULL', 'null', 'N/A', 'n/a'],
            'skipinitialspace': True,
            'skip_blank_lines': True
        }
        
        print("Suggested pandas options:")
        for key, value in suggestions.items():
            print(f"  {key}: {value}")
        
        return suggestions

# Usage
diagnostic = FileFormatDiagnostic("problematic_file.csv")
suggestions = diagnostic.suggest_pandas_options()
```

### Issue 2: Memory Issues with Large Files

**Symptoms:**
- `MemoryError` when loading files
- System becomes unresponsive
- Out of memory errors

**Solutions:**

```python
# Memory-Efficient Loading Strategies
import pandas as pd
import psutil
from typing import Iterator, Optional

class MemoryEfficientLoader:
    """Load large files with memory optimization"""
    
    def __init__(self):
        self.memory_threshold = 0.8  # 80% memory usage threshold
    
    def check_memory_usage(self) -> Dict[str, float]:
        """Check current memory usage"""
        memory = psutil.virtual_memory()
        return {
            'total_gb': memory.total / 1024**3,
            'available_gb': memory.available / 1024**3,
            'percent_used': memory.percent,
            'can_load_large': memory.percent < (self.memory_threshold * 100)
        }
    
    def estimate_file_memory_requirement(self, file_path: str) -> float:
        """Estimate memory needed to load file"""
        file_size_mb = os.path.getsize(file_path) / 1024**2
        
        # CSV files typically require 2-4x their file size in memory
        # (depends on data types and pandas overhead)
        estimated_memory_mb = file_size_mb * 3
        
        print(f"File size: {file_size_mb:.1f} MB")
        print(f"Estimated memory requirement: {estimated_memory_mb:.1f} MB")
        
        return estimated_memory_mb
    
    def load_large_csv_chunked(
        self, 
        file_path: str, 
        chunk_size: int = 10000,
        process_func: Optional[callable] = None
    ) -> Iterator[pd.DataFrame]:
        """Load large CSV in chunks"""
        
        memory_info = self.check_memory_usage()
        if not memory_info['can_load_large']:
            print(f"Warning: High memory usage ({memory_info['percent_used']:.1f}%)")
        
        try:
            reader = pd.read_csv(file_path, chunksize=chunk_size, iterator=True)
            
            for i, chunk in enumerate(reader):
                print(f"Processing chunk {i+1}: {chunk.shape}")
                
                # Optimize data types
                chunk = self._optimize_dtypes(chunk)
                
                # Apply processing function if provided
                if process_func:
                    chunk = process_func(chunk)
                
                yield chunk
                
                # Monitor memory usage
                current_memory = psutil.virtual_memory().percent
                if current_memory > (self.memory_threshold * 100):
                    print(f"Warning: Memory usage high ({current_memory:.1f}%)")
                    
        except Exception as e:
            print(f"Error loading file in chunks: {e}")
            raise
    
    def _optimize_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """Optimize dataframe data types for memory efficiency"""
        original_memory = df.memory_usage(deep=True).sum() / 1024**2
        
        for col in df.columns:
            col_type = df[col].dtype
            
            if col_type == 'object':
                # Check if should be category
                unique_ratio = df[col].nunique() / len(df)
                if unique_ratio < 0.5:  # Less than 50% unique values
                    df[col] = df[col].astype('category')
            
            elif col_type in ['int64', 'int32']:
                # Downcast integers
                df[col] = pd.to_numeric(df[col], downcast='integer')
            
            elif col_type in ['float64', 'float32']:
                # Downcast floats
                df[col] = pd.to_numeric(df[col], downcast='float')
        
        optimized_memory = df.memory_usage(deep=True).sum() / 1024**2
        print(f"Memory optimization: {original_memory:.1f} MB → {optimized_memory:.1f} MB")
        
        return df

# Usage example
loader = MemoryEfficientLoader()

# Check if file can be loaded
memory_req = loader.estimate_file_memory_requirement("large_file.csv")
memory_info = loader.check_memory_usage()

if memory_req > memory_info['available_gb'] * 1024:
    print("Loading in chunks...")
    for chunk in loader.load_large_csv_chunked("large_file.csv"):
        # Process each chunk
        processed_chunk = analyze_chunk(chunk)
else:
    print("Loading entire file...")
    df = pd.read_csv("large_file.csv")
```

## Statistical Analysis Issues

### Issue 1: Assumption Violations

**Symptoms:**
- Unreliable statistical results
- Warning messages about assumptions
- Unexpected p-values or effect sizes

**Solutions:**

```python
# Statistical Assumption Checker
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import normaltest, levene, shapiro
import warnings

class AssumptionChecker:
    """Check statistical assumptions for various tests"""
    
    def __init__(self, alpha: float = 0.05):
        self.alpha = alpha
        self.violations = []
    
    def check_normality(self, data: pd.Series, test: str = 'shapiro') -> Dict[str, Any]:
        """Check normality assumption"""
        
        if len(data) < 3:
            return {'violation': True, 'reason': 'Insufficient data for normality test'}
        
        # Remove missing values
        clean_data = data.dropna()
        
        if test == 'shapiro' and len(clean_data) <= 5000:
            statistic, p_value = shapiro(clean_data)
            test_name = 'Shapiro-Wilk'
        else:
            statistic, p_value = normaltest(clean_data)
            test_name = "D'Agostino"
        
        is_normal = p_value > self.alpha
        
        result = {
            'test': test_name,
            'statistic': statistic,
            'p_value': p_value,
            'is_normal': is_normal,
            'violation': not is_normal,
            'recommendation': self._get_normality_recommendation(is_normal, len(clean_data))
        }
        
        if not is_normal:
            self.violations.append(f"Normality violation in {data.name or 'data'}")
        
        return result
    
    def check_homogeneity_of_variance(self, groups: List[pd.Series]) -> Dict[str, Any]:
        """Check homogeneity of variance (homoscedasticity)"""
        
        # Remove missing values from all groups
        clean_groups = [group.dropna() for group in groups]
        
        # Check if any group has insufficient data
        if any(len(group) < 2 for group in clean_groups):
            return {'violation': True, 'reason': 'Insufficient data in one or more groups'}
        
        # Levene's test
        statistic, p_value = levene(*clean_groups)
        
        equal_variance = p_value > self.alpha
        
        result = {
            'test': 'Levene',
            'statistic': statistic,
            'p_value': p_value,
            'equal_variance': equal_variance,
            'violation': not equal_variance,
            'recommendation': self._get_variance_recommendation(equal_variance)
        }
        
        if not equal_variance:
            self.violations.append("Homogeneity of variance violation")
        
        return result
    
    def check_independence(self, data: pd.DataFrame, time_column: str = None) -> Dict[str, Any]:
        """Check independence assumption"""
        
        if time_column and time_column in data.columns:
            # Check for autocorrelation if time series data
            from statsmodels.stats.diagnostic import acorr_ljungbox
            
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            autocorr_results = {}
            
            for col in numeric_cols:
                if col != time_column:
                    clean_data = data[col].dropna()
                    if len(clean_data) > 10:
                        lb_stat, lb_pvalue = acorr_ljungbox(clean_data, return_df=False)
                        autocorr_results[col] = {
                            'statistic': lb_stat,
                            'p_value': lb_pvalue,
                            'independent': lb_pvalue > self.alpha
                        }
            
            violations = [col for col, result in autocorr_results.items() 
                         if not result['independent']]
            
            return {
                'test': 'Ljung-Box',
                'results': autocorr_results,
                'violation': len(violations) > 0,
                'violated_variables': violations,
                'recommendation': 'Consider time series methods if autocorrelation detected'
            }
        
        return {
            'test': 'Manual inspection recommended',
            'violation': False,
            'recommendation': 'Verify independence through study design review'
        }
    
    def comprehensive_check(self, data: pd.DataFrame, test_type: str, **kwargs) -> Dict[str, Any]:
        """Perform comprehensive assumption checking"""
        
        results = {'test_type': test_type, 'violations': []}
        
        if test_type == 'ttest':
            # Check normality for both groups
            group_col = kwargs.get('group_column')
            value_col = kwargs.get('value_column')
            
            if group_col and value_col:
                groups = [group for name, group in data.groupby(group_col)[value_col]]
                
                # Normality check for each group
                for i, group in enumerate(groups):
                    norm_result = self.check_normality(group)
                    results[f'group_{i+1}_normality'] = norm_result
                
                # Homogeneity of variance
                var_result = self.check_homogeneity_of_variance(groups)
                results['homogeneity_of_variance'] = var_result
        
        elif test_type == 'anova':
            # Similar checks for ANOVA
            group_col = kwargs.get('group_column')
            value_col = kwargs.get('value_column')
            
            if group_col and value_col:
                groups = [group for name, group in data.groupby(group_col)[value_col]]
                
                # Normality for each group
                for i, group in enumerate(groups):
                    norm_result = self.check_normality(group)
                    results[f'group_{i+1}_normality'] = norm_result
                
                # Homogeneity of variance
                var_result = self.check_homogeneity_of_variance(groups)
                results['homogeneity_of_variance'] = var_result
        
        elif test_type == 'correlation':
            # Check normality for correlation variables
            var1 = kwargs.get('variable1')
            var2 = kwargs.get('variable2')
            
            if var1 and var2:
                norm1 = self.check_normality(data[var1])
                norm2 = self.check_normality(data[var2])
                
                results['variable1_normality'] = norm1
                results['variable2_normality'] = norm2
        
        # Compile all violations
        results['all_violations'] = self.violations
        results['has_violations'] = len(self.violations) > 0
        
        return results
    
    def _get_normality_recommendation(self, is_normal: bool, n: int) -> str:
        """Get recommendation based on normality test result"""
        if is_normal:
            return "Data appears normally distributed. Parametric tests appropriate."
        else:
            if n >= 30:
                return "Non-normal but large sample (n≥30). CLT may apply - parametric tests may still be valid."
            else:
                return "Non-normal distribution with small sample. Consider non-parametric tests or data transformation."
    
    def _get_variance_recommendation(self, equal_variance: bool) -> str:
        """Get recommendation based on variance test result"""
        if equal_variance:
            return "Equal variances assumed. Standard tests appropriate."
        else:
            return "Unequal variances. Use Welch's correction or non-parametric alternatives."

# Usage
checker = AssumptionChecker()

# Check assumptions for t-test
assumptions = checker.comprehensive_check(
    data=df,
    test_type='ttest',
    group_column='treatment',
    value_column='score'
)

print("Assumption Check Results:")
for key, value in assumptions.items():
    if isinstance(value, dict) and 'violation' in value:
        status = "VIOLATED" if value['violation'] else "SATISFIED"
        print(f"{key}: {status}")
        if 'recommendation' in value:
            print(f"  Recommendation: {value['recommendation']}")
```

### Issue 2: Insufficient Sample Size

**Symptoms:**
- Low statistical power
- Non-significant results despite apparent effects
- Wide confidence intervals

**Solutions:**

```python
# Power Analysis and Sample Size Calculator
import numpy as np
from scipy import stats
import math

class PowerAnalysis:
    """Perform power analysis and sample size calculations"""
    
    def __init__(self):
        self.standard_power = 0.8
        self.standard_alpha = 0.05
    
    def calculate_effect_size_cohens_d(self, group1: pd.Series, group2: pd.Series) -> float:
        """Calculate Cohen's d effect size"""
        n1, n2 = len(group1), len(group2)
        
        # Calculate means
        mean1, mean2 = group1.mean(), group2.mean()
        
        # Calculate pooled standard deviation
        s1, s2 = group1.std(ddof=1), group2.std(ddof=1)
        pooled_std = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
        
        # Cohen's d
        cohens_d = (mean1 - mean2) / pooled_std
        
        return abs(cohens_d)
    
    def interpret_effect_size(self, effect_size: float, test_type: str = 'cohens_d') -> str:
        """Interpret effect size magnitude"""
        if test_type == 'cohens_d':
            if effect_size < 0.2:
                return "Very small effect"
            elif effect_size < 0.5:
                return "Small effect"
            elif effect_size < 0.8:
                return "Medium effect"
            else:
                return "Large effect"
        
        return "Effect size interpretation not available"
    
    def calculate_required_sample_size_ttest(
        self, 
        effect_size: float, 
        power: float = 0.8, 
        alpha: float = 0.05,
        two_tailed: bool = True
    ) -> int:
        """Calculate required sample size for t-test"""
        
        # Convert to z-scores
        if two_tailed:
            z_alpha = stats.norm.ppf(1 - alpha/2)
        else:
            z_alpha = stats.norm.ppf(1 - alpha)
        
        z_beta = stats.norm.ppf(power)
        
        # Sample size calculation for two-sample t-test
        n = 2 * ((z_alpha + z_beta) / effect_size) ** 2
        
        return math.ceil(n)
    
    def post_hoc_power_analysis(
        self, 
        effect_size: float, 
        sample_size: int, 
        alpha: float = 0.05,
        test_type: str = 'ttest'
    ) -> Dict[str, Any]:
        """Calculate achieved power given effect size and sample size"""
        
        if test_type == 'ttest':
            # Convert to z-score equivalent
            z_alpha = stats.norm.ppf(1 - alpha/2)  # two-tailed
            
            # Calculate z_beta
            z_beta = effect_size * math.sqrt(sample_size / 2) - z_alpha
            
            # Calculate power
            power = stats.norm.cdf(z_beta)
        else:
            power = None
        
        return {
            'effect_size': effect_size,
            'sample_size': sample_size,
            'power': power,
            'adequate_power': power >= 0.8 if power else None,
            'interpretation': self.interpret_effect_size(effect_size)
        }
    
    def sample_size_recommendations(self, current_data: pd.DataFrame, 
                                  group_col: str, value_col: str) -> Dict[str, Any]:
        """Provide sample size recommendations based on current data"""
        
        groups = list(current_data.groupby(group_col)[value_col])
        
        if len(groups) != 2:
            return {"error": "This analysis requires exactly 2 groups"}
        
        group1_data = groups[0][1]
        group2_data = groups[1][1]
        
        # Calculate current effect size
        effect_size = self.calculate_effect_size_cohens_d(group1_data, group2_data)
        
        # Current sample sizes
        n1, n2 = len(group1_data), len(group2_data)
        current_n = min(n1, n2)  # Use smaller group size
        
        # Calculate current power
        current_power = self.post_hoc_power_analysis(effect_size, current_n)['power']
        
        # Calculate required sample size for adequate power
        required_n = self.calculate_required_sample_size_ttest(effect_size)
        
        recommendations = {
            'current_effect_size': effect_size,
            'effect_interpretation': self.interpret_effect_size(effect_size),
            'current_sample_size': current_n,
            'current_power': current_power,
            'required_sample_size': required_n,
            'additional_participants_needed': max(0, required_n - current_n),
            'recommendations': []
        }
        
        # Generate recommendations
        if current_power < 0.8:
            recommendations['recommendations'].append(
                f"Current power ({current_power:.2f}) is below 0.8. "
                f"Consider collecting {required_n - current_n} more participants."
            )
        
        if effect_size < 0.2:
            recommendations['recommendations'].append(
                "Very small effect size detected. Consider if the effect is practically meaningful."
            )
        
        if required_n > 1000:
            recommendations['recommendations'].append(
                "Large sample size required. Consider if smaller, practically significant effect would be acceptable."
            )
        
        return recommendations

# Usage
power_analyzer = PowerAnalysis()

# Analyze current study power
recommendations = power_analyzer.sample_size_recommendations(
    current_data=df,
    group_col='treatment',
    value_col='outcome'
)

print("Power Analysis Results:")
print(f"Effect size: {recommendations['current_effect_size']:.3f} ({recommendations['effect_interpretation']})")
print(f"Current power: {recommendations['current_power']:.3f}")
print(f"Required sample size: {recommendations['required_sample_size']}")

for rec in recommendations['recommendations']:
    print(f"• {rec}")
```

## Performance Issues

### Issue 1: Slow Analysis Performance

**Symptoms:**
- Long execution times
- System becomes unresponsive
- Memory usage increases over time

**Solutions:**

```python
# Performance Optimization Tools
import time
import cProfile
import pstats
from functools import wraps
import psutil
import gc

class PerformanceOptimizer:
    """Optimize analysis performance"""
    
    def __init__(self):
        self.profiling_results = {}
    
    def profile_function(self, func):
        """Decorator to profile function performance"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            
            # Start profiling
            start_time = time.time()
            start_memory = psutil.Process().memory_info().rss / 1024**2
            
            profiler.enable()
            result = func(*args, **kwargs)
            profiler.disable()
            
            # End profiling
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024**2
            
            # Store results
            execution_time = end_time - start_time
            memory_used = end_memory - start_memory
            
            self.profiling_results[func.__name__] = {
                'execution_time': execution_time,
                'memory_used': memory_used,
                'profiler': profiler
            }
            
            print(f"{func.__name__} Performance:")
            print(f"  Execution time: {execution_time:.3f} seconds")
            print(f"  Memory used: {memory_used:.1f} MB")
            
            return result
        
        return wrapper
    
    def get_detailed_profile(self, function_name: str) -> str:
        """Get detailed profiling results"""
        if function_name not in self.profiling_results:
            return f"No profiling data for {function_name}"
        
        profiler = self.profiling_results[function_name]['profiler']
        
        # Create stats object
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        
        # Capture output
        import io
        s = io.StringIO()
        stats.print_stats(20)  # Top 20 functions
        return s.getvalue()
    
    def optimize_dataframe_operations(self, df: pd.DataFrame) -> pd.DataFrame:
        """Optimize dataframe for better performance"""
        print("Optimizing dataframe...")
        original_memory = df.memory_usage(deep=True).sum() / 1024**2
        
        # 1. Optimize data types
        df_optimized = df.copy()
        
        for col in df_optimized.columns:
            col_type = df_optimized[col].dtype
            
            if col_type == 'object':
                # Try to convert to numeric first
                try:
                    df_optimized[col] = pd.to_numeric(df_optimized[col])
                    continue
                except (ValueError, TypeError):
                    pass
                
                # Check if should be category
                unique_ratio = df_optimized[col].nunique() / len(df_optimized)
                if unique_ratio < 0.5:
                    df_optimized[col] = df_optimized[col].astype('category')
            
            elif 'int' in str(col_type):
                df_optimized[col] = pd.to_numeric(df_optimized[col], downcast='integer')
            
            elif 'float' in str(col_type):
                df_optimized[col] = pd.to_numeric(df_optimized[col], downcast='float')
        
        # 2. Remove unnecessary columns (if any are all NaN)
        null_cols = df_optimized.columns[df_optimized.isnull().all()].tolist()
        if null_cols:
            print(f"Removing columns with all null values: {null_cols}")
            df_optimized = df_optimized.drop(columns=null_cols)
        
        final_memory = df_optimized.memory_usage(deep=True).sum() / 1024**2
        memory_reduction = (1 - final_memory / original_memory) * 100
        
        print(f"Memory usage: {original_memory:.1f} MB → {final_memory:.1f} MB")
        print(f"Memory reduction: {memory_reduction:.1f}%")
        
        return df_optimized
    
    def enable_parallel_processing(self, n_jobs: int = -1):
        """Configure parallel processing settings"""
        import os
        
        if n_jobs == -1:
            n_jobs = psutil.cpu_count()
        
        # Set environment variables for parallel processing
        os.environ['NUMBA_NUM_THREADS'] = str(n_jobs)
        os.environ['MKL_NUM_THREADS'] = str(n_jobs)
        os.environ['OMP_NUM_THREADS'] = str(n_jobs)
        
        print(f"Parallel processing enabled with {n_jobs} threads")
    
    def memory_cleanup(self):
        """Clean up memory"""
        gc.collect()
        
        # Print memory usage
        memory = psutil.virtual_memory()
        print(f"Memory usage after cleanup: {memory.percent:.1f}%")
        print(f"Available memory: {memory.available / 1024**3:.1f} GB")

# Usage
optimizer = PerformanceOptimizer()

# Profile a function
@optimizer.profile_function
def slow_analysis(data):
    # Some analysis that might be slow
    return data.groupby('category').agg({
        'value': ['mean', 'std', 'count'],
        'score': ['min', 'max']
    })

# Run analysis
result = slow_analysis(df)

# Get detailed profiling
detailed_profile = optimizer.get_detailed_profile('slow_analysis')
print(detailed_profile)

# Optimize dataframe
df_optimized = optimizer.optimize_dataframe_operations(df)

# Enable parallel processing
optimizer.enable_parallel_processing()
```

## Visualization Issues

### Issue 1: Plot Rendering Problems

**Symptoms:**
- Blank or corrupted plots
- Memory errors during plotting
- Slow plot generation

**Solutions:**

```python
# Visualization Troubleshooting
import matplotlib.pyplot as plt
import matplotlib
import plotly.graph_objects as go
from IPython.display import display
import warnings

class VisualizationTroubleshooter:
    """Troubleshoot visualization issues"""
    
    def __init__(self):
        self.backend_tested = {}
    
    def diagnose_matplotlib_backend(self):
        """Diagnose matplotlib backend issues"""
        current_backend = matplotlib.get_backend()
        print(f"Current matplotlib backend: {current_backend}")
        
        # Test different backends
        backends_to_test = ['Qt5Agg', 'TkAgg', 'Agg']
        
        for backend in backends_to_test:
            try:
                matplotlib.use(backend, force=True)
                
                # Test simple plot
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot([1, 2, 3], [1, 4, 2])
                ax.set_title(f"Test plot with {backend}")
                
                # Try to save (tests if backend works properly)
                fig.savefig(f'test_{backend}.png', dpi=100, bbox_inches='tight')
                plt.close(fig)
                
                self.backend_tested[backend] = True
                print(f"✓ {backend} backend working")
                
            except Exception as e:
                self.backend_tested[backend] = False
                print(f"✗ {backend} backend failed: {str(e)}")
        
        # Recommend best backend
        working_backends = [b for b, works in self.backend_tested.items() if works]
        if working_backends:
            recommended = working_backends[0]
            matplotlib.use(recommended, force=True)
            print(f"Recommended backend: {recommended}")
        else:
            print("No working backends found. Check matplotlib installation.")
    
    def test_plotly_rendering(self):
        """Test Plotly rendering capabilities"""
        try:
            # Test basic plotly plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2]))
            fig.update_layout(title="Plotly Test Plot")
            
            # Test different renderers
            renderers = ['browser', 'notebook', 'png']
            
            for renderer in renderers:
                try:
                    import plotly.io as pio
                    pio.renderers.default = renderer
                    
                    # Test if renderer works
                    fig.show()
                    print(f"✓ Plotly {renderer} renderer working")
                    
                except Exception as e:
                    print(f"✗ Plotly {renderer} renderer failed: {str(e)}")
            
        except ImportError:
            print("Plotly not installed. Install with: pip install plotly")
        except Exception as e:
            print(f"Plotly test failed: {str(e)}")
    
    def optimize_plot_memory(self, plot_function, *args, **kwargs):
        """Optimize plot generation for memory efficiency"""
        
        # Check initial memory
        initial_memory = psutil.Process().memory_info().rss / 1024**2
        
        try:
            # Set memory-efficient defaults
            if 'dpi' not in kwargs:
                kwargs['dpi'] = 100  # Lower DPI for memory efficiency
            
            if 'figsize' not in kwargs:
                kwargs['figsize'] = (8, 6)  # Reasonable figure size
            
            # Generate plot
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                result = plot_function(*args, **kwargs)
            
            # Check memory usage
            final_memory = psutil.Process().memory_info().rss / 1024**2
            memory_used = final_memory - initial_memory
            
            print(f"Plot memory usage: {memory_used:.1f} MB")
            
            if memory_used > 100:  # More than 100 MB
                print("High memory usage detected. Consider:")
                print("- Reducing figure size")
                print("- Lowering DPI")
                print("- Simplifying plot complexity")
                print("- Using data sampling for large datasets")
            
            return result
            
        except MemoryError:
            print("MemoryError during plotting. Suggestions:")
            print("1. Reduce data size by sampling")
            print("2. Lower figure DPI")
            print("3. Use simpler plot types")
            print("4. Plot data in batches")
            
            # Try fallback approach
            return self._create_fallback_plot(*args, **kwargs)
    
    def _create_fallback_plot(self, data, plot_type='scatter', sample_size=1000):
        """Create simplified plot as fallback"""
        
        if len(data) > sample_size:
            print(f"Sampling {sample_size} points from {len(data)} total")
            data_sample = data.sample(n=sample_size)
        else:
            data_sample = data
        
        # Create simple plot
        plt.figure(figsize=(6, 4))
        
        if plot_type == 'scatter' and len(data_sample.columns) >= 2:
            plt.scatter(data_sample.iloc[:, 0], data_sample.iloc[:, 1], alpha=0.6)
            plt.xlabel(data_sample.columns[0])
            plt.ylabel(data_sample.columns[1])
        elif plot_type == 'histogram' and len(data_sample.columns) >= 1:
            plt.hist(data_sample.iloc[:, 0], bins=30, alpha=0.7)
            plt.xlabel(data_sample.columns[0])
            plt.ylabel('Frequency')
        
        plt.title('Fallback Plot (Simplified)')
        plt.tight_layout()
        
        return plt.gcf()

# Usage
troubleshooter = VisualizationTroubleshooter()

# Diagnose backend issues
troubleshooter.diagnose_matplotlib_backend()

# Test Plotly
troubleshooter.test_plotly_rendering()

# Optimize memory usage for plotting
def create_scatter_plot(data):
    plt.figure(figsize=(10, 8))
    plt.scatter(data['x'], data['y'])
    return plt.gcf()

# Use memory-optimized plotting
optimized_plot = troubleshooter.optimize_plot_memory(
    create_scatter_plot, 
    large_dataset,
    dpi=150
)
```

## Getting Additional Help

### 1. Community Resources

```python
# Generate detailed bug report
def generate_bug_report():
    """Generate comprehensive bug report"""
    
    import platform
    import sys
    import pandas as pd
    import numpy as np
    
    report = f"""
    BUG REPORT
    ==========
    
    System Information:
    - OS: {platform.system()} {platform.release()}
    - Python: {sys.version}
    - Pandas: {pd.__version__}
    - NumPy: {np.__version__}
    
    Memory Information:
    - Total: {psutil.virtual_memory().total / 1024**3:.1f} GB
    - Available: {psutil.virtual_memory().available / 1024**3:.1f} GB
    - Usage: {psutil.virtual_memory().percent:.1f}%
    
    Error Information:
    [Paste your error message and traceback here]
    
    Steps to Reproduce:
    [Describe the steps that led to the error]
    
    Expected Behavior:
    [Describe what you expected to happen]
    
    Actual Behavior:
    [Describe what actually happened]
    
    Additional Context:
    [Any additional information that might be helpful]
    """
    
    print(report)
    return report

# Generate bug report
generate_bug_report()
```

### 2. Log Configuration for Debugging

```python
# Enhanced logging setup
import logging
from datetime import datetime

def setup_debug_logging():
    """Setup comprehensive logging for debugging"""
    
    # Create logger
    logger = logging.getLogger('data_analysis_debug')
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Create file handler with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"debug_log_{timestamp}.log"
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    print(f"Debug logging enabled. Log file: {log_file}")
    
    return logger

# Setup debug logging
debug_logger = setup_debug_logging()

# Use in your code
debug_logger.info("Starting analysis...")
debug_logger.debug("Processing data with shape: %s", data.shape)
```

This troubleshooting guide covers the most common issues users encounter. For additional help, consult the community forums or create a detailed bug report using the provided template.
