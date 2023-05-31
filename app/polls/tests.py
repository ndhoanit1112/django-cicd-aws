from django.test import TestCase
from app.polls.models import Poll

# Create your tests here.
class PollTestCase(TestCase):
    SOCKET_PATH = "unix://%2Fvar%2Frun%2Fgunicorn%2Fgunicorn.sock"

    def test_index_loads_properly(self):
        """The index page loads properly"""
        print("Test index page loads properly...")
        response = self.client.get(f'http+{self.SOCKET_PATH}/polls/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        Poll.objects.create(name="test_poll")

    def test_poll_created(self):
        poll = Poll.objects.first()
        self.assertEqual(poll.name, "test_poll")
