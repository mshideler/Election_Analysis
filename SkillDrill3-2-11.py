counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     # print(county + " county has " + str(voters) + " registered voters.")
#     print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#WTF
# for county_dict in voting_data:
#     #for value in county_dict.values():
#     #print(county_dict['county'])
#     #print(county_dict['registered_voters'])
#     #print(county_dict['county'] + " county has " + str(county_dict['registered_voters']) + " registered voters.")
#         print(f'{county_dict}')