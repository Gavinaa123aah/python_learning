#coding=utf-8
#webDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,sys




if __name__ == "__main__":

    arg_list = sys.argv[1].split('=')

    print arg_list[1]

if arg_list[1]=='chrome':
    chrome_options=Options()
    chrome_options.add_extension('')
    driver=webdriver.Chrome()
    
    driver = webdriver.Chrome("/Users/working_tool/chromedriver")
elif arg_list[1]=='firefox':
    driver = webdriver.Firefox(executable_path=r'/Users/jundongli-ext/Downloads/geckodriver')

    driver.get("http://mail.bjtu.edu.cn/")

    element_username = driver.find_element_by_id("uid")
    element_password = driver.find_element_by_id("password")
    element_loginbutton = driver.find_element_by_id("login_button")



    print driver.title
    print driver.name
    element_username.send_keys("14301066")
    time.sleep(0.1)
    element_password.send_keys("010915")
    time.sleep(0.4)
    element_loginbutton.click()
    print driver.title
    print driver.name

    time.sleep(2)
    driver.quit()