#!/usr/bin/env python3
"""
Installation Verification Script for Comprehensive Tiered Analytics Suite

This script verifies that all required dependencies are properly installed
and provides diagnostic information for troubleshooting.

Author: Brandon Deloatch
Affiliation: Quipu Research Labs, LLC
Date: 2025-10-02
Version: v1.3
"""

import sys
import importlib
from typing import Tuple

def check_python_version() -> bool:
"""Check if Python version meets requirements."""
required_version = (3, 8)
current_version = sys.version_info[:2]

print("🐍 Python Version Check:")
print(f" Current: {sys.version}")
print(f" Required: >={required_version[0]}.{required_version[1]}")

if current_version >= required_version:
print(" Python version OK")
return True

print(" Python version too old")
return False

def check_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
"""Check if a package is installed and get version."""
if import_name is None:
import_name = package_name

try:
module = importlib.import_module(import_name)
version = getattr(module, '__version__', 'Unknown')
return True, version
except ImportError:
return False, 'Not installed'

def get_package_categories():
"""Get all package categories for verification."""
core_packages = [
('pandas', 'pandas'),
('numpy', 'numpy'),
('scipy', 'scipy'),
('matplotlib', 'matplotlib'),
('seaborn', 'seaborn'),
('plotly', 'plotly'),
('scikit-learn', 'sklearn'),
('statsmodels', 'statsmodels'),
]

ml_packages = [
('xgboost', 'xgboost'),
('lightgbm', 'lightgbm'),
('catboost', 'catboost'),
]

specialized_packages = [
('PyWavelets', 'pywt'),
('diptest', 'diptest'),
('ta', 'ta'),
('pykalman', 'pykalman'),
]

jupyter_packages = [
('jupyter', 'jupyter'),
('jupyterlab', 'jupyterlab'),
('ipywidgets', 'ipywidgets'),
]

optional_packages = [
('tensorflow', 'tensorflow'),
('torch', 'torch'),
]

return [
("Core Data Science", core_packages),
("🤖 Machine Learning", ml_packages),
(" Specialized Analytics", specialized_packages),
(" Jupyter Environment", jupyter_packages),
("🧠 Deep Learning (Optional)", optional_packages),
]


def verify_packages(all_packages):
"""Verify all packages and return installation statistics."""
total_packages = 0
installed_packages = 0
missing_packages = []

for category, packages in all_packages:
print(f"{category}:")

for package_name, import_name in packages:
total_packages += 1
is_installed, version = check_package(package_name, import_name)

if is_installed:
installed_packages += 1
print(f" [OK] {package_name:<20} {version}")
else:
missing_packages.append(package_name)
print(f" [MISSING] {package_name:<20} {version}")

print()

return total_packages, installed_packages, missing_packages


def test_basic_functionality():
"""Test basic functionality with core packages."""
print("\n🧪 BASIC FUNCTIONALITY TEST:")
try:
import pandas as pd # pylint: disable=import-outside-toplevel
import numpy as np # pylint: disable=import-outside-toplevel

# Create test data
test_df = pd.DataFrame({
'x': np.random.randn(100),
'y': np.random.randn(100)
})

# Test basic operations
correlation = test_df.corr().iloc[0, 1]

print(" Data creation: OK")
print(f" Correlation calculation: {correlation:.3f}")
print(" Basic functionality: WORKING")

except ImportError as import_error:
print(f" Basic functionality test failed: {import_error}")


def print_summary(python_ok, total_packages, installed_packages, missing_packages):
"""Print installation summary and recommendations."""
print("=" * 70)
print("INSTALLATION SUMMARY:")
print(f" Python Version: {'OK' if python_ok else 'Needs Update'}")
print(f" Packages Installed: {installed_packages}/{total_packages}")
print(f" Success Rate: {installed_packages/total_packages*100:.1f}%")

if missing_packages:
print(f"\nMissing Packages ({len(missing_packages)}):")
for package in missing_packages:
print(f" • {package}")

print("\nInstallation Commands:")
print(f" pip install {' '.join(missing_packages)}")
print(" # or")
print(" pip install -r requirements.txt")


def print_final_status(python_ok, installed_packages, core_package_count):
"""Print final status and next steps."""
print("\nOVERALL STATUS:")
if python_ok and installed_packages >= core_package_count:
print(" READY TO USE!")
print(" Start with: jupyter lab Tier1_Descriptive.ipynb")
else:
print(" SETUP REQUIRED")
print(" Please install missing dependencies")

print("=" * 70)


def main():
"""Main verification function."""
print("=" * 70)
print(" COMPREHENSIVE TIERED ANALYTICS SUITE - INSTALLATION VERIFICATION")
print("=" * 70)

# Check Python version
python_ok = check_python_version()
print()

# Get package categories
all_packages = get_package_categories()
core_package_count = len(all_packages[0][1]) # Core packages count

# Verify all packages
total_packages, installed_packages, missing_packages = verify_packages(all_packages)

# Print summary
print_summary(python_ok, total_packages, installed_packages, missing_packages)

# Test basic functionality if core packages are available
if installed_packages >= core_package_count:
test_basic_functionality()

# Print final status
print_final_status(python_ok, installed_packages, core_package_count)

if __name__ == "__main__":
main()
