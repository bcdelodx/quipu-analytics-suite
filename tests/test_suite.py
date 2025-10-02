#!/usr/bin/env python3
"""
Test Suite for Comprehensive Tiered Analytics Suite

This module contains unit tests for core functionality, validation tests
for notebooks, and integration tests for the overall suite.

Author: Brandon Deloatch
Affiliation: Quipu Research Labs, LLC
Date: 2025-10-02
Version: v1.3
"""

import unittest
import sys
import os
import importlib
import subprocess
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import verify_installation


class TestInstallationVerification(unittest.TestCase):
"""Test the installation verification functionality."""

def test_python_version_check(self):
"""Test Python version checking function."""
result = verify_installation.check_python_version()
self.assertIsInstance(result, bool)
# Should pass since we're running in the environment
self.assertTrue(result)

def test_package_checking(self):
"""Test package checking functionality."""
# Test with a package that should be installed
is_installed, version = verify_installation.check_package('sys', 'sys')
self.assertTrue(is_installed)

# Test with a package that shouldn't exist
is_installed, version = verify_installation.check_package('nonexistent_package_xyz')
self.assertFalse(is_installed)
self.assertEqual(version, 'Not installed')

def test_get_package_categories(self):
"""Test package category retrieval."""
categories = verify_installation.get_package_categories()
self.assertIsInstance(categories, list)
self.assertGreater(len(categories), 0)

# Check structure
for category_name, packages in categories:
self.assertIsInstance(category_name, str)
self.assertIsInstance(packages, list)
for package_name, import_name in packages:
self.assertIsInstance(package_name, str)
self.assertIsInstance(import_name, str)


class TestNotebookStructure(unittest.TestCase):
"""Test that notebooks have proper structure and metadata."""

def setUp(self):
"""Set up test environment."""
self.notebook_dir = project_root
self.notebooks = list(self.notebook_dir.glob("Tier*.ipynb"))

def test_notebooks_exist(self):
"""Test that expected notebooks exist."""
self.assertGreater(len(self.notebooks), 0)

# Check for each tier
tier_patterns = [f"Tier{i}_*.ipynb" for i in range(1, 7)]
for pattern in tier_patterns:
matching_notebooks = list(self.notebook_dir.glob(pattern))
self.assertGreater(len(matching_notebooks), 0,
f"No notebooks found for pattern {pattern}")

def test_notebook_naming_convention(self):
"""Test that notebooks follow naming convention."""
for notebook in self.notebooks:
name = notebook.name
# Should start with Tier followed by number
self.assertTrue(name.startswith("Tier"),
f"Notebook {name} doesn't start with 'Tier'")
# Should end with .ipynb
self.assertTrue(name.endswith(".ipynb"),
f"Notebook {name} doesn't end with '.ipynb'")

def test_notebook_readability(self):
"""Test that notebooks can be read as valid JSON."""
import json

for notebook in self.notebooks[:3]: # Test first 3 to avoid long test times
try:
with open(notebook, 'r', encoding='utf-8') as f:
nb_content = json.load(f)

# Check basic notebook structure
self.assertIn('cells', nb_content)
self.assertIn('metadata', nb_content)
self.assertIn('nbformat', nb_content)

except json.JSONDecodeError as e:
self.fail(f"Notebook {notebook.name} is not valid JSON: {e}")
except Exception as e:
self.fail(f"Failed to read notebook {notebook.name}: {e}")


class TestSecurityCompliance(unittest.TestCase):
"""Test security compliance across the codebase."""

def setUp(self):
"""Set up security test environment."""
self.project_root = project_root

def test_no_hardcoded_secrets(self):
"""Test that no hardcoded secrets exist in the codebase."""
suspicious_patterns = [
'password', 'api_key', 'secret', 'token', 'credential'
]

python_files = list(self.project_root.glob("*.py"))

for py_file in python_files:
with open(py_file, 'r', encoding='utf-8') as f:
content = f.read().lower()

for pattern in suspicious_patterns:
if pattern in content:
# Check if it's in a comment or docstring (acceptable)
lines = content.split('\n')
for i, line in enumerate(lines):
if pattern in line and not (line.strip().startswith('#') or
'"""' in line or "'''" in line):
# Further check if it's a variable assignment
if '=' in line and pattern in line:
self.fail(f"Potential hardcoded secret in {py_file.name} "
f"line {i+1}: {pattern}")

def test_import_safety(self):
"""Test that no unsafe imports are used."""
unsafe_imports = ['eval', 'exec', 'compile', '__import__']

python_files = list(self.project_root.glob("*.py"))

for py_file in python_files:
with open(py_file, 'r', encoding='utf-8') as f:
content = f.read()

for unsafe in unsafe_imports:
if unsafe + '(' in content:
self.fail(f"Unsafe function {unsafe} used in {py_file.name}")


class TestDependencyCompliance(unittest.TestCase):
"""Test dependency management and security."""

def test_requirements_files_exist(self):
"""Test that requirements files exist and are readable."""
req_files = ['requirements.txt', 'requirements-dev.txt']

for req_file in req_files:
req_path = project_root / req_file
self.assertTrue(req_path.exists(), f"{req_file} not found")

# Test that file is readable and has content
with open(req_path, 'r', encoding='utf-8') as f:
content = f.read().strip()
self.assertTrue(len(content) > 0, f"{req_file} is empty")

def test_pinned_versions(self):
"""Test that dependencies have pinned versions."""
req_path = project_root / 'requirements.txt'

with open(req_path, 'r', encoding='utf-8') as f:
lines = f.readlines()

for line in lines:
line = line.strip()
if line and not line.startswith('#'):
# Should have version specifier
has_version = any(op in line for op in ['==', '>=', '<=', '~=', '!='])
self.assertTrue(has_version,
f"Dependency {line} should have version pinned")


class TestDocumentationCompliance(unittest.TestCase):
"""Test documentation standards and completeness."""

def test_required_documentation_exists(self):
"""Test that required documentation files exist."""
required_docs = [
'README.md', 'LICENSE', 'CHANGELOG.md',
'CONTRIBUTING.md', 'CONTRIBUTORS.md'
]

for doc in required_docs:
doc_path = project_root / doc
self.assertTrue(doc_path.exists(), f"Required documentation {doc} not found")

# Check that file has content
with open(doc_path, 'r', encoding='utf-8') as f:
content = f.read().strip()
self.assertTrue(len(content) > 0, f"Documentation {doc} is empty")

def test_setup_py_metadata(self):
"""Test that setup.py contains proper metadata."""
setup_path = project_root / 'setup.py'
self.assertTrue(setup_path.exists(), "setup.py not found")

with open(setup_path, 'r', encoding='utf-8') as f:
content = f.read()

required_fields = ['name', 'version', 'author', 'description', 'license']
for field in required_fields:
self.assertIn(field, content, f"setup.py missing {field} field")


def run_tests():
"""Run all tests and return results."""
print("=" * 70)
print("🧪 COMPREHENSIVE TIERED ANALYTICS SUITE - TEST SUITE")
print("=" * 70)

# Create test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add all test classes
test_classes = [
TestInstallationVerification,
TestNotebookStructure,
TestSecurityCompliance,
TestDependencyCompliance,
TestDocumentationCompliance
]

for test_class in test_classes:
tests = loader.loadTestsFromTestCase(test_class)
suite.addTests(tests)

# Run tests
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Print summary
print("\n" + "=" * 70)
print("TEST SUMMARY:")
print(f" Tests Run: {result.testsRun}")
print(f" Failures: {len(result.failures)}")
print(f" Errors: {len(result.errors)}")
print(f" Success Rate: {(result.testsRun - len(result.failures) - len(result.errors))/result.testsRun*100:.1f}%")

if result.failures:
print(f"\nFAILURES ({len(result.failures)}):")
for test, traceback in result.failures:
print(f" • {test}")

if result.errors:
print(f"\n💥 ERRORS ({len(result.errors)}):")
for test, traceback in result.errors:
print(f" • {test}")

if not result.failures and not result.errors:
print(f"\nALL TESTS PASSED!")

print("=" * 70)

return result.wasSuccessful()


if __name__ == "__main__":
success = run_tests()
sys.exit(0 if success else 1)