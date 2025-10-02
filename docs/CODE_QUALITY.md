# Code Quality Guidelines

## Pylint Configuration

This project uses pylint for maintaining high code quality standards. A comprehensive `.pylintrc` configuration file is provided that's optimized for data science projects.

### Running Pylint

```bash
# Check all Python files
pylint *.py

# Check specific files
pylint verify_installation.py setup.py

# Generate detailed report
pylint --reports=y *.py
```

### Current Scores

- `verify_installation.py`: **10.00/10**
- `setup.py`: **10.00/10**

### Configuration Highlights

Our `.pylintrc` is optimized for data science workflows:

- **Variable Names**: Accepts common data science variables (`df`, `ax`, `fig`, `x`, `y`, `z`, `np`, `pd`, etc.)
- **Line Length**: 100 characters (suitable for modern displays)
- **Complexity Limits**: Reasonable for analytics code
- **Disabled Rules**: Overly strict rules for research environments are disabled

### Integration with Development Workflow

```bash
# Install development dependencies (includes pylint)
pip install -r requirements-dev.txt

# Run full code quality check
black . # Format code
isort . # Sort imports
flake8 . # Check style
pylint *.py # Comprehensive linting
```

### Pre-commit Integration

Consider setting up pre-commit hooks to automatically run pylint:

```bash
pip install pre-commit
pre-commit install
```

This ensures code quality checks run automatically before each commit.