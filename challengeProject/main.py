if __name__ == '__main__':

    import csv

    with open('MontanaCounties.csv', newline='') as data:

        reader = csv.reader(data)

        done = False
        while not done:

            plateNum = input('Type the License Plate you wish to look up: ')

            if len(plateNum) == 0:
                print('thank you for using this software')
                done = True

            elif len(plateNum) < 2:
                print('too short of an entry')

            else:

                print(f'searching for {plateNum}')
                temp = ''
                for i in plateNum:
                    if i.isdigit():
                        temp = temp + i
                    else:
                        break

                print(f'searching for prefix: {temp}')

                found = False

                for row in reader:

                    if temp == row[2]:

                        found = True
                        print(f'County: {row[0]} \n County Seat: {row[1]}')

                if not found:

                    print('Not found')

                data.seek(0)