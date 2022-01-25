
if __name__ == '__main__':

    #using a queue here to keep track of the text for the editor since we want text to be saved in order
    from queue import Queue

    #arbitrarily making the max sze of the queue 1000
    textQueue = Queue(maxsize=1000)

    #variable to let user know which line they are at
    lineCount = 1

    #the loop, continually receives string input from the user until either they enter a blank line or fill the queue
    end = False
    while not end:
        tempText = input(f'Line {lineCount}, enter blank line when done: ')

        if len(tempText) == 0:
            break
        elif not textQueue.not_full:
            print('too much text, save this file and make another')
        else:
            textQueue.put(tempText)
            lineCount += 1

    #letting user name their file
    fileName = input('Name your file:')

    #making sure they actually named the file
    if len(fileName) == 0:
        fileName = 'default'

    #creating a big string to save all the text into the file, making sure there is something in the queue to
    #begin creating the big string
    if not textQueue.empty():
        finalString = textQueue.get()
    else:
        finalString = ''

    #looping through the queue and adding line breaks until the queue is empty
    while not textQueue.empty():
        finalString = (finalString + '\n' + textQueue.get())

    #finally we write the big string to the file
    with open(fileName, 'w') as file:
        file.write(finalString)
