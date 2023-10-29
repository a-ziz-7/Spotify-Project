import requests
from credentials import token, client_id, lms, analysis

### u8o56z7ik44qt8mlvmr191t2m ###

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
    # z = create_playlist("Tutorial playlist", False)
    # print(z)
    r = a()
    print(r)
