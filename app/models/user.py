from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
import datetime
import enum
import uuid


class UserType(enum.Enum):
    ADMINISTRATOR = 1, "ADMINISTRATOR"
    USER = 2, "USER"
    TEACHER = 3, "TEACHER"


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    picture = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, nullable=False, server_default="0")
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    lessons = db.relationship("LessonUser", back_populates="user")

    def __init__(self, name, surname, email, active=1):
        self.name = name
        self.surname = surname
        self.email = email
        self.active = active

    def save_to_db(self):
        """
        Saves User to Database

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
        Deletes user by ID
        Args:
            id:

        Returns:

        """
        user = cls.query.filter_by(id=id).scalar()
        if user:
            return user.delete_self()
        else:
            return False

    @classmethod
    def find_by_id(cls, id):
        """
        Find User by ID

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


class ApplicationUser(db.Model):
    __tablename__ = "application_user"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(
        db.String(36),
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.Enum(UserType), server_default="USER", nullable=False)
    user = db.relationship("User", foreign_keys=user_id, lazy="select")

    def __init__(self, user_id, username, password, user_type: UserType):
        self.user_id = user_id
        self.username = username
        self.password = generate_password_hash(password, method="sha256", salt_length=8)
        self.user_type = user_type

    def save_to_db(self):
        """
        Saves Application User to Database

        Returns:

        """
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    @classmethod
    def authenticate(cls, username: str, password: str):
        """
        Authenticate function.

        Args:
            username: Represents the username
            password: Represents the password

        Returns:
            ApplicationUser object.
            Account details are accessible by calling "user" property of this result

            Ex:

            account =  ApplicationUser.authenticate(username='john', password='john123')
            if not account:
                print("Credentials incorrect or user does not exists")
            else:
                account_details = account.user

        """

        if not username or not password:
            return None

        account = cls.query.filter_by(username=username).first()
        if not account or not check_password_hash(account.password, password):
            return None

        return account
