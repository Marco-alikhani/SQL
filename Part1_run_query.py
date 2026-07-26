"""
Run a .sql file against the sql_learning.db DuckDB database.

Usage:
    uv run Part1_run_query.py queries/q01_all_customers.sql
"""
import duckdb
import sys
from pathlib import Path

# --- Argument check ---
if len(sys.argv) < 2:
    print("❌ Usage: uv run Part1_run_query.py <path_to_sql_file>")
    print("   Example: uv run Part1_run_query.py queries/q01_all_customers.sql")
    sys.exit(1)

sql_path = Path(sys.argv[1])

if not sql_path.exists():
    print(f"❌ File not found: {sql_path}")
    sys.exit(1)

# --- Read the SQL file ---
query = sql_path.read_text()

print(f"▶ Running: {sql_path}")
print("─" * 60)
print(query.strip())
print("─" * 60)

# --- Run it against the persistent database ---
con = duckdb.connect("sql_learning.db")
try:
    con.sql(query).show()
finally:
    con.close()