"""
Enterprise Data Analysis Framework
==================================

A comprehensive enterprise-grade data analysis framework providing:
- Advanced data loading and preprocessing capabilities
- Statistical analysis with enterprise validation standards
- Publication-quality visualizations and dashboards
- Business intelligence and reporting tools

Components:
- DataLoader: Enterprise data ingestion with metadata preservation
- StatisticalAnalyzer: Advanced statistical analysis and validation
- EnterpriseVisualizer: Professional visualization and dashboard creation
"""

__version__ = "1.0.0"
__author__ = "Enterprise Data Analysis Team"

# Import core components for easy access
from .utils.data_utils import DataLoader, StatisticalAnalyzer
from .visualization.plot_utils import EnterpriseVisualizer

__all__ = [
    'DataLoader',
    'StatisticalAnalyzer', 
    'EnterpriseVisualizer'
]
