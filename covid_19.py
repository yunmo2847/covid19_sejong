#%%
from json.encoder import INFINITY
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import os
school1 = input('학교 입력:')
name1 = input('이름입력:')
birthday1 = input('생일 입력: ')
num = input('비밀번호 : ')
opt = Options()
opt.add_argument('--start-maximized')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension',False)



d = webdriver.Chrome('C:\Chromedriver\chromedriver.exe', options=opt)
d.maximize_window()
d.get("https://hcs.eduro.go.kr/#/loginHome")
a = d.find_element_by_id("btnConfirm2")
a.click()
s = d.find_element_by_id("schul_name_input")
s.click()
s1_select = d.find_element_by_id("sidolabel")
s1_select.click()
s1_select_ok = d.find_element_by_xpath("//option[@value='08']")
s1_select_ok.click()
s2_select = d.find_element_by_id("crseScCode")
s2_select.click()
s2_select_ok = d.find_element_by_xpath("//option[@value='3']")
s2_select_ok.click()
school_search = d.find_element_by_id("orgname")
school_search.send_keys(school1)
d.find_element_by_class_name("searchBtn").click()
time.sleep(1)
d.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
time.sleep(1)
d.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

username= d.find_element_by_xpath('//*[@id="user_name_input"]')
username.send_keys(name1)
birthday = d.find_element_by_id("birthday_input")
birthday.send_keys(birthday1)
time.sleep(1)
keybord = d.find_element_by_class_name("keyboard-icon")
keybord.click()
password= d.find_element_by_css_selector('[aria-label="0"]')


for i in num:
    time.sleep(1)
    password= d.find_element_by_css_selector(f"[aria-label='{i}']")
    password.click()
time.sleep(1)
password_c = d.find_element_by_id("btnConfirm")
password_c.click()
time.sleep(1)
k_yunmo = d.find_element_by_class_name("survey-button")
k_yunmo.click()
time.sleep(1)
ans = ["survey_q1a1","survey_q2a3","survey_q3a1"]
for i in ans:
    time.sleep(1)
    answer = d.find_element_by_id(i)
    answer.click()

submit= d.find_element_by_id("btnConfirm")
submit.click()

os.system("shutdown /t /s 1")
# %%
