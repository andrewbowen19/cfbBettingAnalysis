# Script to get financial candlestick data and average return of bluechip stocks/index funds
# Want to compare this to the return on Alabama national championship futures since Nick Saban became coach

import pandas as pd
import os


api_key = os.environ['FINNHUB_KEY']

class getFinancialData(object):
    '''
    Class to pull financial candlestick data for different blue-chip stocks/index funds
    '''
    
    

