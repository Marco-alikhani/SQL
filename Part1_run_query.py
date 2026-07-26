# Part1_run_query.py
import duckdb
import sys

con = duckdb.connect("sql_learning.db")

# Read the SQL file passed as an argument
with open(sys.argv[1]) as f:
    query = f.read()

con.sql(query).show()
con.close()