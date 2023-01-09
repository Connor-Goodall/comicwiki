import time

from django.test import TestCase
from selenium import webdriver
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

class ProfileNoLoginTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/profile/')

    def test_correctPage(self):
        assert 'Profile Info' not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
class ProfileTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/login/')
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("test")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("TestPassword123!")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        self.driver.get('http://127.0.0.1:8000/profile/')
    def test_correctPage(self):
        assert 'Profile Info' in self.driver.page_source
    def test_changeFavoriteHero(self):
        favorite_hero = self.driver.find_element(By.XPATH, "//input[@name='favorite_hero']")
        length =  len(favorite_hero.get_attribute("value"))
        count = 0
        while(count < length):
            favorite_hero.send_keys(Keys.BACKSPACE)
            count += 1
        favorite_hero.send_keys("Batman")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        self.driver.get('http://127.0.0.1:8000/users/test')
        assert 'Favorite Hero: Batman' in self.driver.page_source

    def test_changeFavoriteAntihero(self):
        favorite_antihero = self.driver.find_element(By.XPATH, "//input[@name='favorite_antihero']")
        length = len(favorite_antihero.get_attribute("value"))
        count = 0
        while (count < length):
            favorite_antihero.send_keys(Keys.BACKSPACE)
            count += 1
        favorite_antihero.send_keys("Venom")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        self.driver.get('http://127.0.0.1:8000/users/test')
        assert 'Favorite Anti-Hero: Venom' in self.driver.page_source
    def test_changeFavoriteVillian(self):
        favorite_villian = self.driver.find_element(By.XPATH, "//input[@name='favorite_villian']")
        length = len(favorite_villian.get_attribute("value"))
        count = 0
        while (count < length):
            favorite_villian.send_keys(Keys.BACKSPACE)
            count += 1
        favorite_villian.send_keys("Green Goblin")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        self.driver.get('http://127.0.0.1:8000/users/test')
        assert 'Favorite Villian: Green Goblin' in self.driver.page_source
    def test_changeFavoriteTeam(self):
        favorite_team = self.driver.find_element(By.XPATH, "//input[@name='favorite_team']")
        length = len(favorite_team.get_attribute("value"))
        count = 0
        while (count < length):
            favorite_team.send_keys(Keys.BACKSPACE)
            count += 1
        favorite_team.send_keys("The Avengers")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        self.driver.get('http://127.0.0.1:8000/users/test')
        assert 'Favorite Team: The Avengers' in self.driver.page_source
    def test_changeUsername(self):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        length = len(username.get_attribute("value"))
        count = 0
        while (count < length):
            username.send_keys(Keys.BACKSPACE)
            count += 1
        username.send_keys("cag3dmr")
        name = username.get_attribute("value")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        self.driver.get(f"http://127.0.0.1:8000/users/{name}")
        assert 'Username: cag3dmr' in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
