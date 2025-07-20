"""
Data Analysis Utilities
Enterprise-grade utility functions for statistical analysis and data processing
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import logging
import warnings

# Optional imports with graceful fallback
try:
    import pyreadstat
except ImportError:
    pyreadstat = None
    warnings.warn("pyreadstat not available - cannot read SPSS files")

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    logging.warning("scipy not available - advanced statistical tests will be limited")

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
        if pyreadstat is None:
            raise ImportError("pyreadstat is required to read SPSS files")
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
                
    @staticmethod
    def create_data_dictionary(df: pd.DataFrame, 
                             metadata: Optional[Dict] = None) -> pd.DataFrame:
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
    """Enterprise statistical analysis utilities with business intelligence capabilities"""
    
    @staticmethod
    def business_kpi_analysis(data: pd.DataFrame, 
                            metrics: List[str],
                            time_column: str = 'date',
                            baseline_period: int = 30) -> Dict:
        """
        Comprehensive business KPI analysis with trend detection
        
        Args:
            data: DataFrame containing business metrics
            metrics: List of KPI metric column names
            time_column: Name of the time/date column
            baseline_period: Number of periods for baseline comparison
            
        Returns:
            Dictionary containing KPI analysis results
        """
        results = {}
        
        # Sort by time
        data_sorted = data.sort_values(time_column)
        
        for metric in metrics:
            if metric not in data_sorted.columns:
                continue
                
            metric_data = data_sorted[metric].dropna()
            if len(metric_data) < baseline_period:
                continue
            
            # Calculate key statistics
            current_value = metric_data.iloc[-1]
            baseline_value = metric_data.iloc[-baseline_period:-1].mean()
            overall_mean = metric_data.mean()
            overall_std = metric_data.std()
            
            # Trend analysis
            trend_results = StatisticalAnalyzer.analyze_trend(metric_data)
            
            # Percentage change
            pct_change = ((current_value - baseline_value) / baseline_value * 100) if baseline_value != 0 else 0
            
            # Volatility (coefficient of variation)
            volatility = (overall_std / overall_mean * 100) if overall_mean != 0 else 0
            
            # Performance classification
            performance = 'improving' if trend_results['slope'] > 0 and trend_results['p_value'] < 0.05 else \
                         'declining' if trend_results['slope'] < 0 and trend_results['p_value'] < 0.05 else 'stable'
            
            results[metric] = {
                'current_value': current_value,
                'baseline_average': baseline_value,
                'overall_average': overall_mean,
                'percentage_change': pct_change,
                'trend_slope': trend_results['slope'],
                'trend_significance': trend_results['p_value'],
                'r_squared': trend_results['r_squared'],
                'volatility': volatility,
                'performance': performance,
                'interpretation': f"{'Significant' if trend_results['p_value'] < 0.05 else 'Non-significant'} {performance} trend"
            }
        
        return results
    
    @staticmethod
    def analyze_trend(data: pd.Series) -> Dict:
        from scipy.stats import linregress
        x = np.arange(len(data))
        slope, intercept, r_value, p_value, std_err = tuple(linregress(x, data.to_numpy()))
        slope = float(slope)
        intercept = float(intercept)
        r_value = float(r_value)
        p_value = float(p_value)
        std_err = float(std_err)
        if slope > 0 and p_value < 0.05:
            performance = 'improving'
        elif slope < 0 and p_value < 0.05:
            performance = 'declining'
        else:
            performance = 'stable'
        return {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value,
            'performance': performance,
            'interpretation': f"{'Significant' if p_value < 0.05 else 'Non-significant'} {performance} trend"
        }
    
    @staticmethod
    def detect_anomalies(data: pd.Series) -> Tuple[List[int], List[float]]:
        arr = data.dropna().to_numpy()
        median = np.median(arr)
        mad = np.median(np.abs(arr - median))
        if mad == 0:
            modified_z_scores = np.zeros_like(arr)
        else:
            modified_z_scores = 0.6745 * (arr - median) / mad
        anomalies = np.abs(modified_z_scores) > 3.5
        anomaly_indices = np.where(anomalies)[0].tolist()
        anomaly_values = arr[anomalies].tolist()
        return anomaly_indices, anomaly_values
    
    @staticmethod
    def correlation_analysis(data: pd.DataFrame, 
                           target_metric: str,
                           feature_columns: Optional[List[str]] = None) -> Dict:
        """
        Analyze correlations between business metrics
        
        Args:
            data: DataFrame containing metrics
            target_metric: Target metric to analyze correlations with
            feature_columns: Specific columns to analyze (if None, uses all numeric)
            
        Returns:
            Dictionary with correlation analysis results
        """
        if feature_columns is None:
            numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
            feature_columns = [col for col in numeric_columns if col != target_metric]
        
        correlations = {}
        
        for feature in feature_columns:
            if feature in data.columns and target_metric in data.columns:
                # Calculate Pearson correlation
                corr_coef = data[feature].corr(data[target_metric])
                
                # Calculate significance
                from scipy.stats import pearsonr
                _, p_value = pearsonr(data[feature].dropna(), data[target_metric].dropna())
                import numpy as np
                if isinstance(p_value, (tuple, list, np.ndarray)):
                    val = p_value[0]
                else:
                    val = p_value
                if isinstance(val, (float, int, np.floating)):
                    p_value_float = float(val)
                else:
                    p_value_float = 1.0
                # Interpret correlation strength
                abs_corr = abs(corr_coef)
                if abs_corr >= 0.7:
                    strength = 'strong'
                elif abs_corr >= 0.3:
                    strength = 'moderate'
                else:
                    strength = 'weak'
                direction = 'positive' if corr_coef > 0 else 'negative'
                correlations[feature] = {
                    'correlation': corr_coef,
                    'p_value': p_value_float,
                    'significant': p_value_float < 0.05,
                    'strength': strength,
                    'direction': direction,
                    'interpretation': f"{strength.title()} {direction} correlation"
                }
        
        # Sort by absolute correlation value
        sorted_correlations = dict(sorted(correlations.items(), 
                                        key=lambda x: abs(x[1]['correlation']), 
                                        reverse=True))
        
        return {
            'target_metric': target_metric,
            'correlations': sorted_correlations,
            'strongest_correlation': list(sorted_correlations.keys())[0] if sorted_correlations else None
        }
    
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
    
    @staticmethod
    def chi_square_test(data: pd.DataFrame, col1: str, col2: str) -> Dict:
        from scipy.stats import chi2_contingency
        contingency_table = pd.crosstab(data[col1], data[col2])
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        import numpy as np
        if isinstance(p_value, (tuple, list, np.ndarray)):
            val = p_value[0]
        else:
            val = p_value
        if isinstance(val, (float, int, np.floating)):
            p_value_float = float(val)
        else:
            p_value_float = 1.0
        return {
            'chi2': chi2,
            'p_value': p_value_float,
            'dof': dof,
            'expected': expected,
            'significant': p_value_float < 0.05
        }

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
