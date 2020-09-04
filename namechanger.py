import os
import random

dirs = []

for (dirpath, dirnames, filenames) in os.walk("."):
    dirs.extend(filenames)
    break

dirs = [ x for x in dirs if ".py" not in x ]

if input("RANDOM NAMES OR ITER (r, i): ").lower() == "r":
    n = 0
    for x in dirs:
        os.rename(x, f"file{random.randrange(1, 10000000)}." + x.split(".")[-1])
        n += 1
else:
    n = 0
    for x in dirs:
        os.rename(x, f"file{n}."+x.split(".")[-1])
        n += 1
