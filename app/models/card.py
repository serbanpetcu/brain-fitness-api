from app.extensions import db
import datetime
import enum
import uuid


class Card(db.Model):
    __tablename__ = "card"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    lesson_id = db.Column(
        db.String(36),
        db.ForeignKey("lesson.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    text = db.Column(db.BLOB, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    lesson = db.relationship(
        "Lesson",
        foreign_keys=lesson_id,
        backref=db.backref("card", lazy="select", cascade="all,delete"),
    )

    def __init__(self, lesson_id, text):
        self.lesson_id = lesson_id
        self.text = text

    def save_to_db(self):
        """
        Saves Card to Database

        Returns:

        """
        try:
            self.updated_at = datetime.datetime.utcnow()
            self.created_at = datetime.datetime.utcnow()

            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update(self):
        """
        Updates object

        Returns:

        """
        try:
            self.updated_at = datetime.datetime.utcnow()
            db.session.commit()
        except:
            db.session.rollback()
            raise
