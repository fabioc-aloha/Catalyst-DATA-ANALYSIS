"""
Data Loader Module
Provides enterprise-grade data loading capabilities
"""

import sys
from pathlib import Path

# Add the src directory to path for imports
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from utils.data_utils import DataLoader

__all__ = ['DataLoader']
