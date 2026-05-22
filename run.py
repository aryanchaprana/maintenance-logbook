"""
Maintenance Manager — Startup Script
Run: python run.py
Then open: http://localhost:5000
Default login: admin / admin123
"""
from database import init_db
from app import app

if __name__ == '__main__':
    print("=" * 50)
    print("  Maintenance Manager")
    print("  Initializing database…")
    init_db()
    print("  Open your browser: http://localhost:5000")
    print("  Default login:     admin / admin123")
    print("  Press Ctrl+C to stop.")
    print("=" * 50)
    app.run(debug=False, port=5000, host='0.0.0.0')
