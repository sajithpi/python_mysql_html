import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"

)
cursor = con.cursor()
cursor.execute("select t1.user_id,t1.user_name,SUM(t2.amount) from user_data as t1  inner join amount as t2 on t1.user_id = t2.user_id  group by t1.user_id")
myresults = cursor.fetchall()
for x in myresults:
    print(x)
    sql1 = "INSERT INTO wallet values (%s,%s,%s)"
    args = (int(x[0]),x[1],x[2])
    cursor.execute(sql1,args)
    con.commit()
cursor.close()
con.close()