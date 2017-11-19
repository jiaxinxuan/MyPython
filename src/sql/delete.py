import pymysql


# 4.删除操作
db = pymysql.connect(host="localhost", user="root", password="552373", db="pymysql", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
sql_delete = "delete from user where uid = %d"
try:
    cur.execute(sql_delete % (3))
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()