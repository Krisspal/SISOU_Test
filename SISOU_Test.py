import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import csv

driver = webdriver.Chrome()
driver.get("https://sis.ou.edu.vn/")

driver.find_element(By.CSS_SELECTOR, "button.login100-form-btn").click()

with open('login.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

(driver.find_element(By.NAME,'form-username')).send_keys(user)
(driver.find_element(By.NAME,'form-password')).send_keys(password)

driver.find_element(By.CLASS_NAME,'m-loginbox-submit-btn').click()

time.sleep(10)



diemtk10 = driver.find_element(By.ID, 'DTBTK')
diemtk4 = driver.find_element(By.ID, 'DTBTKH4')
diemrltk = driver.find_element(By.ID, 'DiemRLTK')

print("Diem TK he 10: " + diemtk10.text)
print("Diem TK he 4: " + diemtk4.text)
print("Diem Rl: " + diemrltk.text)

driver.quit()