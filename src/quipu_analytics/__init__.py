"""
Quipu Analytics Suite - Comprehensive Tiered Analytics Framework

A comprehensive data science and analytics framework providing structured
approaches to data analysis from basic descriptive statistics to advanced
machine learning techniques.

Modules:
execution_tracking: Academic provenance and reproducibility utilities
verify_installation: Installation verification and dependency checking

Author: Brandon Deloatch
Affiliation: Quipu Research Labs, LLC
License: MIT
Version: 1.3.0
"""

__version__ = "1.3.0"
__author__ = "Brandon Deloatch"
__email__ = "brandon@quipuresearchlabs.com"
__license__ = "MIT"

# Import main modules
from .execution_tracking import setup_notebook_tracking, get_execution_metadata
from .verify_installation import main as verify_installation

__all__ = [
'setup_notebook_tracking',
'get_execution_metadata',
'verify_installation'
]