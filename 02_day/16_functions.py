global_variable = "global"
print("global_variable:", global_variable)


def log():
    print("global_variable in log:", global_variable)
    local_variable = "local"
    print("local_variable in log:", local_variable)


log()
# local_variable is not accessible here
# print("local_variable in global:", local_variable)

config = "config"


def change_config():
    global config
    config = "new config"


change_config()
print(config)

configs = ["https", "127.0.0.1", "8080"]


def add_config(configs, value):
    configs = []
    configs.append(value)


add_config(configs, "new value")
print(configs)


def gcd_loop(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd_loop(11, 33))


def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)
