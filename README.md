# College Football Betting Analysis
Repository for testing the hypothesis: "Is Nick Saban and Alabama football a safer investment than the US Economy?"

Nicholas Lou Saban Jr. | The U.S. Economy
:------------:|:------------------:
![](/img/the_croatian_atm.png?raw=true) |  ![](/img/index_funds_graph.png?raw=true).

Is betting on Alabama every week (spread or moneyline) a better investment than [the stock market](https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/s-p-500-returns-to-halve-in-coming-decade-8211-goldman-sachs-59439981) or an [index fund](https://www.businessinsider.com/personal-finance/average-stock-market-return)?

Historical betting lines were scraped from [Sports Odds History](https://www.sportsoddshistory.com/cfb-team/?Team=Alabama&sa=cfb#nc) via pandas read_html methods. Financial data was pulled from [Finnhub](https://finnhub.io) via a free API key. 

## The Results

Turns out, betting on the Crimson Tide to win a national championship yearly is a pretty safe bet. Nick Saban was hired as [Alabama football's](https://en.wikipedia.org/wiki/Alabama_Crimson_Tide_football) 27th head coach on January 3rd, 2007. Since then, he has gone on to win 6 national titles with the team (2009, 2011, 2012, 2015, 2017, 2020). Using American-style ("moneyline") odds, the Tide have not been listed as +1000 (10-to-1 odds) or worse to win the national championship in the pre-season.

We assumed a $100 bet per year using the lines scraped from [Sports Odds History](https://www.sportsoddshistory.com/cfb-team/?Team=Alabama&sa=cfb#nc). In years where Alabama **does not** win the title, a 'True Payout' of -$100 is tallied. In years in which Alabama does win the national championship, the true payout is determined as `100 * odds / bet`, where odds are the moneyline odds listed and bet is the amount bet (assumed to be $100). The constant 100 is to ensure the rate of payout is correct. This can also be determined using the `calculatePayout` method included in the `cfbBettingAnalysis` module/script.

    rate of return = payoff / amount bet
    where amount bet = $100
    
    
### Comparing to Index Fund Returns
Assuming an average index fund return rate of [~15%](https://www.investopedia.com/ask/answers/042415/what-average-annual-return-sp-500.asp), Saban outperforms the market consistently. While he does not win the national championship [every year](https://www.sports-reference.com/cfb/schools/louisiana-state/2019.html), his continued run of championships has made his performance return positive gains over the past 14 years. 

#### Alabama's Performance and Odds under Saban
Year | Pre-season Odds |  Payout | Rate of Return | ROR % | Won Championship? | True Payout | True ROR | True ROR %                                         :---:|:---:| :---:|:---:| :---:|:---:| :---:|:---:| :---:                     
2020 | +300  | 300.0   |3.00  |  300   |  True   |      300.0    |   3.0   |     300
2019 |  +250 |  250.0  | 2.50 |   200  |  False |       -100.0  |    -1.0|        -100
2018 | +175  | 175.0  | 1.75  |  100   |  False |      -100.0   |   -1.0 |       -100
2017 | +250  | 250.0  | 2.50  |  200   |  True   |      250.0    |   2.5   |       200
2016 | +600  | 600.0  | 6.00  |  600   |  False |      -100.0   |   -1.0 |       -100
2015 | +700  | 700.0  | 7.00  |  700   |  True  |      700.0     |  7.0   |      700
2014 | +450  | 450.0  | 4.50  |  400   |  False |      -100.0   |   -1.0 |       -100
2013 | +275  | 275.0  | 2.75  |  200   |  False |      -100.0   |   -1.0  |      -100
2012 | +550  | 550.0  | 5.50  |  500   |  True  |      550.0     |  5.5     |    500
2011 | +600  | 600.0  | 6.00  |  600   |  True   |     600.0     |  6.0     |    600
2010 | +400  | 400.0  | 4.00  |  400   |  False  |     -100.0   |   -1.0  |      -100
2009 | +1200 | 1200.0|  12.00 |  1200|True   |    1200.0    |  12.0  |      1200
2008 | +6000  |6000.0 | 60.00 |  6000|False |      -100.0   |   -1.0  |      -100
2007 | +7500  |7500.0  |75.00 |  7500| False |      -100.0  |    -1.0  |      -100

**Average Returns** |
:--------------------:|:-:
Avg Principal  | 100.0
Avg Winnings | 200.0
Avg Return Rate | 200.0%

---
## Installation
All dependencies used in the development environment can be found in the `requirements.txt` file. In order to install use the command:

    pip install --r requirements.txt
    
Note that it is recommended to use a [python virtual enviroment](https://docs.python.org/3/library/venv.html) for the above dependencies.

## Running the code

To pull this code to your local machine run the following from the command line:

    git clone https://github.com/andrewbowen19/cfbBettingAnalysis.git

In order to grab the historical returns for betting on Alabama after installation, run the following from the command line in the `src` directory:

    python cfbBettingAnalysis.py
    
This script will output to the screen data on hypothetically dollar-cost averaging 

For grabbing desired financial market data, run the following command:

    python getFinancialData.py
    
The `getFinancialData.py` script is still under development to allow for comparison of Alabama's dominance to other securities!

## TODO:

- [ ] Incorporate index fund api call (I don't want to pay for Finnhub)
- [ ] Allow command line arguments for other CFB teams ([argparse](https://docs.python.org/3/library/argparse.html))
- [ ] Improve method and class documentation.

---
### Disclaimer
*It should be noted that this repository does not offer any sound (or reasonable) investment advice. Please do not actually use any of the information presented here to inform your investment strategy (or god forbid your retirement savings). I'm really just a dummy with a GitHub and too much free time, not a financial advisor or fiduciary.



