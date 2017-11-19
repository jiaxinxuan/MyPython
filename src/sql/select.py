import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="552373", db="pymysql", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from user"
try:
    # 执行sql语句
    cur.execute(sql)
    # 获取查询的所有记录
    results = cur.fetchall()
    print("id", "name", "password")
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)
except Exception as e:
    raise e
finally:
    # 关闭连接
    db.close()
