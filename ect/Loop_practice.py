
'''
#while loop practice
x=0
while x <= 5:
    print(x)
    x=x+1

counties = ["Araphoe","Denver", "Jefferson"]

for county in counties:
    print(county)


for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Araphaoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.values():
    print(county)

for key, values in counties_dict.items():
    print(key, 'county has', values, 'registered voters')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for x in voting_data:
    print(x)

for x in range(len(voting_data)):
    print(voting_data[x])

for x in voting_data:
    for value in x.values():
        print(value)


counties_dict = {"Araphaoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(county, 'county has', voters, 'registered voters')

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
'''

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election? "))
messages_to_canidate = (
    f" Your received {candidate_votes:,} number of votes."
    f" The total number of votes in the election was {total_votes:,}"
    f" You received {candidate_votes/ total_votes * 100:2f}% of the total votes")
print(messages_to_canidate)

f'{value:{width}.{precision}}'