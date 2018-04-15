import requests 
from bs4 import BeautifulSoup
from urlparse import urljoin


#Detects a cycle in a list of url that have been visited.  
def detect_cycle(search_history):
	search_history_length = len(search_history)
	curr_index = 0 
	curr_item = search_history[curr_index]

	while curr_index != search_history_length - 1:
		curr_item = search_history[curr_index]
		iter_index = curr_index + 1
		while iter_index < search_history_length:
			if search_history[iter_index] == curr_item: 
				return True
			iter_index += 1
		curr_index += 1

	return False

#$Checks if the crawl is to continue
def continue_crawl(search_history, target_url, limit = 25):
	#returns False if the target url has been visited
    if search_history[(len(search_history) -1)] == target_url:
    	print "The target URL has been found"
        return False 
    #returns False if the search history has already reached a limit. 
    elif len(search_history) >= limit: 
    	print "The number of links traversed has reached the max limiy"
        return False
     #returns False if a cycle has been detected
    elif detect_cycle(search_history): 
    	print "A cycle was detected. Exiting traversal"
        return False
    #returns True
    else: 
        return True

#finds the first link in a html page
def find_first_link(start_url):
	response = requests.get(start_url)
	html = response.text 
	soup = BeautifulSoup(html, 'html.parser')
	first_link = ""

	#gets the content in the div mw-content-text with the class mw-parser-output
	content_div = soup.find(id = 'mw-content-text').find(class_ = 'mw-parser-output')

	#This loop finds all the paragraph in the content_dic
	for element in content_div.find_all('p', recursive=False): 
		#finds the first a tags in the paragraph if it exists
		if element.find('a', recursive = False):
			#Gets the value of the href tag in the first a tag
			first_link = element.find('a', recursive = False).get('href')
			#breaks from the loop as the first tag has been found
			break

	
	#constructs the complete link
	first_link = urljoin("https://en.wikipedia.org/", first_link)
	print first_link
	return first_link


#The start URL 
search_history = ["https://en.wikipedia.org/wiki/London"]
#The target URL 
target_url = "https://en.wikipedia.org/wiki/Quality_(philosophy)"
#as long as contibe_crawl coninues to return True, the code finds the first link of the last visited link. 
#If the retrieved link is the target url, the iteration stops. 
#Else the link is appened to the list of URLs visited
while continue_crawl(search_history, target_url):
	search_history.append(find_first_link(search_history[-1]))

