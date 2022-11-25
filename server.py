#!/usr/bin/python
import psycopg2
import re
from psycopg2 import Error
# python -m pip install psycopg2
class Server:
    def getItem(password):
        try:
            connect = psycopg2.connect(database="bruteforce", host="localhost", user="postgres", password="astros5", port="5432")
            cursor = connect.cursor()

            cursor.execute("SELECT password FROM accounts WHERE accountname='offthecookies'")

            myPassword = cursor.fetchone()
            # regular expression to shorten the text
            result = re.search("('(.*)',)",str(myPassword))
            x = result.group(1)
            # having problems using re to only show the password
            x = x.split("'")
            # print(x[1])
            # print(password)
            if password.__eq__(x[1]):
                # def returnPassword(x):
                return True
            else:
                return False
        except (Exception, Error) as error:
            print("Error: ", error)
        # finally:
        #     if (connect):
        #         cursor.close()
        #         connect.close()
        #         # print("PostgreSQL connection is closed")