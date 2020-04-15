from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os.path as path
import platform
import time

absolute_path = path.abspath(path.join(__file__ ,"../.."))

if platform.system() == 'Windows': 
	driver = webdriver.Chrome(executable_path=absolute_path + '/test/resources/ChromeDriver/chromedriver_win32/chromedriver.exe')
elif platform.system == 'Darwin':
	driver = webdriver.Chrome(executable_path=absolute_path + '/test/resources/ChromeDriver/chromedriver_mac64/chromedriver')
else:
	driver = webdriver.Chrome(executable_path=absolute_path + '/test/resources/ChromeDriver/chromedriver_linux64/chromedriver')


username = "pedro"
password = "pedro"
driver.get("http://" + username + ":" + password + "@localhost")
assert "localhost" in driver.current_url

upload_field = driver.find_element_by_xpath("//input[@type='file']")
submit = driver.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que deveria funcionar
path = absolute_path + "/src/desafio.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver.find_element_by_xpath("//tbody/tr[1]/td[3]")
assert ok_label.text == "OK!"

upload_field = driver.find_element_by_xpath("//input[@type='file']")
submit = driver.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que NAO deveria funcionar
path = absolute_path + "/src/desafio_errado.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver.find_element_by_xpath("//tbody/tr[1]/td[3]")
print(ok_label.text)
assert ok_label.text == "Erro"

if platform.system == 'Windows': 
	driver_firefox = webdriver.Firefox(executable_path=absolute_path + '/test/resources/GeckoDriver/geckodriver-v0.26.0-win64/geckodriver')
elif platform.system == 'Darwin':
	driver_firefox = webdriver.Firefox(executable_path=absolute_path + '/test/resources/GeckoDriver/geckodriver-v0.26.0-macos/geckodriver')
else:
	driver_firefox = webdriver.Firefox(executable_path=absolute_path + '/test/resources/GeckoDriver/geckodriver-v0.26.0-linux64/geckodriver')

username = "pedro"
password = "pedro"
driver_firefox.get("http://" + username + ":" + password + "@localhost")
assert "localhost" in driver_firefox.current_url

upload_field = driver_firefox.find_element_by_xpath("//input[@type='file']")
submit = driver_firefox.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que deveria funcionar
path = absolute_path + "/src/desafio.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver_firefox.find_element_by_xpath("//tbody/tr[1]/td[3]")
assert ok_label.text == "OK!"

upload_field = driver_firefox.find_element_by_xpath("//input[@type='file']")
submit = driver_firefox.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que NAO deveria funcionar
path = absolute_path + "/src/desafio_errado.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver_firefox.find_element_by_xpath("//tbody/tr[1]/td[3]")
print(ok_label.text)
assert ok_label.text == "Erro"
