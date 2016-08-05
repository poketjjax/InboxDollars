def login(driver):
	config = open('../InboxDollarsConfig/config.txt', 'r')
		
	credentials = config.read().splitlines()

	config.close()

	username = driver.find_element_by_id('loginname')
	username.send_keys(credentials[0])	

	password = driver.find_element_by_id('pwd')
	password.send_keys(credentials[1] + '\n')
