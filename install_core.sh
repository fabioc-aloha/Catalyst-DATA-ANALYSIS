# Step-by-Step Installation Guide
# To avoid dependency resolution conflicts

echo "🚀 Installing Data Analysis Environment..."

# Step 1: Core Foundation (Essential)
echo "📦 Step 1: Installing core scientific computing libraries..."
pip install numpy>=1.24.0,<2.0.0
pip install pandas>=2.0.0,<3.0.0
pip install scipy>=1.10.0

# Step 2: Visualization Foundation
echo "📊 Step 2: Installing visualization libraries..."
pip install matplotlib>=3.7.0
pip install seaborn>=0.12.0

# Step 3: Statistical Analysis Core
echo "📈 Step 3: Installing statistical analysis libraries..."
pip install statsmodels>=0.14.0
pip install scikit-learn>=1.3.0

# Step 4: Jupyter Environment
echo "📝 Step 4: Installing Jupyter environment..."
pip install jupyter>=1.0.0
pip install jupyterlab>=4.0.0
pip install ipywidgets>=8.0.0

# Step 5: Data I/O
echo "💾 Step 5: Installing data I/O libraries..."
pip install openpyxl>=3.1.0
pip install requests>=2.28.0
pip install python-dotenv>=1.0.0

# Step 6: Testing Framework
echo "🧪 Step 6: Installing testing framework..."
pip install pytest>=7.0.0

echo "✅ Core installation complete!"
echo "📋 Run 'pip install -r requirements-analysis.txt' for advanced features"
echo "🔍 Run 'pip install -r requirements-SPSS.txt' for SPSS integration"
echo "🛠️ Run 'python verify_environment.py' to test installation"
