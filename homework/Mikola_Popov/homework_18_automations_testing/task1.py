import requests


def all_posts():
    response = requests.get('http://167.172.172.115:52353/object')
    print(response.json())


all_posts()


def one_post():
    response = requests.get('http://167.172.172.115:52353/object/1').json()
    print(response)


one_post()


def post_post():
    body = {
        "data": {
            "color": "black",
            "size": "medium"
        },
        "name": "Second object",
    }
    headers = {
        "Content-type": "application/json",
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers).json()
    return response


print(post_post())


def put_a_post():
    post_id = post_post()['id']
    body = {
        "data": {
            "color": "black_and_white",
            "size": "too big"
        },
        "name": "current object",
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers).json()
    return response


print(put_a_post())


def patch_a_post():
    post_id = post_post()['id']
    body = {
        "data": {
            "color": "black_and_white",
            "size": "too big",
            "scale": "world"
        }
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers).json()
    print(response)


patch_a_post()


def delete_post():
    post_id = post_post()['id']
    response = requests.delete(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    )
    print(response.status_code)


delete_post()
