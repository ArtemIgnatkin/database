import mysql.connector

host = ""
user = ""
password = ""
database = ""
def request_return(request):
    """
    Запрос с выводом результата
    """
    with mysql.connector.connect(host=host, user=user, password=password, database=database) as connection:
      cursor = connection.cursor()
      cursor.execute(request)
      result = cursor.fetchall()
      connection.commit()
      return result

def request_not_return(request):
    """
    Запрос без результата
    """
    with mysql.connector.connect(host=host, user=user, password=password, database=database) as connection:
      cursor = connection.cursor()
      cursor.execute(request)
      connection.commit()
