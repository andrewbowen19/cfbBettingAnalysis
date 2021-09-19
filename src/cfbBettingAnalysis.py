# Script to generate historical gambling performance of college football teams
# Will use to determine whether or not Alabama football since 2009-2010 has been a safer bet than the US Economy
 

import pandas as pd
import numpy as np
import os


class cfbBettingAnalysis(object):
    '''
    Generates historical betting performance report for college football teams.
    Currently set up to scrape data and calculate for Alabama betting results
    
    params:
        team - str (default = Alabama); team name desired. First letter should be capitalized
        season - int or str (default 2020); college football season desired
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
        Scrapes sports-reference.com for a team's game-by-game results in a given year
        
        parameters:
            season - int (default 2020); season desired for a team
            
        returns:
            df - pandas.DataFrame object; includes game-by-game results for a given teeam and season
        """
        
#    https://www.sports-reference.com/cfb/schools/alabama/2020-schedule.html#schedule
        team_code = self.team.lower()
        print(team_code, season)
        url = f"https://www.sports-reference.com/cfb/schools/{team_code}/{season}-schedule.html#schedule"
        df = pd.read_html(url)[1]
        print(df)
        
        return df
        
    def calculateTeamPayouts(self):
        """
        Calculates payouts for a given team's pre-season odds
        Adds payouts to the classes preseason_odds attribute
        
        returns:
            df - pandas DataFrame object; includes a team's success
            self.preseason_odds - class attribute with columns added for championship result, payout and rates of return (on $100 bet per year)
        """
        self.preseason_odds['Pre-season Odds'] = self.preseason_odds['Pre-season Odds'].str.replace("+", '')
        self.preseason_odds['Pre-season Odds'] = self.preseason_odds['Pre-season Odds'].str.replace("-", '')
        
        payouts = []
        ror = []
        
#        Calculating payouts for each season based on a $100 bet
        for i in self.preseason_odds['Pre-season Odds']:
            p, r = self.calculatePayout(int(i), 100)
            payouts.append(p)
            ror.append(r)
    
#        Adding Payout mertics to odds dataframe
        self.preseason_odds['Payout'] = payouts
        self.preseason_odds['ROR'] = ror
        self.preseason_odds['ROR %'] = self.preseason_odds['ROR'].astype(int) * 100
        
#        Adding boolean series for championship results
        self.preseason_odds['Won Championship?'] = self.getChampionshipYears(self.preseason_odds.index)
        
#        True RORs & Payout -- only will get payout in seasons they actually win the Natty
        won_chip = self.preseason_odds['Won Championship?']==True
        self.preseason_odds['True Payout'] = np.where(won_chip, self.preseason_odds['Payout'], 0)
        self.preseason_odds['True ROR'] = np.where(won_chip, self.preseason_odds['ROR'], 0)
        self.preseason_odds['True ROR %'] = np.where(won_chip, self.preseason_odds['ROR %'], 0)

        print(self.preseason_odds)
        
        df = self.preseason_odds.loc[self.bama_championship_years]
        print(f'{self.team} Championship years & odds: ')
        print(df)
        
        return df, self.preseason_odds
        
    def getReturns(self, desired_years):
        '''
        Calculates net returns for consisten $100 bets on collegiate futures
        
        paramters:
            desired_years - list; year range for which returns should be calculated
            
        returns:
            principal - int, amount wagered in total (default 100 * # of desired_years
            winnings - int; return, amount paid back to "investor" on their principal
            r - float; rate of return as a %. Defined as (100 * winnings/principal)
        '''
        
        print('Calculating returns....')
    
#        Grabbing only years where Saban is coach -- Alabama analysis
        df = self.preseason_odds.loc[desired_years[0]: desired_years[1]]
        print(df)
        
        print('---------------------------------')
#        Calculating net rate of return
        principal = 100 * len(df)
        winnings = np.sum(df['True Payout'])
        r = round(100 * (winnings / principal), 2)
        
        print(f'Principal {principal}')
        print(f'Total won back {winnings}')
        print(f'Return on Investment: {r}%')
        
        return principal, winnings, r

if __name__=="__main__":
    c = cfbBettingAnalysis()
    c.getFutureOdds()
    dat, ps_odds = c.calculateTeamPayouts()
    print('#################################')



