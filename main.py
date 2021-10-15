import traceback
import gc
import time
import random
import requests
import json
import sys
import os
import zipfile
import threading
import undetected_chromedriver as uc
from discord import Webhook, RequestsWebhookAdapter

sys.path.append("/fake-useragent-master/fake_useragent")
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities
capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
desired_capabilities = capabilities



webhook = Webhook.from_url("https://discord.com/api/webhooks/898417514214723584/XWDGspn1pUmYvorMJPj6BIAb9xGoPstqxAKNEYhjK5fzCtvm6XrcMSrXmW8NyayDI4QU",adapter=RequestsWebhookAdapter())
INVITE = 'https://discord.com'
first = open("first_names.txt", "r").readlines()
last = open("last_names.txt", "r").readlines()
password = os.environ.get('password')

users_agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
       "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
       "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
       "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
       "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
       "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
       "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
]


class Browser():

    def __init__(self, PROXY):
        print("[...] Initializing browser")
        try:
            self.ua = UserAgent(use_cache_server=False)
        except Exception as e:
            print(f"useragent Error: {e}")

        options = webdriver.ChromeOptions()

        try:
            # options.add_extension(pluginfile) # PROXY SETTINGS
            options.headless = True
            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument('--proxy-server=%s' % PROXY)
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('--remote-debugging-port=9222')
            # options.add_argument('--proxy-server=' + proxy)
            # options.add_argument('--headless')

            try:
                options.add_argument(f"--user-agent={self.ua.random}")
                print("[%] ua.random generated random user agent")
            except:
                user_agent = random.choice(users_agent)
                options.add_argument(f"--user-agent={user_agent}")
                print(f"[%] Random user agent picked from user agent list{user_agent}")

        except Exception as e:
            print(f"[-] Failed to initialize browser: {e}")
            return

        # self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
        self.driver = uc.Chrome(options=options)
        # self.driver = webdriver.Chrome(options=options)
        print(f"[*] Browser initialized")


    def _quit(self):
        print("[...] Closing browser")
        self.driver.quit()
        return

    def getLogs(self):
        return self.driver.get_log("performance")

    def wait(self):
        time.sleep(random.uniform(0.87, 2.33))
        return

    def invite(self, invitelink):
        try:
            self.driver.get(invitelink)
        except Exception as e:
            print(f"[-] Failed to send request")
            self._quit()
            return
        pass

        captcha_not_complete = True
        refresh = 3

        while refresh > 0 and captcha_not_complete:
            refresh -= 1
            time.sleep(1)

            open_in_browser = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#app-mount > div > div > div.grid-3Ykf_K.heroBackground-3m0TRU > div.row-3wW-Fx.heroContainer-3j1eQg > div > div.ctaContainer-3vWJHU > button'))
            )
            self.wait()
            open_in_browser.click()
            username = self.driver.find_element_by_css_selector('#app-mount > div > div > div.grid-3Ykf_K.heroBackground-3m0TRU > div.row-3wW-Fx.heroContainer-3j1eQg > div > div.formContainer-1p5okg > form > input')
            user = str(random.choice(first).strip("\n") + " " + random.choice(last).strip("\n"))
            self.wait()
            username.send_keys(user)
            checkbox = self.driver.find_element_by_css_selector(
                '#app-mount > div > div > div.grid-3Ykf_K.heroBackground-3m0TRU > div.row-3wW-Fx.heroContainer-3j1eQg > div > div.formContainer-1p5okg > div > div > div')
            if checkbox:
                print(f"[!] Checkbox")
                checkbox.click()
            self.wait()
            button = self.driver.find_element_by_css_selector('#app-mount > div > div > div.grid-3Ykf_K.heroBackground-3m0TRU > div.row-3wW-Fx.heroContainer-3j1eQg > div > div.formContainer-1p5okg > form > button')
            self.wait()
            button.click()

            LOGS = self.driver.get_log("performance")
            # print(LOGS)
            for entry in LOGS:
                try:
                    if "limited" in entry['message']:
                        print(f"[-] Rate limited")
                        self._quit()
                        return
                except:
                    pass

            self.wait()

            # CAPTCHA SOLVER
            captcha_checkbox = '#checkbox'
            captcha_iframe = '[data-hcaptcha-response]'

            # REFRESH THE PAGE IF NOT LOADED IN 3 TRIES THEN GIVE IT 3 MORE TRIES
            tries = 4
            nocaptcha = True
            while tries > 0 and nocaptcha:
                tries -= 1
                print(f"Finding captcha Attempt #{4-tries}")

                time.sleep(random.uniform(2.3, 6.3))
                print("Trying to find captcha")
                try:
                    self.driver.switch_to.frame(self.driver.find_element_by_css_selector(captcha_iframe))
                    print("Captcha found")
                    nocaptcha = False
                    captcha_not_complete = False
                except Exception as e:
                    pass
                    try:
                        time.sleep(random.uniform(1.82, 3.25))
                        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(captcha_iframe))
                    except Exception as e:
                        pass

                try:
                    time.sleep(random.uniform(.35, .75))
                    self.driver.find_element_by_css_selector(captcha_checkbox).click()
                    time.sleep(random.uniform(.12, .23))
                    self.driver.switch_to.default_content()
                    time.sleep(random.uniform(1.3, 2.2))
                    nocaptcha = False
                    captcha_not_complete = False
                    print("[!] Captcha solved")
                except:
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
                        # print(entry['message'])
                        token = json.loads(entry['message'])['message']['params']['response']['payloadData']
                        token = json.loads(token)['d']['token']
                        print("[!] Found token")
                        print(f"[...] Sending token: {token}")
                        webhook.send(f"{token}")
                        notoken = False
                except Exception as e:
                    notoken = False
                    print(f"Error while receiving token: {e}")
                    pass

        if token:
            day = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#app-mount > div:nth-child(7) > div.layer-2KE1M9 > div > div > div.content-1KT39n.theme-light > div > div > div > form > div.container-3bTSed.formItem-B8CDn8 > div.inputs-14Hc7m > div:nth-child(2) > div > div > div > div > div.css-1hwfws3'))
            )
            day.click()
            actions = ActionChains(self.driver)
            actions.send_keys(str(random.randint(10, 28)))
            actions.perform()
            self.wait()
            year = self.driver.find_element_by_css_selector('#app-mount > div:nth-child(7) > div.layer-2KE1M9 > div > div > div.content-1KT39n.theme-light > div > div > div > form > div.container-3bTSed.formItem-B8CDn8 > div.inputs-14Hc7m > div:nth-child(3) > div > div > div > div > div.css-1hwfws3')
            year.click()
            actions = ActionChains(self.driver)
            actions.send_keys(str(random.randint(1980, 1990)))
            actions.perform()
            self.wait()
            month = self.driver.find_element_by_css_selector('#app-mount > div:nth-child(7) > div.layer-2KE1M9 > div > div > div.content-1KT39n.theme-light > div > div > div > form > div.container-3bTSed.formItem-B8CDn8 > div.inputs-14Hc7m > div:nth-child(1) > div > div > div > div > div.css-1hwfws3')
            month.click()
            actions = ActionChains(self.driver)
            actions.send_keys(str(random.randint(1, 12)))
            actions.perform()
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            self.wait()
            submit = self.driver.find_element_by_css_selector('#app-mount > div:nth-child(7) > div.layer-2KE1M9 > div > div > div.content-1KT39n.theme-light > div > div > div > form > div.footer-3_fPee > div > button')
            submit.click()
        else:
            print("[-] Token not found")
            return
        time.sleep(5)
        self._quit()
        return

def get_proxies():
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all")
    proxies = r.content.decode().split("\r\n")
    if r.status_code == 200:
        print(f"[%] Got {len(proxies)} proxies")
    return proxies


def checkProxy(proxy):
    try:
        r = requests.get(INVITE, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'}, timeout=4)
        if r.status_code == 200:
            print(f"[...] Using {proxy}")
            return proxy
    except Exception as e:
        print(f"proxyCheck Error: {e}")
        pass
    return None


def run(proxy):
    try:
        if checkProxy(proxy) != None:
            browser = Browser(proxy)
            browser.invite(INVITE)
            # time.sleep(5)
    except Exception as e:
        print("Error while trying to create account")
        print(e)
        print(traceback.format_exc())
        pass


proxies = []
for p in open("proxies.txt", "r"):
    proxies.append(p.strip("\r\n"))
while True:
    if len(proxies) == 0:
        print("Refreshing proxies")
        proxies = get_proxies()
    if threading.activeCount() <= 1:
        # print(len(gc.get_objects()))
        # print(threading.activeCount())
        proxy = random.choice(proxies)
        proxies.remove(proxy)
        thread = threading.Thread(target=run, args=(proxy,))
        thread.start()
