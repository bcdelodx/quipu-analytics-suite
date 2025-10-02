#!/usr/bin/env python3
"""
Setup configuration for Comprehensive Tiered Analytics Suite

Author: Brandon Deloatch
Affiliation: Quipu Research Labs, LLC
Date: 2025-10-02
Version: v1.3
License: MIT
"""

from setuptools import setup, find_packages

# Read README for long description
def read_readme():
"""Read README.md file for package long description."""
with open("README.md", "r", encoding="utf-8") as fh:
return fh.read()

# Read requirements
def read_requirements(filename):
"""Read requirements from specified file, filtering comments and empty lines."""
with open(filename, "r", encoding="utf-8") as fh:
return [line.strip() for line in fh
if line.strip() and not line.startswith("#")]

# Package metadata
setup(
name="quipu-analytics-suite",
version="1.3.0",
author="Brandon Deloatch",
author_email="brandon@quipuresearchlabs.com",
description="Comprehensive Tiered Analytics Framework for Data Science",
long_description=read_readme(),
long_description_content_type="text/markdown",
url="https://github.com/bcdelodx/quipu-analytics-suite",
packages=find_packages(where="src"),
package_dir={"": "src"},
classifiers=[
"Development Status :: 4 - Beta",
"Intended Audience :: Science/Research",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.8",
"Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10",
"Programming Language :: Python :: 3.11",
"Topic :: Scientific/Engineering :: Information Analysis",
"Topic :: Software Development :: Libraries :: Python Modules",
],
python_requires=">=3.8",
install_requires=[
"pandas>=1.5.0",
"numpy>=1.21.0",
"matplotlib>=3.5.0",
"seaborn>=0.11.0",
"scikit-learn>=1.1.0",
"jupyter>=1.0.0",
"ipykernel>=6.0.0",
],
extras_require={
"dev": [
"pytest>=7.0.0",
"pylint>=2.15.0",
"black>=22.0.0",
"flake8>=5.0.0",
],
"full": [
"scipy>=1.9.0",
"statsmodels>=0.13.0",
"plotly>=5.0.0",
"dash>=2.0.0",
],
},
license="MIT",
project_urls={
"Bug Reports": "https://github.com/bcdelodx/quipu-analytics-suite/issues",
"Source": "https://github.com/bcdelodx/quipu-analytics-suite",
"Documentation": "https://github.com/bcdelodx/quipu-analytics-suite/blob/main/README.md",
},
)
