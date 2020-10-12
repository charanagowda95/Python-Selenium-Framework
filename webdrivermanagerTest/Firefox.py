from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

gdriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
gdriver.get("http://localhost:8888")
gdriver.close()

