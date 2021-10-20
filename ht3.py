import pandas as pd
from os import listdir
container = "./vitamins/"
sources = listdir(container)
vitamins = pd.DataFrame(columns = [ "vitamin",
	    "vitamers",
	    "solubility",
	    "daily_requirement",
	    "deficiency_diseases"])
n = 0
for i in sources:
	if i.endswith(".txt"):
		with open(container+i) as file:
			data = list(map(str.rstrip(),file.readlines())) # Reading all lines and deleting \n on right end
			data[1] = data[1].split(',')
			data[3] = float(data[3])
			data[4] = data[4].split(',')
			vitamins.loc[n,:] = data
		n+=1
vitamins.to_csv("vitamins.csv")
