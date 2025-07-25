# Step-by-Step Installation Script for Windows PowerShell
# To avoid dependency resolution conflicts

Write-Host "🚀 Installing Data Analysis Environment..." -ForegroundColor Green

# Step 1: Core Foundation (Essential)
Write-Host "📦 Step 1: Installing core scientific computing libraries..." -ForegroundColor Cyan
& python -m pip install "numpy>=1.24.0,<2.0.0"
& python -m pip install "pandas>=2.0.0,<3.0.0"  
& python -m pip install "scipy>=1.10.0"

# Step 2: Visualization Foundation
Write-Host "📊 Step 2: Installing visualization libraries..." -ForegroundColor Cyan
& python -m pip install "matplotlib>=3.7.0"
& python -m pip install "seaborn>=0.12.0"

# Step 3: Statistical Analysis Core
Write-Host "📈 Step 3: Installing statistical analysis libraries..." -ForegroundColor Cyan
& python -m pip install "statsmodels>=0.14.0"
& python -m pip install "scikit-learn>=1.3.0"

# Step 4: Jupyter Environment
Write-Host "📝 Step 4: Installing Jupyter environment..." -ForegroundColor Cyan
& python -m pip install "jupyter>=1.0.0"
& python -m pip install "jupyterlab>=4.0.0"
& python -m pip install "ipywidgets>=8.0.0"

# Step 5: Data I/O
Write-Host "💾 Step 5: Installing data I/O libraries..." -ForegroundColor Cyan
& python -m pip install "openpyxl>=3.1.0"
& python -m pip install "requests>=2.28.0"
& python -m pip install "python-dotenv>=1.0.0"

# Step 6: Testing Framework
Write-Host "🧪 Step 6: Installing testing framework..." -ForegroundColor Cyan
& python -m pip install "pytest>=7.0.0"

Write-Host "✅ Core installation complete!" -ForegroundColor Green
Write-Host "📋 Run 'pip install -r requirements-analysis.txt' for advanced features" -ForegroundColor Yellow
Write-Host "🔍 Run 'pip install -r requirements-SPSS.txt' for SPSS integration" -ForegroundColor Yellow
Write-Host "🛠️ Run 'python verify_environment.py' to test installation" -ForegroundColor Yellow
