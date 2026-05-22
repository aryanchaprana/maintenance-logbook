import sqlite3, os
from werkzeug.security import generate_password_hash

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "maintenance.db"))

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    # Create tables (new installs)
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, role TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    c.execute("CREATE TABLE IF NOT EXISTS machines (id INTEGER PRIMARY KEY AUTOINCREMENT, equipment_no TEXT UNIQUE NOT NULL, name TEXT NOT NULL, asset_code TEXT, location TEXT, area TEXT, module TEXT, capacity TEXT, unit TEXT, make TEXT, installation_date TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    c.execute("CREATE TABLE IF NOT EXISTS dropdown_options (id INTEGER PRIMARY KEY AUTOINCREMENT, field_name TEXT NOT NULL, value TEXT NOT NULL, display_order INTEGER DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, UNIQUE(field_name, value))")
    c.execute("CREATE TABLE IF NOT EXISTS log_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, machine_id INTEGER NOT NULL, area TEXT, module TEXT, entry_date TEXT NOT NULL, shift TEXT, start_time TEXT NOT NULL, end_time TEXT NOT NULL, down_time_minutes INTEGER NOT NULL DEFAULT 0, error_message TEXT, trouble_description TEXT, maintenance_action TEXT, quality_confirmation TEXT, category TEXT, occurrence TEXT, status TEXT DEFAULT 'Open', engineer1 TEXT, engineer2 TEXT, engineer3 TEXT, submitted_by INTEGER NOT NULL, checked_by TEXT, review_status TEXT NOT NULL DEFAULT 'pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (machine_id) REFERENCES machines(id), FOREIGN KEY (submitted_by) REFERENCES users(id))")

    # Migrate machines table - add any missing columns
    m_cols = [r[1] for r in c.execute("PRAGMA table_info(machines)").fetchall()]
    for col, typ in [("asset_code","TEXT"), ("location","TEXT"), ("area","TEXT"), ("module","TEXT"),
                     ("capacity","TEXT"), ("unit","TEXT"), ("make","TEXT"), ("installation_date","TEXT"),
                     ("updated_at","TIMESTAMP")]:
        if col not in m_cols:
            c.execute("ALTER TABLE machines ADD COLUMN " + col + " " + typ)

    # Migrate log_entries table - add any missing columns
    le_cols = [r[1] for r in c.execute("PRAGMA table_info(log_entries)").fetchall()]
    for col, typ in [("area","TEXT"), ("module","TEXT"), ("shift","TEXT"), ("end_date","TEXT"),
                     ("error_message","TEXT"), ("trouble_description","TEXT"),
                     ("maintenance_action","TEXT"), ("quality_confirmation","TEXT"),
                     ("category","TEXT"), ("occurrence","TEXT"),
                     ("engineer1","TEXT"), ("engineer2","TEXT"), ("engineer3","TEXT"),
                     ("checked_by","TEXT"), ("down_time_minutes","INTEGER DEFAULT 0"),
                     ("review_status","TEXT DEFAULT 'pending'"), ("updated_at","TIMESTAMP")]:
        if col not in le_cols:
            c.execute("ALTER TABLE log_entries ADD COLUMN " + col + " " + typ)

    # Default admin user
    c.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                  ("admin", generate_password_hash("admin123"), "admin"))

    # Seed dropdown options
    for f, v in [("category","Electrical"),("category","Mechanical"),("category","Software"),
                 ("category","Operator Error"),("category","Periodic PM"),
                 ("occurrence","First Time"),("occurrence","Recurring"),("occurrence","Resolved but Re-opened"),
                 ("status","Open"),("status","In Progress"),("status","Awaiting Parts"),("status","Closed"),
                 ("quality_confirmation","Yes"),("quality_confirmation","No"),("quality_confirmation","N/A")]:
        c.execute("INSERT OR IGNORE INTO dropdown_options (field_name, value) VALUES (?, ?)", (f, v))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")
