from selenium import webdriver
import config

uid = config.username
pwd = config.password
branch = input("Branch Code :    ")
text= input("ID :   ")
year = input("Year Code :   ")
chromedriver = "C:/Users/Chinmay/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit")

usr_box= driver.find_element_by_xpath("//input[@name='uid']")
usr_box.send_keys(uid)

pwd_box = driver.find_element_by_xpath("//input[@name='pwd']")
pwd_box.send_keys(pwd)


captcha = driver.find_element_by_id("txtCaptcha").get_attribute("value")


add = driver.find_element_by_xpath("//input[@name='txtInput']")
add.send_keys(captcha)

button = driver.find_element_by_xpath("//input[@value='Login']")
button.click()

driver.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/aisMenu.php")

element = driver.find_element_by_link_text("View Grade")

driver.execute_script("arguments[0].href = 'https://hib.iiit-bh.ac.in/Hibiscus/Grades/stutransDet.php?sid=B{}1{}0{}'".format(branch,year,text),element)

grades = driver.find_element_by_link_text("View Grade")
grades.click()
try:
        test = driver.find_element_by_css_selector("body > div > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(3) > b")
        testcase = test.get_attribute("innerHTML")

        if(str(testcase) == "Grade NA"):
            namelink = driver.find_element_by_css_selector("body > div > table:nth-child(1) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2)")
            name = namelink.get_attribute("innerHTML")
            print( str(text) + " -----   "  + str(name)   +  "    :   "  + "NA")
            driver.back()
except:
  try:

        gplink= driver.find_element_by_css_selector("body > div > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(38) > td:nth-child(2) > font > b")
        gpa= gplink.get_attribute("innerHTML")
        namelink = driver.find_element_by_css_selector("body > div > table:nth-child(1) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2)")
        name = namelink.get_attribute("innerHTML")
        print( str(text) + " -----   "  + str(name)   +  "    :   "  + str(gpa))
        driver.back()
  except:
          gplink= driver.find_element_by_css_selector("body > div > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(37) > td:nth-child(2) > font > b")
          gpa= gplink.get_attribute("innerHTML")
          namelink = driver.find_element_by_css_selector("body > div > table:nth-child(1) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2)")
          name = namelink.get_attribute("innerHTML")
          print( str(text) + " -----   "  + str(name)   +  "    :   "  + str(gpa))
          driver.back()
