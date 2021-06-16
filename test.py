"""
Python script to test web application using selenium web driver.
"""
import time
import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

url = "http://127.0.0.1:8080/"
correct_email = "test@test.com"
correct_password = "test"
wrong_email = "asdf@asdf.com"
wrong_password = "asdf"

driver: Firefox


class LoginTest(unittest.TestCase):
    def login(self, email: str, password: str):
        """Function tries to login with given email address and password.

        The driver must be on login page before calling function.
        """
        try:
            email_field = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located((By.ID, "email"))
            )
            password_field = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located((By.ID, "password"))
            )
            submit_button = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, "submit-button")
                )
            )
            email_field.clear()
            password_field.clear()
            email_field.send_keys(email)
            password_field.send_keys(password)
            submit_button.click()
            time.sleep(1)
            return driver.title != "Try Now"
        except Exception:
            return False

    def load_login_page(self):
        """Function loads the login page."""
        driver.get(url)

        try_now_button = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".nav ul li a")
            )
        )[-1]
        try_now_button.click()
        self.assertEqual(driver.title, "Try Now")

    def test_empty_both(self):
        self.load_login_page()
        self.assertFalse(
            self.login(email="", password=""),
            "Empty email and password.",
        )

    def test_empty_email(self):
        self.load_login_page()
        self.assertFalse(
            self.login(email="", password=wrong_password),
            "Empty password.",
        )

    def test_empty_password(self):
        self.load_login_page()
        self.assertFalse(
            self.login(email=wrong_email, password=""),
            "Empty email address.",
        )

    def test_wrong_password(self):
        self.load_login_page()
        self.assertFalse(
            self.login(email=correct_email, password=wrong_password),
            "Correct email wrong password",
        )

    def test_wrong_email(self):
        self.load_login_page()
        self.assertFalse(
            self.login(email=wrong_email, password=correct_password),
            "Wrong email correct password",
        )

    def test_correct_both(self):
        self.load_login_page()
        self.assertTrue(
            self.login(email=correct_email, password=correct_password),
            "Correct email correct password",
        )
        logout = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "logout"))
        )
        logout.click()


class SignupTest(unittest.TestCase):
    def load_signup_page(self):
        """Function loads the login page."""
        driver.get(url)

        try_now_button = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".nav ul li a")
            )
        )[-1]
        try_now_button.click()
        self.assertEqual(driver.title, "Try Now")

        switch_btn = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "switch-action"))
        )
        switch_btn.click()

    def signup(self, email: str, password: str):
        try:
            email_field = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located((By.ID, "email"))
            )
            password_field = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located((By.ID, "password"))
            )
            submit_button = WebDriverWait(driver=driver, timeout=10).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, "submit-button")
                )
            )
            email_field.clear()
            password_field.clear()
            email_field.send_keys(email)
            password_field.send_keys(password)
            submit_button.click()
            time.sleep(1)
            return driver.title != "Try Now"
        except Exception:
            return False

    def test_empty_both(self):
        self.load_signup_page()
        self.assertFalse(self.signup(email="", password=""), "Empty email and password")

    def test_empty_email(self):
        self.load_signup_page()
        self.assertFalse(
            self.signup(email="", password=correct_password), "Empty email"
        )

    def test_empty_password(self):
        self.load_signup_page()
        self.assertFalse(
            self.signup(email=correct_email, password=""), "Empty password"
        )

    def test_existing_account(self):
        self.load_signup_page()
        self.assertFalse(
            self.signup(email=correct_email, password=correct_password),
            "existing email id and password",
        )


class PredictionTest(unittest.TestCase):
    def login(self):

        driver.get(url)

        try_now_button = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".nav ul li a")
            )
        )[-1]
        try_now_button.click()
        self.assertEqual(driver.title, "Try Now")

        email_field = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "email"))
        )
        password_field = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "password"))
        )
        submit_button = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "submit-button"))
        )
        email_field.clear()
        password_field.clear()
        email_field.send_keys(correct_email)
        password_field.send_keys(correct_password)
        submit_button.click()
        time.sleep(1)

    def logout(self):
        logout_btn = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "logout"))
        )
        logout_btn.click()

    def upload(self, path: str):
        upload_btn = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload-btn"))
        )
        upload_btn.send_keys(path)

        plant_name = WebDriverWait(driver=driver, timeout=10).until(
            expected_conditions.presence_of_element_located((By.ID, "plant-name"))
        )
        time.sleep(1)
        return plant_name.text

    def test_image(self):
        self.login()
        res = self.upload(path="/tmp/index.jpg")
        self.assertNotEqual(len(res), 0, "No plant name found")
        self.logout()


if __name__ == "__main__":
    driver = Firefox()
    unittest.main()
