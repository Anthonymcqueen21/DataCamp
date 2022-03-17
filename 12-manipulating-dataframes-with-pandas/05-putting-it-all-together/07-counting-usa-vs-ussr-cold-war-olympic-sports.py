'''
Counting USA vs. USSR Cold War Olympic Sports

The Olympic competitions between 1952 and 1988 took place during the height of the Cold War between the United States of America (USA) & the Union of Soviet Socialist Republics (USSR). Your goal in this exercise is to aggregate the number of distinct sports in which the USA and the USSR won medals during the Cold War years.

The construction is mostly the same as in the preceding exercise. There is an additional filtering stage beforehand in which you reduce the original DataFrame medals by extracting data from the Cold War period that applies only to the US or to the USSR. The relevant country codes in the DataFrame, which has been pre-loaded as medals, are 'USA' & 'URS'.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Create a Boolean Series called during_cold_war by extracting all rows from medals for which the 'Edition' is >= 1952 and <= 1988.
Create a Boolean Series called is_usa_urs by extracting rows from medals for which 'NOC' is either 'USA' or 'URS'.
Filter the medals DataFrame using during_cold_war and is_usa_urs to create a new DataFrame called cold_war_medals.
Group cold_war_medals by 'NOC'.
Create a Series Nsports from country_grouped using indexing & chained methods:
Extract the column 'Sport'.
Use .nunique() to get the number of unique elements in each group;
Apply .sort_values(ascending=False) to rearrange the Series.
Print the final Series Nsports. This has been done for you, so hit 'Submit Answer' to see the result!
'''
# Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
during_cold_war = (medals['Edition'] >= 1952) & (medals['Edition'] <= 1988)

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA', 'URS'])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

# Group cold_war_medals by 'NOC'
country_grouped = cold_war_medals.groupby('NOC')

# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

# Print Nsports
print(Nsports)
