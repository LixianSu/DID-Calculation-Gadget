import pandas as pd
import chardet


file = r"C:\Software\Russian-Ukrainian War\Data\Recent\USA\USA_EXPORT.csv"

df = pd.read_csv(file, low_memory=False)
newd = {'source':[], 'date':[], 'agriculture':[], 'apparel':[], 'chemicals':[], 'machinery':[], 'materials':[], 'metals':[], 'miscellaneous':[], 'transport':[], 'minerals':[]}

initial_date = df.loc[1, "date"]
initial_source = df.loc[1, "source"]
initial_sector = df.loc[1, "sector"]
initial_value = df.loc[1, "value"]

inspector = ['agriculture', 'apparel', 'chemicals', 'machinery', 'materials', 'metals', 'miscellaneous',
                     'transport,minerals']

newd['source'].append(initial_source)
newd['date'].append(initial_date)
newd[initial_sector].append(initial_value)
inspector.remove(initial_sector)


for i in range(2, len(df)):
    idate = df.loc[i, "date"]
    isource = df.loc[i, "source"]
    isector = df.loc[i, "sector"]
    ivalue = df.loc[i, "value"]

    if idate != initial_date or isource != initial_source:
        if inspector:
            print("finish one loop\n")
        else:
            for i in inspector:
                newd[i].append(0)
            print("finish one loop\n")
        inspector = ['agriculture', 'apparel', 'chemicals', 'machinery', 'materials', 'metals', 'miscellaneous',
                     'transport,minerals']
        newd['source'].append(isource)
        newd['date'].append(idate)
        newd[isector].append(ivalue)
        inspector.remove(isector)
        initial_date = idate
        initial_source = isource
    else:
        inspector.remove(isector)
        newd[isector].append(ivalue)

newdf = pd.DataFrame(newd)
newdf.to_csv('DataFrame_ab.csv', index=False, sep=',')