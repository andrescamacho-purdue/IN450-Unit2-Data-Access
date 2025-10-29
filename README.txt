IN450 — Unit 2 Submission (macOS + VS Code)
Andres Camacho

Contents
--------
- create_in450_tables.sql
- business_layer.py
- gui_app.py
- requirements.txt

Quick Steps
-----------
1) PostgreSQL install (VS Code Terminal):
   brew install postgresql@16
   brew services start postgresql@16

2) Open psql and run the SQL (update CSV absolute paths first):
   psql -U postgres -h localhost -d postgres -f create_in450_tables.sql
   (or paste the statements interactively inside psql)

3) Python venv + deps (VS Code Terminal inside this folder):
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

4) Run GUI:
   python3 gui_app.py

5) Screenshots to include:
   - psql SELECT COUNT(*) results for in450a/b/c
   - GUI window open
   - After clicking "Get Row Count (in450a)"
   - After clicking "Show Names (in450b)"
   - GitHub repo page with files

Notes
-----
- If you set a postgres password, put it into the connection string in gui_app.py:
    CONN = "dbname=postgres user=postgres password=YourPass host=localhost port=5432"
- If connection fails on macOS, consider setting a password in psql:
    \password postgres
- If Tkinter window does not appear, ensure you are running with Python 3 from python.org or a Tk-enabled build.
