import traceback
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import requests
import json
from fake_useragent import UserAgent

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url(
    "https://discord.com/api/webhooks/895131312120295454/Jnf8vKrN6_bswb-PoJFAbqOc7J0KUVqESsyB_oysDMJByrzTKgXzM3eVinb-E35u9RQo",
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


class Browser():

    def __init__(self, PROXY):
        print(PROXY)
        try:
            self.ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
        except Exception as e:
            print(f"SOME USERAGENT BS: {e}")

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--proxy-server=%s' % PROXY)
        options.add_argument(f"--user-agent={self.ua.random}")
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

        # self.driver = webdriver.Chrome(options=options)

    def _quit(self):
        print("closing")
        self.driver.quit()
        return

    def getLogs(self):
        return self.driver.get_log("performance")

    def invite(self, invitelink):
        try:
            self.driver.get(invitelink)
        except Exception as e:
            print(e)
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
            except:
                print("Page did not load")
                self._quit()
                return

            try:
                checkbox = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[2]/label/input')
                checkbox.click()
            except:
                print("no checkbox")
                pass

            time.sleep(random.uniform(1.4, 3.7))

            try:
                submit = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[2]/button')
                submit.submit()
            except:
                pass

            try:
                submit = self.driver.find_element_by_xpath(
                    '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div[2]/div[3]/button')
                submit.submit()
            except:
                pass

            time.sleep(1)

            LOGS = self.driver.get_log("performance")
            for entry in LOGS:
                try:
                    if "limited" in entry['message']:
                        # print("fuked up")
                        self.driver.quit()
                        return
                except:
                    pass

            # Some magic shit hcaptcha solver thing
            captcha_checkbox = '#checkbox'
            captcha_iframe = '[data-hcaptcha-response]'

            # REFRESH THE PAGE IF NOT LOADED IN 3 TRIES THEN GIVE IT 3 MORE TRIES

            tries = 4
            nocaptcha = True
            while tries > 0 and nocaptcha:
                print(tries)
                tries -= 1

                time.sleep(random.uniform(2.3, 6.3))
                print("Trying to find captcha")
                try:
                    self.driver.switch_to.frame(self.driver.find_element_by_css_selector(captcha_iframe))
                    print("captcha found")
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
                    print("solved i think")
                except:
                    pass

                try:
                    # IF CAPTCHA IS NOT SOLVABLE, QUIT
                    print("checking solvability")
                    time.sleep(random.uniform(0.6, 1.2))
                    notdoable = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]')  # /html/body/div[5]
                except:
                    print("solvable")
                    pass

            if captcha_not_complete:
                self.driver.refresh()
                print("Refreshing captcha...")

        if tries == 0:
            self._quit()
            return

        print("checking for token")
        count = 100000
        notoken = True
        while notoken and count > 0:
            count -= 1
            time.sleep(0.01)
            LOGS = self.getLogs()
            for entry in LOGS:
                try:
                    if "token" in entry['message']:
                        print("found token")
                        print(entry['message'])
                        token = json.loads(entry['message'])['message']['params']['response']['payloadData']
                        token = json.loads(token)['d']['token']
                        #                         webhook.send(f"{token}")
                        print(token, type(token))
                        notoken = False
                        # self.driver.quit()
                except Exception as e:
                    notoken = False
                    print('what happened')
                    print(e)
                    pass
        print("reached1")
        try:
            print("reached2")

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

            time.sleep(1)

            self.driver.quit()
            return


        except Exception as e:
            print(e)


def get_proxies():
    r = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=3000&country=US&ssl=all&anonymity=all")
    proxies = r.content.decode().split("\r\n")
    return proxies


def checkProxy(proxy):
    try:
        print(proxy)
        r = requests.get('https://discord.gg/eS4qmCVM', proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'},
                         timeout=2)
        if r.status_code == 200:
            print(r.text)
            return proxy
    except Exception as e:
        print(e)
        pass

    return None


# if __name__ == "__main__":
#     # accounts = get_accounts()
#     proxies = get_proxies()
#
#     try:
#         while True:
#             proxy = random.choice(proxies)
#             while checkProxy(proxy) == None:
#                 proxy = random.choice(proxies)
#
#             browser = Browser(proxy)
#             browser.invite("https://discord.gg/eS4qmCVM")
#             time.sleep(1)
#             browser._quit()
#             time.sleep(5)
#     except Exception as e:
#         print("Error while trying to create account")
#         print(e)
#         print(traceback.format_exc())

def run(proxy):
    # print("100")
    try:
        if checkProxy(proxy) != None:
            browser = Browser(proxy)
            browser.invite(invite)
            time.sleep(1)
            browser._quit()
            time.sleep(5)
    except Exception as e:
        print("Error while trying to create account")
        print(e)
        print(traceback.format_exc())
        pass


proxies = get_proxies()
proxies = []
# for p in open("proxies.txt", "r"):
#     proxies.append(p.strip("\r\n"))
while True:
    if len(proxies) == 0:
        proxies = get_proxies()
        print("Refreshing proxies")
    if threading.activeCount() <= 1:
        print(len(gc.get_objects()))

        print(threading.activeCount())
        proxy = random.choice(proxies)
        proxies.remove(proxy)
        print(proxy)
        thread = threading.Thread(target=run, args=(proxy,))
        thread.start()
