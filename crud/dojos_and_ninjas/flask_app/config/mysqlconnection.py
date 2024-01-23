import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootroot',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)

                if query.lower().startswith(("insert", "update", "delete")):
                    self.connection.commit()
                elif query.lower().startswith("select"):
                    result = cursor.fetchall()
                    return result

        except pymysql.Error as e:
            print("Something went wrong:", e)
            return False

    def __del__(self):
        self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)