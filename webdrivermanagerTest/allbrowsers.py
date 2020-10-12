from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

cdriver = webdriver.Chrome(ChromeDriverManager().install())
cdriver.get("http://localhost:8888")
cdriver.close()


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

gdriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
gdriver.get("http://localhost:8888")
gdriver.close()

from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager

iedriver = webdriver.Ie(IEDriverManager().install())
iedriver.get("localhost:8888")
iedriver.close()

