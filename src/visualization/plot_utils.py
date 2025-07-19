"""
Enterprise Visualization Utilities
Publication-quality plotting and dashboard creation utilities
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
import warnings

# Optional imports with graceful fallback
try:
    import seaborn as sns
    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False
    warnings.warn("seaborn not available - some visualizations will be limited")

try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    warnings.warn("plotly not available - interactive dashboards will be limited")

# Set style defaults
plt.style.use('default')  # Use default instead of seaborn if not available
if SEABORN_AVAILABLE:
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")

class EnterpriseVisualizer:
    """Enterprise-grade visualization tools with business intelligence capabilities"""
    
    def __init__(self, style_config: Dict = None):
        """Initialize with custom styling configuration"""
        self.config = style_config or self._get_default_config()
        self._apply_styling()
    
    def _get_default_config(self) -> Dict:
        """Get default styling configuration"""
        return {
            'figure_size': (12, 8),
            'dpi': 300,
            'color_palette': 'husl',
            'font_size': 12,
            'title_size': 16,
            'label_size': 14,
            'executive_colors': {
                'primary': '#1f77b4',
                'secondary': '#ff7f0e', 
                'success': '#2ca02c',
                'warning': '#ffbb78',
                'danger': '#d62728',
                'info': '#17becf'
            }
        }
    
    def _apply_styling(self):
        """Apply consistent styling across all plots"""
        plt.rcParams['figure.figsize'] = self.config['figure_size']
        plt.rcParams['figure.dpi'] = self.config['dpi']
        plt.rcParams['font.size'] = self.config['font_size']
        plt.rcParams['axes.titlesize'] = self.config['title_size']
        plt.rcParams['axes.labelsize'] = self.config['label_size']
    
    def create_executive_kpi_dashboard(self, 
                                     kpi_data: Dict,
                                     title: str = "Executive KPI Dashboard") -> go.Figure:
        """
        Create executive-level KPI dashboard
        
        Args:
            kpi_data: Dictionary containing KPI metrics and values
            title: Dashboard title
            
        Returns:
            Plotly Figure object for interactive dashboard
        """
        from plotly.subplots import make_subplots
        
        # Calculate layout based on number of KPIs
        n_kpis = len(kpi_data)
        cols = min(3, n_kpis)
        rows = (n_kpis + cols - 1) // cols
        
        fig = make_subplots(
            rows=rows, cols=cols,
            subplot_titles=list(kpi_data.keys()),
            specs=[[{"type": "indicator"}] * cols for _ in range(rows)]
        )
        
        for i, (kpi_name, kpi_info) in enumerate(kpi_data.items()):
            row = i // cols + 1
            col = i % cols + 1
            
            # Extract values with defaults
            current_value = kpi_info.get('current_value', 0)
            target_value = kpi_info.get('target_value', current_value * 1.1)
            previous_value = kpi_info.get('previous_value', current_value * 0.95)
            
            # Determine color based on performance
            if current_value >= target_value:
                color = self.config['executive_colors']['success']
            elif current_value >= previous_value:
                color = self.config['executive_colors']['primary']
            else:
                color = self.config['executive_colors']['danger']
            
            fig.add_trace(
                go.Indicator(
                    mode="number+delta+gauge",
                    value=current_value,
                    delta={'reference': previous_value, 'relative': True},
                    gauge={
                        'axis': {'range': [0, target_value * 1.2]},
                        'bar': {'color': color},
                        'steps': [
                            {'range': [0, target_value * 0.8], 'color': "lightgray"},
                            {'range': [target_value * 0.8, target_value], 'color': "gray"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': target_value
                        }
                    },
                    title={'text': kpi_name}
                ),
                row=row, col=col
            )
        
        fig.update_layout(
            title=title,
            height=400 * rows,
            font=dict(size=12)
        )
        
        return fig
    
    def create_business_trend_analysis(self,
                                     data: pd.DataFrame,
                                     metrics: List[str],
                                     time_column: str = 'date',
                                     title: str = "Business Trend Analysis") -> go.Figure:
        """
        Create comprehensive business trend analysis dashboard
        
        Args:
            data: DataFrame containing business metrics over time
            metrics: List of metric column names to analyze
            time_column: Name of the time/date column
            title: Dashboard title
            
        Returns:
            Plotly Figure object
        """
        from plotly.subplots import make_subplots
        
        n_metrics = len(metrics)
        cols = 2
        rows = (n_metrics + cols - 1) // cols
        
        fig = make_subplots(
            rows=rows, cols=cols,
            subplot_titles=metrics,
            specs=[[{"secondary_y": True}] * cols for _ in range(rows)]
        )
        
        colors = px.colors.qualitative.Set1
        
        for i, metric in enumerate(metrics):
            if metric not in data.columns:
                continue
                
            row = i // cols + 1
            col = i % cols + 1
            color = colors[i % len(colors)]
            
            # Time series data
            time_data = data[[time_column, metric]].dropna()
            
            # Main metric line
            fig.add_trace(
                go.Scatter(
                    x=time_data[time_column],
                    y=time_data[metric],
                    mode='lines+markers',
                    name=metric,
                    line=dict(color=color, width=2),
                    marker=dict(size=4)
                ),
                row=row, col=col
            )
            
            # Add moving average
            if len(time_data) > 7:
                ma_7 = time_data[metric].rolling(window=7).mean()
                fig.add_trace(
                    go.Scatter(
                        x=time_data[time_column],
                        y=ma_7,
                        mode='lines',
                        name=f'{metric} (7-day MA)',
                        line=dict(color=color, width=1, dash='dash'),
                        opacity=0.7
                    ),
                    row=row, col=col
                )
        
        fig.update_layout(
            title=title,
            height=400 * rows,
            showlegend=True
        )
        
        return fig
    
    def create_performance_scorecard(self,
                                   metrics_data: Dict,
                                   title: str = "Performance Scorecard") -> go.Figure:
        """
        Create executive performance scorecard
        
        Args:
            metrics_data: Dictionary with metric names and performance data
            title: Scorecard title
            
        Returns:
            Plotly Figure object
        """
        
        # Prepare data for table
        metric_names = []
        current_values = []
        targets = []
        variances = []
        performance_indicators = []
        
        for metric, data in metrics_data.items():
            current = data.get('current_value', 0)
            target = data.get('target_value', current)
            variance = ((current - target) / target * 100) if target != 0 else 0
            
            metric_names.append(metric)
            current_values.append(f"{current:,.2f}")
            targets.append(f"{target:,.2f}")
            variances.append(f"{variance:+.1f}%")
            
            # Performance indicator
            if variance >= 5:
                performance_indicators.append("🟢 Exceeding")
            elif variance >= -5:
                performance_indicators.append("🟡 On Track")
            else:
                performance_indicators.append("🔴 Below Target")
        
        # Create table
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Metric', 'Current Value', 'Target', 'Variance', 'Status'],
                fill_color='#1f77b4',
                font=dict(color='white', size=14),
                align="center"
            ),
            cells=dict(
                values=[metric_names, current_values, targets, variances, performance_indicators],
                fill_color=[['lightgray', 'white'] * len(metric_names)],
                font=dict(size=12),
                align="center",
                height=30
            )
        )])
        
        fig.update_layout(
            title=title,
            height=400,
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        return fig
    
    def create_distribution_plot(self, 
                               data: pd.Series, 
                               title: str = None,
                               bins: int = 30,
                               show_stats: bool = True) -> plt.Figure:
        """
        Create comprehensive distribution plot with statistics
        
        Args:
            data: Series to plot
            title: Plot title
            bins: Number of histogram bins
            show_stats: Whether to show statistical annotations
            
        Returns:
            matplotlib Figure object
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=self.config['figure_size'])
        
        # Histogram with KDE
        sns.histplot(data=data, bins=bins, kde=True, ax=ax1)
        if title:
            ax1.set_title(f'Distribution: {title}')
        
        # Box plot
        sns.boxplot(x=data, ax=ax2)
        ax2.set_title('Box Plot')
        
        # Add statistics if requested
        if show_stats:
            stats_text = (f'Mean: {data.mean():.2f}\n'
                          f'Median: {data.median():.2f}\n'
                          f'Std: {data.std():.2f}\n'
                          f'Skewness: {data.skew():.2f}')
            
            ax1.text(0.02, 0.98, stats_text, transform=ax1.transAxes,
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        return fig
    
    def create_correlation_heatmap(self, 
                                 data: pd.DataFrame,
                                 title: str = "Correlation Matrix",
                                 method: str = 'pearson') -> plt.Figure:
        """
        Create comprehensive correlation heatmap
        
        Args:
            data: DataFrame with numeric variables
            title: Plot title
            method: Correlation method ('pearson', 'spearman', 'kendall')
            
        Returns:
            matplotlib Figure object
        """
        # Calculate correlation matrix
        corr_matrix = data.corr(method=method)
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=self.config['figure_size'])
        
        # Create mask for upper triangle
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        
        # Generate heatmap
        sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', center=0,
                   square=True, ax=ax, cbar_kws={'label': f'{method.title()} Correlation'})
        
        ax.set_title(title)
        plt.tight_layout()
        return fig
    
    def create_comparison_plot(self, 
                             data: pd.DataFrame,
                             x_var: str,
                             y_var: str,
                             group_var: str = None,
                             plot_type: str = 'scatter') -> plt.Figure:
        """
        Create comprehensive comparison plots
        
        Args:
            data: DataFrame containing variables
            x_var: X-axis variable name
            y_var: Y-axis variable name
            group_var: Optional grouping variable
            plot_type: Type of plot ('scatter', 'box', 'violin')
            
        Returns:
            matplotlib Figure object
        """
        fig, ax = plt.subplots(figsize=self.config['figure_size'])
        
        if plot_type == 'scatter':
            if group_var:
                sns.scatterplot(data=data, x=x_var, y=y_var, hue=group_var, ax=ax)
            else:
                sns.scatterplot(data=data, x=x_var, y=y_var, ax=ax)
                
        elif plot_type == 'box':
            sns.boxplot(data=data, x=x_var, y=y_var, ax=ax)
            
        elif plot_type == 'violin':
            sns.violinplot(data=data, x=x_var, y=y_var, ax=ax)
        
        ax.set_title(f'{plot_type.title()} Plot: {y_var} by {x_var}')
        plt.tight_layout()
        return fig

class InteractiveDashboard:
    """Interactive dashboard creation utilities"""
    
    @staticmethod
    def create_overview_dashboard(data: pd.DataFrame) -> go.Figure:
        """
        Create interactive overview dashboard
        
        Args:
            data: DataFrame to visualize
            
        Returns:
            Plotly Figure object
        """
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Data Overview', 'Missing Values', 'Numeric Distributions', 'Correlation Matrix'),
            specs=[[{"type": "table"}, {"type": "bar"}],
                   [{"type": "histogram"}, {"type": "heatmap"}]]
        )
        
        # Data overview table
        overview_data = []
        for col in data.columns:
            overview_data.append([
                col,
                str(data[col].dtype),
                data[col].count(),
                data[col].isnull().sum(),
                f"{(data[col].isnull().sum() / len(data)) * 100:.1f}%"
            ])
        
        fig.add_trace(
            go.Table(
                header=dict(values=['Variable', 'Type', 'Non-Null', 'Missing', 'Missing %']),
                cells=dict(values=list(zip(*overview_data)))
            ),
            row=1, col=1
        )
        
        # Missing values bar chart
        missing_counts = data.isnull().sum()
        fig.add_trace(
            go.Bar(x=missing_counts.index, y=missing_counts.values, name='Missing Values'),
            row=1, col=2
        )
        
        # Numeric distributions (first numeric column)
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            fig.add_trace(
                go.Histogram(x=data[numeric_cols[0]], name=f'Distribution: {numeric_cols[0]}'),
                row=2, col=1
            )
        
        # Correlation heatmap
        if len(numeric_cols) > 1:
            corr_matrix = data[numeric_cols].corr()
            fig.add_trace(
                go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='RdBu',
                    zmid=0
                ),
                row=2, col=2
            )
        
        fig.update_layout(height=800, title_text="Data Analysis Dashboard")
        return fig

def save_publication_figure(fig: plt.Figure, 
                          filename: str, 
                          output_dir: str = "data/output",
                          formats: List[str] = ['png', 'pdf']) -> List[str]:
    """
    Save figure in multiple publication-quality formats
    
    Args:
        fig: matplotlib Figure object
        filename: Base filename (without extension)
        output_dir: Output directory
        formats: List of formats to save
        
    Returns:
        List of saved file paths
    """
    from pathlib import Path
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    saved_files = []
    for fmt in formats:
        filepath = output_path / f"{filename}.{fmt}"
        fig.savefig(filepath, format=fmt, dpi=300, bbox_inches='tight')
        saved_files.append(str(filepath))
    
    return saved_files
