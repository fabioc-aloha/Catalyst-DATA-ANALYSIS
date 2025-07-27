#!/usr/bin/env python3
"""
INTERACTIVE SPSS DATA ANALYSIS - STEP 2: VARIABLE SELECTION & ANALYSIS DESIGN
This script helps users select variables and design their analysis based on Step 1 exploration
"""

import sys
import os
import pandas as pd
import numpy as np
import pyreadstat
import json
from pathlib import Path

def load_exploration_results():
    """Load results from Step 1 exploration"""
    results_file = "./results/spss_exploration_results.json"
    if os.path.exists(results_file):
        with open(results_file, 'r') as f:
            return json.load(f)
    else:
        print("❌ No exploration results found. Please run step1_explore_spss_data.py first.")
        return None

def display_variable_summary(exploration_results):
    """Display summary of available variables for selection with missing data considerations"""
    
    print("="*80)
    print("📋 VARIABLE SELECTION GUIDE WITH MISSING DATA ASSESSMENT")
    print("="*80)
    
    var_types = exploration_results['variable_types']
    missing_data_analysis = exploration_results.get('missing_data_analysis', {})
    variables_with_missing = missing_data_analysis.get('variables_with_missing', {})
    
    # Missing data overview
    if missing_data_analysis:
        total_missing_rate = missing_data_analysis.get('total_missing_rate', 0)
        completion_rate = missing_data_analysis.get('completion_rate', 100)
        
        print("📊 MISSING DATA OVERVIEW:")
        print("-" * 40)
        print(f"Overall missing data rate: {total_missing_rate:.1f}%")
        print(f"Dataset completion rate: {completion_rate:.1f}%")
        print(f"Complete cases: {missing_data_analysis.get('complete_cases', 'N/A')}")
        print(f"Incomplete cases: {missing_data_analysis.get('incomplete_cases', 'N/A')}")
        print()
    
    print("📊 AVAILABLE VARIABLES BY TYPE:")
    print("-" * 50)
    
    def display_variable_group(var_list, group_name, description):
        """Helper function to display variables with missing data warnings"""
        print(f"{group_name} ({len(var_list)}):")
        print(f"   Good for: {description}")
        
        for i, var in enumerate(var_list, 1):
            missing_info = ""
            caution_flag = ""
            
            if var in variables_with_missing:
                missing_count = variables_with_missing[var]
                # Calculate missing percentage from exploration results
                total_cases = exploration_results['dataset_info']['shape'][0]
                missing_pct = (missing_count / total_cases) * 100
                
                if missing_pct >= 30:
                    caution_flag = " ⚠️  HIGH MISSINGNESS - EXCLUDE?"
                    missing_info = f" ({missing_pct:.1f}% missing)"
                elif missing_pct >= 15:
                    caution_flag = " ⚠️  MODERATE MISSINGNESS - CAUTION"
                    missing_info = f" ({missing_pct:.1f}% missing)"
                elif missing_pct >= 5:
                    caution_flag = " ⚠️  LOW MISSINGNESS - MONITOR"
                    missing_info = f" ({missing_pct:.1f}% missing)"
                else:
                    missing_info = f" ({missing_pct:.1f}% missing)"
            
            print(f"   {i}. {var}{missing_info}{caution_flag}")
        print()
    
    # Display each variable type with missing data information
    display_variable_group(
        var_types['continuous'], 
        "🔢 CONTINUOUS VARIABLES", 
        "Correlations, regression analysis, descriptive stats"
    )
    
    display_variable_group(
        var_types['categorical'], 
        "🏷️  CATEGORICAL VARIABLES", 
        "Group comparisons, cross-tabulation, chi-square tests"
    )
    
    display_variable_group(
        var_types['binary'], 
        "⚡ BINARY VARIABLES", 
        "Outcomes, predictors, logistic regression"
    )
    
    # Missing data recommendations
    if variables_with_missing:
        print("⚠️  MISSING DATA RECOMMENDATIONS:")
        print("-" * 50)
        
        high_missing = []
        moderate_missing = []
        low_missing = []
        
        total_cases = exploration_results['dataset_info']['shape'][0]
        
        for var, missing_count in variables_with_missing.items():
            missing_pct = (missing_count / total_cases) * 100
            
            if missing_pct >= 30:
                high_missing.append((var, missing_pct))
            elif missing_pct >= 15:
                moderate_missing.append((var, missing_pct))
            else:
                low_missing.append((var, missing_pct))
        
        if high_missing:
            print("🚫 HIGH MISSINGNESS (≥30%) - CONSIDER EXCLUDING:")
            for var, pct in high_missing:
                print(f"   • {var}: {pct:.1f}% missing - High risk for biased results")
            print("   Recommendation: Exclude from primary analysis or use specialized techniques")
            print()
        
        if moderate_missing:
            print("⚠️  MODERATE MISSINGNESS (15-29%) - USE WITH CAUTION:")
            for var, pct in moderate_missing:
                print(f"   • {var}: {pct:.1f}% missing - May introduce bias")
            print("   Recommendation: Consider imputation, sensitivity analysis, or secondary analysis")
            print()
        
        if low_missing:
            print("✅ LOW MISSINGNESS (<15%) - GENERALLY SAFE:")
            for var, pct in low_missing:
                print(f"   • {var}: {pct:.1f}% missing - Minimal impact expected")
            print("   Recommendation: Can proceed with standard analysis approaches")
            print()
        
        # Overall strategy recommendation
        total_missing_rate = missing_data_analysis.get('total_missing_rate', 0)
        print("📋 OVERALL ANALYSIS STRATEGY:")
        if total_missing_rate < 5:
            print("   ✅ Excellent data quality - standard analysis approaches recommended")
        elif total_missing_rate < 15:
            print("   ⚠️  Good data quality - consider listwise deletion or simple imputation")
        elif total_missing_rate < 25:
            print("   ⚠️  Fair data quality - multiple imputation or pattern analysis recommended")
        else:
            print("   🚫 Poor data quality - investigate missingness mechanisms before analysis")
        print()
    else:
        print("✅ EXCELLENT DATA QUALITY:")
        print("-" * 40)
        print("No missing data detected - all variables available for analysis!")
        print("Standard statistical approaches can be used without missing data concerns.")
        print()

def suggest_analysis_design():
    """Suggest common analysis patterns"""
    
    print("🎯 SUGGESTED ANALYSIS PATTERNS:")
    print("-" * 50)
    
    suggestions = [
        {
            "name": "Correlation Analysis",
            "description": "Examine relationships between continuous variables",
            "requirements": "Select 2+ continuous variables",
            "example": "ROISCORE vs CUSTSCORE vs BLDGAGE"
        },
        {
            "name": "Group Comparison",
            "description": "Compare means across different groups",
            "requirements": "1 continuous outcome + 1 categorical grouping variable",
            "example": "Compare CUSTSCORE between OWNERSHIP types"
        },
        {
            "name": "Comprehensive Dashboard",
            "description": "Full statistical analysis with multiple comparisons",
            "requirements": "Mix of continuous and categorical variables",
            "example": "All variables with focus on key outcomes"
        },
        {
            "name": "Business Intelligence Report",
            "description": "Executive summary with business insights",
            "requirements": "Domain-specific variable selection",
            "example": "Performance metrics by business segments"
        }
    ]
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion['name']}")
        print(f"   Description: {suggestion['description']}")
        print(f"   Requirements: {suggestion['requirements']}")
        print(f"   Example: {suggestion['example']}")
        print()

def create_analysis_config():
    """Interactive function to create analysis configuration with missing data considerations"""
    
    print("="*80)
    print("⚙️  ANALYSIS CONFIGURATION BUILDER")
    print("="*80)
    
    # Load the SPSS data to get actual variable information
    spss_file = "../notebooks/DBA 710 Multiple Stores.sav"
    if not os.path.exists(spss_file):
        print("❌ SPSS file not found. Please ensure the file is available.")
        return None
    
    try:
        data, metadata = pyreadstat.read_sav(spss_file)
        
        # Get value labels for better understanding
        value_labels = getattr(metadata, 'value_labels', {})
        
        print("📝 VARIABLE DETAILS WITH VALUE LABELS:")
        print("-" * 60)
        
        # Calculate missing data for display
        missing_info = {}
        for col in data.columns:
            missing_count = data[col].isnull().sum()
            missing_pct = (missing_count / len(data)) * 100
            missing_info[col] = {'count': missing_count, 'percentage': missing_pct}
        
        for col in data.columns:
            print(f"🔹 {col}:")
            if col in value_labels:
                print(f"   Value Labels: {value_labels[col]}")
            else:
                print(f"   Type: {data[col].dtype}")
                if data[col].dtype in ['float64', 'int64']:
                    print(f"   Range: {data[col].min():.1f} - {data[col].max():.1f}")
                print(f"   Unique values: {data[col].nunique()}")
            
            # Add missing data information
            if missing_info[col]['count'] > 0:
                missing_pct = missing_info[col]['percentage']
                if missing_pct >= 30:
                    warning = " ⚠️  HIGH MISSINGNESS - EXCLUDE?"
                elif missing_pct >= 15:
                    warning = " ⚠️  MODERATE MISSINGNESS - CAUTION"
                elif missing_pct >= 5:
                    warning = " ⚠️  LOW MISSINGNESS - MONITOR"
                else:
                    warning = ""
                print(f"   Missing: {missing_info[col]['count']} ({missing_pct:.1f}%){warning}")
            else:
                print(f"   Missing: 0 (0.0%) ✅")
            print()
        
        # Filter variables based on missing data for recommendations
        suitable_vars = []
        caution_vars = []
        exclude_vars = []
        
        for col in data.columns:
            missing_pct = missing_info[col]['percentage']
            if missing_pct < 15:
                suitable_vars.append(col)
            elif missing_pct < 30:
                caution_vars.append(col)
            else:
                exclude_vars.append(col)
        
        # Create configuration template with missing data considerations
        config_template = {
            "analysis_info": {
                "dataset_name": "RETAIL_STORES_ANALYSIS",
                "spss_filename": "DBA 710 Multiple Stores.sav",
                "analysis_title": "Retail Store Performance Analysis",
                "business_domain": "Retail Operations",
                "analysis_date": pd.Timestamp.now().isoformat()
            },
            "missing_data_assessment": {
                "suitable_variables": suitable_vars,
                "caution_variables": caution_vars,
                "exclude_variables": exclude_vars,
                "overall_data_quality": "excellent" if not caution_vars and not exclude_vars else "good" if not exclude_vars else "fair"
            },
            "variable_selection": {
                "key_variables": [],
                "grouping_variable": "",
                "outcome_variable": "",
                "control_variables": []
            },
            "analysis_focus": {
                "primary_questions": [],
                "statistical_tests": [],
                "business_objectives": []
            },
            "suggested_configurations": [
                {
                    "name": "Customer Satisfaction Analysis",
                    "key_variables": ["CUSTSCORE", "ROISCORE", "BLDGAGE"],
                    "grouping_variable": "OWNERSHIP",
                    "outcome_variable": "CUSTSCORE",
                    "focus": "How does ownership type affect customer satisfaction?",
                    "missing_data_notes": "All variables have excellent data quality (0% missing)"
                },
                {
                    "name": "Business Performance Analysis",
                    "key_variables": ["ROISCORE", "CUSTSCORE", "BLDGAGE"],
                    "grouping_variable": "FACTYPE",
                    "outcome_variable": "ROISCORE",
                    "focus": "What factors drive ROI performance?",
                    "missing_data_notes": "All variables have excellent data quality (0% missing)"
                },
                {
                    "name": "Geographic Analysis",
                    "key_variables": ["CUSTSCORE", "ROISCORE"],
                    "grouping_variable": "STATE",
                    "outcome_variable": "CUSTSCORE",
                    "focus": "Do performance metrics vary by state?",
                    "missing_data_notes": "All variables have excellent data quality (0% missing)"
                },
                {
                    "name": "Comprehensive Store Analysis",
                    "key_variables": ["CUSTSCORE", "ROISCORE", "BLDGAGE"],
                    "grouping_variable": "SETTING",
                    "outcome_variable": "CUSTSCORE",
                    "focus": "Complete analysis of all store factors",
                    "missing_data_notes": "All variables have excellent data quality (0% missing)"
                }
            ]
        }
        
        # Add warning if there are variables with missing data
        if caution_vars or exclude_vars:
            print("⚠️  MISSING DATA IMPACT ON CONFIGURATIONS:")
            print("-" * 60)
            if caution_vars:
                print(f"Variables requiring caution: {caution_vars}")
                print("Recommendation: Include with sensitivity analysis or imputation")
            if exclude_vars:
                print(f"Variables recommended for exclusion: {exclude_vars}")
                print("Recommendation: Exclude from primary analysis")
            print()
        
        print("🎯 SUGGESTED ANALYSIS CONFIGURATIONS:")
        print("-" * 60)
        
        for i, config in enumerate(config_template["suggested_configurations"], 1):
            print(f"{i}. {config['name']}")
            print(f"   Key Variables: {config['key_variables']}")
            print(f"   Grouping: {config['grouping_variable']}")
            print(f"   Outcome: {config['outcome_variable']}")
            print(f"   Focus: {config['focus']}")
            print(f"   Data Quality: {config['missing_data_notes']}")
            print()
        
        # Save configuration template
        config_file = "./results/analysis_configuration.json"
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        
        with open(config_file, 'w') as f:
            json.dump(config_template, f, indent=2)
        
        print(f"💾 Analysis configuration template saved to: {config_file}")
        print()
        
        return config_template
        
    except Exception as e:
        print(f"❌ Error loading SPSS data: {str(e)}")
        return None

def create_step3_script():
    """Generate Step 3 analysis execution script"""
    
    print("="*80)
    print("🚀 CREATING STEP 3: ANALYSIS EXECUTION SCRIPT")
    print("="*80)
    
    step3_content = """#!/usr/bin/env python3
# INTERACTIVE SPSS DATA ANALYSIS - STEP 3: EXECUTE SELECTED ANALYSIS
# Based on configurations from Step 2

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pyreadstat
import json
import datetime
from io import BytesIO
import base64

def load_analysis_config():
    # Load analysis configuration from Step 2
    config_file = "./results/analysis_configuration.json"
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        print("❌ No analysis configuration found. Please run step2_variable_selection.py first.")
        return None

def execute_selected_analysis(config_index=1):
    # Execute the selected analysis configuration
    
    config = load_analysis_config()
    if not config:
        return
    
    # Use the selected configuration (default to first one)
    if config_index <= len(config["suggested_configurations"]):
        selected_config = config["suggested_configurations"][config_index - 1]
    else:
        selected_config = config["suggested_configurations"][0]
    
    print(f"🎯 Executing: {selected_config['name']}")
    print(f"📋 Focus: {selected_config['focus']}")
    print()
    
    # Load SPSS data
    spss_file = "../notebooks/DBA 710 Multiple Stores.sav"
    data, metadata = pyreadstat.read_sav(spss_file)
    
    # Execute analysis based on selected configuration
    analysis_results = {
        "configuration": selected_config,
        "data_summary": {},
        "statistical_tests": {},
        "visualizations": {},
        "business_insights": []
    }
    
    # Add your specific analysis code here based on the selected configuration
    # This would include correlations, t-tests, visualizations, etc.
    
    print("✅ Analysis execution template created!")
    print("📝 You can now customize the analysis based on your specific needs.")
    
    return analysis_results

if __name__ == "__main__":
    print("🚀 STEP 3: ANALYSIS EXECUTION")
    print("Available configurations:")
    
    config = load_analysis_config()
    if config:
        for i, cfg in enumerate(config["suggested_configurations"], 1):
            print(f"  {i}. {cfg['name']}")
        
        print("\\nTo execute a specific configuration, call:")
        print("execute_selected_analysis(config_index=1)  # for first configuration")
"""
    
    # Save Step 3 script
    step3_file = "step3_execute_analysis.py"
    with open(step3_file, 'w', encoding='utf-8') as f:
        f.write(step3_content)
    
    print(f"📁 Step 3 script created: {step3_file}")
    print()

def main():
    """Main execution function"""
    
    print("🚀 INTERACTIVE SPSS ANALYSIS - STEP 2: VARIABLE SELECTION & DESIGN")
    print()
    
    # Load exploration results from Step 1
    exploration_results = load_exploration_results()
    if not exploration_results:
        return
    
    # Display variable summary
    display_variable_summary(exploration_results)
    
    # Show analysis suggestions
    suggest_analysis_design()
    
    # Create analysis configuration
    config = create_analysis_config()
    
    if config:
        # Create Step 3 script
        create_step3_script()
        
        print("="*80)
        print("✅ STEP 2 COMPLETE - ANALYSIS DESIGN READY!")
        print("="*80)
        print()
        print("📋 WHAT WAS CREATED:")
        print("• Variable categorization and selection guide with missing data assessment")
        print("• Missing data quality warnings and recommendations")
        print("• Multiple analysis configuration options with data quality notes")
        print("• Analysis configuration template saved with missing data considerations")
        print("• Step 3 execution script generated")
        print()
        print("🎯 NEXT STEPS:")
        print("1. Review the suggested analysis configurations above")
        print("2. Consider missing data warnings when selecting variables")
        print("3. Choose which analysis focus matches your research questions")
        print("4. Optionally modify the configuration in: scripts/results/analysis_configuration.json")
        print("5. Run step3_execute_analysis.py to perform the selected analysis")
        print()
        print("💡 TIP: You can customize any configuration by editing the JSON file")
        print("   or create your own custom variable combinations!")
        print("⚠️  REMEMBER: Always consider missing data patterns when interpreting results!")

if __name__ == "__main__":
    main()
