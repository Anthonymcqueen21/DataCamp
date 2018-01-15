'''
Dropping duplicate data

Duplicate data causes a variety of problems. From the point of view of performance, they use up unnecessary amounts of memory and cause unneeded calculations to be performed when processing data. In addition, they can also bias any analysis results.

A dataset consisting of the performance of songs on the Billboard charts has been pre-loaded into a DataFrame called billboard. Check out its columns in the IPython Shell. Your job in this exercise is to subset this DataFrame and then drop all duplicate rows.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
-Create a new DataFrame called tracks that contains the following columns from billboard: 'year', 'artist', 'track', and 'time'.
-Print the info of tracks. This has been done for you.
-Drop duplicate rows from tracks using the .drop_duplicates() method. Save the result to tracks_no_duplicates.
-Print the info of tracks_no_duplicates. This has been done for you, so hit 'Submit Answer' to see the results!
'''
# Create the new DataFrame: tracks
tracks = billboard[['year','artist','track','time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())
