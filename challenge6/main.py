import pandas


def main():

    # reading the csv and creating the dataset as csv
    csv = pandas.read_csv("2015.csv")

    # this adds a new column called institution id and all
    # columns with the same institution and city have the same institution id
    csv['Institution ID'] = csv.groupby(['ï»¿Institution', 'City']).ngroup()

    # trying to get a count of all the times an institution entered a team
    csv['Teams Entered'] = csv['Institution ID'].value_counts()

    # sorting the csv and outputting it to a new csv file
    ordered = csv[['Institution ID', 'ï»¿Institution', 'City', 'State/Province', 'Country', 'Teams Entered']]
    ordered = ordered.sort_values('Teams Entered', ascending=False)
    ordered.to_csv('Ordered.csv', index=False)

    # getting all the outstandingTeams
    teams = csv[['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']]

    # loc is basically panda's version of a select statement
    outstanding = teams.loc[teams['Ranking'] == 'Outstanding Winner']
    outstanding.to_csv('OutstandingTeams.csv', index=False)

    # getting all the meritorious us teams
    usTeams = csv.loc[csv['Country'] == 'USA']
    usTeams = usTeams[['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']]
    usTeams = usTeams.loc[usTeams['Ranking'].isin(['Meritorious', 'Finalist', 'Outstanding Winner'])]
    usTeams.to_csv('UsWinners.csv', index=False)

    # getting a txt file with the average number of teams entered per institution
    mean = csv['Teams Entered'].mean()
    file = open('MeanTeamsEntered.txt', 'w')
    file.write(repr(mean))




if __name__ == '__main__':
    main()
