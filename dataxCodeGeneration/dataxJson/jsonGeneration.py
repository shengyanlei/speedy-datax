import pymysql

def mysql_table_info(table_name):
#连接数据库
    conn=pymysql.connect(host = 'nodev2001',user = 'root',passwd='1234kxmall!@#ABC',port= 3306,db='gmall',charset='utf8')
    cur = conn.cursor() # 生成游标对象
    columnSql="desc {table};".format(table=table_name)
    cur.execute(columnSql)
    column=cur.fetchall()
    column_name = []
    column_type = []

    for j in range(len(column)):
        column_name.append(str(column[j][0]))
        column_type.append(column[j][1])

    table_info_tuple=(table_name,column_name,column_type)
    cur.close() # 关闭游标
    conn.close() # 关闭连接
    return table_info_tuple



