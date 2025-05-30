from app import app, db, Comment

with app.app_context():
    if not db.inspect(db.engine).has_table("comment"):
        Comment.__table__.create(db.engine)
        print("✅ Tabela Comment została utworzona.")
    else:
        print("ℹ️ Tabela Comment już istnieje.")
