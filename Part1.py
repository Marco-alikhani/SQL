import duckdb
con = duckdb.connect()  # in-memory database
con.sql("SELECT 'hello duckdb' AS greeting").show()


# Loading sample dataset:
