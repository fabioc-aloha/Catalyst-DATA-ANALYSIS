#!/usr/bin/env python3
"""
INTERACTIVE SPSS DATA EXPLORATION SCRIPT
Step 1: Load and understand SPSS data structure, variables, and types
"""

import sys
import os
import pandas as pd
import numpy as np
import pyreadstat
from pathlib import Path

def explore_spss_file(file_path):
    """
    Comprehensive exploration of SPSS file structure and variables
    
    Parameters:
    file_path (str): Path to the SPSS .sav file
    
    Returns:
    dict: Complete data structure analysis
    """
    
    print("="*80)
    print("🔍 SPSS DATA EXPLORATION - STEP 1: UNDERSTANDING THE DATA")
    print("="*80)
    
    try:
        # Load SPSS file with metadata
        print(f"📂 Loading SPSS file: {file_path}")
        data, metadata = pyreadstat.read_sav(file_path)
        
        print(f"✅ Successfully loaded SPSS file!")
        print()
        
        # Basic dataset information
        print("📊 DATASET OVERVIEW")
        print("-" * 40)
        print(f"Dataset shape: {data.shape[0]} rows × {data.shape[1]} columns")
        print(f"Total variables: {len(data.columns)}")
        print(f"Memory usage: {data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        print()
        
        # Variable information
        print("📋 VARIABLE INFORMATION")
        print("-" * 40)
        
        # Create comprehensive variable analysis
        variable_analysis = []
        
        for i, col in enumerate(data.columns, 1):
            var_info = {
                'position': i,
                'name': col,
                'data_type': str(data[col].dtype),
                'non_null_count': data[col].count(),
                'null_count': data[col].isnull().sum(),
                'null_percentage': (data[col].isnull().sum() / len(data)) * 100,
                'unique_values': data[col].nunique(),
                'sample_values': list(data[col].dropna().unique()[:5])  # First 5 unique values
            }
            
            # Add SPSS metadata if available
            if hasattr(metadata, 'variable_labels') and metadata.variable_labels and col in metadata.variable_labels:
                var_info['spss_label'] = metadata.variable_labels[col]
            elif hasattr(metadata, 'column_labels') and metadata.column_labels and col in metadata.column_labels:
                var_info['spss_label'] = metadata.column_labels[col]
            else:
                var_info['spss_label'] = "No label"
                
            if hasattr(metadata, 'value_labels') and metadata.value_labels and col in metadata.value_labels:
                var_info['value_labels'] = metadata.value_labels[col]
            else:
                var_info['value_labels'] = None
                
            variable_analysis.append(var_info)
        
        # Display variable summary table
        print(f"{'#':<3} {'Variable Name':<25} {'Type':<12} {'Non-Null':<8} {'Missing%':<9} {'Unique':<7} {'SPSS Label':<30}")
        print("-" * 95)
        
        for var in variable_analysis:
            print(f"{var['position']:<3} {var['name']:<25} {var['data_type']:<12} "
                  f"{var['non_null_count']:<8} {var['null_percentage']:<8.1f}% {var['unique_values']:<7} "
                  f"{var['spss_label'][:30]:<30}")
        
        print()
        
        # Categorize variables by type
        categorical_vars = []
        continuous_vars = []
        binary_vars = []
        
        for var in variable_analysis:
            if var['data_type'] in ['object', 'category']:
                categorical_vars.append(var['name'])
            elif var['unique_values'] == 2:
                binary_vars.append(var['name'])
            elif var['data_type'] in ['int64', 'float64'] and var['unique_values'] > 10:
                continuous_vars.append(var['name'])
            else:
                categorical_vars.append(var['name'])  # Treat as categorical if few unique values
        
        print("🏷️  VARIABLE CATEGORIZATION")
        print("-" * 40)
        print(f"Continuous variables ({len(continuous_vars)}): {continuous_vars}")
        print(f"Categorical variables ({len(categorical_vars)}): {categorical_vars}")
        print(f"Binary variables ({len(binary_vars)}): {binary_vars}")
        print()
        
        # Missing data analysis
        missing_data = data.isnull().sum()
        vars_with_missing = missing_data[missing_data > 0]
        
        if len(vars_with_missing) > 0:
            print("⚠️  COMPREHENSIVE MISSING DATA ANALYSIS")
            print("-" * 50)
            
            # Basic missing data summary
            print("📊 MISSING DATA SUMMARY:")
            for var, count in vars_with_missing.items():
                percentage = (count / len(data)) * 100
                print(f"  {var}: {count} missing ({percentage:.1f}%)")
            print()
            
            # Missing data patterns analysis
            print("🔍 MISSING DATA PATTERNS:")
            
            # Create missing data matrix
            missing_matrix = data.isnull()
            
            # Count complete cases
            complete_cases = len(data.dropna())
            incomplete_cases = len(data) - complete_cases
            
            print(f"  Complete cases: {complete_cases} ({(complete_cases/len(data)*100):.1f}%)")
            print(f"  Incomplete cases: {incomplete_cases} ({(incomplete_cases/len(data)*100):.1f}%)")
            
            # Pattern analysis - show combinations of missing values
            if len(vars_with_missing) > 1:
                print("\n  📋 Missing Data Patterns (top 5):")
                pattern_counts = missing_matrix[vars_with_missing.index].value_counts().head()
                
                for i, (pattern, count) in enumerate(pattern_counts.items(), 1):
                    pattern_str = ", ".join([f"{var}:{'Missing' if missing else 'Present'}" 
                                           for var, missing in zip(vars_with_missing.index, pattern)])
                    percentage = (count / len(data)) * 100
                    print(f"    {i}. {count} cases ({percentage:.1f}%) - {pattern_str}")
            
            # Missing data mechanism assessment
            print("\n  🔬 MISSING DATA MECHANISM ASSESSMENT:")
            print("     Based on patterns observed:")
            
            # Simple heuristics for missing data mechanisms
            total_missing_rate = (data.isnull().sum().sum() / (len(data) * len(data.columns))) * 100
            
            if total_missing_rate < 5:
                mechanism = "Likely MCAR (Missing Completely At Random)"
                recommendation = "Safe to use listwise deletion or simple imputation"
            elif total_missing_rate < 20:
                mechanism = "Possibly MAR (Missing At Random) - investigate further"
                recommendation = "Consider multiple imputation or pattern-based analysis"
            else:
                mechanism = "Possibly MNAR (Missing Not At Random) - high missingness"
                recommendation = "Investigate missingness mechanisms before analysis"
            
            print(f"     Overall missing rate: {total_missing_rate:.1f}%")
            print(f"     Assessment: {mechanism}")
            print(f"     Recommendation: {recommendation}")
            
            # Variable-specific missing data recommendations
            print("\n  💡 VARIABLE-SPECIFIC RECOMMENDATIONS:")
            for var, count in vars_with_missing.items():
                percentage = (count / len(data)) * 100
                if percentage < 5:
                    rec = "Low missingness - safe for most analyses"
                elif percentage < 15:
                    rec = "Moderate missingness - consider imputation"
                elif percentage < 30:
                    rec = "High missingness - investigate patterns, consider exclusion"
                else:
                    rec = "Very high missingness - likely exclude from analysis"
                
                print(f"    {var} ({percentage:.1f}%): {rec}")
            
            print()
            
        else:
            print("✅ MISSING DATA ANALYSIS")
            print("-" * 40)
            print("No missing data detected - excellent data quality!")
            print("All variables have complete cases for analysis.")
            print()
        
        # Sample data preview
        print("👀 DATA PREVIEW (First 5 rows)")
        print("-" * 40)
        
        # Display first few rows with better formatting
        preview_data = data.head()
        
        # Limit column width for better display
        with pd.option_context('display.max_columns', None, 
                              'display.width', None, 
                              'display.max_colwidth', 20):
            print(preview_data)
        print()
        
        # Value labels information (if available)
        value_labels_available = hasattr(metadata, 'value_labels') and metadata.value_labels
        if value_labels_available:
            print("🏷️  SPSS VALUE LABELS")
            print("-" * 40)
            for var, labels in list(metadata.value_labels.items())[:5]:  # Show first 5
                print(f"{var}: {labels}")
            if len(metadata.value_labels) > 5:
                print(f"... and {len(metadata.value_labels) - 5} more variables with value labels")
            print()
        
        # Summary statistics for continuous variables
        if continuous_vars:
            print("📈 DESCRIPTIVE STATISTICS (Continuous Variables)")
            print("-" * 60)
            stats_data = data[continuous_vars].describe()
            print(stats_data.round(2))
            print()
        
        # Prepare comprehensive missing data analysis for next steps
        missing_data_analysis = {}
        if len(vars_with_missing) > 0:
            # Calculate missing data patterns
            missing_matrix = data.isnull()
            pattern_counts = missing_matrix[vars_with_missing.index].value_counts()
            
            missing_data_analysis = {
                'variables_with_missing': vars_with_missing.to_dict(),
                'total_missing_rate': (data.isnull().sum().sum() / (len(data) * len(data.columns))) * 100,
                'complete_cases': len(data.dropna()),
                'incomplete_cases': len(data) - len(data.dropna()),
                'completion_rate': (len(data.dropna()) / len(data)) * 100,
                'missing_patterns': {
                    'pattern_count': len(pattern_counts),
                    'most_common_patterns': pattern_counts.head().to_dict()
                },
                'recommendations': {
                    'overall_mechanism': "MCAR" if (data.isnull().sum().sum() / (len(data) * len(data.columns))) * 100 < 5 else "MAR/MNAR",
                    'suggested_approach': "listwise_deletion" if (data.isnull().sum().sum() / (len(data) * len(data.columns))) * 100 < 5 else "imputation"
                }
            }
        else:
            missing_data_analysis = {
                'variables_with_missing': {},
                'total_missing_rate': 0.0,
                'complete_cases': len(data),
                'incomplete_cases': 0,
                'completion_rate': 100.0,
                'missing_patterns': {'pattern_count': 0},
                'recommendations': {
                    'overall_mechanism': "No missing data",
                    'suggested_approach': "no_action_needed"
                }
            }
        
        # Prepare results for next steps
        exploration_results = {
            'dataset_info': {
                'shape': data.shape,
                'total_variables': len(data.columns),
                'memory_usage_mb': data.memory_usage(deep=True).sum() / 1024**2
            },
            'variable_analysis': variable_analysis,
            'variable_types': {
                'continuous': continuous_vars,
                'categorical': categorical_vars,
                'binary': binary_vars
            },
            'missing_data': vars_with_missing.to_dict() if len(vars_with_missing) > 0 else {},
            'missing_data_analysis': missing_data_analysis,
            'metadata': {
                'variable_labels': getattr(metadata, 'variable_labels', None),
                'value_labels': getattr(metadata, 'value_labels', None)
            },
            'data_sample': data.head().to_dict()
        }
        
        print("="*80)
        print("✅ DATA EXPLORATION COMPLETE!")
        print("="*80)
        print()
        print("🎯 NEXT STEPS:")
        print("1. Review the variable analysis and missing data patterns above")
        print("2. Consider missing data implications for your analysis plan")
        print("3. Identify key variables for your analysis")
        print("4. Select variables for correlation analysis")
        print("5. Choose grouping variables for comparisons")
        print("6. Specify the main outcome variable")
        print()
        print("📝 VARIABLE SELECTION GUIDANCE:")
        print("- Continuous variables are good for correlations and regression")
        print("- Categorical variables can be used for group comparisons")
        print("- Binary variables work well as outcomes or predictors")
        print("- Variables with high missing data (>20%) may need special handling")
        print("- Consider missing data mechanisms when planning analysis strategy")
        print()
        
        # Add missing data specific guidance
        if len(vars_with_missing) > 0:
            print("⚠️  MISSING DATA CONSIDERATIONS:")
            total_missing_rate = missing_data_analysis['total_missing_rate']
            if total_missing_rate < 5:
                print("- Low overall missingness - proceed with standard analysis")
                print("- Listwise deletion is generally safe")
            elif total_missing_rate < 20:
                print("- Moderate missingness - consider imputation strategies")
                print("- Multiple imputation recommended for unbiased estimates")
                print("- Investigate patterns before finalizing approach")
            else:
                print("- High missingness detected - investigate thoroughly")
                print("- Consider if data is suitable for planned analysis")
                print("- May need specialized missing data techniques")
            print()
        else:
            print("✅ NO MISSING DATA ISSUES:")
            print("- Complete dataset available for all planned analyses")
            print("- No special missing data handling required")
            print()
        
        return data, exploration_results
        
    except Exception as e:
        print(f"❌ Error loading SPSS file: {str(e)}")
        return None, None

def main():
    """Main execution function"""
    
    print("🚀 INTERACTIVE SPSS ANALYSIS - STEP 1: DATA EXPLORATION")
    print()
    
    # Check for SPSS files in common locations
    possible_locations = [
        '../data/raw/',
        '../data/',
        '../notebooks/',
        './'
    ]
    
    spss_files = []
    for location in possible_locations:
        if os.path.exists(location):
            for file in os.listdir(location):
                if file.endswith('.sav'):
                    spss_files.append(os.path.join(location, file))
    
    if spss_files:
        print("📁 Found SPSS files:")
        for i, file in enumerate(spss_files, 1):
            print(f"  {i}. {file}")
        print()
        
        # For now, let's analyze the first one found
        # In interactive mode, user would select
        file_to_analyze = spss_files[0]
        print(f"🎯 Analyzing: {file_to_analyze}")
        print()
        
        # Run exploration
        data, results = explore_spss_file(file_to_analyze)
        
        if data is not None and results is not None:
            # Save exploration results for next steps
            import json
            results_file = "./results/spss_exploration_results.json"
            os.makedirs(os.path.dirname(results_file), exist_ok=True)
            
            # Convert results to JSON-serializable format
            json_results = {
                'dataset_info': results['dataset_info'],
                'variable_types': results['variable_types'],
                'missing_data': results['missing_data'],
                'exploration_timestamp': pd.Timestamp.now().isoformat()
            }
            
            with open(results_file, 'w') as f:
                json.dump(json_results, f, indent=2)
            
            print(f"💾 Exploration results saved to: {results_file}")
            print()
            print("🔄 Ready for Step 2: Variable Selection and Analysis Design")
        else:
            print("❌ Failed to explore SPSS data. Please check the file and try again.")
            
    else:
        print("❌ No SPSS (.sav) files found in common locations.")
        print("📍 Please place your SPSS file in one of these folders:")
        for location in possible_locations:
            print(f"  - {location}")
        print()
        print("💡 Or specify the full path to your SPSS file.")

if __name__ == "__main__":
    main()
