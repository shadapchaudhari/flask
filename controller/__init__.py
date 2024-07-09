# __all__ = ["user_controller" , "product_controller"]
import os
import glob

# Find all Python files in the current directory except __init__.py
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))

# Populate the __all__ list with module names, stripping the ".py" extension
__all__ = [
    os.path.basename(f)[:-3]
    for f in modules
    if os.path.isfile(f) and not os.path.basename(f).startswith("__")
]

# Import all modules listed in __all__
for module in __all__:
    __import__(f"{__name__}.{module}")

