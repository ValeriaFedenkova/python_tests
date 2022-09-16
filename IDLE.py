import yaml
import re
import pandas as pd
with open(r'C:\Users\v.fedenkova\Desktop\Санкт-Петербург\Данные\14\klt.014.001.info (2).yml', 'r') as file:
	file = yaml.safe_load(file)
shots_fule = list(file['shots'])
#print(shots_fule[1:1354])
list_shots = "".join(str(shots_fule))
print(list_shots['gpsd'])

