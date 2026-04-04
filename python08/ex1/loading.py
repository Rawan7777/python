import sys
import importlib

required = ["pandas", "numpy", "matplotlib"]

def check_dependencies():

    print("Checking dependencies:")

    versions = {}
    missing = []

    for pkg in required:
        try:
            mod = importlib.import_module(pkg)
            versions[pkg] = getattr(mod, "__version__", "unknown")
        except Exception:
            missing.append(pkg)
    return versions, missing

def run_analysis():

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")
    x = np.random.rand(1000) * 100
    y = np.random.rand(1000) * 100

    data = pd.DataFrame({
        "x": x,
        "y": y
    })

    print("Generating visualization...")
    plt.figure()
    plt.scatter(data["x"], data["y"], s=20)
    plt.title("Random Points Visualization")
    plt.xlabel("X values")
    plt.ylabel("Y values")

    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

def main():

    print("LOADING STATUS: Loading programs...\n")

    versions, missing = check_dependencies()

    if missing:
        print("Missing dependencies:", ", ".join(missing))
        print("Install with: pip install -r requirements.txt")
        print("OR poetry install")
        sys.exit(1)

    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computing ready",
        "matplotlib": "Visualization ready"
    }

    for pkg, ver in versions.items():
        msg = descriptions.get(pkg, "ready")
        print(f"[OK] {pkg} ({ver}) - {msg}")

    print("\nAnalyzing Matrix data...")
    run_analysis()

if __name__ == "__main__":
    main()
