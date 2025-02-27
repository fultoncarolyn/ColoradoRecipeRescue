import unittest


from starter.index_page import index_page
from tests.blueprint_test_support import test_client
from tests.db_test_support import TestDatabaseTemplate


class TestIndexPage(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.db = TestDatabaseTemplate()
        self.db.clear()

        self.client = test_client(index_page())

    def test_index_page(self):
        response = self.client.get("/")

        self.assertEqual(200, response.status_code)
        self.assertIn("Capstone Starter", response.text)
