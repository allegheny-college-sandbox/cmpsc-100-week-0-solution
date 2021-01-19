#!/usr/bin/env python3

ballot = {}

while True:
    choice = input("Enter a candidate's name ([N]o to quit): ")
    if choice == "N":
        break
    try:
        ballot[choice] += 1
    except KeyError:
        ballot[choice] = 1

winner = None
max_votes = 0

for candidate in ballot:
    votes = ballot[candidate]
    print(candidate,"received",ballot[candidate],"votes.")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print(f"The winner is {winner} -- with {max_votes} votes.")