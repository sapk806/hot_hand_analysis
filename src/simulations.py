import pandas as pd
import numpy as np

def monte_carlo_simulation(n, seed, fgperc, fga):
    outcomes = [0, 1]
    probabilities = [1-fgperc, fgperc]
    rng = np.random.default_rng(seed=seed)
    simulation = rng.choice(outcomes, p=probabilities, replace=True, size=(n, fga))
    return simulation

def calculate_simulated_streaks(simulation):
    largest_streaks = np.zeros(shape=simulation.shape[0])
    current_streaks = np.zeros(shape=simulation.shape[0])
    fg_atm_after_3 = np.zeros(shape=simulation.shape[0])
    fg_made_after_3 = np.zeros(shape=simulation.shape[0])

    for col in range(simulation.shape[1]):
        fg_atm_after_3 = np.where(current_streaks >= 3, fg_atm_after_3 + 1, fg_atm_after_3)
        fg_made_after_3 = np.where((current_streaks >= 3) & (simulation[:, col] == 1), fg_made_after_3 + 1, fg_made_after_3)
        current_streaks = np.where((simulation[:, col] == 1), current_streaks + 1, current_streaks - current_streaks)
        largest_streaks = np.where(current_streaks > largest_streaks, current_streaks, largest_streaks)
        
    fgp_after_3 = fg_made_after_3 / fg_atm_after_3

    return largest_streaks, fgp_after_3

def create_df(simulation, longest_streaks, fgp_after_3):
    df = pd.DataFrame(index=range(simulation.shape[0]))
    df["Longest Streak"] = longest_streaks
    df["FG% After 3 Makes"] = fgp_after_3
    return df

