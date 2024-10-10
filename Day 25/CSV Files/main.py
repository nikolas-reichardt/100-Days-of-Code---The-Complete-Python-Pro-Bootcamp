import os
# import csv

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Build the full path to the CSV file
file_path = os.path.join(script_dir, "weather_data.csv")


# with open(file_path) as file:
#     data = csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
# import os

df = pd.read_csv(file_path)
# print(df["temp"])
# print(df)
# print(type(df))


# temp_list = df["temp"].to_list()
# avg_temp = round(sum(temp_list) / len(temp_list))
# # print(avg_temp)
# # print(df["temp"].mean())
# # print(df["temp"].median())
# # print(df["temp"].mode())
# # print(df["temp"].max())

# # Get data from more columns
# condition = df["condition"].to_list()
# print(condition)

# #Get data from rows
# rows = df[df.day == "Monday"]
# # or
# rows = df[df["day"] == "Monday"]
# print(rows)

# #ROW
# print(df[df["temp"] == df["temp"].max()])
# #COLUMN
# print(df["temp"])

monday = df[df["day"] == "Monday"]
print(monday["temp"])
# How to get the actual value? Address the value with [0]
print(monday.temp[0])

# #create a data frame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# #create a csv file from your data frame
# #data.to_csv("FILENAME.csv")






# ------
# import pandas as pd
# data_dict = {
#     "Fur Color": [],
#     "Count": []
# }
# colors =["Gray", "Cinnamon", "Black"]
# df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(df[df["Primary Fur Color"] == "Black"]) 
# # print(df["Primary Fur Color"])
# for color in colors:
#     rows_with_color = df[df["Primary Fur Color"] == color]
#     #count = rows_with_color.shape[0]  
#     #Alternative for count method
#     count  = len(rows_with_color)
#     print(f"Die Farbe {color} kommt {count} oft mal vor")
#     data_dict["Fur Color"].append(color)
#     data_dict["Count"].append(count)

# push_df = pd.DataFrame(data_dict)
# push_df.to_csv("squirrel_count.csv")