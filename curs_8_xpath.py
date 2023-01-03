# XPATH
# toate elementele de la root si pana la elementul selectat
import time
# //*[@id="username"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
test = chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
test.get('https://the-internet.herokuapp.com/login')
time.sleep(2)
# test.find_element(By.XPATH, '//*[@id="username"]').send_keys('hello')
# // = select curent note
# * (select all) tine locul unui tag cum ar fi: name, input, div, form, img precedat de structura atribut=valoare
# @ = select atribute name cand avem nevoie de val unui atribut
# Xpath=//tagname[@attribute='value']
# in loc de //*[@type="text"] se poate si asa //input[@type="text"]
# time.sleep(3)
# test.find_element(By.XPATH, '//input[@type="password"]').send_keys('abcd')
# time.sleep(3)

# keyword 'contain' pt xpath
# test.find_element(By.XPATH, "//input[contains(@name,'pas')]").send_keys('1234')
# time.sleep(3)
# xpath dupa text
# test.find_element(By.XPATH, '//i[text()= " Login"]').click()
# time.sleep(3)

#:: parinte = cand vrem sa navigam in sus catre parinte
# are structura //select_item/parent::tag
# //i[text()= " Login"]/parent::button - cand de la element vrem sa ajungem la parinte
#parent e keyword
# navigarea din parinte in copil se face cu /
#navigarea catre un urmas care nu e urmas direct se face cu //
#navigare in sens invers, la frate anterior =  /preceding-sibling::tag ex: //*[@id="username"]//preceding-sibling::label
#navigare la urmatorul frate =  /following-sibling::tag

test.find_element(By.XPATH, '//form[@name="login"]/div[1]//input').send_keys('123')
time.sleep(4)

test.quit()