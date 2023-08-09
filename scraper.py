import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By

url = 'https://www.opentable.com/state-of-industry'

#Get DataFrame Set
dfs = pd.read_html(url)

#Get COUNTRY DataFrame and write to excel
df = dfs[0]
fileName = 'OpenTable/country.xlsx'
writer = pd.ExcelWriter(fileName, engine='openpyxl', mode='a', if_sheet_exists='overlay')
df.to_excel(writer, index=False)
#Close writer
writer.close()

#Create an object of the chrome webdriver
driver = webdriver.Chrome()
#Open selenium URL in chrome browser
driver.get('https://www.opentable.com/state-of-industry')

#Select STATE table using class value. ?!COULD CHANGE!?
select = Select(driver.find_element(By.CLASS_NAME, "x3G8ivweF9MW6w3zqa6N"))
select.select_by_value('states')
#Get state DataFrame and write to excel
dfs = pd.read_html(driver.page_source)
df = dfs[0]
fileName = 'OpenTable/state.xlsx'
writer = pd.ExcelWriter(fileName, engine='openpyxl', mode='a', if_sheet_exists='overlay')
df.to_excel(writer, index=False)
#Close writer
writer.close()

#Select CITY table using class value. ?!COULD CHANGE!?
select = Select(driver.find_element(By.CLASS_NAME, "x3G8ivweF9MW6w3zqa6N"))
select.select_by_value('cities')
#Get city table and write to excel file
dfs = pd.read_html(driver.page_source)
df = dfs[0]
fileName = 'OpenTable/city.xlsx'
writer = pd.ExcelWriter(fileName, engine='openpyxl', mode='a', if_sheet_exists='overlay')
df.to_excel(writer, index=False)
#Close writer
writer.close()

#Close browser
driver.close()


