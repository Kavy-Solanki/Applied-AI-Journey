import pandas as pd
import re

'''Loading Data'''
df = pd.read_csv("pokemon_data.csv") #Load a CSV 
print(df.head(3)) #to see first x rows
print(df.tail(3)) #to last first x rows
df_excel = pd.read_excel("pokemon_data.xlsx") #Load excel file
df_excel = pd.read_csv("pokemon_data.txt", delimiter="\t")
#delimter is used to specify what is used to seperate data so it is easy to load readable data
#both head and tail can be used with txt and xlsx also

'''Reading Data'''
print(df.columns) #Read Headers
print(df["Name"][0:5]) #Reading specific column and rows if required
#can do df[["Name", "Type 1", "HP"]] for multiple columns
print(df.iloc[1]) #reading a specific row
#[1:4] for multiple rows
#REMEMBER HERE [1], [1:4], etc ARE INDEXES NOT ROW NUMBER
print(df.iloc[2,1]) #getting a specific data
print(df.iloc[0:2,1:3]) #Get specific amount data

# for index,rows in df.iterrows():
#     print(index , rows)
#to iterate each row, rows["Name"] for a specific column
print(df.loc[df["Type 1"] == "Fire"]) #reading a specific amount of data based on textual or numericla info
#can do multiple conditions also

'''Sorting/Describing Data'''
print(df.describe()) #Get all statistical data
print(df.sort_values(["Type 1", "HP"], ascending = [True, False])) # to sort values acc to Name
#for multiple use a list and ascending = t/f, 
#for multiple need to use a list in ascending attr also, can do [True,False] or [1,0] 
#1 = True, 0 = False 
#eg ["Type 1", "HP"] will sort ascending acc to both

'''Making Changes in Data'''
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#Another Method: df["Total"] = df.iloc[:, 4:10].sum(axis=1)
#axis = 1 to add horizontally and =1 to add vertically
#adding a new column "total"
#df = df.drop(columns=["Total"]) #removing total column and storing the data again
cols = list(df.columns)
print(cols)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]] #re-arranging columns
#df = df[["#", "Name", "Type 1", "Type 2", "Total", "HP",'Attack','Defense','Sp. Atk','Sp. Def','Speed',"Generation", "Legendary"]]

'''Saving Data'''
df.to_csv("pokemon_data_modified.csv", index = False)
df.to_excel("pokemon_data_modified.xlsx", index = False)
df.to_csv("pokemon_data_modified.txt", index = False, sep="\t") #to sep data using \t = tab

'''Filtering Data'''
print("-----------------------------------")
print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]) # | = or , & = and.
#Using Paranthesis for each cond. is comp. 
new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]
# new_df = new_df.reset_index(drop = True) #drop = True to remove all indexes
new_df.reset_index(drop = True, inplace=True) #to not to save in a new df, change in existing one
print(new_df)
# new_df.to_csv("pokemon_data_filtered.csv")
print(df.loc[df["Name"].str.contains("Mega")]) # prints all data having mega in its name
print(df.loc[df["Type 1"].str.contains("fire|grass", flags = re.I, regex=True)])
#regex is used to check data in which type 1 = fire or grass, | = or
#flags = re.I to ingnore case. It tells Python to match text without caring about uppercase or lowercase letters.
#another example: print(df.loc[df["Name"].str.contains("^pi[a-z]*", flags = re.I, regex=True)]) 

'''Conditional Changes'''
df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"
print(df)
#For all fire typpe pokemon change its type 1 to flamer
df.loc[df["Type 1"] == "Flamer", "Type 1"] = "Fire" #restoring back
#multiple change cna be made using a list

'''Aggregate Statistics(Groupby)'''
print(df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("Defense", ascending=False))
#Find mean of all the data by grouping Type 1, i.e keeping type 1 as the base
#print(df.groupby(["Type 1"]).sum())
#print(df.groupby(["Type 1"]).count()) -> 1. df["count"] = 1 -> print(df.groupby(["Type 1"]).count())["count"]
#will only give the count column, can groupby with multiple columns also, like ["Tpye 1", "Type 2"]

'''Working with large data'''
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])