import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(ChromeDriverManager().install())
    elif browser=="firefox":
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser=="edge":
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver=webdriver.Ie(IEDriverManager().install())
    return driver


def pytest_addoption(parser):       #this will get value from cli/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #this will return browser value to setup method
    return request.config.getoption("--browser")


######   pytest html report############
def pytest_configure(config):
    config._metadata['Project Name']='vtiger'
    config._metadata['Module Name'] = 'login'
    config._metadata['Tester'] = 'charan'


##hook for deleting/modifying env info html report
@pytest.mark.optionalhook
def pytets_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugind",None)