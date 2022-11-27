from db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, default=None)

    category = db.relationship(
        "RecordModel",
        back_populates="category",
        lazy="dynamic"
    )


