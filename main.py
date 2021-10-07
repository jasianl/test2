import traceback
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import requests
import json
import sys
sys.path.append("/fake-useragent-master/fake_useragent")
from fake_useragent import UserAgent

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc
import os

from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url(
    "https://discord.com/api/webhooks/893910139030077490/RyxDhwx80TFw0WfYXugBtlUFhOYuDa67MIG7QFp5SnKTeOoPM1KwCKtgLDqSKG-rBXJX",
    adapter=RequestsWebhookAdapter())

from selenium.webdriver import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
desired_capabilities = capabilities

import concurrent.futures
import threading

import gc

invite = 'https://discord.gg/XDjNdNdG'  #
invite = 'https://discord.gg/334xGGKa'

emails = []
for line in open("emails.txt", "r"):
    if line not in open("used_emails.txt", "r"):
        emails.append(line)

password = os.environ.get('password')

first = open("first_names.txt", "r").readlines()
last = open("last_names.txt", "r").readlines()

users_agent = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36", "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36", "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36", "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"]


class Browser():

    def __init__(self, PROXY):
        print("Intializing a browser...")
        PROXY = PROXY.strip("\r\n")
        try:
            self.ua = UserAgent(use_cache_server=False, fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
        except Exception as e:
            print(f"USERAGENT FAILED TO GET FAKE AGENTS") # Error with library fake_useragents (does not work well with heroku)

            options = webdriver.ChromeOptions()
        try:
            options.headless = True
            options.addArguments("start-maximized")
            options.add_argument('--headless')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument('--proxy-server=%s' % PROXY)
            try:
                options.add_argument(f"--user-agent={self.ua.random}")
                print("random ua used")
            except:
                random_ua = random.choice(users_agent)
                options.add_argument(f"--user-agent={random_ua}")
                print(f"UA used: {random_ua}")
            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")

#             options.add_argument('--disable-gpu')
#             options.add_argument('--remote-debugging-port=9222')
#             options.add_argument('--proxy-server='+PROXY)
#             self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
        except Exception as e:
            print(f"Failed to initialize browser: {e}")
            
        self.driver = uc.Chrome(options=options)
        
        # self.driver = webdriver.Chrome(options=options)

    def _quit(self):
        print("Closing browser...")
        self.driver.quit()
        return

    def getLogs(self):
        return self.driver.get_log("performance")

    def invite(self, invitelink):
        try:
            self.driver.get(invitelink)
        except Exception as e:
            print(f"Failed to open url: {e}")
            self._quit()
            return
        pass

        captcha_not_complete = True
        refresh = 3

        while refresh > 0 and captcha_not_complete:
            refresh -= 1
            time.sleep(1)

            try:
                failed = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/section/div/button[1]/div'))
                )
                self._quit()
                print("Invite not found")
                return
            except:
                pass

            try:
                username = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[1]/div/input'))
                )
                user = str(random.choice(first).strip("\n") + " " + random.choice(last).strip("\n"))
                username.send_keys(user)
                print("Page loaded")
            except:
                print("Page did not load")
                self._quit()
                return

            try:
                checkbox = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[2]/label/input')
                checkbox.click()
            except:
#                 print("No checkbox")
                pass

            time.sleep(random.uniform(1.4, 3.7))

            try:
                submit = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[2]/button')
                submit.submit()
                print("Submitted")
            except:
                pass

            try:
                submit = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[3]/button')
                submit.submit()
                print("Submitted")
            except:
                pass

            time.sleep(1)

            LOGS = self.driver.get_log("performance")
            for entry in LOGS:
                try:
                    if "limited" in entry['message']:
                        # print("fuked up")
                        self.driver.quit()
                        print("Rate Limited")
                        return
                except:
                    pass

            # Some magic shit hcaptcha solver thing
            captcha_checkbox = '#checkbox'
            captcha_iframe = '[data-hcaptcha-response]'

            # REFRESH THE PAGE IF NOT LOADED IN 3 TRIES THEN GIVE IT 3 MORE TRIES
            # These tries represent the number of times the while loop checked for a checkbox
            tries = 4
            nocaptcha = True
            while tries > 0 and nocaptcha:
                tries -= 1
                print(f"Finding hcaptcha; Attempt #{4-tries}")

                time.sleep(random.uniform(2.3, 6.3))
#                 print("Trying to find captcha...")
                try:
                    self.driver.switch_to.frame(self.driver.find_element_by_css_selector(captcha_iframe))
                    print("Captcha found")
                    nocaptcha = False
                    captcha_not_complete = False
                except Exception as e:
                    # print(cPrint.yellow("Couldn't find captcha"))
                    pass
                    try:
                        time.sleep(random.uniform(1.82, 3.25))
                        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(captcha_iframe))
                    except Exception as e:
                        # print(print.yellow("Couldn't find captcha 2"))
                        pass

                try:
                    time.sleep(random.uniform(.35, .75))
                    self.driver.find_element_by_css_selector(captcha_checkbox).click()
                    time.sleep(random.uniform(.12, .23))
                    self.driver.switch_to.default_content()
                    time.sleep(random.uniform(1.3, 2.2))
                    nocaptcha = False
                    captcha_not_complete = False
                    print("Clicked captcha")
                except:
                    print("Captcha not found/couldn't be clicked")
                    pass

                try:
                    # IF CAPTCHA IS NOT SOLVABLE, QUIT
                    print("Checking solvability")
                    time.sleep(random.uniform(0.6, 1.2))
                    notdoable = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]')  # /html/body/div[5]
                except:
                    print("Solvable")
                    pass

            if captcha_not_complete:
                self.driver.refresh()
                print("Refreshing captcha...")

        if tries == 0:
            self._quit()
            return

        print("Checking for token")
        count = 3000
        notoken = True
        while notoken and count > 0:
            count -= 1
            time.sleep(0.01)
            LOGS = self.getLogs()
            for entry in LOGS:
                try:
                    if "token" in entry['message']:
                        print(entry['message'])
                        token = json.loads(entry['message'])['message']['params']['response']['payloadData']
                        token = json.loads(token)['d']['token']
                        print(f"Found token: [{token}]")
                        
                        webhook.send(f"{token}")
#                         print(token, type(token))
                        notoken = False
                        # self.driver.quit()
                except Exception as e:
                    notoken = False
                    print(f"Error while trying to find token: {e}")
                    pass
                
        try:
            try:
                phone = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[6]/div/div/div[1]/div[4]/div'))
                )
                print("Phone blocked")
                self._quit()
                return
            except:
                pass

            day = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[1]'))
            )
            day.click()
            actions = ActionChains(self.driver)
            actions.send_keys('23')
            actions.perform()

            year = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/form/div[2]/div[1]/div[3]/div/div/div/div/div[1]/div[1]')
            year.click()
            actions = ActionChains(self.driver)
            actions.send_keys('1989')
            actions.perform()

            month = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/form/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div[1]')
            month.click()
            actions = ActionChains(self.driver)
            actions.send_keys('9')
            actions.perform()
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            submit = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[5]/div[2]/div/div/div/form/button')
            submit.click()

            time.sleep(1)

            # Email
            email_entry = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/div[2]/form/div[1]/div/input')
            email = emails.pop(0)
            email_entry.send_keys(email)
            f = open("used_emails.txt", "a")
            f.write(email + "\n")
            f.close()

            # Password
            password_entry = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/div[2]/form/div[2]/div/input')
            password_entry.send_keys(password)

            time.sleep(1)

            submit2 = self.driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/div[2]/form/button')
            submit2.click()
               
            print(f"Email created for token -> {token}")
            time.sleep(1)

            self.driver.quit()
            return


        except Exception as e:
            print(e)


def get_proxies():
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=all")
    proxies = r.content.decode().split("\r\n")
    return proxies


def checkProxy(proxy):
    try:
        r = requests.get(invite, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'}, timeout=4)
        if r.status_code == 200:
#             print(r.text)
            return proxy
    except Exception as e:
#         print(e)
        pass

    return None

def run(proxy):
    try:
        if checkProxy(proxy) != None:
            browser = Browser(proxy)
            browser.invite(invite)
#             time.sleep(1)
            if browser:
                browser._quit()
            time.sleep(5)
    except Exception as e:
        print("Error while trying to create account")
        print(e)
        print(traceback.format_exc())
        pass
    return


proxies = get_proxies()
proxies = []
# for p in open("proxies.txt", "r"):
#     proxies.append(p.strip("\r\n"))
while True:
    if len(proxies) == 0:
        proxies = get_proxies()
        print("Refreshing proxies")
    if threading.activeCount() <= 1:
#         print(len(gc.get_objects()))
#         print(threading.activeCount())
        proxy = random.choice(proxies)
        proxies.remove(proxy)
        thread = threading.Thread(target=run, args=(proxy,))
        thread.start()
