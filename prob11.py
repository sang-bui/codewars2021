
f = input();
k = input();
x = input();

if "?" in f:
    print("F " + str(round(-1 * float(k.split()[1]) * float(x.split()[1]), 2)))
elif "?" in k:
    print("K " + str(round(-1 * float(f.split()[1]) / float(x.split()[1]), 2)))
elif "?" in x:
    print("X " + str(round(-1 * float(f.split()[1]) / float(k.split()[1]), 2)))