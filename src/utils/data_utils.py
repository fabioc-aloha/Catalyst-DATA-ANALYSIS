"""
Data Analysis Utilities
Enterprise-grade utility functions for statistical analysis and data processing
"""

import pandas as pd
import numpy as np
import pyreadstat
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Enterprise data loading with comprehensive metadata preservation"""
    
    @staticmethod
    def load_spss(file_path: Union[str, Path], 
                  preserve_metadata: bool = True) -> Tuple[pd.DataFrame, Dict]:
        """
        Load SPSS .sav files with complete metadata preservation
        
        Args:
            file_path: Path to SPSS .sav file
            preserve_metadata: Whether to preserve variable and value labels
            
        Returns:
            Tuple of (DataFrame, metadata dictionary)
        """
        try:
            df, meta = pyreadstat.read_sav(str(file_path))
            
            if preserve_metadata:
                # Create comprehensive metadata dictionary
                metadata = {
                    'variable_labels': meta.column_names_to_labels,
                    'value_labels': meta.variable_value_labels,
                    'missing_ranges': meta.missing_ranges,
                    'variable_types': {col: str(df[col].dtype) for col in df.columns},
                    'file_info': {
                        'rows': len(df),
                        'columns': len(df.columns),
                        'file_path': str(file_path)
                    }
                }
                
                logger.info(f"Loaded SPSS file: {len(df)} rows, {len(df.columns)} columns")
                return df, metadata
            else:
                return df, {}
                
        except Exception as e:
            logger.error(f"Error loading SPSS file {file_path}: {str(e)}")
            raise

    @staticmethod
    def create_data_dictionary(df: pd.DataFrame, 
                             metadata: Dict = None) -> pd.DataFrame:
        """
        Create comprehensive data dictionary for dataset
        
        Args:
            df: DataFrame to document
            metadata: Optional metadata from SPSS loading
            
        Returns:
            DataFrame with variable documentation
        """
        data_dict = []
        
        for col in df.columns:
            var_info = {
                'variable': col,
                'type': str(df[col].dtype),
                'non_null_count': df[col].count(),
                'null_count': df[col].isnull().sum(),
                'null_percentage': (df[col].isnull().sum() / len(df)) * 100,
                'unique_values': df[col].nunique()
            }
            
            # Add metadata if available
            if metadata:
                var_info['label'] = metadata.get('variable_labels', {}).get(col, '')
                var_info['value_labels'] = str(metadata.get('value_labels', {}).get(col, ''))
            
            # Add descriptive statistics for numeric variables
            if pd.api.types.is_numeric_dtype(df[col]):
                var_info.update({
                    'mean': df[col].mean(),
                    'std': df[col].std(),
                    'min': df[col].min(),
                    'max': df[col].max()
                })
            
            data_dict.append(var_info)
        
        return pd.DataFrame(data_dict)

class StatisticalAnalyzer:
    """Enterprise statistical analysis utilities"""
    
    @staticmethod
    def check_assumptions(data: pd.DataFrame, 
                         variables: List[str],
                         test_type: str = 'normality') -> Dict:
        """
        Check statistical assumptions for analysis
        
        Args:
            data: DataFrame containing variables
            variables: List of variable names to test
            test_type: Type of assumption test ('normality', 'homogeneity', etc.)
            
        Returns:
            Dictionary of test results
        """
        from scipy import stats
        
        results = {}
        
        if test_type == 'normality':
            for var in variables:
                if pd.api.types.is_numeric_dtype(data[var]):
                    # Shapiro-Wilk test for normality
                    stat, p_value = stats.shapiro(data[var].dropna())
                    results[var] = {
                        'test': 'Shapiro-Wilk',
                        'statistic': stat,
                        'p_value': p_value,
                        'normal': p_value > 0.05,
                        'interpretation': 'Normal distribution' if p_value > 0.05 else 'Non-normal distribution'
                    }
        
        return results
    
    @staticmethod
    def effect_size_cohens_d(group1: pd.Series, group2: pd.Series) -> float:
        """
        Calculate Cohen's d effect size
        
        Args:
            group1: First group data
            group2: Second group data
            
        Returns:
            Cohen's d effect size
        """
        n1, n2 = len(group1), len(group2)
        s1, s2 = group1.std(ddof=1), group2.std(ddof=1)
        
        # Pooled standard deviation
        pooled_std = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
        
        # Cohen's d
        d = (group1.mean() - group2.mean()) / pooled_std
        
        return d

def load_environment_config() -> Dict:
    """Load configuration from environment variables"""
    import os
    from dotenv import load_dotenv
    
    # Load .env file
    load_dotenv()
    
    config = {
        'data_paths': {
            'raw': os.getenv('DATA_RAW_PATH', 'data/raw'),
            'processed': os.getenv('DATA_PROCESSED_PATH', 'data/processed'),
            'output': os.getenv('DATA_OUTPUT_PATH', 'data/output')
        },
        'analysis': {
            'significance_level': float(os.getenv('DEFAULT_SIGNIFICANCE_LEVEL', 0.05)),
            'confidence_interval': float(os.getenv('DEFAULT_CONFIDENCE_INTERVAL', 0.95)),
            'missing_threshold': float(os.getenv('MAX_MISSING_THRESHOLD', 0.1))
        },
        'visualization': {
            'dpi': int(os.getenv('DEFAULT_DPI', 300)),
            'figure_size': tuple(map(int, os.getenv('DEFAULT_FIGURE_SIZE', '12,8').split(',')))
        }
    }
    
    return config

# Initialize configuration
CONFIG = load_environment_config()
