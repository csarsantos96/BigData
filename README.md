# 🏈 NFL Team Pass Completions Visualization (2003–2023)

This project generates clean, professional line charts showing the number of completed passes per year (2003–2023) for each NFL team.

Each chart includes:
- ✅ The team's logo at the top
- ✅ Conference logo (AFC or NFC) in the bottom-left corner
- ✅ NFL logo in the bottom-right corner
- ✅ All logos placed outside the chart area for clean visualization
- ✅ Logos are automatically resized and the conference/NFL ones are slightly transparent

---

## 📊 Dataset

- `team_stats_2003_2023.csv`: Historical team-level stats from 2003 to 2023.
- `nfl_teams.csv`: Maps each team to its respective conference (AFC/NFC).

---

## 🖼️ Output

- All generated charts are saved in the `numeroPassePorAno` folder.
- Each file is named after the team: `Green_Bay_Packers_passes_por_ano.png`, etc.

---

## 🛠️ Requirements

Make sure you have Python 3.8+ and the following packages installed:

```bash
pip install pandas matplotlib seaborn pillow numpy
