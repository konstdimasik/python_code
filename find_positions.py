# Write a program that reads a sequence of numbers from the first line and
# the number x from the second line. Then it should output all positions of x in the numerical sequence.
#
# The position count starts from 0. In case x is not in the sequence,
# print the line "not found" (quotes omitted, lowercased).
#
# Positions should be displayed in one line, in ascending order of the value.

seq = input().split()
digit = input()
positions = []
for ind, val in enumerate(seq):
    if val == digit:
        positions += [str(ind)]
if positions:
    print(" ".join(positions))
else:
    print("not found")

# ints = input().split()
# x = input()
# idx = [str(i) for i in range(len(ints)) if ints[i] == x]
# print(" ".join(idx) if idx else "not found")
