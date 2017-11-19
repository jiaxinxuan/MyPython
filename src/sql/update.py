import pymysql

# 3.更新操作
db = pymysql.connect(host="localhost", user="root",
                     password="552373", db="pymysql", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql_update = "update user set name = '%s' where uid = %d"

try:
    # 像sql语句传递参数
    cur.execute(sql_update % ("xiongda", 3))
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()