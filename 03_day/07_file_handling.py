from os import path, chdir

chdir(path.join(path.dirname(__file__), "files"))


def read_file():
    users = []
    with open("users.csv", "r", encoding="UTF-8") as file:
        for line in file:
            id, first_name, last_name, email = line.strip().split(";")
            users.append(
                {
                    "id": int(id),
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                }
            )
    return users


users = read_file()


def append_file(file_path, user):
    with open(file_path, "a", encoding="UTF-8") as file:
        user_line = ";".join(str(val) for val in user.values())
        file.write("\n" + user_line)


append_file(
    "users.csv",
    {"id": 4, "first_name": "Jane", "last_name": "Doe", "email": "janedoe@gmail.com"},
)
