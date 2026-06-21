from app import db

class Setting(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)

    private_profile = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )