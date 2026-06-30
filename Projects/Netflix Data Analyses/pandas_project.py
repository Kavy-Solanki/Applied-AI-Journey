import pandas as pd

def menu():
    print("What type of File is it?")
    try:
        file_type = int(input("1.Excel File(.xlsx)\n2.CSV File(.csv)\n3.Text File(.txt): "))
        return file_type
    except ValueError:
        print("The Input Must be a intger.")
        return menu()
while True:
    file_type = menu()
    if file_type == 1:
        file_name = input("Enter File Name(without Extension): ")
        try:
            df = pd.read_excel(f"{file_name}.xlsx")
            break
        except FileNotFoundError:
            print("File Not Found!")
    elif file_type == 2:
        file_name = input("Enter File Name(without Extension): ")
        try:
            df = pd.read_csv(f"{file_name}.csv")
            break
        except FileNotFoundError:
            print("File Not Found!")
    elif file_type == 3:
        file_name = input("Enter File Name(without Extension): ")
        print("A delimeter is way to seperate data. Like \\n, \\t, ',' , etc")
        dl = input("Enter delimeter: ")
        try:
            df = pd.read_csv(f"{file_name}.txt", delimiter=f"{dl}")
            break
        except FileNotFoundError:
            print("File Not found!")
    else:
        print("Please Enter a Valid Option.")

#shapes = df.shape
#cols = list(df.columns)
#print(f"Number of rows: {shapes[0]}")
#print(f"Number of Columns: {shapes[1]}")
#print(f"The Columns present are: {cols}")
#print(df.head(5))
#print(df.tail(5))
print(f"The Most Common Category: {df["listed_in"].value_counts().idxmax()}")
print(f"Number of movies in that category is: {df["listed_in"].value_counts().max()}")
print(f"Nulls Values present in each column: {df.isnull().sum()}")
print(f"Number of Movies: {df["type"].value_counts()["Movie"]}")
print(f"Number of Movies: {df["type"].value_counts()["TV Show"]}")
print(f"The county which produced max movies is: {df["country"].value_counts().idxmax()}")
print(f"The oldest title was: {df.loc[df["release_year"] == df["release_year"].min(), "title"].iloc[0]}")
print(f"The newest title was: {df.loc[df["release_year"] == df["release_year"].max(), "title"].iloc[0]}")
print(f"The titles released after 2020s are: {df.loc[df['release_year'] > 2020, "title"]}")
print(f"The Most appeared Rating: {df["rating"].value_counts().idxmax()}")
print(f"Top 10 Category: {df["listed_in"].value_counts().head(10)}")
print(f"The Most released yr: {df["release_year"].value_counts().idxmax()}")
duration = df[df["type"] == "Movie"]["duration"].value_counts().idxmax()
print(f"The Movies with most Duration: {df.loc[(df['duration'] == duration) & (df['type'] == 'Movie')]}")
#print(f"THe movies released in India are: {df.loc[df['country'] == "India"]}")
#print(f"The TV Shows released after 2018 are: {df.loc[(df['release_year'] > 2018) & (df['type'] == 'TV Show')]}")
#print(df.loc[df["title"].str.contains("Love")])