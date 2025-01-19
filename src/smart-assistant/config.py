from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define and retrieve variables
API_KEY = os.getenv("API_KEY")
print(f'SECRET_KEY: {API_KEY}')
