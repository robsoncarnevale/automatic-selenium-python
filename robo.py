from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
import subprocess
#import pyautogui

navegador = webdriver.Chrome(executable_path=r'./chromedeiver.exe')

navegador.get('https://github.com/')
sleep(2)

navegador.find_element('xpath', '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a').click()
sleep(3)

navegador.find_element('xpath', '//*[@id="login_field"]').send_keys("email")
sleep(1)

navegador.find_element('xpath', '//*[@id="password"]').send_keys("password")
sleep(1)

navegador.find_element('xpath', '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]').click()
sleep(1)

""" DENTRO DA PAGINA """

navegador.find_element('xpath', '/html/body/div[1]/div[5]/div/aside/div/loading-context/div/div[1]/div/ul/li[5]/div/div/a').click()
sleep(2)

navegador.find_element('xpath', '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary').click()
sleep(2)

navegador.find_element('xpath', '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/tab-container/div[2]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy').click()
sleep(2)

""" ABRIR PROMPT """
os.system("start cmd")

""" cmd = "ping -c 3 8.8.8.8"
os.system(cmd) """
""" 
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("rccimini@gmail.com")
sleep(2)

navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("11964529085")
sleep(2)

navegador.find_element('xpath', '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/tab-container/div[2]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy').click()
sleep(5)


 """
