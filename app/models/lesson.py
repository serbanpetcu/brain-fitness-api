from sqlalchemy import UniqueConstraint

from app.extensions import db
import datetime
import enum
import uuid


class LessonStatus(enum.Enum):
    DRAFT = 1, "DRAFT"
    PUBLISHED = 2, "PUBLISHED"


class UserLessonStatus(enum.Enum):
    INPROGRESS = 1, "INPROGRESS"
    FINISHED = 2, "FINISHED"


# Intermediate table for lessons followed by users
class LessonUser(db.Model):
    __tablename__ = "lesson_user"
    __table_args__ = (
        UniqueConstraint("lesson_id", "user_id", name="_lesson_user_unique"),
        {"extend_existing": True},
    )
    lesson_id = db.Column(
        db.String(36), db.ForeignKey("lesson.id", ondelete="CASCADE"), primary_key=True
    )
    user_id = db.Column(
        db.String(36), db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    status = db.Column(
        db.Enum(UserLessonStatus),
        server_default="INPROGRESS",
        index=True,
        nullable=False,
    )
    lesson = db.relationship(
        "Lesson",
       # back_populates="users",
        backref=db.backref(
            "lu_users", cascade="save-update, merge, " "delete, delete-orphan"
        ),
    )
    user = db.relationship(
        "User",
        # back_populates="lessons",
        backref=db.backref(
            "lu_lessons", cascade="save-update, merge, " "delete, delete-orphan"
        ),
    )

    def __init__(self, lesson_id, user_id, status: UserLessonStatus):
        self.lesson_id = lesson_id
        self.user_id = user_id
        self.status = status

    def save_to_db(self):
        """
        Saves Lesson to Database

        Returns:

        """
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise


class Lesson(db.Model):
    __tablename__ = "lesson"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    subname = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(LessonStatus), server_default="DRAFT", nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    users = db.relationship("LessonUser", back_populates="lesson")

    # Cards of this lesson
    cards = db.relationship(
        "Card", primaryjoin="Card.lesson_id==Lesson.id", lazy="joined"
    )

    def __init__(self, name, subname, duration, status: LessonStatus):
        self.name = name
        self.subname = subname
        self.duration = duration
        self.status = status

    def save_to_db(self):
        """
        Saves Lesson to Database

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

    @classmethod
    def find_by_id(cls, id):
        """
        Find Lesson by ID

        Args:
            id: user uuid

        Returns:
            User object

        """
        result = cls.query.filter_by(id=id).scalar()
        if result:
            return result
        else:
            return None

    def delete_self(self):
        """
        Deletes itself
        Returns:

        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            raise

    @classmethod
    def delete_by_id(cls, id):
        """
        Deletes lesson by ID
        Args:
            id:

        Returns:

        """
        lesson = cls.query.filter_by(id=id).scalar()
        if lesson:
            return lesson.delete_self()
        else:
            return False
