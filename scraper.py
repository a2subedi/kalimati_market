import time
import requests
import MySQLdb

from datetime import date

from bs4 import BeautifulSoup as bs
from config import host,user,passwd,database
from helpers import *


url = "https://kalimatimarket.gov.np/index.php/lang/en"

db = MySQLdb.connect(host,user,passwd,database) # Imported from config

then = time.time()
try:
    res = requests.get(url)
    # wait for page load and data transfer
    time.sleep(10)
    soup = bs(res.text,"html.parser")
    
    prices_table = soup.find('table',{'id':'commodityDailyPrice'})
    tbody = prices_table.find('tbody')
    rows = tbody.findAll('tr')
    # print(rows)
    # initialize empty strings for variables
    name = unit = min_rate = max_rate = avg_rate = rate_date = ''
    for row in rows:
        cols = row.findAll('td')
        name = cols[0].text.strip()
        unit = cols[1].text.strip()
        min_rate = int(cols[2].text.replace('Rs. ','').strip())
        max_rate = int(cols[3].text.replace('Rs. ','').strip())
        avg_rate = int(cols[4].text.replace('Rs. ','').strip())
        rate_date = date.today()

        c = db.cursor()
        # insert into commodity
        c.execute(insert_commodity.format(
            name, unit, max_rate, min_rate, avg_rate, rate_date))
        # create table commodity_name if not exists and then insert
        c.execute(create_stmt.format(name))
        c.execute(insert_item_date.format(
            name, max_rate, min_rate, avg_rate, rate_date))
        c.close()

except Exception as e:
    print(e)