import string
from random import sample

n = 8

def get_random_password() -> str:
    variats = string.digits + string.ascii_lowercase + string.ascii_uppercase
    parols = sample(variats, k=n)
    return parols

print(''.join(get_random_password()))
