# create_db.py
from market import app, db

with app.app_context():
    db.create_all()
    print("✅ Database created successfully!")
