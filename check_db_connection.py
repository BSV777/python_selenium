import pymysql.cursors


connection = pymysql.connect(host="lab", port=3306, user="root", passwd="", db="addressbook")
connection.autocommit(1)
cursor = connection.cursor(pymysql.cursors.DictCursor)


# connection = pymysql.connect(host="lab", database="addressbook", user="root", passwd="")
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
