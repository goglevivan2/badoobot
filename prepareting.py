from selenium import webdriver
import time
import random
driver = webdriver.Firefox()
# вход на badoo выполняется пользователем
driver.get('https://badoo.com/ru/sngin/?f=top')
time.sleep(15)

resp = str(input("Are you logged?(y): "))
q = int(input("How many likes to put :) "))
if resp == 'y':
    while q != 0:
        btn_like = driver.find_element_by_css_selector('.js-profile-header-vote-yes')
        btn_like.click()
        print(':)')
        q = q -1
        time.sleep(random.randrange(1,3))# после каждого лайка ждём от одной до трёх секунд
else:
    driver.quit()

driver.quit()