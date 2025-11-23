"""estimated time: 20 mins
    Actual time:60mins """
# Read winners
data = []
country_and_player = []
with open('wimbledon.csv') as in_file:
    next(in_file)
    for line in in_file:
        fields = line.strip().split(',')
        country = fields[1]
        player = fields[2]
        data.append(player)
        country_and_player.append((country, player))
    player_for_sorted_country = sorted(set(country_and_player))

# Count wins
win_count = {}
for name in data:
    if name in win_count:
        win_count[name] += 1
    else:
        win_count[name] = 1

# Print total number of unique winners
print(f"There are {len(win_count)} winners\n")

# Print each winner and how many times they won
for name, count in win_count.items():
    print(f"{name:20} won {count:3} times")

print(f"the people are from:\n")

for country, name in player_for_sorted_country:
    print(f"{name:20} is from {country:3}")