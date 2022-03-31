import urllib.request
import json
from html.parser import HTMLParser
import xml.dom.minidom

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
import smtplib

def Send_Email():

    #Try to Connect
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
    except:
        print('Something went wrong connecting ...')
    gmail_user = 'crypto.services.enterprise@gmail.com'
    gmail_password = 'Alohomora2'

    sent_from = gmail_user
    to = ['david.araujo.pereira@gmail.com']
    subject = 'NIE AVAILABLE'
    body = 'NIE AVAILABLE :\nhttps://sede.administracionespublicas.gob.es/icpplustieb/citar?p=8&locale=es'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except Exception as e :
        print ('Something went wrong...',e)

#Operations to open browser and select NIE appointment
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(r'C:\Users\David Pereira\Documents\chromedriver_win32\chromedriver.exe',chrome_options=chrome_options)
driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/citar?p=8&locale=es")

time.sleep(2)

tramites_options = driver.find_element(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]')

#scroll to element
driver.execute_script("arguments[0].scrollIntoView();", tramites_options)
tramites = Select(driver.find_element(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]'))
tramites.select_by_value('4079')
accepttramite = driver.find_element(by=By.XPATH, value='//*[@id="btnAceptar"]')
actions = ActionChains(driver)
actions.move_to_element(accepttramite).perform()
time.sleep(1)
accepttramite.click()
time.sleep(1)

EnterBtn = driver.find_element(by=By.XPATH, value='//*[@id="btnEntrar"]')
driver.execute_script("arguments[0].scrollIntoView();", EnterBtn)
EnterBtn.click()

time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="rdbTipoDocPas"]').click() #SelectPassport
PassportFill = (driver.find_element(by=By.XPATH, value='//*[@id="txtIdCitado"]')).send_keys("CA395990")
NameFill = (driver.find_element(by=By.XPATH, value='//*[@id="txtDesCitado"]')).send_keys("DAVID ARAUJO PEREIRA")

AcceptClick = driver.find_element(by=By.XPATH, value='//*[@id="btnEnviar"]')
driver.execute_script("arguments[0].scrollIntoView();", AcceptClick)
AcceptClick.click()

time.sleep(1)
SendBtn = driver.find_element(by=By.XPATH, value='//*[@id="btnEnviar"]')
driver.execute_script("arguments[0].scrollIntoView();", SendBtn)
SendBtn.click()

time.sleep(1)
Message_NoAppointment = driver.find_element(by=By.XPATH, value='//*[@id="mainWindow"]/div/div/section/div[2]/form/div[1]/p')

appointment_not_available_text = "En este momento no hay citas disponibles"
if appointment_not_available_text in Message_NoAppointment.text:
    print("Appointment not available")
    Send_Email()
else:
    print("Available")
    Send_Email()
   

time.sleep(2)
driver.close()


