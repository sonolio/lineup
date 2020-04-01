from generate_dk_csv import generate_csv
from scrape_googlesheets_predictions import scrape_googlesheets_predictions
from solver import solve

#generate final csv to be used for DraftKings
scrape_googlesheets_predictions()
a = solve(5, 7, 'googlesheets_predictions.csv', 'teams.csv')
generate_csv(a)
