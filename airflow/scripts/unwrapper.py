import mysql.connector
import sys


def unwrapper(host, user, password, columns, data_types, schema):
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database="db"
    )
    DATA_TYPES_MAP = {
        'FLOAT': float,
        'LONGTEXT': str,
        'VARCHAR': str,
        'INT': int,
    }
    data_identifier_map = {
        'FLOAT': "%s",
        'LONGTEXT': "%s",
        'VARCHAR': "%s",
    }
    assert len(columns) == len(data_types) == len(schema)
    data = {}
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS unwrapper")
    create_string = "CREATE TABLE unwrapper("
    insert_string = "INSERT INTO unwrapper ("
    values_string = " VALUES ("
    for count, i in enumerate(columns):
        create_string += "" + columns[count] + " " + data_types[count]
        insert_string += "" + columns[count]
        values_string += data_identifier_map[data_types[count]]
        if count != len(columns) - 1:
            create_string += ","
            insert_string += ","
            values_string += ","
        print("select JSON_EXTRACT(data_col, '" + schema[count] + "' ) as value from ingestion;")
        mycursor.execute(
            "select JSON_EXTRACT(data_col, '" + schema[count] + "' ) as value from ingestion;")
        myresult = mycursor.fetchall()
        for result in myresult:
          res = result[0].replace('"', '').strip('][').split(', ')
          data[columns[count]] = list(map(DATA_TYPES_MAP[data_types[count]], res))
    print(insert_string + values_string)
    mycursor.execute(create_string + ',  hash_id VARCHAR(200))')
    mycursor.execute("ALTER TABLE unwrapper ADD PRIMARY KEY(hash_id)")
    list_of_cols = []
    for i in data.keys():
        list_of_cols.append(data[i])

    data_to_load = list(zip(*data.values()))
    hash_to_load = []

    for i in data_to_load:
        hash_to_load.append((*i, str(hash(i) + sys.maxsize + 1)))
    print(insert_string + ',hash_id)' + values_string + ',%s)')
    mycursor.executemany(insert_string + ',hash_id)' + values_string + ',%s)', hash_to_load)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
    mycursor.close()
    mydb.close()


