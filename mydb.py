import mariadb

conn = mariadb.connect(
        user="aniruddha",
        password="aniruddha",
        host="localhost",
        port=3306,
        # database="elderco"
    )

cur = conn.cursor()

cur.execute("CREATE DATABASE elderco")

print("ALL Done!")
