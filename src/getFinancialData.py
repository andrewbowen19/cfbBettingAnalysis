# Script to get financial candlestick data and average return of bluechip stocks/index funds
# Want to compare this to the return on Alabama national championship futures since Nick Saban became coach

import pandas as pd
import os
import finnhub

api_key = os.environ['FINNHUB_KEY']

class getFinancialData(object):
    """
    Class to pull financial candlestick data for different blue-chip stocks/index funds
    
    params:
        symbol - str (default AAPL); stock symbol to pull data from  (can't do index funds)
        start_date - unix timestamp, int (default Jan 3rd, 2007); start date to search for stock data for
        end_date - 
    """
    def __init__(self, symbol="AAPL", start_date=1167803629,end_date=1618894464):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        
    def getIndexData(self):
        '''
        Grabs data for a specific index
        '''
        
        

        finnhub_client = finnhub.Client(api_key="c17ck1f48v6se55vrra0")
        f = finnhub_client.stock_candles(self.symbol, 'M', self.start_date, self.end_date)
        print(f)
        print(f.keys())
        print('--------------------------------')
        
        print('Opening Price:', f['o'][0])
        print('Closing Price:', f['c'][-1])
        
        time_return = f['c'][-1] - f['o'][0]
        print(time_return)
#        return
        
        

    
    
if __name__=="__main__":
    g = getFinancialData().getIndexData()
        
    
    

