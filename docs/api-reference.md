# API Reference Documentation

## Data Analysis Utilities API

### DataLoader Class

The `DataLoader` class provides enterprise-grade data loading capabilities with comprehensive metadata preservation.

#### Methods

##### `load_spss_file(file_path: Union[str, Path], preserve_metadata: bool = True) -> Tuple[pd.DataFrame, Dict]`

Loads SPSS .sav files with complete metadata preservation.

**Parameters:**
- `file_path` (str or Path): Path to the SPSS .sav file
- `preserve_metadata` (bool): Whether to preserve SPSS metadata (default: True)

**Returns:**
- `Tuple[pd.DataFrame, Dict]`: DataFrame with data and dictionary with metadata

**Example:**
```python
from src.utils.data_utils import DataLoader

loader = DataLoader()
df, metadata = loader.load_spss_file('data/survey_data.sav')

# Access metadata
print(f"Variable labels: {metadata['variable_labels']}")
print(f"Value labels: {metadata['value_labels']}")
```

##### `load_csv_with_validation(file_path: Union[str, Path], **kwargs) -> pd.DataFrame`

Loads CSV files with comprehensive validation and quality checks.

**Parameters:**
- `file_path` (str or Path): Path to the CSV file
- `**kwargs`: Additional parameters passed to `pd.read_csv()`

**Returns:**
- `pd.DataFrame`: Validated DataFrame

**Example:**
```python
df = loader.load_csv_with_validation('data/customers.csv', encoding='utf-8')
```

### StatisticalAnalyzer Class

The `StatisticalAnalyzer` class provides enterprise statistical analysis utilities.

#### Methods

##### `check_assumptions(data: pd.DataFrame, variables: List[str], test_type: str = 'normality') -> Dict`

Validates statistical assumptions for various analytical procedures.

**Parameters:**
- `data` (pd.DataFrame): Input dataset
- `variables` (List[str]): Variables to test
- `test_type` (str): Type of assumption test ('normality', 'homoscedasticity', 'independence')

**Returns:**
- `Dict`: Test results with statistics and interpretations

**Example:**
```python
from src.utils.data_utils import StatisticalAnalyzer

analyzer = StatisticalAnalyzer()
results = analyzer.check_assumptions(df, ['age', 'income'], 'normality')
print(results['normality_tests'])
```

##### `effect_size_cohens_d(group1: pd.Series, group2: pd.Series) -> float`

Calculates Cohen's d effect size for comparing two groups.

**Parameters:**
- `group1` (pd.Series): First group data
- `group2` (pd.Series): Second group data

**Returns:**
- `float`: Cohen's d effect size

**Example:**
```python
effect_size = analyzer.effect_size_cohens_d(treatment_group, control_group)
print(f"Effect size (Cohen's d): {effect_size:.3f}")
```

## Visualization Utilities API

### EnterpriseVisualizer Class

Enterprise-grade visualization utilities for publication-quality graphics.

#### Methods

##### `create_distribution_plot(data: pd.Series, title: str = None, **kwargs) -> go.Figure`

Creates publication-quality distribution plots.

**Parameters:**
- `data` (pd.Series): Data to plot
- `title` (str): Plot title
- `**kwargs`: Additional plotting parameters

**Returns:**
- `go.Figure`: Plotly figure object

##### `correlation_heatmap(data: pd.DataFrame, method: str = 'pearson', **kwargs) -> go.Figure`

Creates interactive correlation heatmaps.

**Parameters:**
- `data` (pd.DataFrame): Input data
- `method` (str): Correlation method ('pearson', 'spearman', 'kendall')
- `**kwargs`: Additional plotting parameters

**Returns:**
- `go.Figure`: Interactive heatmap figure

## Configuration

### Environment Variables

The system uses the following environment variables:

- `DATA_ANALYSIS_ENV`: Environment setting ('development', 'production')
- `LOG_LEVEL`: Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR')
- `DEFAULT_ALPHA`: Default significance level (default: 0.05)
- `DEFAULT_POWER`: Default statistical power (default: 0.80)

### Configuration Files

- `.env`: Environment variables and local settings
- `config/analysis_config.yaml`: Analysis configuration parameters
- `pyproject.toml`: Project metadata and dependencies

## Error Handling

All API functions include comprehensive error handling:

```python
try:
    df, metadata = loader.load_spss_file('data/survey.sav')
except FileNotFoundError:
    print("SPSS file not found")
except Exception as e:
    print(f"Error loading file: {e}")
```

## Type Hints

All functions include complete type hints for better IDE support and code clarity:

```python
from typing import Dict, List, Tuple, Optional, Union
import pandas as pd
from pathlib import Path
```
