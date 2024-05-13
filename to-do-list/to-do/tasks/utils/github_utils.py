# utils/github_utils.py

import os
import requests

def save_gist_locally(gist_id, file_path):
    # Construct URL to fetch gist content
    gist_url = f"https://api.github.com/gists/{gist_id}"
    
    # Fetch gist content from GitHub API
    response = requests.get(gist_url)
    if response.status_code == 200:
        # Extract content from response
        gist_content = response.json()['files'].popitem()[1]['content']
        
        # Write gist content to local markdown file
        try:
            with open(file_path, 'w') as file:
                file.write(gist_content)
            return True, "Gist content saved successfully."
        except Exception as e:
            return False, f"Failed to save gist content: {str(e)}"
    else:
        return False, f"Failed to fetch gist content. Status code: {response.status_code}"
