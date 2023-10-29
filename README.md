# Spotify-Project

This Python script allows you to create a playlist and make an analysis request using the `requests` library. The credentials needed for these operations are loaded from a `credentials.py` file.

## Usage

1. Install the `requests` library if you haven't already by running:

   ```bash
   pip install requests
Create a credentials.py file in the same directory as this script with the following content:

python
Copy code

token = "YOUR_ACCESS_TOKEN"

client_id = "YOUR_CLIENT_ID"

lms = "YOUR_LMS_ENDPOINT"

analysis = "YOUR_ANALYSIS_ENDPOINT"


Replace the placeholders with your actual credentials and endpoints.
