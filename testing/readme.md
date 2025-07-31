# Testing Notebooks

This folder contains Jupyter notebooks used for testing and prototyping.

## Importing from `src/`

To run notebooks in this folder that import modules from the `src/` directory (e.g., `from src import config_loader`), Python needs to know where the project root is.

### Fix: Add Project Root to `sys.path`

At the top of each notebook, add the following snippet to ensure imports work correctly:

```python
import sys
import os

# Append the project root to sys.path so Python can find the `src` package

PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(PROJECT_ROOT)

from src import config_loader
