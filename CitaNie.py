import urllib.request
import json
from html.parser import HTMLParser
import xml.dom.minidom

# DaPe- The objective is to access TimeTac
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import mechanize
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import time

driver = webdriver.Chrome(r'C:\Users\David Pereira\Documents\chromedriver_win32\chromedriver.exe')
driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/citar?p=8&locale=es")

time.sleep(4)
#*******LOGIN***************

# find username and fill
tramites_options = driver.find_element(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]')
#scroll to element
driver.execute_script("arguments[0].scrollIntoView();", tramites_options)
tramites = Select(driver.find_element(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]'))
tramites.select_by_value('4079')
accepttramite = driver.find_element(by=By.XPATH, value='//*[@id="btnAceptar"]')
time.sleep(1)
accepttramite.click()
time.sleep(4)

EnterBtn = driver.find_element(by=By.XPATH, value='//*[@id="btnEntrar"]')

EnterBtn.click()
driver.find_element(by=By.XPATH, value='//*[@id="rdbTipoDocPas"]').click() #SelectPassport
PassportFill = (driver.find_element(by=By.XPATH, value='//*[@id="txtIdCitado"]')).send_keys("CA395990")
NameFill = (driver.find_element(by=By.XPATH, value='//*[@id="txtDesCitado"]')).send_keys("DAVID ARAUJO PEREIRA")
AcceptClick = driver.find_element(by=By.XPATH, value='//*[@id="btnEnviar"]')
driver.execute_script("arguments[0].scrollIntoView();", AcceptClick)
AcceptClick.click()
RequestAppointment = driver.find_element(by=By.XPATH, value='//*[@id="btnEnviar"]').click()

#'//*[@id="mainWindow"]/div/div/section/div[2]/form/div[1]/p/text()[1]'

Message_NoAppointment = driver.find_element(by=By.XPATH, value='//*[@id="mainWindow"]/div/div/section/div[2]/form/div[1]/p')

a = 0
if Message_NoAppointment.text is not "En este momento no hay citas disponibles.":
    a = 1
