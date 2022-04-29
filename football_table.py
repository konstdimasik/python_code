dict = {}
# n_games = int(input())
# for i in range(n_games):
#     str_in = [i for i in input().split(';')]
with open('football_input.txt', 'r') as file:
    n_games = int(file.readline())
    for line in file:
        str_in = line.strip().split(';')
        team1, goal1, team2, goal2 = str_in[0], int(str_in[1]), str_in[2], int(str_in[3])
        if team1 not in dict:
            dict[team1] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
        if team2 not in dict:
            dict[team2] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
        dict[team1]['plays'] += 1
        dict[team2]['plays'] += 1
        if goal1 < goal2:
            dict[team1]['loses'] += 1
            dict[team2]['wins'] += 1
            dict[team2]['score'] += 3
        elif goal1 > goal2:
            dict[team1]['wins'] += 1
            dict[team2]['loses'] += 1
            dict[team1]['score'] += 3
        else:
            dict[team1]['draws'] += 1
            dict[team2]['draws'] += 1
            dict[team1]['score'] += 1
            dict[team2]['score'] += 1

for team in dict:
    print(
        f"{team}: {dict[team]['plays']} {dict[team]['wins']}"
        f"{dict[team]['draws']} {dict[team]['loses']} {dict[team]['score']}"
    )

# dict = {}
# # n_games = int(input())
# # for i in range(n_games):
# #     str_in = [i for i in input().split(';')]
# with open('football_input.txt', 'r') as file:
#     n_games = int(file.readline())
#     for line in file:
#         str_in = line.strip().split(';')
#         team1, goal1, team2, goal2 = str_in[0], int(str_in[1]), str_in[2], int(str_in[3])
#         if team1 not in dict:
#             dict[team1] = [0, 0, 0, 0, 0]
#         if team2 not in dict:
#             dict[team2] = [0, 0, 0, 0, 0]
#         dict[team1][0] += 1
#         dict[team2][0] += 1
#         if goal1 < goal2:
#             dict[team1][3] += 1
#             dict[team2][1] += 1
#             dict[team2][4] += 3
#         elif goal1 > goal2:
#             dict[team1][1] += 1
#             dict[team2][3] += 1
#             dict[team1][4] += 3
#         else:
#             dict[team1][2] += 1
#             dict[team2][2] += 1
#             dict[team1][4] += 1
#             dict[team2][4] += 1
#
# for team in dict:
#     print(f'{team}: {dict[team][0]} {dict[team][1]} {dict[team][2]} {dict[team][3]} {dict[team][4]}')
