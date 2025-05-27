import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

statsNFL = pd.read_csv('team_stats_2003_2023.csv')

columnYear = 'year'
columnTurnovers = 'turnovers'
columnFirstDown = 'first_down'
columnTeam = 'team'

# --- Top 5 times com mais Turnovers ---
top5_turnovers = statsNFL.groupby(columnTeam)[columnTurnovers].sum().sort_values(ascending=False).head(5).index.tolist()
df_turnovers = statsNFL[statsNFL[columnTeam].isin(top5_turnovers)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_turnovers, x=columnYear, y=columnTurnovers, hue=columnTeam, palette="Set1")
plt.title("Mais de Turnovers sofridos por Ano (Top 5 Times)")
plt.xlabel("Ano")
plt.ylabel("Total de Turnovers")
plt.legend(title="Time", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("turnovers.png")
plt.show()

# --- Top 5 times com mais First Downs ---
top5_firstdowns = statsNFL.groupby(columnTeam)[columnFirstDown].sum().sort_values(ascending=False).head(5).index.tolist()
df_firstdowns = statsNFL[statsNFL[columnTeam].isin(top5_firstdowns)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_firstdowns, x=columnYear, y=columnFirstDown, hue=columnTeam, palette="Set2")
plt.title("Mais de First Downs por Ano (Top 5 Times)")
plt.xlabel("Ano")
plt.ylabel("Total de First Downs")
plt.legend(title="Time", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("firstDowns.png")
plt.show()
