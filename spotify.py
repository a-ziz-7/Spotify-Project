import requests
from credentials import token, client_id, lms, analysis


def create_playlist(name, public):
    response = requests.post(
        lms,
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
    return json_resp


def a():
    r = requests.post(analysis, f"Bearer {token}")
    r_r = r.json()
    return r_r


if __name__ == '__main__':
    r = a()
    print(r)
