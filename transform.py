import pandas as pd
import os
from datetime import datetime as dt

for file in os.listdir("./raw"):
    if file.endswith(".csv"):
        df = pd.read_csv("./raw/" + file)
        df["fileName"] = [file] * len(df)
        df.to_csv("./process/" + file, index=False)
        with open("dumm.txt", "a") as f:
            f.write(file + "      " + str(dt.now()) + "\n")
