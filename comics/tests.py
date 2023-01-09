import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class EditNoLoginTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/comics/Spider-Man (Miles Morales)/edit/')
    def test_correctPage(self):
        assert 'Log in' in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

class EditSuperheroBiographyTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/login/')
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("test")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("TestPassword123!")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        self.driver.get('http://127.0.0.1:8000/comics/Spider-Man (Miles Morales)/edit/')
    def test_correctPage(self):
        assert 'Biography' in self.driver.page_source

    def test_changeFullName(self):
        fullName = self.driver.find_element(By.XPATH, "//input[@name='fullName']")
        length = len(fullName.get_attribute("value"))
        count = 0
        while (count < length):
            fullName.send_keys(Keys.BACKSPACE)
            count += 1
        fullName.send_keys("Miles Gonzalo Morales")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Full Name: Miles Gonzalo Morales' in self.driver.page_source
    def test_changeAlterEgos(self):
        alterEgos = self.driver.find_element(By.XPATH, "//input[@name='alterEgos']")
        length = len(alterEgos.get_attribute("value"))
        count = 0
        while (count < length):
            alterEgos.send_keys(Keys.BACKSPACE)
            count += 1
        alterEgos.send_keys("Captain Universe")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Alter Egos: Captain Universe' in self.driver.page_source

    def test_changeAliases(self):
        aliases = self.driver.find_element(By.XPATH, "//input[@name='aliases']")
        length = len(aliases.get_attribute("value"))
        count = 0
        while (count < length):
            aliases.send_keys(Keys.BACKSPACE)
            count += 1
        aliases.send_keys("Spiderman")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Aliases: Spiderman' in self.driver.page_source
    def test_changeBirthPlace(self):
        birthPlace = self.driver.find_element(By.XPATH, "//input[@name='birthPlace']")
        length = len(birthPlace.get_attribute("value"))
        count = 0
        while (count < length):
            birthPlace.send_keys(Keys.BACKSPACE)
            count += 1
        birthPlace.send_keys("Forest Hills, New York")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Birth Place: Forest Hills, New York' in self.driver.page_source
    def test_changeFirstAppearance(self):
        firstAppearance = self.driver.find_element(By.XPATH, "//input[@name='firstAppearance']")
        length = len(firstAppearance.get_attribute("value"))
        count = 0
        while (count < length):
            firstAppearance.send_keys(Keys.BACKSPACE)
            count += 1
        firstAppearance.send_keys("Ultimate Comics Fallout #4 (October, 2011)")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'First Appearance: Ultimate Comics Fallout #4 (October, 2011)' in self.driver.page_source
    def test_changePublisher(self):
        publisher = self.driver.find_element(By.XPATH, "//input[@name='publisher']")
        length = len(publisher.get_attribute("value"))
        count = 0
        while (count < length):
            publisher.send_keys(Keys.BACKSPACE)
            count += 1
        publisher.send_keys("Marvel Comics")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Publisher: Marvel Comics' in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

class EditSuperheroAppearanceTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000/login/')
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("test")
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("TestPassword123!")
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        login.click()
        self.driver.get('http://127.0.0.1:8000/comics/Spider-Man (Miles Morales)/edit/')
    def test_changeGender(self):
        gender = self.driver.find_element(By.XPATH, "//input[@name='gender']")
        length = len(gender.get_attribute("value"))
        count = 0
        while (count < length):
            gender.send_keys(Keys.BACKSPACE)
            count += 1
        gender.send_keys("Male")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Gender: Male' in self.driver.page_source

    def test_changeRace(self):
        race = self.driver.find_element(By.XPATH, "//input[@name='race']")
        length = len(race.get_attribute("value"))
        count = 0
        while (count < length):
            race.send_keys(Keys.BACKSPACE)
            count += 1
        race.send_keys("Human")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert 'Race: Human' in self.driver.page_source
    def test_changeHeight(self):
        height = self.driver.find_element(By.XPATH, "//input[@name='height']")
        length = len(height.get_attribute("value"))
        count = 0
        while (count < length):
            height.send_keys(Keys.BACKSPACE)
            count += 1
        height.send_keys("5'8 or 172.7 cm")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert "Height: 5'8 or 172.7 cm" in self.driver.page_source
    def test_changeWeight(self):
        weight = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        length = len(weight.get_attribute("value"))
        count = 0
        while (count < length):
            weight.send_keys(Keys.BACKSPACE)
            count += 1
        weight.send_keys("160.06 lbs or 72.6 kg")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert "Weight: 160.06 lbs or 72.6 kg" in self.driver.page_source
    def test_changeEyeColor(self):
        eyeColor = self.driver.find_element(By.XPATH, "//input[@name='eyeColor']")
        length = len(eyeColor.get_attribute("value"))
        count = 0
        while (count < length):
            eyeColor.send_keys(Keys.BACKSPACE)
            count += 1
        eyeColor.send_keys("Brown")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert "Eye Color: Brown" in self.driver.page_source
    def test_changeHairColor(self):
        hairColor = self.driver.find_element(By.XPATH, "//input[@name='hairColor']")
        length = len(hairColor.get_attribute("value"))
        count = 0
        while (count < length):
            hairColor.send_keys(Keys.BACKSPACE)
            count += 1
        hairColor.send_keys("Black")
        update = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-outline-info')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", update)
        time.sleep(2)
        update.click()
        assert "Hair Color: Black" in self.driver.page_source
    def tearDown(self):
        self.driver.quit()