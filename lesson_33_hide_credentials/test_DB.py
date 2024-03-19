from Hillel_october_23.lesson_33_hide_credentials.main import DB_connect
from Hillel_october_23.lesson_33_hide_credentials.setting import *



def test_connection():
    connection = DB_connect(login, password)
    print(login, password)
    assert connection == True
