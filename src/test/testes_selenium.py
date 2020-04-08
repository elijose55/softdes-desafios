from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Victo\Downloads\chromedriver_win32\chromedriver.exe')
username = "admin"
password = "admin"
driver.get("http://" + username + ":" + password + "@localhost")
assert "localhost" in driver.current_url

upload_field = driver.find_element_by_xpath("//input[@type='file']")
submit = driver.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que deveria funcionar
path = r"C:\Users\victo\Documents\dev-aberto\aulas\06-projeto-desconhecido\codigo\src\desafio.py"
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
path = r"C:\Users\victo\Documents\dev-aberto\aulas\06-projeto-desconhecido\codigo\src\desafio_errado.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver.find_element_by_xpath("//tbody/tr[1]/td[3]")
print(ok_label.text)
assert ok_label.text == "Erro"


driver_firefox = webdriver.Firefox(executable_path=r'C:\Users\Victo\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
username = "admin"
password = "admin"
driver_firefox.get("http://" + username + ":" + password + "@localhost")
assert "localhost" in driver_firefox.current_url

upload_field = driver_firefox.find_element_by_xpath("//input[@type='file']")
submit = driver_firefox.find_element_by_xpath("//form/button[@class='btn btn-primary']")
#Testando arquivo que deveria funcionar
path = r"C:\Users\victo\Documents\dev-aberto\aulas\06-projeto-desconhecido\codigo\src\desafio.py"
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
path = r"C:\Users\victo\Documents\dev-aberto\aulas\06-projeto-desconhecido\codigo\src\desafio_errado.py"
upload_field.send_keys(path)
#Enviando
submit.submit()
#Procurando pelo ok
time.sleep(1)
ok_label = driver_firefox.find_element_by_xpath("//tbody/tr[1]/td[3]")
print(ok_label.text)
assert ok_label.text == "Erro"