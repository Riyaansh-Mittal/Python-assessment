from .models import db

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()  # This creates all tables defined in models.py, including 'app'

def get_app_by_id(app_id):
    from .models import App
    return App.query.get(app_id)

def add_app(app_name, version, description):
    from .models import App
    new_app = App(app_name=app_name, version=version, description=description)
    db.session.add(new_app)
    db.session.commit()

def delete_app(app_id):
    from .models import App
    app = App.query.get(app_id)
    if app:
        db.session.delete(app)
        db.session.commit()
