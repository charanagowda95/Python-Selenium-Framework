from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager

iedriver = webdriver.Ie(IEDriverManager().install())
iedriver.get("localhost:8888")
iedriver.close()