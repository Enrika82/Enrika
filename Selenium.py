from selenium import webdriver
driver = webdriver.Chrome(executable_path='\\vmware-host\Shared Folders\Downloads\chromedriver_win32')
driver.implicitly_wait(10)
driver.get("https://translate.google.co.il")

#current url will show the current url
#print("current URL: ", driver.current_url)
#title returns the tab title as shown in chrome
#print("title: ",driver.title)
#print(driver.page_source)


my_url = driver.current_url
#my_button = driver.find_element_by_class_name('active-result')
my_list = driver.find_element_by_id("source")
#x = my_list[1]
print(my_list)
my_xp = driver.find_element_by_xpath("//textarea[@id='source']")
print(my_xp)
my_list.click()
my_xp.click()

from selenium.webdriver.common.keys import Keys

click_elem = driver.find_element_by_xpath("//div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='source-wrap']/div[@class='input-full-height-wrapper tlid-input-full-height-wrapper']/div[@class='source-input']/div[@id='input-wrap']/textarea[@id='source']")
click_elem.click()

driver.find_element_by_id("source").send_keys("hello")
driver.find_element_by_id("source").send_keys(Keys.ENTER)
#driver.find_element_by_id("source").clear()

print(my_list.is_displayed())
print(my_list.is_enabled())
print(my_list.is_selected())

element_list = driver.find_elements_by_id("source")
print(len(element_list))
element_list[0].click()


#driver.close()
#driver.quit()