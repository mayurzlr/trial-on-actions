import os
from datetime import datetime as dt

print(str(dt.now()).replace(" ", "|"))

with open("log.txt", "a") as f:
    f.write(str(dt.now()) + "\n")
