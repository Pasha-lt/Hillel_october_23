import logging
from datetime import datetime

time_now  = datetime.now()
formatted_time = time_now.strftime('%Y_%m_%d_%H_%M')


logging.basicConfig(level=logging.INFO, filename=f'logging_{formatted_time}.log')  # вказуємо від рівня виводити логування

logging.debug('--> debug')
logging.info('--> info')
logging.warning('--> warning')
logging.error('--> error')
logging.critical('--> critical')


def DB_connect():
    print('connection')
    logging.info('підєдналось до бази даних')

def DB_close_connection():
    a = 10
    if a > 10:
        print('close connection')
        logging.info('закрили зʼєднання')

DB_connect()
DB_close_connection()

try:
    10/0
except Exception as e:
    logging.exception(e)


# # більш розширений
# logging.basicConfig(level=logging.DEBUG, filename='my_logging.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d)', datefmt='%d/%m/%Y %I:%M:%S',
#                     encoding = 'utf-8', filemode='w')