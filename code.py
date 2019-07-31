# --------------
import yaml

# Read the data of the format .yaml type
with open (path) as f:
    data = yaml.load(f)
data

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']

venue = data['info'] ['venue']
print("The match was played in " + city + " at " + venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info'] ['teams']
print("The teams played in the tournament are " + teams[0] + " and " + teams[1])

print("The total number of teams participated are : " + str(len(teams)))

# Which team won the toss and what was the decision of toss winner ?
toss_decision = data['info']['toss']['decision']
toss_winner = data['info']['toss']['winner']

print("The team who won the toss was " + toss_winner + " and selected to " + toss_decision)


# Find the first bowler and first batsman who played the first ball of the first inning

first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsmen = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print("The first bowler who with the first delivery is " + first_bowler + " and the first batsmen who played first ball is " + first_batsmen)

# How many deliveries were delivered in first inning ?
deliveries_1 = len(data['innings'][0]['1st innings']['deliveries'])
print("The first innings consists of the deliveries as", deliveries_1)

# How many deliveries were delivered in second inning ?
deliveries_2 = len(data['innings'][1]['2nd innings']['deliveries'])
print("The first innings consists of the deliveries as", deliveries_2)

# Which team won and how ?
team_winner = data['info']['outcome']['winner']
team_winner_by_runs = data['info']['outcome']['by']['runs']

print("The winnner team was" + team_winner + " by runs",team_winner_by_runs)


