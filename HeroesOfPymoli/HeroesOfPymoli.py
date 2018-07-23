
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%). 

* Amongst all the players, Lisosia93 has contributed the most (18.96 USD) to the total purchase value followed by Idastidru52 (15.45 USD) and Chamjask73 (13.83 USD)

* Amongst all the items, Item ID 178 is the most popular followed by Item IDs 145 and 108

* Amongst all the items, Item ID 178 is the most profitable followed by Item IDs 82 and 145

* Amongst players of various age groups, "<10" and "35-39" are contributing less to the total purchase value because of low headcount and purchases. However, these 2 groups seem to have more purchasing power than any of the other groups. Further research can be done to include/modify some  items that would attract these age groups so that they can contirbute more to the total purchase 
value

* Item ID 19 - "Pursuit, Cudgel of Necromancy" is one of the top 5 popular items. However, its generating less value (8.16 USD) compared to other 4 top popular items as it is only priced at 1.02 USD. The price for this item can be bumped up a little (in small measured proportions) to generate further value out of it.
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)


## Player Count

* Display the total number of players


## Purchasing Analysis (Total)

#Finding the count of Unique Players
unique_player_count = [purchase_data["SN"].nunique()]

#Create dataframe to display the number of players
total_players = pd.DataFrame(unique_player_count,columns=["Total Players"])

total_players

#Creating a sub data frame with just the player name, age and gender
unique_player_df = purchase_data[["SN","Gender","Age"]]

#Removing duplicate rows so that we have only one row for each player
unique_player_df = unique_player_df.drop_duplicates("SN", keep='first')


* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


#Create a dictionary which will hold all the calculated values
summary_dict = {"Number of Unique Items":[purchase_data["Item ID"].nunique()],
                            "Average Price":[purchase_data["Price"].mean()],
                            "Number of Purchases":[purchase_data["Purchase ID"].count()],
                            "Total Revenue":[purchase_data["Price"].sum()]}

#Create dataframe to display all values
summary_frame = pd.DataFrame(summary_dict, columns=["Number of Unique Items","Average Price",
                                                   "Number of Purchases","Total Revenue"])

#Formatting the Average Price and Total Revenue columns
summary_frame["Average Price"] = summary_frame["Average Price"].map("${:.2f}".format)
summary_frame["Total Revenue"] = summary_frame["Total Revenue"].map("${:,}".format)

#Displaying the output
summary_frame

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




#This step calculates Gender Demographics taking into consideration the entire data set ("purchase_data") which has multiple
#rows for certain players

#Calculating the count of unique Genders and assigning to a dataframe
grouped_gender_count = purchase_data.groupby("Gender").size().reset_index(name='Total Count')

#Calculating the percentage of unique Genders and assigning to a dataframe
grouped_gender_percent = (purchase_data.groupby("Gender").size().divide(sum(purchase_data["Gender"].notnull()))*100).reset_index(name='Percentage of Players')

#Formatting the Percentage of Players
grouped_gender_percent["Percentage of Players"] = grouped_gender_percent["Percentage of Players"].map("{:.2f}%".format)

#Merging the 2 data frames
grouped_gender_demo= pd.merge(grouped_gender_percent, grouped_gender_count, on="Gender")

#Sorting the data in descending order on Total Count column
grouped_gender_demo = grouped_gender_demo.sort_values("Total Count", ascending = False)

#Displaying the output
grouped_gender_demo

#This step calculates Gender Demographics for unique players and works on data set ("unique_player_df") which has 
#only one row for each player


#Calculating the count of unique Genders and assigning to a dataframe
grouped_gender_count = unique_player_df.groupby("Gender").size().reset_index(name='Total Count')

#Calculating the percentage of unique Genders and assigning to a dataframe
grouped_gender_percent = (unique_player_df.groupby("Gender").size().divide(sum(unique_player_df["Gender"].notnull()))*100).reset_index(name='Percentage of Players')

#Formatting the Percentage of Players
grouped_gender_percent["Percentage of Players"] = grouped_gender_percent["Percentage of Players"].map("{:.2f}%".format)

#Merging the 2 data frames
grouped_gender_demo= pd.merge(grouped_gender_percent, grouped_gender_count, on="Gender")

#Sorting the data in descending order on Total Count column
grouped_gender_demo = grouped_gender_demo.sort_values("Total Count", ascending = False)

#Displaying the output
grouped_gender_demo


## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

#Creating a dataframe by grouping the original dataset on "Gender" and fetching required values 
#through aggregate function
grouped_gender = purchase_data.groupby("Gender").agg({'Purchase ID': {'Purchase Count': 'count'},
                                     'Price': {'Average Purchase Price' : 'mean',
                                               'Total Purchase Value': 'sum',
                                                  'Avg Purchase Total per Person':'mean'}})

#Setting the column names for each calculated parameter
grouped_gender.columns = ["_".join(x) for x in grouped_gender.columns.ravel()]

#Renaming to generate meaningful and required column names
grouped_gender.rename(columns={'Purchase ID_Purchase Count': 'Purchase Count', 
                        'Price_Average Purchase Price': 'Average Purchase Price',
                        'Price_Total Purchase Value':'Total Purchase Value',
                       'Price_Avg Purchase Total per Person':'Avg Purchase Total per Person'}, inplace=True)

#Formatting the values 
grouped_gender["Average Purchase Price"] = grouped_gender["Average Purchase Price"].map("${:.2f}".format)
grouped_gender["Avg Purchase Total per Person"] = grouped_gender["Avg Purchase Total per Person"].map("${:.2f}".format)
grouped_gender["Total Purchase Value"] = grouped_gender["Total Purchase Value"].map("${:,.2f}".format)

#Displaying the preview
grouped_gender.head()



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


#This step calculates Age demographics considering the original dataset ("purchase_data") which has one player more than once


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]

# Establishing the group labels
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#Slicing the originl data set and grouping it into respective bins(Age Group) as per "Age"
# Setting the corresponding age group as a new column in the dataframe
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

#Grouping the dataframe on basis of "Age Group" and getting count of each group
grouped_age_count = purchase_data.groupby("Age Group").size().reset_index(name='Total Count')

#Grouping the dataframe on basis of "Age Group" and getting percent count of each group
grouped_age_percent = (purchase_data.groupby("Age Group").size().divide(sum(purchase_data["Age Group"].notnull()))*100).reset_index(name='Percentage of Players')

#Formatting the column
grouped_age_percent["Percentage of Players"] = grouped_age_percent["Percentage of Players"].map("{:.2f}%".format)

# Merging the dataframes to get final consolidated output
grouped_age_demo= pd.merge(grouped_age_percent, grouped_age_count, on="Age Group")

#Display the dataframe
grouped_age_demo


#This step calculates Age demographics considering the modified dataset ("unique_player_df") which has one player only once 


#Slicing the originl data set and grouping it into respective bins(Age Group) as per "Age"
# Setting the corresponding age group as a new column in the dataframe
unique_player_df["Age Group"] = pd.cut(unique_player_df["Age"], age_bins, labels=group_names)

#Grouping the dataframe on basis of "Age Group" and getting count of each group
grouped_age_count = unique_player_df.groupby("Age Group").size().reset_index(name='Total Count')

#Grouping the dataframe on basis of "Age Group" and getting percent count of each group
grouped_age_percent = (unique_player_df.groupby("Age Group").size().divide(sum(unique_player_df["Age Group"].notnull()))*100).reset_index(name='Percentage of Players')

#Formatting the column
grouped_age_percent["Percentage of Players"] = grouped_age_percent["Percentage of Players"].map("{:.2f}%".format)

# Merging the dataframes to get final consolidated output
grouped_age_demo= pd.merge(grouped_age_percent, grouped_age_count, on="Age Group")

#Display the dataframe
grouped_age_demo

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

#Creating a dataframe by grouping the original dataset on "Age Group" and fetching required values 
#through aggregate function
grouped_age = purchase_data.groupby("Age Group").agg({'Purchase ID': {'Purchase Count': 'count'},
                                     'Price': {'Average Purchase Price' : 'mean',
                                               'Total Purchase Value': 'sum',
                                                  'Avg Purchase Total per Person':'mean'}})

#Setting the column names for each calculated parameter
grouped_age.columns = ["_".join(x) for x in grouped_age.columns.ravel()]

#Renaming to generate meaningful and required column names
grouped_age.rename(columns={'Purchase ID_Purchase Count': 'Purchase Count', 
                        'Price_Average Purchase Price': 'Average Purchase Price',
                        'Price_Total Purchase Value':'Total Purchase Value',
                       'Price_Avg Purchase Total per Person':'Avg Purchase Total per Person'}, inplace=True)

#Formatting the values
grouped_age["Average Purchase Price"] = grouped_age["Average Purchase Price"].map("${:.2f}".format)
grouped_age["Avg Purchase Total per Person"] = grouped_age["Avg Purchase Total per Person"].map("${:.2f}".format)
grouped_age["Total Purchase Value"] = grouped_age["Total Purchase Value"].map("${:,.2f}".format)

#Displaying the dataframe
grouped_age


## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#Creating a dataframe by grouping the original dataset on "SN" and fetching required values 
#through aggregate function
grouped_user = purchase_data.groupby("SN").agg({'Purchase ID': {'Purchase Count': 'count'},
                                     'Price': {'Average Purchase Price' : 'mean',
                                               'Total Purchase Value': 'sum'}})

#Setting the column names for each calculated parameter
grouped_user.columns = ["_".join(x) for x in grouped_user.columns.ravel()]

#Renaming to generate meaningful and required column names
grouped_user.rename(columns={'Purchase ID_Purchase Count': 'Purchase Count', 
                        'Price_Average Purchase Price': 'Average Purchase Price',
                        'Price_Total Purchase Value':'Total Purchase Value'}, inplace=True)

#Formatting and sorting based on "Total Purchase Value"
grouped_user["Average Purchase Price"] = grouped_user["Average Purchase Price"].map("${:.2f}".format)
grouped_user = grouped_user.sort_values("Total Purchase Value", ascending = False)
grouped_user["Total Purchase Value"] = grouped_user["Total Purchase Value"].map("${:,.2f}".format)

#Displaying the preview
grouped_user.head()


## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#Creating a dataframe by fetching "Item ID","Item Name" and "Price" from original dataset
items_data = purchase_data[["Item ID","Item Name","Price"]]

#Creating a dataframe by grouping the original dataset on "Item ID","Item Name" and"Price" 
#and fetching required values through aggregate function
grouped_item = items_data.groupby(["Item ID","Item Name"]).agg({'Price': {'Count': 'count',
                                                                            'ItemPrice': 'max',
                                                                           'Value': 'sum'}})


#Setting the column names for each calculated parameter
grouped_item.columns = ["_".join(x) for x in grouped_item.columns.ravel()]

#Renaming to generate meaningful and required column names
grouped_item.rename(columns={'Price_Count': 'Purchase Count',
                             'Price_ItemPrice': 'Item Price',
                        'Price_Value': 'Total Purchase Value'}, inplace=True)

#Formatting and sorting based on "Purchased Count"
grouped_item_countsort = grouped_item.sort_values("Purchase Count",ascending = False)
grouped_item_countsort["Item Price"] = grouped_item_countsort["Item Price"].map("${:.2f}".format)
grouped_item_countsort["Total Purchase Value"] = grouped_item_countsort["Total Purchase Value"].map("${:,.2f}".format)

#Displaying the preview
grouped_item_countsort.head()

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



#Formatting and sorting based on "Total Purchase Value"
grouped_item_pricesort = grouped_item.sort_values("Total Purchase Value",ascending = False)
grouped_item_pricesort["Item Price"] = grouped_item_pricesort["Item Price"].map("${:.2f}".format)
grouped_item_pricesort["Total Purchase Value"] = grouped_item_pricesort["Total Purchase Value"].map("${:,.2f}".format)

#Displaying the preview
grouped_item_pricesort.head()
