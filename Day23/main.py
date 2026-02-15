#combining objects with zip

names = ['Bulbasaur', 'Charmander', 'Squirtle']
hps = [45,39,44]

combined_zip = zip(names,hps)
combined_zip_list = [*combined_zip]
print(combined_zip_list)

#Counting with loop using Counter
poke_types = [
    "Normal", "Fire", "Water", "Grass", "Electric", "Ice", 
    "Fighting", "Poison", "Ground", "Flying", "Psychic", 
    "Bug", "Rock", "Ghost", "Dragon", "Steel", "Dark", "Fairy"
]
from collections import Counter
type_counts = Counter(poke_types)
print(type_counts)

#using itertools.combinations()
pokemon_types = ['Bug','Fire','Ghost','Grass','Water']
from itertools import combinations
combos_obj = combinations(pokemon_types, 2)
combos = [*combos_obj]
print(combos)

#set theory
list_a = ['Bulbasaur','Charmander','Squirtle']
list_b = ['Caterpie','Pidgey','Squirtle']

set_a = set(list_a)
set_b = set(list_b)
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.union(set_b))
print(set_a.symmetric_difference(set_b))

#Elimating loops with NumPy
import numpy as np

poke_states = np.array([
    [90, 92,75,60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]
])

avgs_np = poke_states.mean(axis=1)
print(avgs_np)

#DataFrame iteration using iterator method: iterrows()
import numpy as np
import pandas as pd

def calc_win_perc(wins, game_played):
    win_perc = wins/game_played
    return np.round(win_perc,2)

baseball_df = pd.read_csv('Day23/baseball.csv')

win_perc_list = []

for i,row in baseball_df.iterrows():
    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins,games_played)
    win_perc_list.append(win_perc)

baseball_df['WP'] = win_perc_list

print(baseball_df)

#DataFrame iteration using iterator method: itertuples()

def calc_run_diff(runs_scored,runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff

run_diffs = []

for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored,runs_allowed)
    run_diffs.append(run_diff)

baseball_df['RD'] = run_diffs
print(baseball_df)
