import randomWord
from random import randint

def getRandomSearchPhrase():
	counter = 0
	numberOfWords = randint(1,6)
	searchPhrase = ''
	
	while counter < numberOfWords:
		searchPhrase += randomWord.getRandomWord() + " "		
		counter += 1
		
	return searchPhrase


def sendSearch(driver):
	searchPhrase = getRandomSearchPhrase()
	
	try: 
		searchBox = driver.find_element_by_id('SearchKeywords')		
	except:
		searchBox = driver.find_element_by_id('SearchKeywords2')
		
	searchBox.clear()
		
	searchBox.send_keys(searchPhrase + '\n')	
