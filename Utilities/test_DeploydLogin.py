from selenium.webdriver import Chrome
#from selenium.webdriver.support.select import Select #from drop down and lists
#from selenium.webdriver.common.action_chains import ActionChains #keyboard and mouse function
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import TakeScreenshot
import pytest
import time

@pytest.fixture(scope="module")
def setup():
    global driver
    #launch Deployd application on chrome
    path = "../Driver/chromedriver.exe"
    driver = Chrome(executable_path=path)
    #driver.set_page_load_timeout(1)
    driver.implicitly_wait(20)
    driver.get("http://dev.compass-deployd.io")

    #maximize browser
    driver.maximize_window()
    yield
    driver.close()

def test_login(setup):
    #Validate that Login page is open
    assert driver.title == 'Deployd', "Page not found"

    #Input Username and Password
    driver.find_element_by_id("normal_login_username").send_keys("nitin.srivastava@deployd.io")
    driver.find_element_by_id("normal_login_password").send_keys("Summer@13")
    #wait = WebDriverWait(driver,100)
    #wait.until(ec.text_to_be_present_in_element(By.ID),'')

    driver.find_element_by_xpath("//span[text() = 'Log In']").click()
    time.sleep(10)
    #act = ActionChains(driver)
    #act.send_keys(Keys.TAB).perform()
    #act.click().perform() # left click. provide obj identification in click method
    #act.context_click().perform() #right click
    #act.double_click().perform()#double click
    #act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()#hover
    assert driver.current_url == "http://dev.compass-deployd.io/analyze/repositories"

    TakeScreenshot.takeScreenshot(driver,"First")
    #Scroll
    #driver.execute_script("windows.scroll(0,400);")