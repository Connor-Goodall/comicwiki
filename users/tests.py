from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create your tests here.

class RightWebsiteTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_website(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/comics/')
        assert 'Comics Universal' in driver.page_source

    def tearDown(self):
        self.driver.quit()

class LogInTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/login/')

    def test_correctPage(self):
        assert 'Log in' in self.driver.page_source
    def test_correctLogin(self):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("test")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("TestPassword123!")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        assert 'Profile' in self.driver.page_source
        assert 'Comics Universal' in self.driver.page_source
    def test_wrongUsername(self):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("batman")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("TestPassword123!")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        assert 'Please enter a correct username and password. Note that both fields may be case-sensitive.' \
               in self.driver.page_source
    def test_wrongPassword(self):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("test")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("ABCD")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        assert 'Please enter a correct username and password. Note that both fields may be case-sensitive.' \
               in self.driver.page_source
    def tearDown(self):
        self.driver.quit()
