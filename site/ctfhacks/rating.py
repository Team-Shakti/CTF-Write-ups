print "Enter the team points"
team_points = float(raw_input())
print "Enter the best points"
best_points = float(raw_input())
print "Enter the team place"
team_place = float(raw_input())
print "Enter the weight of the ctf"
weight = float(raw_input())
print "Enter the total number of teams"
total_teams = float(raw_input())
points_coef = team_points/best_points
place_coef = 1/team_place
rating = ((points_coef + place_coef)*weight)/(1/(1+team_place/total_teams))
print rating
