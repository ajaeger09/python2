#https://www.py4u.net/discuss/10884
print("Enter the round 1 score, round 2 score, and players name")
input_values = [input() for i in range(3)]
print(input_values)
print(type(input_values))
round_1_score = int(input_values[0])
round_2_score = int(input_values[1])
name = input_values[2]
