import time
import requests

from bs4 import BeautifulSoup as bs


url = "https://kalimatimarket.gov.np/index.php/lang/en"


then = time.time()
try:
    res = requests.get(url)
    # wait for page load and data transfer
    time.sleep(10)
    soup = bs(res.text,"html.parser")
    
    prices_table = soup.find('table',{'id':'commodityDailyPrice'})
    rows = prices_table.find('tbody').findAll 
    print(rows)

except Exception:
    pass