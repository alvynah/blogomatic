import unittest
from app.models import Blog, Upvote, User
from app import db


class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Vee = User(username='zeluuhyne',password='banana', email='zeluuhyne@ms.com')
        self.blog_vee = Blog(title='love', blog='This is the ghetto', user=self.user_Vee)

        self.upvote_vee = Upvote(upvote='2', blog=self.blog_vee)

    def tearDown(self):
        Upvote.query.delete()
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.upvote_vee, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.upvote_vee.upvote, '2')
        self.assertEquals(self.upvote_vee.blog, self.blog_vee)

    def test_save_upvote(self):
        self.upvote_vee.save_upvote()
        self.assertTrue(len(Upvote.query.all()) > 0)
