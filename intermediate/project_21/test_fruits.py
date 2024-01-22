from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = Chrome()
    driver.get("https://labasse.github.io/fruits/")


def teardown_function(function):
    driver.quit()


def test_title():
    assert driver.title == "Salade de fruits"


def test_init_chercher_actif():
    chercher = driver.find_element(By.LINK_TEXT, "Chercher")
    assert "active" in chercher.get_attribute("class")