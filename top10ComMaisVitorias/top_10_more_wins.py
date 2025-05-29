import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks")

statsNFL = pd.read_csv('../csv/team_stats_2003_2023.csv')

columnYear = 'year'
columnRaNking = 'wins'
columnTeam = 'team'

total_wins = statsNFL.groupby(columnTeam)[columnRaNking].sum().sort_values(ascending=False).reset_index()
print("\nTimes com mais vitórias entre 2003 e 2023: ")
print(total_wins.head(10))

plt.figure(figsize=(10, 6))
sns.barplot(data=total_wins.head(10), x=columnTeam, y=columnRaNking, palette="Blues_d")
plt.title("Top 10 Times com Mais Vitórias (2003–2023)")
plt.ylabel("Total de Vitórias")
plt.xlabel("Time")
plt.xticks(rotation=45, ha='right')

for bar in plt.gca().patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{int(height)}',
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig("top_10_vitorias.png")
plt.show()
