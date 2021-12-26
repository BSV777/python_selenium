import pymysql

print(pymysql.__version__)

connection = pymysql.connect(host="lab", database="addressbook", user="root", passwd="")
# connection.autocommit(1)
#
# try:
#     cursor = connection.cursor()
#     # cursor.execute("select * from group_list")
#     # for row in cursor.fetchall():
#     #     print(row)
# finally:
#     connection.close()
#
