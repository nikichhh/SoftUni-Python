import re


def better_player(curr_first_player, curr_second_player, all_players: dict):
    for first in all_players[curr_first_player].keys():
        for second in all_players[curr_second_player].keys():
            if first == second:
                if all_players[curr_first_player][first] > all_players[curr_second_player][second]:
                    all_players.pop(curr_second_player)
                    return all_players
                if all_players[curr_second_player][second] > all_players[curr_first_player][first]:
                    all_players.pop(curr_first_player)
                    return all_players
    return all_players


def check_points(points, position, player_name, all_players: dict):
    if all_players[player_name][position] < points:
        return True
    return False


player_pattern = r"(?P<player>[A-Za-z]+) -> (?P<position>[A-Za-z]+) -> (?P<skill>\d+)"
battle_pattern = r"(?P<player_1>[A-Za-z]+) vs (?P<player_2>[A-Za-z]+)"

players = {}
points_for_player = {}

while True:
    line = input()
    if line == 'Season end':
        break

    first_pattern = re.findall(player_pattern, line)
    second_pattern = re.findall(battle_pattern, line)

    if first_pattern:
        match = first_pattern[0]
        player, position, skill = match[0], match[1], int(match[2])

        if player not in players:
            players[player] = {position: skill}
            points_for_player[player] = skill
        else:
            if position not in players[player]:
                players[player][position] = skill
                points_for_player[player] += skill
            else:
                if check_points(skill, position, player, players):
                    points_to_add = skill - players[player][position]
                    players[player][position] = skill
                    points_for_player[player] += points_to_add
    else:
        match = second_pattern[0]
        first_player, second_player = match[0], match[1]

        if first_player in players and second_player in players:
            players = better_player(first_player, second_player, players)
            if first_player not in players.keys():
                points_for_player.pop(first_player)
            if second_player not in players.keys():
                points_for_player.pop(second_player)

for name, total_points in sorted(points_for_player.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {total_points} skill")

    for position, points in sorted(players[name].items(), key=lambda x: x[1], reverse=True):
        print(f"- {position} <::> {points}")
