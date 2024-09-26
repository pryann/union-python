users = [
    {
        "id": 1,
        "first_name": "Rosemaria",
        "last_name": "O'Neil",
        "email": "roneil0@webmd.com",
    },
    {
        "id": 2,
        "first_name": "Paige",
        "last_name": "Gylle",
        "email": "pgylle1@cdbaby.com",
    },
    {
        "id": 3,
        "first_name": "Abigael",
        "last_name": "Tallyn",
        "email": "atallyn2@stanford.edu",
    },
    {
        "id": 4,
        "first_name": "Barbabra",
        "last_name": "Warner",
        "email": "bwarner3@craigslist.org",
    },
    {"id": 5, "first_name": "Elie", "last_name": "Haine", "email": "ehaine4@icio.us"},
]

# CRUD - Create, Read, Update, Delete


def get_users():
    return users


def find_user(id):
    for user in users:
        if user["id"] == id:
            return user
    # unnecessary
    # return None


print(find_user(1))


def generate_id():
    # new_id = 1
    # for user in users:
    #     if user["id"] >= new_id:
    #         new_id = user["id"] + 1
    # return new_id
    try:
        return max(user["id"] for user in users) + 1
    except ValueError:
        return 1


def create_user(user):
    # if the list elements ordered by id and not empty
    # last_id = users[-1]["id"]
    new_user = {"id": generate_id()}
    new_user.update(user)
    users.append(new_user)
    # return new_user
    return users[-1]


# users = []
create_user({"first_name": "John", "last_name": "Doe", "email": "johndoe@gmail.com"})
print(users)


def update_user(id, user):
    # keresd meg az adott id-jú elemet
    # ha van ilyen, akkor keresd meg, hgoy a listában ez melyik indexű helyen található
    # frissítsd (írd felül) az adott indexű elemet a kapott értékkel
    user_from_list = find_user(id)
    if user_from_list is not None:
        index = users.index(user_from_list)
        # v1 - frissítés - partial update
        users[index].update(user)
        # v2 - felülírás - replace
        # users[index] = user
        return users[index]


def delete_user(id):
    user = find_user(id)
    if user is not None:
        users.remove(user)
