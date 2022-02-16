def numCheck(checkString):
    for character in checkString:
        if character.isdigit():
            return True

    return False


if __name__ == '__main__':

    import csv

    with open('MontanaCounties.csv', 'w', newline='') as data:

        reader = csv.reader(data)
        writer = csv.writer(data)

        done = False
        while not done:

            cityName = input('Type the City you wish to look up information on. Enter Blank line when done: ')

            if len(cityName) == 0:
                print('thank you for using this software')
                done = True

            elif len(cityName) < 2:
                print('too short of an entry')

            elif numCheck(cityName):
                print('incorrect format')

            else:

                print(f'searching for {cityName}')

                empty = '-'
                found = False

                for row in reader:

                    if cityName.lower() == row[1].lower():

                        found = True

                        if row[0] == '-' or row[2] == '-':

                            if row[0] == '-':
                                print('data incomplete, please provide the county name')
                                print('leave blank if unknown')

                                nameinput = input('county name:')

                                if len(nameinput) != 0:
                                    row[0] = nameinput
                                    writer.writerow(row)

                            if row[2] == '-':
                                print('data incomplete, please provide license prefix')
                                print('leave blank if unknown:')

                                prefixinput = input('county prefix:')

                                if len(prefixinput) != 0:
                                    row[2] = prefixinput
                                    writer.writerow(row)

                        print('[1] show county name')
                        print('[2] show county license prefix')
                        print('[3] show all')
                        resultinput = input('input:')

                        if resultinput == 1:
                            print(row[0])
                        elif resultinput == 2:
                            print(row[2])
                        else:
                            print(f'{row[0]}, {row[1]}, {row[2]}')

                if not found:

                    print('Not found')
                    newEntry = input('would you like to create a new entry? (y/n):')

                    if newEntry.lower() == 'y':
                        nameinput = input('enter the county name:')
                        prefixinput = input('enter the license plate prefix')

                        row = [nameinput, cityName, prefixinput]
                        writer.writerow(row)

                data.seek(0)