#!/usr/bin/env python3
"""
Environment Verification Script
Tests all critical libraries for the data analysis environment
"""

import sys
import importlib
from typing import Dict, List, Tuple

def test_import(module_name: str, alternative_name: str = None) -> Tuple[bool, str]:
    """Test importing a module and return success status and message."""
    try:
        importlib.import_module(module_name)
        return True, f"✅ {module_name}"
    except (ImportError, ValueError) as e:
        if alternative_name:
            try:
                importlib.import_module(alternative_name)
                return True, f"✅ {alternative_name} (alternative for {module_name})"
            except (ImportError, ValueError):
                return False, f"❌ {module_name} and {alternative_name} failed"
        return False, f"❌ {module_name}: {str(e)[:50]}..."

def test_environment() -> Dict[str, List[Tuple[bool, str]]]:
    """Test all environment components."""
    
    results = {
        "Core Data Analysis": [
            test_import("pandas"),
            test_import("numpy"),
            test_import("scipy"),
            test_import("matplotlib"),
            test_import("seaborn"),
        ],
        
        "Statistical Analysis": [
            test_import("statsmodels"),
            test_import("pingouin"),
            test_import("factor_analyzer"),
            test_import("reliability"),
            test_import("scipy.stats"),
        ],
        
        "Machine Learning": [
            test_import("sklearn"),
            test_import("xgboost"),
            test_import("lightgbm"),
            test_import("imblearn"),
        ],
        
        "Visualization": [
            test_import("plotly"),
            test_import("bokeh"),
            test_import("altair"),
            test_import("matplotlib"),
            test_import("seaborn"),
        ],
        
        "Business Intelligence": [
            test_import("dash"),
            test_import("dash_bootstrap_components"),
            test_import("kaleido"),
        ],
        
        "SPSS Integration": [
            test_import("pyreadstat"),
            # savReaderWriter disabled due to Python 3.11 compatibility issues
            # pyreadstat provides robust SPSS file reading capabilities
        ],
        
        "Specialized Analysis": [
            test_import("nltk"),
            test_import("textblob"),
            test_import("geopandas"),
            test_import("folium"),
            test_import("networkx"),
            test_import("arch"),
        ],
        
        "Time Series": [
            test_import("arch"),
            test_import("pmdarima", "statsmodels.tsa"),  # pmdarima has issues
        ],
        
        "Bayesian Analysis": [
            test_import("pymc"),
            test_import("arviz"),
        ],
        
        "Jupyter Environment": [
            test_import("jupyter"),
            test_import("jupyterlab"),
            test_import("ipywidgets"),
        ],
        
        "Data I/O": [
            test_import("openpyxl"),
            test_import("xlsxwriter"),
            test_import("requests"),
            test_import("dotenv"),  # python-dotenv imports as 'dotenv'
        ],
    }
    
    return results

def print_results(results: Dict[str, List[Tuple[bool, str]]]):
    """Print test results in a formatted way."""
    
    print("🎯 DATA ANALYSIS ENVIRONMENT VERIFICATION")
    print("=" * 50)
    
    total_tests = 0
    passed_tests = 0
    
    for category, tests in results.items():
        print(f"\n📊 {category}:")
        print("-" * 30)
        
        for success, message in tests:
            print(f"  {message}")
            total_tests += 1
            if success:
                passed_tests += 1
    
    print("\n" + "=" * 50)
    print(f"📈 SUMMARY: {passed_tests}/{total_tests} tests passed")
    
    success_rate = (passed_tests / total_tests) * 100
    if success_rate >= 90:
        print(f"🎉 Environment Status: EXCELLENT ({success_rate:.1f}%)")
    elif success_rate >= 80:
        print(f"✅ Environment Status: GOOD ({success_rate:.1f}%)")
    elif success_rate >= 70:
        print(f"⚠️ Environment Status: ACCEPTABLE ({success_rate:.1f}%)")
    else:
        print(f"❌ Environment Status: NEEDS ATTENTION ({success_rate:.1f}%)")
    
    print("\n🚀 Ready for data analysis workflows!")

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print()
    
    results = test_environment()
    print_results(results)
