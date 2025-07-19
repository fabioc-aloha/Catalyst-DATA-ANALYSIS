# Installation Guide

## System Requirements

### Operating System
- Windows 10/11 (recommended)
- macOS 10.15+ 
- Linux (Ubuntu 18.04+)

### Python Requirements
- Python 3.11.0 or higher
- pip 21.0 or higher
- Virtual environment support (venv, conda)

### Hardware Requirements
- Minimum: 8GB RAM, 2GB free disk space
- Recommended: 16GB RAM, 10GB free disk space
- For large datasets: 32GB+ RAM

## Quick Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd DATA-ANALYSIS
```

### 2. Create Virtual Environment

**Using venv (recommended):**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**Using conda:**
```bash
conda create -n data-analysis python=3.11
conda activate data-analysis
```

### 3. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# For development
pip install -r requirements-dev.txt

# For analysis-specific packages
pip install -r requirements-analysis.txt
```

### 4. Verify Installation

```bash
# Test Python environment
python -c "import pandas, numpy, scipy, matplotlib; print('Core packages installed successfully')"

# Test SPSS support
python -c "import pyreadstat; print('SPSS support available')"

# Test custom utilities
python -c "
import sys
sys.path.append('src')
from utils.data_utils import DataLoader, StatisticalAnalyzer
print('Custom utilities loaded successfully')
"
```

## Detailed Installation

### Prerequisites Installation

#### Windows

1. **Install Python 3.11:**
   - Download from [python.org](https://python.org)
   - Ensure "Add Python to PATH" is checked
   - Verify: `python --version`

2. **Install Git:**
   - Download from [git-scm.com](https://git-scm.com)
   - Use default settings during installation

3. **Install Visual Studio Code (optional):**
   - Download from [code.visualstudio.com](https://code.visualstudio.com)
   - Install Python extension

#### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11
brew install python@3.11

# Install Git
brew install git
```

#### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3.11
sudo apt install python3.11 python3.11-venv python3.11-dev

# Install Git
sudo apt install git

# Install additional dependencies
sudo apt install build-essential
```

### Package Installation Details

#### Core Analysis Packages

```bash
# Data manipulation and analysis
pip install pandas==2.3.1 numpy==2.3.1

# Statistical analysis
pip install scipy==1.16.0 statsmodels==0.14.5 scikit-learn==1.7.1

# SPSS file support
pip install pyreadstat==1.3.0

# Visualization
pip install matplotlib==3.10.3 seaborn==0.13.2 plotly==6.2.0

# Jupyter environment
pip install jupyter==1.1.1 jupyterlab==4.4.4
```

#### Development Packages

```bash
# Code formatting and linting
pip install black==25.1.0 flake8==8.0.0 mypy==1.17.0

# Testing
pip install pytest==8.4.1 pytest-cov==6.0.0

# Documentation
pip install sphinx==8.1.3 sphinx-rtd-theme==3.0.2
```

#### Optional Packages

```bash
# Advanced machine learning
pip install xgboost lightgbm optuna

# Additional visualization
pip install bokeh altair

# Database connectivity
pip install sqlalchemy psycopg2-binary pymongo

# Big data processing
pip install dask[complete] polars
```

## Configuration Setup

### 1. Environment Variables

Create `.env` file in project root:

```bash
# Environment settings
DATA_ANALYSIS_ENV=development
LOG_LEVEL=INFO

# Statistical defaults
DEFAULT_ALPHA=0.05
DEFAULT_POWER=0.80

# Visualization settings
PLOT_STYLE=publication
DPI=300

# Performance settings
MAX_MEMORY_GB=8
PARALLEL_JOBS=-1
```

### 2. Jupyter Configuration

```bash
# Generate Jupyter config
jupyter notebook --generate-config

# Enable extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### 3. IDE Setup (VS Code)

Install recommended extensions:
- Python
- Jupyter
- Python Docstring Generator
- GitLens
- Markdown All in One

## Verification Tests

### Basic Functionality Test

```python
# test_installation.py
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pyreadstat

# Test data creation
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': np.random.normal(0, 1, 100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

# Test statistical analysis
correlation = stats.pearsonr(data['x'], data['y'])
print(f"Correlation test passed: r = {correlation[0]:.3f}, p = {correlation[1]:.3f}")

# Test visualization
fig = px.scatter(data, x='x', y='y', color='category', title='Installation Test Plot')
print("Visualization test passed")

print("✅ All tests passed successfully!")
```

### Enterprise Features Test

```python
# test_enterprise_features.py
import sys
sys.path.append('src')

from utils.data_utils import DataLoader, StatisticalAnalyzer, CONFIG
from visualization.plot_utils import EnterpriseVisualizer

# Test configuration loading
print(f"Configuration loaded: {bool(CONFIG)}")

# Test custom utilities
loader = DataLoader()
analyzer = StatisticalAnalyzer()
visualizer = EnterpriseVisualizer()

print("✅ Enterprise features test passed!")
```

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Reinstall packages
pip install --force-reinstall -r requirements.txt
```

#### SPSS File Issues
```bash
# Install additional system dependencies (Linux)
sudo apt-get install libicu-dev

# Reinstall pyreadstat
pip uninstall pyreadstat
pip install pyreadstat
```

#### Memory Issues
```bash
# Increase swap space (Linux)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Getting Help

1. **Check log files:** `logs/data_analysis.log`
2. **Verify environment:** Run verification tests
3. **Update packages:** `pip install --upgrade -r requirements.txt`
4. **Reset environment:** Delete `.venv` and reinstall

## Performance Optimization

### Large Dataset Handling

```python
# Use chunked processing for large files
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    pass

# Use efficient data types
df = df.astype({
    'category_col': 'category',
    'int_col': 'int32',
    'float_col': 'float32'
})
```

### Memory Management

```python
# Monitor memory usage
import psutil
import gc

def check_memory():
    process = psutil.Process()
    memory_mb = process.memory_info().rss / 1024 / 1024
    print(f"Memory usage: {memory_mb:.1f} MB")

# Force garbage collection
gc.collect()
```

## Next Steps

1. **Run sample analysis:** Open `notebooks/exploratory/enterprise_analysis_template.ipynb`
2. **Explore documentation:** Review `MANUAL-DATA-ANALYSIS.md`
3. **Try cognitive commands:** Use `"analyze data patterns"` with sample data
4. **Configure for your needs:** Modify `.env` and configuration files
