import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('img', exist_ok=True)


nflStats = pd.read_csv ('../csv/team_stats_2003_2023.csv')


rushAtt = 'rush_att' # TENTATIVA DE CORRICA
rushYds = 'rush_yds' # CORRIDA POR JARDAS
rushTD = 'rush_td' # NUMERO DE TOUCH DOWN POR CORRIDA
rushYdsPerAtt ='rush_yds_per_att' # JARDAS DE CORRIDA POR TENTATIVA

passCmp = 'pass_cmp' # Passes completos
passAtt = 'pass_att' # Tentativas de passe
passYds = 'pass_yds' # Total de jardas ganha por passe
passTD = 'pass_td' # Passes de touchdown
passInt = 'pass_int' # Passes interceptados
passNYA = 'pass_net_yds_per_att' #  Jardas Líquidas por Tentativa de Passe
passFD = 'pass_fd' # PASSES PARA FIRTS DOWN

nflStats['rush_td_pct'] = nflStats[rushTD] / nflStats[rushAtt]
nflStats['pass_td_pct'] = nflStats[passTD] / nflStats[passAtt]

pivot_rush = nflStats.pivot(index='team', columns='year', values='rush_td_pct')
pivot_pass = nflStats.pivot(index='team', columns='year', values='pass_td_pct')


plt.figure(figsize = (18,12))
sns.heatmap(pivot_rush, cmap='YlGnBu', annot=True, fmt='.2%', linewidths=.5, cbar_kws={'label': '% TD por Corrida'})
plt.title('Heatmap de % de Touchdowns por Corrida (2003-2023)')
plt.xlabel('Ano')
plt.ylabel('Time')
plt.tight_layout()
plt.savefig('img/heatmap_rush_td_pcts.png')
plt.close()

plt.figure(figsize = (18,12))
sns.heatmap(pivot_rush, cmap='OrRd', annot=True, fmt='.2%', linewidths=.5, cbar_kws={'label': '%  TD por passe'})
plt.title('Heatmap de % de Touchdowns por Passe (2003-2023)')
plt.xlabel('Ano')
plt.ylabel('Time')
plt.tight_layout()
plt.savefig('img/heatmap_pass_td_pcts.png')
plt.close()
print(plt.colormaps())


# times que precisam correr menos para fazer o touchdown x times que precisam correr mais para fazer o touchdown

nflStats['rush_att_per_td'] = nflStats[rushAtt] / nflStats[rushTD]

rushDifficulty = nflStats.groupby('team')['rush_att_per_td'].mean().reset_index()

top5Dif = rushDifficulty.sort_values('rush_att_per_td', ascending=False).head(5)  # os piores
top5Eff = rushDifficulty.sort_values('rush_att_per_td', ascending=True).head(5)   # os melhores


top5Compare = pd.concat([
    top5Dif.assign(tipo='Mais tentativas de corridas'),

    top5Eff.assign(tipo='Mais eficientes nas corridas'),
])

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top5Compare,
    x='team',
    y='rush_att_per_td',
    hue='tipo',
    palette='Set2',
    dodge=True
)
plt.title('Top 5 Times - Corridas por Touchdown (2003–2023)')
plt.ylabel('Média de Tentativas por TD Correndo')
plt.xlabel('Time')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('img/top5_corridas_por_td_comparativo.png')
plt.show()


# times que precisam fazer menos pass para fazer o touchdown x times que precisam fazer mais para o touchdown

nflStats['pass_att_per_td'] = nflStats[passAtt] / nflStats[passTD]

passDifficulty = nflStats.groupby('team')['pass_att_per_td'].mean().reset_index()

top5DifPass = passDifficulty.sort_values('pass_att_per_td', ascending=False).head(5)  # os piores
top5EffPass = passDifficulty.sort_values('pass_att_per_td', ascending=True).head(5)   # os melhores


top5ComparePass = pd.concat([
    top5DifPass.assign(tipo='Mais tentativas de passes'),

    top5EffPass.assign(tipo='Mais eficientes nos passes'),
])

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top5ComparePass,
    x='team',
    y='pass_att_per_td',
    hue='tipo',
    palette='Set2',
    dodge=True
)
plt.title('Top 5 Times - Passes  por Touchdown (2003–2023)')
plt.ylabel('Média de Tentativas de TD pr Passes')
plt.xlabel('Time')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('img/top5_passes_por_td_comparativo.png')
plt.show()