# PAUSE 1
# See if you can figure out how to print out "Lille"
# from the nested List called travel_log.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])


#PAUSE 2
# Do you remember how to get items that are nested deeply in a list?
# Try to print "D" from the list nested_list.

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

#PAUSE 3
# Figure out how to print out "Stuttgart" from the following list:

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])

travel_log[1]=4

print(travel_log)
print(travel_log[1])