from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from app import db

class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


    @classmethod
    def get_one_by_id(self, id):
        try:
            return self.query.filter(self.id == id).one()
        except NoResultFound:
            return None