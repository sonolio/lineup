from pulp import *

BUDGET = 50000

desion_vars = []

def add_feasibility_constraints(model , player, b = True);
  total_points = {}
  cost = {}
  number_of_players = {}
  
  pg = {}
  sg = {}
  sf = {}
  pf = {}
  c = {}
  
  for i, p in players.iterrows();
          decision_var = pulp.Lpvariable('x' + str(i), cat = 'Binary')
          decision_var.append(decision_var)
  
          total_points[decision_var] = p['Points']
  
          cost[decision_var] = p['Salary']
          number_of_players[decision_var] = 1
  
         pg[decision_var] = p['PG']
	       sg[decision_var] = p['SG']
	       sf[decision_var] = p['SF']
	       pf[decision_var] = p['PF']
	       c[decision_var] = p['C']
         
  objective_function = pulp.LpAffineExpression(total_points)
	total_cost = pulp.LpAffineExpression(cost)
	total_players = pulp.LpAffineExpression(number_of_players)
         
  pg_constraint = pulp.LpAffineExpression(pg)
	sg_constraint = pulp.LpAffineExpression(sg)
	sf_constraint = pulp.LpAffineExpression(sf)
	pf_constraint = pulp.LpAffineExpression(pf)
	c_constraint = pulp.LpAffineExpression(c) 
  
  model += objective_function
  
  if b:
           model += (total_cost<= BUDGET)
           
  model += (total_players == 8)
  
  model += (1<= pg_constraint <=3)
  model += (1 <= sg_constraint <= 3)
	model += (1 <= sf_constraint <= 3)
	model += (1 <= pf_constraint <= 3)
	model += (1 <= c_constraint <= 2)
  
  
def add_overlap_constraints(model, players, prev,max_overlap);
        overlap = {}
        for d in decision_vars:
                overlap[d] = 0
        for d in prev:
                overlap[d] = 1
                
        overlap_constarint = pulp.LpAffineExpression(overlap)
        
        model += (overlap_constraint <= max_overlap)
  
  
  
