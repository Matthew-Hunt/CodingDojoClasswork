import pymysql.cursors

class MySQLConnection:
    def __init__(self, host, user, password, db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset=charset,
                cursorclass=cursorclass,
                autocommit=autocommit
            )
        except pymysql.Error as e:
            raise Exception(f"Failed to connect to the database: {e}")

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
        except pymysql.Error as e:
            raise Exception(f"Failed to execute the query: {e}")
        finally:
            self.connection.close()

def connectToMySQL(db, host='localhost', user='root', password='rootroot'):
    return MySQLConnection(host, user, password, db)
