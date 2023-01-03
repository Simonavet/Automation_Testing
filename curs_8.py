# Automatizare
'''
LOCATORS in Selenium Python: => folositi pentru a identifica elementele dintr-o pagina HTML
1. ID
2. Name
3. Class Name
4. Tag Name
5. Link Text
6. Partial Link Text
7. CSS Selector
8. XPath
'''

# ce este intre semnele "<>" in html se numec tag-uri
# h - uri = heather, h1 e obligatoriu pe toate paginile web si e unic, daca nu este inseamna ca e o eroare de developer
# cu gri - atribute
# cu portocaliu - valori ale atributelor

# ID
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path='C:\Users\40741\Downloads\chromedriver_win32')

# chrome_page = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
# # chrome_page = webdriver.Chrome() # chrome este clasa din pachetul Selenium
# chrome_page.get('https://the-internet.herokuapp.com/login') # accessarea paginii web
#
# chrome_page.find_element(By.ID, 'username').send_keys('Ramona') # accesam elementul nostru dupa selectorul ID si
#                                                                 # scrie 'Ramona' in field-ul username de pe site-ul nostru
# time.sleep(3) # scriem cate secunde vrem sa stea deschisa pagina in functie de nevoie
# chrome_page.find_element(By.ID, 'password').send_keys('secret')
# time.sleep(3)
#
# #Tag
# chrome_page.find_element(By.TAG_NAME, 'button').click()
# time.sleep(3)
#
# #Link_text
# chrome_page.find_element(By.LINK_TEXT, 'Elemental Selenium').click()
# time.sleep(5)
#
# chrome_page.quit() # inchide toata instanta browserului
# chrome_page.close() # inchide un singur tab, cel activ din instanta de browser

# este de preferat sa inchidem cu totul pe care il punem la sfarsit dupa ce am terminat testarea
# "#username" - cu aceasta comanda putem gasi in cod unde este un ID pe care il cautam
# id este unic si in pagina html se acceseaza cu "#"
# clasele se acceseaza cu "."
# tag-urile cu "<"
# ancora - in inspect html se noteaza cu "a"
# cand cautam dupa nume din webpage copiem nu scriem de mana

# Din notite de curs:
# chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# chrome.get("https://the-internet.herokuapp.com/")
# time.sleep(5)
# chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
# time.sleep(5)
# lista_inputuri = chrome.find_elements(By.TAG_NAME, "input")
# time.sleep(5)
# lista_inputuri[0].send_keys('tomsmith')
# lista_inputuri[1].send_keys("SuperSecretPassword!")
# time.sleep(5)
# chrome.quit()

test = chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
test.get('https://the-internet.herokuapp.com/login')
# test.find_element(By.TAG_NAME, 'form')
# time.sleep(2)
# test.quit()

#CSS_Selector
# inlantuire de tag-uri ex: form >div [type = 'text'] - identificam un element dupa valoare
test.find_element(By.CSS_SELECTOR, "form >div [type='text']").send_keys('dan')
time.sleep(5)
# daca scriem in paranteze patrate putem gasi un atribut ex: type, action, etc - cele cu portocaliu
# cu semnul > putem cauta primul copil direct
# cu spatiu intre element putem gasi toti copii atat directi cat si indirecti ex: form div
#identificam un element in mod unic: form >div:nth-of-type(1) sau si mai precis/adanc in text form >div:nth-of-type(2) input
test.find_element(By.CSS_SELECTOR, "form >div [type='text']").clear()
test.find_element(By.CSS_SELECTOR, "form >div [type='text']").send_keys(Keys.CONTROL + 'a')
test.find_element(By.CSS_SELECTOR, "form >div:nth-of-type(1) input").send_keys('adela')
test.find_element(By.CSS_SELECTOR, "form >div:nth-of-type(2) input").send_keys('adela')
time.sleep(5)

test.find_element(By.CSS_SELECTOR, "form>div:last-of-type input").send_keys('secret')
time.sleep(5)
test.find_element(By.CSS_SELECTOR, "form>div:first-of-type input").send_keys('455')
time.sleep(3)

# din notite de curs
# chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Anton")
# # am facut cautare dupa id
# chrome.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Anton")
# time.sleep(2)
# chrome.find_element(By.CSS_SELECTOR,"#last-name").clear()
# time.sleep(2)
# # am facut cautare dupa atribut = valoare
# chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Pann")
# time.sleep(2)



# Partial link
# ca si link taxt, dar pe o bucata de text
# chrome_page.find_element(By.LINK_TEXT, 'Elemental').click()
# time.sleep(5)

# test.quit()

# Class
# test.find_element(By.CLASS_NAME, "radius").click()
# time.sleep(5)
# test.quit()

#Daca avem o clasa care contine spatiu, de fapt avem doua clase.
#Cand facem cautare dupa class name, vom face cautare ori dupa una ori dupa cealalta, niciodata dupa ambele

test.find_element(By.CLASS_NAME, "class='large-12'")
time.sleep(4)
test.quit()
# test.find_element(By.CLASS_NAME,"class='columns'")

# Name
chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.get("http://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME,"name").send_keys("Cezar")
time.sleep(1)
lista_emails = chrome.find_elements(By.NAME,"email")
lista_emails[1].send_keys("cezarsopterean@gmail.com")
time.sleep(1)
chrome.find_element(By.NAME,"telephone").send_keys("0756891258")
time.sleep(1)
chrome.find_element(By.NAME,"country").send_keys("Romania")
time.sleep(1)
chrome.find_element(By.NAME,"company").send_keys("itfactory")
time.sleep(1)
chrome.find_element(By.NAME,"message").send_keys("mesaj text pentru submit formular")
time.sleep(1)
chrome.find_element(By.LINK_TEXT,"Submit").click()
time.sleep(1)
chrome.quit()