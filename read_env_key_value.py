import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()

# Read specific environment variables
def get_env_value(key, default=None):
    """
    Get environment variable value
    
    Args:
        key: Environment variable name
        default: Default value if key not found
        
    Returns:
        Environment variable value or default
    """
    return os.getenv(key, default)

# Example usage
if __name__ == "__main__":
    # Read individual environment variables
    api_key = get_env_value('API_KEY', 'default_key')
    db_url = get_env_value('DATABASE_URL', 'localhost')
    debug_mode = get_env_value('DEBUG', 'False')
    
    print(f"API Key: {api_key}")
    print(f"Database URL: {db_url}")
    print(f"Debug Mode: {debug_mode}")
    
    # Print all environment variables (optional)
    print("\nAll environment variables loaded:")
    for key, value in os.environ.items():
        if key.isupper():  # Print only uppercase env vars (typically custom ones)
            print(f"{key}={value}")
