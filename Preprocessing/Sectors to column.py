import pandas as pd
import os


path = r"C:\Software\Russian-Ukrainian War\Data\Recent\USA"
file = r"USA_EXPORT.csv"
df = pd.read_csv(os.path.join(path,file), low_memory=False)
newd = {'source':[], 'date':[], 'agriculture':[], 'apparel':[], 'chemicals':[], 'machinery':[], 'materials':[], 'metals':[], 'miscellaneous':[], 'transport':[], 'minerals':[]}

initial_date = df.loc[0, "date"]
initial_source = df.loc[0, "source"]
initial_sector = df.loc[0, "sector"]
initial_value = df.loc[0, "value"]

inspector = ['agriculture', 'apparel', 'chemicals', 'machinery', 'materials', 'metals', 'miscellaneous',
                     'transport', 'minerals']

newd['source'].append(initial_source)
newd['date'].append(initial_date)
newd[initial_sector].append(initial_value)
print(initial_sector)
inspector.remove(initial_sector)


for i in range(1, len(df)):
    idate = df.loc[i, "date"]
    isource = df.loc[i, "source"]
    isector = df.loc[i, "sector"]
    ivalue = df.loc[i, "value"]

    if idate != initial_date or isource != initial_source:
        if inspector:
            for i in inspector:
                newd[i].append(0)
            print("finish one loop.\n")
        else:
            print("finish one loop.\n")
        inspector = ['agriculture', 'apparel', 'chemicals', 'machinery', 'materials', 'metals', 'miscellaneous',
                     'transport', 'minerals']
        newd['source'].append(isource)
        newd['date'].append(idate)
        newd[isector].append(ivalue)
        inspector.remove(isector)
        initial_date = idate
        initial_source = isource
    else:
        inspector.remove(isector)
        newd[isector].append(ivalue)

if inspector:
    for i in inspector:
        newd[i].append(0)
        print("finish one loop.\n")
    else:
        print("finish one loop.\n")

newdf = pd.DataFrame(newd)
newdf.to_csv(os.path.join(path, 'DataFrame_ab.csv'), index=False, sep=',')