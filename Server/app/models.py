from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class App(db.Model):
    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, app_name, version, description):
        self.app_name = app_name
        self.version = version
        self.description = description

    def __repr__(self):
        return f"<App {self.app_name} ({self.version})>"
