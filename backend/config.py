import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')  # Set this in .env
    UPLOAD_FOLDER = 'uploads'  # Local folder to temporarily store files before uploading to GCS
    ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv'}  # Allowed video formats
    API_KEY = os.getenv("API_KEY")
