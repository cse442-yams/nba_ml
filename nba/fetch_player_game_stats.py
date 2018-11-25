import time

import pandas as pd
from nba_api.stats.endpoints import leaguegamelog


def save_players_gamelog():
    for yr in range(7, 19):
        season_str = "20{:02d}-{:02d}".format(yr, yr + 1)
        print("Fetching players game log for season {}".format(season_str))

        resp = leaguegamelog.LeagueGameLog(direction='DESC', season_all_time=season_str, player_or_team_abbreviation='P')
        players_gamelog: pd.DataFrame = resp.get_data_frames()[0]
        players_gamelog.to_csv('data/players_gamelog_{}.csv'.format(season_str))
        print("Wrote file, sleeping before next request...")
        time.sleep(2)



if __name__ == '__main__':
    # save_players_gamelog()
    pass
