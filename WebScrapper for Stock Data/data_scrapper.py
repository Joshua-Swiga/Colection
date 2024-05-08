import requests
from bs4 import BeautifulSoup
import sys
import csv

#Re-directing Output to prevent unicode error 
sys.stdout=open("Output1.txt", "w", encoding="utf-8")

url="https://www.investing.com/crypto/currencies/"

r=requests.get(url)

try:
    crypto_data=[ ]

    if r.status_code in range (200, 300):
        soup=BeautifulSoup(r.text, "lxml")
        
        #Collecting data from the website        
        titles=soup.find_all("button", class_="inv-button datatable_sort__GHCim") #Contains headings for each column

        currencies=soup.find_all("div", class_="crypto-coins-table_cellNameText__aaXmK") #Contains all the curenciess
        prices=soup.find_all("td", class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ text-secondary !text-sm crypto-coins-table_thirdMobileCell__f8EsE")
        Daily_changes=soup.find_all("td", class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--down___c4Fq !text-sm")
        Weekly_Changes=soup.find_all("td", class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--up__hIuZF !text-sm")
        market_capital= soup.find_all("td", class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ !text-sm")
        daily_vollume=soup.find_all("td", {'data-test': 'volume-cell'})
        #Total_volume=soup.find("td", class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ !text-sm", string=lambda x: '%' in x)


        #Creating a nested list of all the data scrapperd
        for currency, price, daily_change, weekly_change, cap, volume in zip(currencies, prices, Daily_changes, Weekly_Changes, market_capital, daily_vollume):
            crypto_data.append([currency.text, price.text, daily_change.text, weekly_change.text, cap.text, volume.text])        

        #Writting to the csv file
        try:

            with open("Collected_Data.csv", "w", newline="") as file:
                csv_writer=csv.writer(file)
                for item in crypto_data:
                    csv_writer.writerow(item)

        except UnicodeEncodeError as e:
            print(f"Error: {e}")

        print("First Batch Collected.")


except r.ConnectionError as e:
    print(f"Connection not established. Error type: {e}. Statuse code: {r.status_code}", sep="\n")