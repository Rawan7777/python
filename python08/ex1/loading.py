import importlib
import sys

# List of required third-party packages for the project
REQUIRED = ["pandas", "numpy", "matplotlib"]


# Check if required dependencies are installed and collect versions
def check_dependencies():
    print("Checking dependencies:")

    versions = {}
    missing = []

    # Try importing each required package dynamically
    for pkg in REQUIRED:
        try:
            mod = importlib.import_module(pkg)
            versions[pkg] = getattr(mod, "__version__", "unknown")
        except Exception:
            # If import fails, mark package as missing
            missing.append(pkg)

    return versions, missing


# Run the data generation and visualization workflow
def run_analysis():
    # Import inside the function so the program can fail gracefully
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Processing 1000 data points...")

    # Generate random X and Y coordinates between 0 and 100
    x = np.random.rand(1000) * 100
    y = np.random.rand(1000) * 100

    # Create a DataFrame to organize the generated data
    data = pd.DataFrame({"x": x, "y": y})

    print("Generating visualization...")

    # Create scatter plot of the generated points
    plt.figure()
    plt.scatter(data["x"], data["y"], s=20)
    plt.title("Random Points Visualization")
    plt.xlabel("X values")
    plt.ylabel("Y values")

    # Save the figure to a file
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


# Program entry point
def main():

    try:

        print("LOADING STATUS: Loading programs...\n")

        # Verify dependencies before running the analysis
        versions, missing = check_dependencies()

        if missing:
            print("Missing dependencies:", ", ".join(missing))
            print("Install with: pip install -r requirements.txt")
            print("OR poetry install")
            sys.exit(1)

        # Friendly status messages for each dependency
        descriptions = {
            "pandas": "Data manipulation ready",
            "numpy": "Numerical computing ready",
            "matplotlib": "Visualization ready",
        }

        # Print detected package versions
        for pkg, ver in versions.items():
            msg = descriptions.get(pkg, "ready")
            print(f"[OK] {pkg} ({ver}) - {msg}")

        print("\nAnalyzing Matrix data...")
        run_analysis()

    except Exception as error:
        # Fallback message if error occured
        print(f"Error occured {error}")


# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
