import unittest
from app import create_app
from app.models.card import Card
from app.models.lesson import Lesson, LessonStatus, LessonUser, UserLessonStatus
from app.models.user import User, UserType, ApplicationUser

app = create_app()


class TestAccounts(unittest.TestCase):
    app = None
    user_id = None
    lesson_id = None
    username = None
    password = None

    @classmethod
    def setUpClass(cls) -> None:
        global app

        cls.app = app
        app.config["TESTING"] = True

        cls.username = "john"
        cls.password = "john123"
        cls.user_id = cls.createAccount()
        cls.lesson_id = cls.createLesson()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.deleteTestLesson()
        cls.deleteTestAccount()

    @classmethod
    def createAccount(cls) -> str:
        with cls.app.app_context():
            new_user = User(name="John", surname="Doe", email="john@doe.com", active=1)
            new_user.save_to_db()

            new_credentials = ApplicationUser(
                user_id=new_user.id,
                username=cls.username,
                password=cls.password,
                user_type=UserType.USER,
            )
            new_credentials.save_to_db()

            return new_user.id

    @classmethod
    def createLesson(cls) -> str:
        with cls.app.app_context():
            new_lesson = Lesson(
                name="Test Lesson",
                subname="Subname of test lesson",
                duration="1 week",
                status=LessonStatus.DRAFT,
            )
            new_lesson.save_to_db()
            return new_lesson.id

    @classmethod
    def deleteTestAccount(cls):
        with cls.app.app_context():
            deleted = User.delete_by_id(id=cls.user_id)

    @classmethod
    def deleteTestLesson(cls):
        with cls.app.app_context():
            deleted = Lesson.delete_by_id(id=cls.lesson_id)

    def test_account_auth(self):
        """
        Test if the authenticate function works
        Returns:

        """
        with self.app.app_context():
            # In order for this to work, make sure you run the "test_account_creation" function (ABOVE)
            account = ApplicationUser.authenticate(
                username=self.username, password=self.password
            )

            self.assertIsNotNone(account)

    def test_lesson_card_creation(self):
        with self.app.app_context():
            # Please change lesson_id to an existing Lesson in your db
            lesson_text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Ut eu nunc id ante pharetra viverra vel et lectus. Etiam finibus massa sit amet lectus sollicitudin cursus.
             Aliquam erat volutpat. Vivamus aliquam elit nec augue vulputate consequat vel euismod tellus. 
             Suspendisse potenti. Proin non felis in mauris tincidunt consequat et non enim. 
             Mauris fermentum, odio a fringilla condimentum, massa orci ornare elit, vel pellentesque sapien tellus at nunc. 
             Vivamus ultrices at tortor et imperdiet. Integer malesuada dolor lectus, quis fringilla ligula pulvinar a. 
             Cras dignissim hendrerit felis, eu gravida urna rhoncus eu. Ut mauris sem, ultrices a efficitur at, pellentesque ac dolor."""

            # Adds a card to database
            new_card = Card(lesson_id=self.lesson_id, text=lesson_text.encode("utf-8"))
            self.assertTrue(new_card.save_to_db())

    def test_lesson_user_follow(self):
        with self.app.app_context():
            new_lesson_user = LessonUser(
                user_id=self.user_id,
                lesson_id=self.lesson_id,
                status=UserLessonStatus.INPROGRESS,
            )
            self.assertTrue(new_lesson_user.save_to_db())

    def test_user_followed_lessons(self):
        with self.app.app_context():
            user = User.find_by_id(id=self.user_id)
            self.assertIsNotNone(user.lessons)
