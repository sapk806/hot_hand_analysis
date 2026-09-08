# A Statistical Analysis of the "Hot Hand" Phenomenon in the NBA
This project uses a Monte Carlo simulation to simulate 10,000 seasons of shooting outcomes using NBA player Luka Doncic's 2024 NBA jump shot stats to investigate whether statistics support the existence of the "hot hand" phenomenon.

## Overview
This project investigates the existence of the "hot hand" in the NBA using player shot data from the 2024 NBA season. I analyze the field goal percentage of the player after having already made three consecutive shots, which we will define as any shot that is attempted after at least three previous consecutive makes. Using a hypothesis tests, the goal of this project is to determine whether the observed data is unusually high relative to a Monte Carlo simulation that assumes an independent, constant-probablity when determining the outcome of a shot. Under the null model, we would expect Luka Doncic's jump shot stats from the 2024 NBA season to be consistent with the independent and constant probability model used in the Monte Carlo simulation.

## Results
Luka Doncic, during the 2024 NBA season, shot 39.86% from the field after making three consecutive jump shots, the average simulated field goal percentage was 38.30%. The p-value for field goal percentage after making three consecutive shots was found to be ~0.367, which is over the significance level of 0.05. Because the p-value did not fall under the signifiance level, we fail to reject the null hypothesis, meaning Luka Doncic's 2024 NBA season jump shot stats are consistent with what we would expect if we followed a model with an independent, constant, probability. 

The longest streak of makes Luka Doncic had during the 2024 NBA season was 8, which puts him at the 77th percentile of simulated seasons. 

Wile Luka Doncic's 2024 NBA season shot stats do perform well compared to a model with a independent and constant probability, his season was not statistically significant when proving the existence of the "hot hand" phenomenon.

## Repository Structure
hot_hand_analysis/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── analysis.ipynb
├── README.md
└── requirements.txt

## Data
The data used is downloaded from Kaggle. The variables used in this project are the following: player_name, action_type, and shot_made_result. In this dataset, one observation represents a shot attempt by a player. 

 A limitation in this dataset to take note of is that the quarter in which a shot was taken is not included. 

Source: https://www.kaggle.com/datasets/mexwell/nba-shots?resource=download&select=NBA_2024_Shots.csv

Raw data is processed and cleaned, then saved to `data/processed`.

## Methods
The data is isolated to Luka Doncic's shots, with layups and floaters filtered out. Layups and floaters have different baseline probabilties, while the model used in this project assumes Luka Doncic's baseline probability of making a jump shot.

Once the data is cleaned, the longest streak of makes and the field goal percentage after three consecutive makes are calculated and recorded.

A Monte Carlo simulation consisting of 10,000 seasons using Luka Doncic's 2024 NBA season jump shot field goal percentage is simulated. Each season Luka Doncic is simulated to take as many jump shots as he did in the 2024 NBA season, and each shot uses an independent, constant-probability model. For each season the longest streak of makes and jump shot field goal percentage after three consecutive makes are calculated and recorded.

Under the null-model, the p-value represents how often simulated seasons produce a field goal percentage after three consecutive makes that is at least as high as Luka Doncic's during the NBA 2024 season. The p-value was calculated as a one-sided, upper-tail p-value because we are looking only to see if the observed field goal percentage is unusually high relative to the simulated distribution. In order to calculate this, the amount of simulated seasons that had a higher or equal jump shot field goal percentage after making three consecutive shots was divided by the number of simulted seasons. In the p-value calculation, the observed statistic is included as an additional value, which explains the +1 in the numerator and denominator of the p-value calculation.

## Technologies
- Python
- NumPy
- pandas
- Matplotlib
- Jupyter Notebook

## How to Run
1. Clone the repository
2. Download dependencies
3. Run the notebook (analysis.ipynb)

## Limitations
This project does not account for two main concepts: game context and interuptions, and changing behavior in offensive and defensive context. Different quarters, timeouts, and different games can disrupt a player's rhythm by having them out of play. Player behavior affects the quality of shots, which also has an effect on jump shot field goal percentage. Player's on defense may start to play more physical, a team might adjust its defensive scheme specifically for an offensive player, and every shot has a different difficulty based on distance, defense, and whether or not the shooter is in motion.

## Future Work
Future work could involve making the model aware of different games and different quarters, which are the longer game interruptions. In regards to changing behavior future work could account for the distance of each jump shot.