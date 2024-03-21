import os

def get_env_variable(key):
    value = os.environ.get(key)
    return value