import requests
# get private data from credentials file
from credentials import token, client_id, lms, analysis

# Create a new playlist
def create_playlist(name, public):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "name": name,
        "public": public
    }
    response = requests.post(lms, headers=headers, json=data)

    if response.status_code == 200:
        json_resp = response.json()
        return json_resp
    else:
        print(f"Failed to create a playlist. Status code: {response.status_code}")
        return None


# Make an analysis request
def a():
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.post(analysis, headers=headers)

    if r.status_code == 200:
        r_r = r.json()
        return r_r
    else:
        print(f"Failed to make an analysis request. Status code: {r.status_code}")
        return None


if __name__ == '__main__':
    # Create a new playlist
    playlist_name = "My Playlist"
    is_public = True  # Set to True if you want the playlist to be public
    playlist_result = create_playlist(playlist_name, is_public)

    if playlist_result:
        print(f"Playlist created: {playlist_result}")

    # Make an analysis request
    analysis_result = a()

    if analysis_result:
        print(f"Analysis result: {analysis_result}")
