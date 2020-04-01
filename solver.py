import warnings

from pulp import *

from constraints import add_feasibility_constraints, add_overlap_constraints
from data_handling import get_teams, get_players, get_solution_lineup

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
#LpSolverDefault.msg = 1

#solve lineups using player information from rotogrinder and generated team information
def solve(num_lineups, overlap, player_csv, team_csv, verbose=False):
	players = get_players(player_csv, get_teams(team_csv)) #initial dataframe of players
	model = pulp.LpProblem('',pulp.LpMaximize)

	lineups = [] #initial list of lineups
	sols = []

	prev = None
	for i in range(num_lineups):
		if i == 0:
			add_feasibility_constraints(model, players)
		else:
			add_overlap_constraints(model, players, prev, overlap)

		if model.solve():
			sol = get_solution_lineup(model, players, verbose)
			lineups.append(sol[0]['Name'].tolist())
			sols.append(sol[0])
			prev = sol[1]
		else:
			return sols

    #provides ending solved lineups
	return sols
