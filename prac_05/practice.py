from collections import defaultdict

# dictionary to store country → list of players
country_players = defaultdict(list)

with open('wimbledon.csv') as in_file:
    next(in_file)  # skip header
    for line in in_file:
        fields = line.strip().split(',')
        country = fields[1]
        player = fields[2]
        country_players[country].append(player)

# Sort countries alphabetically
for country in sorted(country_players):
    # Sort players alphabetically
    players = sorted(country_players[country])
    print(f"{country}: {', '.join(players)}")
