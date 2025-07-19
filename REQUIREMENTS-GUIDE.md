# Data Analysis Environment Setup

This project uses a layered requirements approach for maximum flexibility and stability.

## Installation Order

### 1. Essential Core (Required for all users)
```bash
pip install -r requirements.txt
```
**Contains:** pandas, numpy, scipy, matplotlib, seaborn, jupyter, scikit-learn, statsmodels

### 2. Advanced Analytics (Optional - for specialized analysis)
```bash
pip install -r requirements-analysis.txt
```
**Contains:** xgboost, plotly, nltk, geopandas, opencv, databases, cloud tools

### 3. Development Tools (Optional - for developers)
```bash
pip install -r requirements-dev.txt
```
**Contains:** testing tools, code formatters, documentation tools, profilers

## Quick Start
```bash
# Minimal setup - just core libraries
pip install -r requirements.txt

# Full analytics environment
pip install -r requirements.txt
pip install -r requirements-analysis.txt

# Full development environment
pip install -r requirements.txt
pip install -r requirements-analysis.txt
pip install -r requirements-dev.txt
```

## Environment Verification
```python
# Test core installation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("✅ Core environment ready!")
```

## Python Version
- **Required:** Python 3.11+
- **Tested:** Python 3.11.9

## File Structure
- `requirements.txt` - Essential core (15 packages)
- `requirements-analysis.txt` - Advanced analytics (35+ packages)
- `requirements-dev.txt` - Development tools (15+ packages)
