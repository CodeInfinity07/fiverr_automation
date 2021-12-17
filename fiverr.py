#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:38:07 2021

@author: ryzon
"""
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import subprocess
    import time
    import os
    import pygame
    import undetected_chromedriver.v2 as uc
    from plyer.utils import platform
    from plyer import notification

except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

class Fiverr:
    @staticmethod
    def init_driver(browser_name):
        '''init the driver'''
        def set_properties(browser_option):
            '''sets the driver's properties'''
            browser_option.add_argument('--disable-extensions')
            browser_option.add_argument('--headless')
            browser_option.add_argument('--start-maximized')
            browser_option.add_argument('--disable-gpu')
            browser_option.add_argument('--log-level=3')
            browser_option.add_argument('--disable-notifications')
            browser_option.add_argument('--disable-popup-blocking')
            return browser_option
        try:
            browser_name = browser_name.strip().title()


            #automating and opening URL in headless browser
            if browser_name.lower() == "chrome":
                browser_option = ChromeOptions()
                browser_option = set_properties(browser_option)
                driver = webdriver.Chrome(ChromeDriverManager().install(),options=browser_option)
            elif browser_name.lower() == "firefox":
                browser_option = FirefoxOptions()
                browser_option = set_properties(browser_option)
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=browser_option)
            else:
                driver = "Browser Not Supported!"
            return driver
        except Exception as ex:
            print(ex)

def check(myfile, s):
    with open(myfile) as f:
        if s in f.read():
            return True
        else:
            return False

def write(myfile, s):
    with open(myfile, 'a') as the_file:
        the_file.write(s+'\n')


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('beep-15.wav')
sound2 = pygame.mixer.Sound('beep-15.wav')
sound.set_volume(0.5)
options = uc.ChromeOptions()
f_browser = uc.Chrome(options=options)
f_browser.get("https://www.fiverr.com/login")
time.sleep(5)
email=f_browser.find_element_by_xpath('//*[@id="login"]')
em = "zainriaz950"
for character in em:
    email.send_keys(character)
    time.sleep(0.2)
password=f_browser.find_element_by_xpath('//*[@id="password"]')
ps = "ZAINzain@2"
for character in ps:
    password.send_keys(character)
    time.sleep(0.2)
password.send_keys(Keys.RETURN)
time.sleep(2)
file = "requests.txt"

while True:
    f_browser.get('https://www.fiverr.com/users/zainriaz950/requests')
    time.sleep(3)
    rows = f_browser.find_elements_by_xpath("//table/tbody/tr//td[3]//span")
    print(len(rows))
    if len(rows) > 0:
        for r in rows:
            try:
                print("Checking")
                request = r.get_attribute('innerHTML')
                print(request)
                if check(file, request):
                    print("Request Present")
                else:
                    notification.notify(
                       title='Fiverr Request',
                       message=request,
                       app_name='Here is the application name',
                       app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
                      )
                    sound.play()
                    write(file, request)
                    subprocess.Popen(['notify-send', request])
            except:
                pass

    elif len(rows) == 0:
        pass



    time.sleep(5)

f_browser.quit()
