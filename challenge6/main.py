import pandas

# got a lot of help from Josiah's github, hadn't been exposed to the pandas package before
# https://github.com/jgru-mars/Challenge5CSVsplitting/blob/master/challenge5.py


def main():

    # reading the csv and creating the dataset as csv
    csv = pandas.read_csv("2015.csv")

    # this adds a new column called institution id and all
    # columns with the same institution and city have the same institution id
    csv['Institution ID'] = csv.groupby(['ï»¿Institution', 'City']).ngroup()

    # creating the institutions dataset by selecting the columns from csv dataset
    institutions = csv[['Institution ID', 'ï»¿Institution', 'City', 'State/Province', 'Country']]

    # dropping duplicate ids then writing to the csv
    institutions = institutions.drop_duplicates(['Institution ID'])
    institutions.to_csv('Institutions.csv', index=False)

    # creating the csv for the teams, the same process as above
    teams = csv[['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']]
    teams = teams.drop_duplicates(['Institution ID'])
    teams.to_csv('Teams.csv', index=False)


if __name__ == '__main__':
    main()
