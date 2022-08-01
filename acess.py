import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='teste123',
                             database='mysql',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * from enem.PARTICIPANTE"
        cursor.execute(sql)