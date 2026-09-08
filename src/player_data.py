import pandas as pd
import numpy as np

def clean_data():
    stats = pd.read_csv("data/raw/NBA_2024_Shots.csv")
    stats = stats.loc[stats["PLAYER_NAME"] == "Luka Doncic"]
    stats = stats[["ACTION_TYPE", "SHOT_MADE"]]
    shot_stats = stats.loc[stats["ACTION_TYPE"].str.contains("Jump Shot", case=False, na=False) & ~stats["ACTION_TYPE"].str.contains("Floating", case=False, na=False)]

    return shot_stats

def calculate_metrics(data):
    streaks = np.zeros(shape=(len(data), 1))

    shots = data["SHOT_MADE"]
    current = 0
    fga_after_3 = 0
    fgm_after_3 = 0
    for i in range(len(data)):
        if shots.iloc[i] and current >= 3:
            fga_after_3 += 1
            fgm_after_3 += 1
            current += 1
        elif shots.iloc[i]:
            current += 1
        elif not shots.iloc[i] and current >= 3:
            current = 0
            fga_after_3 += 1
        else:
            current = 0
        streaks[i] = current

    fgper_after_3 = fgm_after_3 / fga_after_3
    data["STREAKS"] = streaks
    longest_streak = max(streaks)

    data.to_csv("data/processed/player_shot_stats.csv", index=False)
    return data, fgper_after_3, longest_streak, fga_after_3, fgm_after_3