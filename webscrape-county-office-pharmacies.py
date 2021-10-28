#import requests
#import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.countyoffice.org/md-prince-georges-county-pharmacy/')
load_btn = driver.find_element(By.CLASS_NAME,'loadmore')
load_btn.click()
load_btn = driver.find_element(By.CLASS_NAME,'loadmore')
load_btn.click()
load_btn = driver.find_element(By.CLASS_NAME,'loadmore')
load_btn.click()

namesOG = driver.find_elements(By.CLASS_NAME,'title')
addressesOG = driver.find_elements(By.CLASS_NAME,'subsidiary')

print(len(namesOG))

location_words = addressesOG[0].text.split(' ')
city = location_words[-2][:-1]

address = ""
for x in range(len(location_words) - 2):
	address += location_words[x] + ' '


total_string = ""

for x in range(len(namesOG)):
	name = (namesOG[x].text.strip())

	location_words = addressesOG[x].text.split(' ')
	city = location_words[-2][:-1]
	#####Does not split cities correctly if two word cities
	#####so I have to clean that by hand (not long)

	address = ""
	for x in range(len(location_words) - 2):
		address += location_words[x] + ' '

	total_string += name + "," + city + "," + address + "\n"

file = open('conty-office-pharamcies.csv','w')
file.write(total_string)
file.close()

if (driver!=None):
	driver.quit()


#response = requests.get('https://www.countyoffice.org/md-prince-georges-county-pharmacy/')
#print(response.text)

#soup = bs4.BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

#print(soup.title.string)

#namesOG = soup.findAll(attrs={'class' : 'title'})
#addressesOG = soup.findAll(attrs={'class' : 'subsidiary'})

#print(addressesOG[0].text.split('\n'))

#total_string = ""

# for x in range(len(namesOG)):
# 	name = (namesOG[x].text.strip())

# 	location = addressesOG[x].text.split('\n')
# 	address = location[2].strip()
# 	city = location[4].strip()[:-1]

# 	total_string += name + "," + city + "," + address + "\n"

# file = open('conty-office-pharamcies.csv','w')
# file.write(total_string)
# file.close()



