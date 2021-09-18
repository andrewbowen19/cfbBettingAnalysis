# Script to generate historical gambling performance of college football teams
# Will use to determine whether or not Alabama football since 2009-2010 has been a safer bet than the US Economy
 

import pandas as pd
import numpy as np
import os


class cfbBettingAnalysis(object):
    '''
    Generates historical betting performance report for college football
    '''

    def __init__(self, team='Alabama', season='All'):
        self.team = team
        self.season = season
        self.bama_championship_years = [2020, 2017, 2015, 2012, 2011, 2009] # Should really make this for the team

    def getFutureOdds(self):
        '''
        Grabs national championship pre-season future odds for desired team
        Scrapes data from https://www.sportsoddshistory.com
        
        returns:
            preseason_odds - pandas.DataFrame obect; columns are ["Year", "Preseason Odds"
        '''
        print(f'Grabbing pre-season national championship odds for {self.team}...')
#        https://www.sportsoddshistory.com/cfb-team/?Team=Alabama&sa=cfb
        url = f"https://www.sportsoddshistory.com/cfb-team/?Team={self.team}&sa=cfb"
        df = pd.read_html(url)[1]

#        Grabbing and re-formatting only pre-season odds
        self.preseason_odds = df[[0,1]]
        self.preseason_odds = self.preseason_odds.drop(df.index[-2::], axis=0)
        self.preseason_odds.columns = ['Year', 'Pre-season Odds']
        self.preseason_odds.index = self.preseason_odds['Year'].astype(int)
            
        return self.preseason_odds
    
    def getChampionshipYears(self, years):
        '''
        Gets championship seasons for a team and returns boolean series with year as index
        '''
        year_results = []
        for y in years:
            if y in self.bama_championship_years:
                year_results.append(True)
            else:
                year_results.append(False)
#        self.preseason_odds['Won Championship?'] = year_results
        
        return pd.Series(year_results, index=years)
        
    
    def calculatePayout(self, moneyline_odds, bet=100):
        '''
        Calculates moneyline payoff from a bet amount
        
        parameters:
            moneyline_odds: str or int; american-format odds (moneyline) odds for a team
            bet: int (default 100); amount of money wagered
            
        returns:
            payoff - int; payoff of bet
            ror - rate of return of the bet (bet / payoff)
        '''

        if moneyline_odds > 0:
            payoff = 100 * int(moneyline_odds) / bet
            
#        If team is favored (won't happen for preseason odds mostly)
        elif moneyline_odds < 0:
            payoff = 100 * (bet / abs(moneyline_odds))
        ror = payoff / bet
            
        return payoff, ror

    def scrapeResults(self, season=2020):
        """
        Scrapes sports-reference.com for a team's results in a given year
        """
        
#    https://www.sports-reference.com/cfb/schools/alabama/2020-schedule.html#schedule
        team_code = self.team.lower()
        print(team_code, season)
        url = f"https://www.sports-reference.com/cfb/schools/{team_code}/{season}-schedule.html#schedule"
        df = pd.read_html(url)[1]
        print(df)
        
    def calculateTeamPayouts(self):
        """
        Calculates payouts for a given team's pre-season odds
        """
        self.preseason_odds['Pre-season Odds'] = self.preseason_odds['Pre-season Odds'].str.replace("+", '')
        self.preseason_odds['Pre-season Odds'] = self.preseason_odds['Pre-season Odds'].str.replace("-", '')
        
        payouts = []
        ror = []
        
#        Calculating payouts for each season based on a $100 bet
        for i in self.preseason_odds['Pre-season Odds']:
            print('Odd', i)
            p, r = self.calculatePayout(int(i), 100)
            payouts.append(p)
            ror.append(r)
    
#        Adding Payout mertics to odds dataframe
        self.preseason_odds['Payout'] = payouts
        self.preseason_odds['ROR'] = ror
        self.preseason_odds['ROR %'] = self.preseason_odds['ROR'].astype(int) * 100
        
#        Adding boolean series for championship results
        self.preseason_odds['Won Championship?'] = self.getChampionshipYears(self.preseason_odds.index)

        print(self.preseason_odds)
        
        df = self.preseason_odds.loc[self.bama_championship_years]
        print(f'{self.team} Championship years & odds: ')
        print(df)
        

if __name__=="__main__":
    c = cfbBettingAnalysis()
    c.getFutureOdds()
    c.calculateTeamPayouts()
    print('#################################')

    


