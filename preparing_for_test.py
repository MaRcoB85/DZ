import requests
from random import choice, randint


base_url = "https://gorest.co.in"
create_user_url = base_url + "/public/v1/users"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer aa17b0247205e8c0237a0ad01a8a6fd037e92ccb55692ae2bf952706e04a1135"
}


class User:
    def __init__(self, name, email, gender, status, id=None):
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status
        self.id = id


def create_random_user():
    random_names = [
        "Olga Kovalenko",
        "Oleg Kovalenko",
        "Marta Tkachenko",
        "Igor Tkachenko",
        "Mariya Velyka",
        "Petro Velykyi",
    ]
    name = choice(random_names)
    first_name, last_name = name.split()
    email = f"{first_name}.{last_name}{randint(10000, 99999)}@test.com"
    gender = choice(["male", "female"])
    status = choice(["active", "inactive"])
    return User(name, email, gender, status)


def create_user():
    user = create_random_user()
    user_data = {
        "name": user.name,
        "email": user.email,
        "gender": user.gender,
        "status": user.status
    }
    response = requests.post(url=create_user_url, json=user_data, headers=headers)
    response_data = response.json()
    user_id = response_data['data'].get("id")
    user.id = user_id
    return user

created_user = create_user()
user_id = created_user.id
print(user_id)

def create_api(user):
    create_post_url = base_url + "/public/v2/users/{}/posts".format(user.id)
    delete_user_url = base_url + "/public/v2/users/{}".format(user.id)
    return create_post_url, delete_user_url

create_post_url, delete_user_url = create_api(user=create_user())
print(create_post_url)


def create_post():
    post_data = {
        "title": 'HOMEWORK',
        "body": "IT IS VERY HARD"
    }

    response = requests.post(url=create_post_url, json=post_data, headers=headers)
    response_post_data = response.json()
    return response_post_data

response_data = create_post()
print(response_data)


def delete_user():
    response = requests.delete(url=delete_user_url, headers=headers)
    response_del = response.status_code
    return response_del

cnx_user = delete_user()
print(cnx_user)
