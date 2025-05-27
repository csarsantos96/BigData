import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Small multiple time series

statsNFL = pd.read_csv('team_stats_2003_2023.csv')

columnYear = 'year'
passYards = 'pass_yds'
passComplete = 'pass_cmp'
columnTeam = 'team'

teams = statsNFL[columnTeam].unique()

for team in teams:
    team_data = statsNFL[statsNFL[columnTeam] == team].sort_values(by=columnYear)
    plt.figure(figsize=(10, 4))
    sns.lineplot(data=team_data, x=columnYear, y=passComplete, marker='o')
    plt.title(f'{team} - Passes Completos por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Passes Completos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"numeroPassePorAno/{team.replace(' ', '_')}_passes_por_ano.png")
    plt.close()