import unittest
from app.models import Blog, Downvote, User
from app import db


class DownvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Vee = User(username='zeluuhyne',password='banana', email='zeluuhyne@ms.com')
        self.blog_vee = Blog(title='love', blog='This is the ghetto', user=self.user_Vee)
        self.downvote_vee = Downvote(downvote='8', blog=self.blog_vee)

    def tearDown(self):
        Downvote.query.delete()
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.downvote_vee, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.downvote_vee.downvote, '8')
        self.assertEquals(self.downvote_vee.blog, self.blog_vee)

    def test_save_upvote(self):
        self.downvote_vee.save_downvote()
        self.assertTrue(len(Downvote.query.all()) > 0)
