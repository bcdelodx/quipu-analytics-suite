#!/usr/bin/env python3
"""
Execution Tracking and Provenance Utilities

This module provides utilities for tracking notebook execution environment,
logging provenance information, and ensuring reproducibility across the
Comprehensive Tiered Analytics Suite.

Author: Brandon Deloatch
Affiliation: Quipu Research Labs, LLC
Date: 2025-10-02
Version: v1.3
"""

import datetime
import getpass
import platform
import uuid
import sys
import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
import hashlib


def get_execution_metadata() -> Dict[str, Any]:
"""
Capture comprehensive execution environment metadata.

Returns:
Dict containing execution environment information
"""
return {
"execution_id": str(uuid.uuid4()),
"timestamp": datetime.datetime.now().isoformat(),
"user": getpass.getuser(),
"system": {
"node": platform.node(),
"system": platform.system(),
"release": platform.release(),
"machine": platform.machine(),
"processor": platform.processor()
},
"python": {
"version": sys.version,
"executable": sys.executable,
"version_info": {
"major": sys.version_info.major,
"minor": sys.version_info.minor,
"micro": sys.version_info.micro
}
},
"environment": {
"working_directory": os.getcwd(),
"python_path": sys.path[:3], # First 3 paths for brevity
"environment_variables": {
key: os.environ.get(key, "Not set")
for key in ["VIRTUAL_ENV", "CONDA_DEFAULT_ENV", "PATH"]
}
}
}


def log_execution_start(notebook_name: str, version: str = "1.3.0") -> Dict[str, Any]:
"""
Log the start of notebook execution with full provenance.

Args:
notebook_name: Name of the notebook being executed
version: Version of the notebook

Returns:
Dict containing execution metadata
"""
metadata = get_execution_metadata()
metadata["notebook"] = {
"name": notebook_name,
"version": version,
"path": os.path.abspath(notebook_name) if os.path.exists(notebook_name) else "Unknown"
}

print("=" * 70)
print("EXECUTION ENVIRONMENT TRACKING")
print("=" * 70)
print(f" Notebook: {notebook_name} (v{version})")
print(f"🆔 Execution ID: {metadata['execution_id']}")
print(f"👤 User: {metadata['user']}")
print(f" System: {metadata['system']['node']} ({metadata['system']['system']} {metadata['system']['release']})")
print(f"🐍 Python: {metadata['python']['version_info']['major']}.{metadata['python']['version_info']['minor']}.{metadata['python']['version_info']['micro']}")
print(f"📅 Timestamp: {metadata['timestamp']}")
print(f"📂 Working Directory: {metadata['environment']['working_directory']}")
print("=" * 70)

return metadata


def get_git_provenance() -> Dict[str, Any]:
"""
Get Git repository provenance information if available.

Returns:
Dict containing Git information or empty dict if not a Git repo
"""
try:
import subprocess

# Get current commit hash
commit_hash = subprocess.check_output(
["git", "rev-parse", "HEAD"],
stderr=subprocess.DEVNULL,
text=True
).strip()

# Get current branch
branch = subprocess.check_output(
["git", "rev-parse", "--abbrev-ref", "HEAD"],
stderr=subprocess.DEVNULL,
text=True
).strip()

# Get repository URL
try:
remote_url = subprocess.check_output(
["git", "config", "--get", "remote.origin.url"],
stderr=subprocess.DEVNULL,
text=True
).strip()
except subprocess.CalledProcessError:
remote_url = "No remote configured"

# Check if there are uncommitted changes
try:
status = subprocess.check_output(
["git", "status", "--porcelain"],
stderr=subprocess.DEVNULL,
text=True
).strip()
has_changes = len(status) > 0
except subprocess.CalledProcessError:
has_changes = True

return {
"commit_hash": commit_hash,
"branch": branch,
"remote_url": remote_url,
"has_uncommitted_changes": has_changes,
"short_hash": commit_hash[:8]
}

except (subprocess.CalledProcessError, FileNotFoundError):
return {}


def log_data_provenance(data_sources: Dict[str, Dict[str, str]]) -> None:
"""
Log data source provenance information.

Args:
data_sources: Dict mapping dataset names to their metadata
Format: {"dataset_name": {"source": "URL", "license": "MIT", "version": "1.0"}}
"""
if not data_sources:
return

print("\n DATA PROVENANCE TRACKING")
print("-" * 50)

for dataset_name, metadata in data_sources.items():
print(f" Dataset: {dataset_name}")
for key, value in metadata.items():
print(f" {key.title()}: {value}")
print()


def validate_reproducibility_requirements() -> Dict[str, bool]:
"""
Validate that reproducibility requirements are met.

Returns:
Dict mapping requirement names to whether they're satisfied
"""
requirements = {}

# Check if random seeds are set
try:
import numpy as np
# This is a basic check - in practice, we'd check if seeds were actually set
requirements["numpy_available"] = True
except ImportError:
requirements["numpy_available"] = False

try:
import random
requirements["random_available"] = True
except ImportError:
requirements["random_available"] = False

# Check if we're in a virtual environment
requirements["virtual_environment"] = (
hasattr(sys, 'real_prefix') or
(hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
'VIRTUAL_ENV' in os.environ
)

# Check if requirements.txt exists
requirements["requirements_file"] = os.path.exists("requirements.txt")

return requirements


def set_reproducible_environment(seed: int = 42) -> None:
"""
Set up reproducible environment with fixed seeds.

Args:
seed: Random seed to use for reproducibility
"""
print(f" Setting reproducible environment (seed={seed})")

# Set Python random seed
import random
random.seed(seed)

# Set NumPy seed if available
try:
import numpy as np
np.random.seed(seed)
print(f" NumPy random seed set to {seed}")
except ImportError:
print(" NumPy not available - seed not set")

# Set TensorFlow seed if available
try:
import tensorflow as tf
tf.random.set_seed(seed)
print(f" TensorFlow random seed set to {seed}")
except ImportError:
print(" TensorFlow not available - seed not set")

# Set PyTorch seed if available
try:
import torch
torch.manual_seed(seed)
print(f" PyTorch random seed set to {seed}")
except ImportError:
print(" PyTorch not available - seed not set")


def generate_execution_summary(metadata: Dict[str, Any],
data_sources: Optional[Dict[str, Dict[str, str]]] = None,
notebook_id: Optional[str] = None) -> Dict[str, Any]:
"""
Generate a comprehensive execution summary for archival.

Args:
metadata: Execution metadata from log_execution_start
data_sources: Data provenance information
notebook_id: Unique notebook identifier

Returns:
Complete execution summary
"""
summary = {
"execution_summary": {
"notebook_id": notebook_id or str(uuid.uuid4()),
"execution_metadata": metadata,
"git_provenance": get_git_provenance(),
"data_sources": data_sources or {},
"reproducibility_check": validate_reproducibility_requirements(),
"generated_at": datetime.datetime.now().isoformat()
}
}

return summary


def save_execution_log(summary: Dict[str, Any],
output_dir: str = "execution_logs") -> str:
"""
Save execution log to file for archival.

Args:
summary: Execution summary from generate_execution_summary
output_dir: Directory to save logs

Returns:
Path to saved log file
"""
# Create output directory if it doesn't exist
Path(output_dir).mkdir(exist_ok=True)

# Generate filename with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
execution_id = summary["execution_summary"]["execution_metadata"]["execution_id"][:8]
filename = f"execution_log_{timestamp}_{execution_id}.json"

log_path = Path(output_dir) / filename

# Save to file
with open(log_path, 'w', encoding='utf-8') as f:
json.dump(summary, f, indent=2, ensure_ascii=False)

print(f"💾 Execution log saved to: {log_path}")
return str(log_path)


# Convenience function for easy notebook integration
def setup_notebook_tracking(notebook_name: str,
version: str = "1.3.0",
notebook_id: Optional[str] = None,
data_sources: Optional[Dict[str, Dict[str, str]]] = None,
seed: int = 42,
save_log: bool = False) -> Dict[str, Any]:
"""
Complete notebook tracking setup - call this at the start of every notebook.

Args:
notebook_name: Name of the notebook
version: Version of the notebook
notebook_id: Unique identifier for the notebook
data_sources: Data source provenance information
seed: Random seed for reproducibility
save_log: Whether to save execution log to file

Returns:
Complete tracking metadata
"""
# Set up reproducible environment
set_reproducible_environment(seed)

# Log execution start
metadata = log_execution_start(notebook_name, version)

# Log data provenance if provided
if data_sources:
log_data_provenance(data_sources)

# Generate summary
summary = generate_execution_summary(metadata, data_sources, notebook_id)

# Save log if requested
if save_log:
save_execution_log(summary)

# Print Git information if available
git_info = get_git_provenance()
if git_info:
print(f"\n🔗 Git Information:")
print(f" Branch: {git_info['branch']}")
print(f" Commit: {git_info['short_hash']}")
if git_info['has_uncommitted_changes']:
print(" Warning: Uncommitted changes detected")

return summary