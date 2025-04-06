from setuptools import setup
import os
import subprocess

def create_project_structure():
    """Create necessary files and directories for the Streamlit project."""
    os.makedirs(".streamlit", exist_ok=True)

    # Create secrets.toml
    with open(".streamlit/secrets.toml", "w") as f:
        f.write("# Add secrets here\n")

    # Create utility and app files
    for filename in ["utils.py", "app.py"]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("# Write your code here\n")

    # Update .gitignore
    gitignore_path = ".gitignore"
    entry = ".streamlit/"

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]
        if entry not in lines:
            with open(gitignore_path, "a") as f:
                f.write(f"\n{entry}\n")
    else:
        with open(gitignore_path, "w") as f:
            f.write(f"{entry}\n")

    print("✅ Streamlit setup completed successfully!")

def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("⬆️ Upgrading pip...")
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)

def install_dependencies():
    """Install required dependencies."""
    dependencies = [
        "streamlit",
        "requests",
        "numpy",
        "pandas",
        "plotly"
    ]
    print("📦 Installing dependencies...")
    subprocess.run(["pip", "install"] + dependencies, check=True)

# Run setup tasks
create_project_structure()
upgrade_pip()
install_dependencies()

# Define setup
setup(
    name="StreamlitProjectSetup",
    version="0.1",
    description="A simple setup script for initializing a Streamlit project",
    install_requires=[
        "streamlit",
        "requests",
        "numpy",
        "pandas",
        "plotly"
    ],
)
