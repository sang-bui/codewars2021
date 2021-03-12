text = input().split(" ")
print(text)

multiplier = 1

if text[5] == "MINUTES":
    multiplier=0.1
if text[5] == "HOUR":
    multiplier=0.01
height = (float(text[1]) * 0.0508) ** 2 / (2*9.805)
if height >= 25.00:
    print(text[0] + " will launch the messenger {} meters high, SUCCESS!".format(round(height, 2)))
elif height > 50:
    print(text[0] + " will launch the messenger {} meters high, OUCH!".format(round(height, 2)))
else:
    print(text[0] + " will launch the messenger {} meters high, SPLAT!".format(round(height, 2)))

