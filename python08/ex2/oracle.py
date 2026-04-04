import os
from dotenv import dotenv_values
from dotenv import load_dotenv

# Required environment variables
REQUIRED = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


# Load configuration from environment and .env file
def load_config():
    # Load variables from .env into environment
    load_dotenv()

    # Collect current environment values
    config = {key: os.getenv(key) for key in REQUIRED}
    return config


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("WARNING: Missing variables:", ", ".join(missing))

    print("Configuration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE')}")
    print(
        "Database:",
        "Connected to local instance"
        if config.get("DATABASE_URL")
        else "Not configured",
    )
    print(
        "API Access:",
        "Authenticated" if config.get("API_KEY") else "Missing key",
    )
    print(f"Log Level: {config.get('LOG_LEVEL')}")
    print(
        "Zion Network:",
        "Online" if config.get("ZION_ENDPOINT") else "Offline",
    )

    print("\nEnvironment security check:")

    # Detect obvious placeholder / hardcoded secret values
    suspicious_values = {
        "development", "sqlite:///matrix.db",
        "your_api_key_here", "DEBUG",
        "https://zion.local/api"
    }

    hardcoded_detected = any(
        str(value).lower() in suspicious_values
        for value in config.values()
        if value
    )

    print(
        "[OK] No hardcoded secrets detected"
        if not hardcoded_detected
        else "[KO] Possible hardcoded secrets detected",
    )

    # Check if .env file exists and contains at least one required key
    env_file_values = dotenv_values(".env")
    dotenv_configured = any(key in env_file_values for key in REQUIRED)

    print(
        "[OK] .env file properly configured"
        if dotenv_configured
        else "[KO] .env file missing or incomplete",
    )

    # Check if any variable is overridden by real environment variables
    overrides_present = any(
        os.environ.get(key) != env_file_values.get(key)
        for key in REQUIRED
        if os.environ.get(key)
    )

    print(
        "[OK] Production overrides available"
        if overrides_present
        else "[KO] No environment overrides detected",
    )


if __name__ == "__main__":
    main()
