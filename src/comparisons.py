import pandas as pd

def fgp_p_value(simulated_fg, real_fg, n):
    return ((simulated_fg["FG% After 3 Makes"] >= real_fg).sum() + 1) / (n + 1)

def streak_percentiles(df, longest_real_streak):
    streaks = df["Longest Streak"]
    new = pd.Series(longest_real_streak)
    all_streaks = pd.concat([streaks, new], ignore_index=True).rank(pct=True)
    return all_streaks