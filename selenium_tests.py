from selenium import webdriver
import unittest

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()  # Or webdriver.Firefox(), depending on your browser choice

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_index_route(self):
        """Test the index route of the Flask application."""
        # Open the index page
        self.driver.get("http://localhost:5000")

        # Assert that the page title is correct
        self.assertEqual(self.driver.title, "BMI Calculator")

        # You can add more assertions to check the content of the index page

    def test_calculate_route(self):
        """Test the calculate route of the Flask application."""
        # Open the calculate page
        self.driver.get("http://localhost:5000/calculate")

        # Assert that the page title is correct
        self.assertEqual(self.driver.title, "BMI Result")

        # You can add more assertions to check the content of the calculate page

if __name__ == "__main__":
    unittest.main()
