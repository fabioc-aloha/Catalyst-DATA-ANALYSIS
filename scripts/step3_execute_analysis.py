#!/usr/bin/env python3
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
        
        print("\nTo execute a specific configuration, call:")
        print("execute_selected_analysis(config_index=1)  # for first configuration")
