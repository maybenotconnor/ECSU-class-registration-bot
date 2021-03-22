import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import pause
from datetime import datetime

browser = webdriver.Firefox()
browser.get('https://ssb-prod.ec.easternct.edu/ssomanager/saml/login?relayState=/c/auth/SSB')

#credentials loaded from .env
load_dotenv('.env')
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(MY_EMAIL_ADDRESS)

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(MY_PASSWORD)

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

time.sleep(3)
browser.get('https://ssb-prod.ec.easternct.edu/PROD/bwskfreg.P_AltPin')
time.sleep(1)
try:
    #select term from dropdown - must know value to set
    browser.execute_script('document.getElementById("term_id").value="202210"')
except:
    pass
browser.execute_script('document.getElementsByTagName("input")[2].click()')
time.sleep(1)
try:
    #if asks confirmation
    browser.execute_script('document.getElementsByName("submit_btn")[1].click()')
except:
    pass
time.sleep(1)

#input registration code
browser.execute_script('document.getElementById("apin_id").value="999999"')

#submit code - should run at 7:00 - make sure to set date
pause.until(datetime(2021,3,29,7,0,0,3))
browser.execute_script('document.getElementsByTagName("input")[3].click()')


#input class CRNs below
browser.execute_script('document.getElementById("crn_id1").value="00000"')
browser.execute_script('document.getElementById("crn_id2").value="00000"')
browser.execute_script('document.getElementById("crn_id3").value="00000"')
browser.execute_script('document.getElementById("crn_id4").value="00000"')
browser.execute_script('document.getElementById("crn_id5").value="00000"')
browser.execute_script('document.getElementsByName("REG_BTN")[1].click()')