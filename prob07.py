from math import atan
from math import degrees
table = [[0.90, 0.62, 0.57],
        [0.80, 0.42, 0.30],
        [0.70, 0.30, 0.74],
        [1.15, 0.80, 0.70],
        [0.15, 0.05, 0.03]]
surfaceMap = {"CONCRETE": 0, "WOOD":1, "STEEL":2, "RUBBER":3, "ICE": 4}
materialMap = {"RUBBER": 0, "WOOD":1, "STEEL":2}
i = input().split()
print(str(table[surfaceMap[i[0]]][materialMap[i[1]]]) + " " + str(round(degrees(atan(table[surfaceMap[i[0]]][materialMap[i[1]]])),1)))