import custom_wait as CW
from xpath import *
from typing import Union
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, WebElement
from selenium.webdriver.support import expected_conditions as EC


class Result:
    def __init__(self, manufacturer: str, serial_number: str, date_purchased: str, warranty_expiration: str):
        self.__manufacturer = manufacturer
        self.__serial_number = serial_number
        self.__date_purchased = date_purchased
        self.__warranty_expiration = warranty_expiration

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @property
    def serial_number(self) -> str:
        return self.__serial_number

    @property
    def date_purchased(self) -> str:
        return self.__date_purchased

    @property
    def warranty_expiration(self) -> str:
        return self.__warranty_expiration


def search(mfg = '', serial = '', model = '') -> Union[Result, None]:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.lookupwarranty.com/")

    # Filling MFG data
    e_mfg = driver.find_element(By.XPATH, MFG)
    mgf_options = e_mfg.find_elements(By.TAG_NAME, "option")
    for option in mgf_options:
        if option.text.upper() == mfg.upper():
            option.click()


    # Filling serial data
    e_serial = driver.find_element(By.XPATH, SERIAL)
    e_serial.send_keys(serial)

    # Filling model data
    e_model = driver.find_element(By.XPATH, MODEL)
    e_model.send_keys(model)

    e_submit = driver.find_element(By.XPATH, SUBMIT)
    e_submit.click()

    try:
        WebDriverWait(driver, 10).until(
            CW.ElementHasStyle((By.XPATH, DATA), DATA_STYLES)
        )
    except:
        return None
    else:
        manufacturer = driver.find_element(By.XPATH, MANUFACTURER_DATA).text
        serial = driver.find_element(By.XPATH, SERIAL_DATA).text
        purchased_date = driver.find_element(By.XPATH, PURCHASED_DATE_DATA).text
        warranty_expiration = driver.find_element(By.XPATH, WARRANTY_EXPIRATION_DATA).text
    finally:
        driver.close()
    
    return Result(manufacturer, serial, purchased_date, warranty_expiration)
