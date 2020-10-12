from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

cdriver = webdriver.Chrome(ChromeDriverManager().install())
cdriver.get("http://localhost:8888")
cdriver.close()

