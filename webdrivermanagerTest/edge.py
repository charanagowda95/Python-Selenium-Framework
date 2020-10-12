from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("http://localhost:8888")
driver.close()