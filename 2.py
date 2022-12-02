score = 0

rule = {
    "A" : 
    {
        "X": 3,
        "Y": 1+3,
        "Z": 2+6,
    },
    "B":
    {
        "X": 1,
        "Y": 2+3,
        "Z": 3+6,
    },
    "C":
    {
        "X": 2,
        "Y": 3+3,
        "Z": 1+6,
    },
}

for i in range(2500):
    x , y = input().split()
    score += rule[x][y]

print(score)