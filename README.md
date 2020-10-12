# Module 3 - Election Analysis

## Overview of Election Audit

#### This Eection Audit was to teach the basics of python, pulling data from an external cvs, progress into writing a complete syntex, then saving it to a txt file and pushing to GitHub.

#### We began by learning simple commands like 'len' and "append'.Then progressed into lists and dictionaries. And finally into writing for loops and f-strings. With some formatting along the way. After the commands we learned how to pull our election data on a csv into visual studio so our commands could pull data from the sheet. Finally once you have code you want to run, writing/saving that code to a txt file to share your results.


## Election-Audit Results

### **Election Results**

#### -Charles Casper Stockham: 23.0% (85,213)
#### -Diana DeGette: 73.8% (272,892)
#### -Raymon Anthony Doane: 3.1% (11,606)

### **Election Winner**

#### -Diana DeGette

### **County Voter Turnout**

#### -Jefferson: 10.5% (38,855)
#### -Denver: 82.8% (306,055)
#### -Arapahoe: 6.7% (24,801)

### **County With Largest Voter Turnout**

#### -Denver
#

![stacked_launch_outcomes](https://github.com/charlieburd/election_analysis/blob/main/ect/image%20(12).png)
#


## Election-Audit Summary:

### **Statement to Election Commission**

#### This script can be used for each election here after. You will either need to edit the CSV. with the currect election data, or link the script to pull from a new CSV. Two changes would be to:

#### 1. Change candidate vote total to be displayed as a 'x' out of 'total votes. For example: _Charles Casper Stockham: 23.0% (85,213/369,711)_ The code line should be changed to `f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}/{total_votes:,})\n"`

#### 2. Add an extra decimal to the pecent of votes reporting. For example: _Charles Casper Stockham: 23.03%_ The code line should be changed to `{vote_percentage:.2f}%`
