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
        self.bluechips = ['AAPL', 'AMZN', 'MSFT', 'GOOG', 'JNJ']
        
        
    def getStockData(self,symbol='AAPL'):
        '''
        Grabs data for a specific index
        '''
        
        finnhub_client = finnhub.Client(api_key="c17ck1f48v6se55vrra0")
        f = finnhub_client.stock_candles(self.symbol, 'M', self.start_date, self.end_date)
        
        print(f'{self.symbol} Opening Price:', f['o'][0])
        print(f'{self.symbol} Closing Price:', f['c'][-1])
        
        time_return = f['c'][-1] - f['o'][0]
        print(time_return)
        return_rate = time_return / f['o'][0]

        return time_return, return_rate
        
        
    def bluechipData(self, stocks):
        '''
        Gets data for blue chip stock symbols desired
        
        params:
            stocks: array-like; ticker symbols of stocks (typically) blue chips desired
        
        returns:
            pandas.DataFrame object containing return rates for each bluechip stock desired
        
        '''
        return_rates = {}
        for b in self.bluechips:
            tr, rr = self.getStockData(b)
                
            
            print(f'Time return: {tr}')
            print(f'Return Rate: {rr}')
            return_rate[b] = rr
            print('-------------------------------')
            
        return pd.DataFrame(return_rates)
    
    
if __name__=="__main__":
    bluechips = ['AAPL', 'AMZN', 'MSFT', 'GOOG', 'JNJ']
    g = getFinancialData()
    start_sp = 1430.73
    end_sp = 4432.99
    r = (end_sp - start_sp) / start_sp
    print(r)
    print(r / 14)
#Start S&P: 1430.73
#END S&P: 4432.99
