import pymysql

def my_db(sql):
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='1',
        db='assignment1',
        charset='utf8'
    )
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)# 建立游标；默认返回二维数组，DictCursor指定返回字典；
    cur.execute(sql) # execute执行sql
    conn.commit()
    res = cur.fetchall()#拿到全部sql执行结果
    cur.close()# 关闭游标
    conn.close()# 关闭数据库
    return res # 返回sql执行的结果

