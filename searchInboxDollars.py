#!/usr/bin/env python
import time
from selenium import webdriver
import loginToInboxDollars
from random import randint
import searcher

driver = webdriver.Firefox()
driver.get("http://www.inboxdollars.com/")

loginToInboxDollars.login(driver)

time.sleep(3)

driver.get("http://www.inboxdollars.com/search")

time.sleep(3)

dailyLimitOfSearches = 70
numberOfSearchesToday = 0

while numberOfSearchesToday < dailyLimitOfSearches:
	searcher.sendSearch(driver)
	
	time.sleep(randint(300,1200))
	
	numberOfSearchesToday += 1
	
driver.quit()


