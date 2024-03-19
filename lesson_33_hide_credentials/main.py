def DB_connect(login: str, password: str) -> bool:
    if login == 'Pavlo' and password == 'admin':
        connection_state = True
    else:
        connection_state = False
    return connection_state
