# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# site1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site1.get('https://www.phptravels.net/')
# time.sleep(5)
# site1.find_element(By.ID, 'hotels').click()
# time.sleep(5)
# site1.quit()
#
# site2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site2.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(5)
# site2.find_element(By.ID, 'continents').send_keys('Europe')
# time.sleep(5)
# site2.quit()
#
# site3 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site3.get('https://the-internet.herokuapp.com/')
# time.sleep(5)
# site3.find_element(By.ID, 'content').click()
# time.sleep(5)
# site3.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# site_link1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_link1.get('https://www.phptravels.net/')
# time.sleep(5)
# site_link1.find_element(By.LINK_TEXT, 'Company').click()
# time.sleep(3)
# site_link1.quit()
#
# site_link2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_link2.get('https://the-internet.herokuapp.com/')
# time.sleep(4)
# site_link2.find_element(By.LINK_TEXT, 'Context Menu').click()
# time.sleep(7)
# site_link2.quit()
#
# site_link3 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_link3.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(3)
# site_link3.find_element(By.LINK_TEXT, 'Java Tutorial').click()
# time.sleep(8)
# site_link3.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# site_tag1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_tag1.get('https://www.phptravels.net/')
# time.sleep(4)
# site_tag1.find_elements(By.TAG_NAME, 'button')
# lista_buttons = site_tag1.find_elements(By.TAG_NAME, 'button')
# lista_buttons[5].click()
# time.sleep(6)
# lista_labels = site_tag1.find_elements(By.TAG_NAME, 'label')
# lista_labels[6].click()
# time.sleep(8)
# site_tag1.quit()

# site_tag2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_tag2.get('https://the-internet.herokuapp.com/')
# site_tag2.find_elements(By.TAG_NAME, 'title')
# lista_title = site_tag2.find_elements(By.TAG_NAME, 'title')
# lista_title[0].get_attribute("Title")
# time.sleep(8)
# site_tag2.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# site_partial_text1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_partial_text1.get('https://the-internet.herokuapp.com/')
# time.sleep(4)
# site_partial_text1.find_element(By.PARTIAL_LINK_TEXT, 'Entry').click()
# time.sleep(4)
# site_partial_text1.quit()
#
# site_partial_text2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_partial_text2.get('https://the-internet.herokuapp.com/')
# time.sleep(4)
# site_partial_text2.find_element(By.PARTIAL_LINK_TEXT, 'Authentication').click()
# time.sleep(4)
# site_partial_text2.quit()
#
# site_partial_text3 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_partial_text3.get('https://the-internet.herokuapp.com/')
# time.sleep(4)
# site_partial_text3.find_element(By.PARTIAL_LINK_TEXT, 'Shifting ').click()
# time.sleep(4)
# site_partial_text3.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# site_name1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_name1.get('https://the-internet.herokuapp.com/')
# time.sleep(2)
# site_name1.find_element(By.NAME, 'viewport')
# site_name1.quit()
#
# site_name2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_name2.get('https://www.phptravels.net/')
# time.sleep(2)
# site_name2.find_element(By.NAME, 'checkin').click()
# time.sleep(3)
# site_name2.quit()
#
# site_name3 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_name3.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(3)
# site_name3.find_element(By.NAME, 'profession').click()
# time.sleep(6)
# site_name3.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# site_class1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_class1.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(3)
# site_class1.find_elements(By.CLASS_NAME, 'control-group')
# lista_class1 = site_class1.find_elements(By.CLASS_NAME, 'control-group')
# lista_class1[5].click()
# time.sleep(6)
# site_class1.quit()
#
# site_class2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_class2.get('https://www.phptravels.net/')
# time.sleep(2)
# site_class2.find_elements(By.CLASS_NAME, 'label-text')
# lista_class2 = site_class2.find_elements(By.CLASS_NAME, 'label-text')
# lista_class2[3].click()
# time.sleep(5)
# site_class2.quit()
#
# site_class1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_class1.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(5)
# lista_class1 = site_class1.find_elements(By.CLASS_NAME, 'dropbtn')
# lista_class1[6].click()
# time.sleep(6)
# site_class1.quit()

#CSS
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# site1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site1.get('https://www.phptravels.net/')
# time.sleep(5)
# site1.find_element(By.CSS_SELECTOR, '#hotels').click()
# time.sleep(5)
# site1.quit()
#
# site_css1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_css1.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(5)
# site_css1.find_elements(By.CSS_SELECTOR, '.dropbtn')[7].click()
# time.sleep(6)
# site_css1.quit()
#
# site_css2 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# site_css2.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(5)
# site_css2.find_element(By.CSS_SELECTOR, 'div > div [name="firstname"]').send_keys('Simona')
# time.sleep(5)
# site_css2.quit()

# site_css2.find_element(By.CSS_SELECTOR, 'div > div:nth-of-type(1) input').send_keys('Simona')


# XPath

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# atribut = valoare
site_xpath = webdriver.Chrome(executable_path=ChromeDriverManager().install())
site_xpath.get('https://www.phptravels.net/')
time.sleep(5)
site_xpath.find_element(By.XPATH, '//*[@id="hotels"]').click()
time.sleep(3)
site_xpath.find_element(By.XPATH, '//*[@id="flights-tab"]').click()
time.sleep(4)
site_xpath.find_element(By.XPATH, '//*[@id="tours-tab"]').click()
time.sleep(4)


# text dupa element
site_xpath.find_element(By.XPATH, '//strong[text()= "Rendezvous Hotels"]')
time.sleep(5)
site_xpath.find_element(By.XPATH, '//a[text()= "View More"]')
time.sleep(5)
site_xpath.find_element(By.XPATH, '//h4[text()= "Secure Payments"]')
time.sleep(3)


# partial text
site_xpath.find_element(By.XPATH, '//*[contains(@id,"fli")]').click()
time.sleep(5)

# cu SAU, folosind pipe |
site_xpath.find_element(By.XPATH, '//*[@id="tours-tabs"] | //*[@id="tours-tab"]').click()
time.sleep(3)

# cu *
site_xpath.find_element(By.XPATH, '//*[@id="visa-tab"]').click()
time.sleep(5)

# în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]
site_xpath1 = webdriver.Chrome(executable_path=ChromeDriverManager().install())
site_xpath1.get('https://www.techlistic.com/p/selenium-practice-form.html')
site_xpath1.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]//input').send_keys('Jessy')

# în care să folosești parent::
site_xpath.find_element(By.XPATH, '//a[text()= "View More"]/parent::div')
time.sleep(3)

# în care să folosești fratele anterior sau de după (la alegere)
site_xpath.find_element(By.XPATH, '//*[@id="Tab"]/li[2]//following-sibling::li').click()
time.sleep(3)
site_xpath.quit()

# o funcție prin care să pot alege eu prin parametru cu ce element vreau să interacționez
from selenium.webdriver.support.select import Select
continents = Select(site_xpath1.find_element(By.XPATH, '//*[@id="continents"]'))
time.sleep(5)
continents.select_by_visible_text('Europe')
time.sleep(6)
site_xpath1.quit()



# years_of_experience = Select(chrome.find_element(By.XPATH,"//*[@id='select-menu']"))
# time.sleep(2)
# years_of_experience.select_by_visible_text("5-9")