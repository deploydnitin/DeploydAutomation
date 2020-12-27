


def test_takeScreenshot(driver, name):
    driver.get_screenshot_as_file("C:/Users/Nitin/PycharmProjects/DeploydAutomation/Screenshots/" +name+ ".png")