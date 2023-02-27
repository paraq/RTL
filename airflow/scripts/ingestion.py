import mysql.connector
import json


def ingestion(host, user, password):
    with open("/data/data.json") as f:
        json_data = json.load(f)
        json_data = json.dumps(json_data)

    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database='db'
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS ingestion")
    mycursor.execute("CREATE TABLE ingestion (data_col JSON)")
    sql = "INSERT INTO ingestion (data_col) VALUES (%s)"
    mycursor.execute(sql, (json_data,))
    print(mycursor.rowcount, "records inserted.")
    mydb.commit()
    mycursor.close()
    mydb.close()

