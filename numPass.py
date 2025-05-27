import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

def apply_transparency(img: Image.Image, alpha: float) -> Image.Image:
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    alpha_layer = img.split()[3].point(lambda p: int(p * alpha))
    img.putalpha(alpha_layer)
    return img

def load_and_resize(path, size, alpha=1.0):
    img = Image.open(path)
    img = img.convert("RGBA")
    if alpha < 1:
        img = apply_transparency(img, alpha)
    img = img.resize(size, Image.LANCZOS)
    return np.asarray(img)

statsNFL = pd.read_csv('team_stats_2003_2023.csv')
conferenceNFL = pd.read_csv("nfl_teams.csv")

columnYear = 'year'
passComplete = 'pass_cmp'
columnTeam = 'team'
conferenceTeam = 'team_conference'
teamInfoColumn = 'team_name'

logo_path = 'logos'
output_path = 'numeroPassePorAno'
os.makedirs(logo_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)

team_logo_map = {
    "Arizona Cardinals": "Cardinals", "Atlanta Falcons": "Falcons", "Baltimore Ravens": "Ravens",
    "Buffalo Bills": "Bills", "Carolina Panthers": "Panthers", "Chicago Bears": "Bears",
    "Cincinnati Bengals": "Bengals", "Cleveland Browns": "Browns", "Dallas Cowboys": "Cowboys",
    "Denver Broncos": "Broncos", "Detroit Lions": "Lions", "Green Bay Packers": "Packers",
    "Houston Texans": "Texans", "Indianapolis Colts": "Colts", "Jacksonville Jaguars": "Jaguars",
    "Kansas City Chiefs": "Chiefs", "Las Vegas Raiders": "Raiders", "Los Angeles Chargers": "Chargers",
    "Los Angeles Rams": "Rams", "Miami Dolphins": "Dolphins", "Minnesota Vikings": "Vikings",
    "New England Patriots": "Patriots", "New Orleans Saints": "Saints", "New York Giants": "Giants",
    "New York Jets": "Jets", "Philadelphia Eagles": "Eagles", "Pittsburgh Steelers": "Steelers",
    "San Francisco 49ers": "49ers", "Seattle Seahawks": "Seahawks", "Tampa Bay Buccaneers": "Buccaneers",
    "Tennessee Titans": "Titans", "Washington Commanders": "Commanders", "Washington Redskins": "Redskins",
    "Washington Football Team": "Football_Team", "St. Louis Rams": "St-Louis",
    "Oakland Raiders": "Oakland", "San Diego Chargers": "San-Diego"
}

statsNFL = statsNFL.merge(conferenceNFL[[teamInfoColumn, conferenceTeam]],
                          left_on=columnTeam, right_on=teamInfoColumn, how='left')

teams = statsNFL[columnTeam].unique()

for team in teams:
    team_data = statsNFL[statsNFL[columnTeam] == team].sort_values(by=columnYear)
    conference = team_data[conferenceTeam].iloc[0] if not team_data.empty else 'Desconhecida'

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=team_data, x=columnYear, y=passComplete, marker='o', ax=ax)
    ax.set_title(f'{team} ({conference}) - Passes Completos por Ano')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Passes Completos')
    ax.tick_params(axis='x', rotation=45)

    logo_name = team_logo_map.get(team, team.replace(' ', '_'))
    team_logo_file = os.path.join(logo_path, f"{logo_name}.png")
    nfl_logo_file = os.path.join(logo_path, "NFL.png")
    conf_logo_file = os.path.join(logo_path, f"{conference}.png")

    if os.path.exists(team_logo_file):
        team_logo = load_and_resize(team_logo_file, (60, 60))
        fig.figimage(team_logo, xo=fig.bbox.xmax // 2 - 30, yo=fig.bbox.ymax - 50, zorder=10)

    if os.path.exists(conf_logo_file):
        conf_logo = load_and_resize(conf_logo_file, (80, 80), alpha=0.5)
        fig.figimage(conf_logo, xo=60, yo=10, zorder=10)

    if os.path.exists(nfl_logo_file):
        nfl_logo = load_and_resize(nfl_logo_file, (80, 80), alpha=0.5)
        fig.figimage(nfl_logo, xo=int(fig.bbox.xmax) - 140, yo=10, zorder=10)

    plt.tight_layout(rect=[0, 0.1, 1, 0.9])  # deixa espaço para as logos fora do gráfico
    plt.savefig(f"{output_path}/{team.replace(' ', '_')}_passes_por_ano.png")
    plt.close()
