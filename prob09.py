pi = 3.1415926536

numOfMinions = int(input())
radiusCockpit = float(input())

radiusHeightBody = input().split()
radiusHeightBody = [float(i) for i in radiusHeightBody]

lengthWidthHeight = input().split()
lengthWidthHeight = [float(i) for i in lengthWidthHeight]

spaceOfMinions = (numOfMinions * 1.20)
targetSpace = spaceOfMinions + 2.20 + 4.10 + 12.10

print("Cockpit " + str(4/3 * pi * radiusCockpit**3))
print("Body " + str(radiusHeightBody[1]*pi*radiusHeightBody[0]*2))
print("Pods " + str((1/3*lengthWidthHeight[0]*lengthWidthHeight[1]*lengthWidthHeight[2]) * 2))
print("Minions Need " + str(spaceOfMinions))

if targetSpace <= (4/3 * pi * radiusCockpit**3) + (radiusHeightBody[1]*pi*radiusHeightBody[0]**2) + ((1/3*lengthWidthHeight[0]*lengthWidthHeight[1]*lengthWidthHeight[2]) * 2):
    print("PLAN ACCEPTED")
else:
    print("PLAN REJECTED")

