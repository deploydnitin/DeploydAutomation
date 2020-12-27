from selenium.webdriver import Chrome

import logging

log=logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
#create worning log

handle_warn = logging.FileHandler('WarningLogs.txt')
handle_warn.setLevel(logging.WARNING)

handle_info = logging.FileHandler('InfoLogs.txt')
handle_info.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handle_warn.setFormatter(formatter)
handle_info.setFormatter((formatter))

path = "./Driver/chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://www.naukri.com")
log.info("[Page Opened]")
log.warning("[Warning]")
windowList = driver.window_handles
print (windowList)
mainWin=""
for windowName in windowList:
    driver.switch_to.window(windowName)
    if (driver.current_url == "https://www.naukri.com/"):
        mainWin=windowName
    else:
        driver.close()
driver.switch_to.window(mainWin)
driver.close()