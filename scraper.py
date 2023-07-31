import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = 'https://www.opentable.com/state-of-industry'

#Get DataFrame
dfs = pd.read_html(url)

#Get first DataFrame
df = dfs[0]
df.to_excel('OpenTable/country.xlsx', index=False)

## create an object of the chrome webdriver
driver = webdriver.Chrome()
## open selenium URL in chrome browser
driver.get('https://www.opentable.com/state-of-industry')

#Switch to state table
select = Select(driver.find_element(By.CLASS_NAME, "x3G8ivweF9MW6w3zqa6N"))
select.select_by_value('states')
#Get state table data and write to excel
dfs = pd.read_html(driver.page_source)
df = dfs[0]
df.to_excel('OpenTable/state.xlsx', index=False)


#Switch to city table
select = Select(driver.find_element(By.CLASS_NAME, "x3G8ivweF9MW6w3zqa6N"))
select.select_by_value('cities')
#Get city table and write to excel file
dfs = pd.read_html(driver.page_source)
df = dfs[0]
df.to_excel('OpenTable/city.xlsx', index=False)

#close browser
driver.close()

