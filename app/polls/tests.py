from django.test import TestCase

# Create your tests here.
class ViewsTestCase(TestCase):
    SOCKET_PATH = "unix://%2Fvar%2Frun%2Fgunicorn%2Fgunicorn.sock"

    def test_index_loads_properly(self):
        """The index page loads properly"""
        print("Test index page loads properly...")
        response = self.client.get(f'http+{self.SOCKET_PATH}/polls/')
        self.assertEqual(response.status_code, 200)
