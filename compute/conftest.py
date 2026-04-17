"""Pytest configuration for the computational verification suite."""
import sys
import os

# Ensure lib/ is importable (Vol II legacy: `from lib.xxx import ...`).
sys.path.insert(0, os.path.dirname(__file__))
# Also make the repo root importable so `from compute.lib.xxx import ...`
# resolves (required by the cross-volume independent_verification infra).
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
