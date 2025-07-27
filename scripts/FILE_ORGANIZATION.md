# SPSS Analysis Scripts - File Organization

## 📁 Organized File Structure

All SPSS analysis scripts now save their outputs in organized folders within the `./scripts/` directory to avoid confusion and maintain better project organization.

### 🎯 Output Folders

```
scripts/
├── results/                           # Analysis results and configurations
│   ├── spss_exploration_results.json  # Step 1: Data exploration results
│   ├── analysis_configuration.json    # Step 2: Analysis configurations
│   └── *.md                          # Generated analysis reports
├── data/                             # Script-specific data files
└── [analysis scripts]               # Python scripts
```

### 📝 Script Workflow

1. **Step 1** (`step1_explore_spss_data.py`):
   - Saves: `./results/spss_exploration_results.json`
   - Contains: Dataset overview, variable analysis, missing data assessment

2. **Step 2** (`step2_variable_selection.py`):
   - Reads: `./results/spss_exploration_results.json`
   - Saves: `./results/analysis_configuration.json`
   - Generates: `step3_execute_analysis.py`

3. **Step 3** (`step3_execute_analysis.py`):
   - Reads: `./results/analysis_configuration.json`
   - Saves: Analysis results in `./results/`

4. **Unified Reports** (`generate_unified_report.py`):
   - Saves: Comprehensive reports in `./results/`

### ✅ Benefits

- **Organized Structure**: All outputs contained within scripts folder
- **No Confusion**: Clear separation from main project data folder
- **Easy Navigation**: Results grouped in dedicated folder
- **Version Control**: Easier to manage and track analysis outputs
- **Self-Contained**: Scripts and their outputs stay together

### 🔄 Migration Complete

All path references have been updated to use the new organized structure:
- ✅ Step 1: Uses `./results/` for output
- ✅ Step 2: Uses `./results/` for input/output
- ✅ Step 3: Uses `./results/` for input/output
- ✅ Unified reports: Already configured for `./results/`

This ensures a clean, organized workflow where all analysis outputs are properly contained within the scripts directory structure.
