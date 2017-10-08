'''
Using a list comprehension
100xp

This time, you're going to use the lists2dict() function you defined in the last
exercise to turn a bunch of lists into a list of dictionaries with the help of a
list comprehension.

The lists2dict() function has already been preloaded, together with a couple of
lists, feature_names and row_lists. feature_names contains the header names of the
World Bank dataset and row_lists is a list of lists, where each sublist is a list
of actual values of a row from the dataset.

Your goal is to use a list comprehension to generate a list of dicts, where the
keys are the header names and the values are the row entries.

Instructions
-Inspect the contents of row_lists by printing the first two lists in row_lists.
-Create a list comprehension that generates a dictionary using lists2dict() for
each sublist in row_lists. The keys are from the feature_names list and the values are
the row entries in row_lists. Use sublist as your iterator variable and assign the
resulting list of dictionaries to list_of_dicts.
-Look at the first two dictionaries in list_of_dicts by printing them out.
'''
feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_lists = [['Arab World',
             'ARB',
             'Adolescent fertility rate (births per 1,000 women ages 15-19)',
             'SP.ADO.TFRT',
             '1960',
             '133.56090740552298'],
            ['Arab World',
             'ARB',
             'Age dependency ratio (% of working-age population)',
             'SP.POP.DPND',
             '1960',
             '87.7976011532547'],
            ['Arab World',
             'ARB',
             'Age dependency ratio, old (% of working-age population)',
             'SP.POP.DPND.OL',
             '1960',
             '6.634579191565161'],
            ['Arab World',
             'ARB',
             'Age dependency ratio, young (% of working-age population)',
             'SP.POP.DPND.YG',
             '1960',
             '81.02332950839141'],
            ['Arab World',
             'ARB',
             'Arms exports (SIPRI trend indicator values)',
             'MS.MIL.XPRT.KD',
             '1960',
             '3000000.0'],
            ['Arab World',
             'ARB',
             'Arms imports (SIPRI trend indicator values)',
             'MS.MIL.MPRT.KD',
             '1960',
             '538000000.0'],
            ['Arab World',
             'ARB',
             'Birth rate, crude (per 1,000 people)',
             'SP.DYN.CBRT.IN',
             '1960',
             '47.697888095096395'],
            ['Arab World',
             'ARB',
             'CO2 emissions (kt)',
             'EN.ATM.CO2E.KT',
             '1960',
             '59563.9892169935'],
            ['Arab World',
             'ARB',
             'CO2 emissions (metric tons per capita)',
             'EN.ATM.CO2E.PC',
             '1960',
             '0.6439635478877049'],
            ['Arab World',
             'ARB',
             'CO2 emissions from gaseous fuel consumption (% of total)',
             'EN.ATM.CO2E.GF.ZS',
             '1960',
             '5.041291753975099'],
            ['Arab World',
             'ARB',
             'CO2 emissions from liquid fuel consumption (% of total)',
             'EN.ATM.CO2E.LF.ZS',
             '1960',
             '84.8514729446567'],
            ['Arab World',
             'ARB',
             'CO2 emissions from liquid fuel consumption (kt)',
             'EN.ATM.CO2E.LF.KT',
             '1960',
             '49541.707291032304'],
            ['Arab World',
             'ARB',
             'CO2 emissions from solid fuel consumption (% of total)',
             'EN.ATM.CO2E.SF.ZS',
             '1960',
             '4.72698138789597'],
            ['Arab World',
             'ARB',
             'Death rate, crude (per 1,000 people)',
             'SP.DYN.CDRT.IN',
             '1960',
             '19.7544519237187'],
            ['Arab World',
             'ARB',
             'Fertility rate, total (births per woman)',
             'SP.DYN.TFRT.IN',
             '1960',
             '6.92402738655897'],
            ['Arab World',
             'ARB',
             'Fixed telephone subscriptions',
             'IT.MLT.MAIN',
             '1960',
             '406833.0'],
            ['Arab World',
             'ARB',
             'Fixed telephone subscriptions (per 100 people)',
             'IT.MLT.MAIN.P2',
             '1960',
             '0.6167005703199'],
            ['Arab World',
             'ARB',
             'Hospital beds (per 1,000 people)',
             'SH.MED.BEDS.ZS',
             '1960',
             '1.9296220724398703'],
            ['Arab World',
             'ARB',
             'International migrant stock (% of population)',
             'SM.POP.TOTL.ZS',
             '1960',
             '2.9906371279862403'],
            ['Arab World',
             'ARB',
             'International migrant stock, total',
             'SM.POP.TOTL',
             '1960',
             '3324685.0']]

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])
