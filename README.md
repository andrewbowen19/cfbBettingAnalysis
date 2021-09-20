# College Football BettingAnalysis
Repository for testing the hypothesis: "Is Nick Saban and Alabama a safer investment than the US Economy?"

![Nick Saban](/img/the_croatian_atm.png?raw=true) versus ![The U.S. Economy](/img/index_funds_graph.png?raw=true).

Is betting on Alabama every week (spread or moneyline) a better investment than [the stock market](https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/s-p-500-returns-to-halve-in-coming-decade-8211-goldman-sachs-59439981) or an [index fund](https://www.businessinsider.com/personal-finance/average-stock-market-return)?

Historical betting lines were scraped from [Sports Odds History](https://www.sportsoddshistory.com/cfb-team/?Team=Alabama&sa=cfb#nc) via pandas read_html methods. Financial data was pulled from [Finnhub](https://finnhub.io) via a free API key. 

---
## Installation
All dependencies used in the development environment can be found in the `requirements.txt` file. In order to install use the command:

    pip install --r requirements.txt
    
Note that it is recommended to use a [python virtual enviroment](https://docs.python.org/3/library/venv.html) for the above dependencies.

## Running the code

In order to grab the historical returns for betting on Alabama after installation, run the following from the command line in the `src` directory:

    python cfbBettingAnalysis.py
    
For grabbing desired financial market data, run the following command:

    python getFinancialData.py
    

## TODO:

- [ ] Incorporate index fund api call (I don't want to pay for Finnhub)
- [ ] Allow command line arguments for other CFB teams ([argparse](https://docs.python.org/3/library/argparse.html))
- [ ] Improve method and class documentation.

---
### Disclaimer
*It should be noted that this repository does not offer any sound (or reasonable) investment advice. Please do not actually use any of the information presented here to inform your investment strategy (or god forbid your retirement savings). I'm really just a dummy with a GitHub and too much free time, not a financial advisor or fiduciary.



