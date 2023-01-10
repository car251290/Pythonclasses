import requests from bs4
import beautifulsoup4



try: 
  url = 'https://webscraping.emmetts.dev'
  page = requests.get(url)

  soup = BeautifulSoup(page.content,'html.parser')
  print(soup.prettify())

except:
  print('there been an erro')

else:
  print("evrything is correct")