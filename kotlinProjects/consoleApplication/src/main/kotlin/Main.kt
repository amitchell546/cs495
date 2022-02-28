import kotlin.random.Random.Default.nextInt

fun main(args: Array<String>) {

    //main game loop
    var finished = false
    while(!finished) {

        //selecting our word
        val tempWord = selectWord()

        println("Guess the 5 letter word. Type your guess below.")
        println("X means the letter is incorrect")
        println("O means the letter is located somewhere else in the word")
        println("C means you got the letter and position correct")

        //loop for guessing the word
        var correct = false
        while(!correct) {

            var guessInput = readLine()
            correct = checkGuess(guessInput!!.lowercase(), tempWord)
        }

        println("play again? Y/N")
        var againInput = readLine()
        if(againInput!!.uppercase()!="Y"){
            finished = true
        }

    }
}

//function for selecting our word
fun selectWord(): String {

    val wordArrays = arrayOf("rated","train","crane","irate", "write")
    val randomInt = nextInt(wordArrays.size-1)

    return(wordArrays[randomInt])
}

fun checkGuess(guess: String, correct: String): Boolean{

    if(guess.length!=correct.length){
        return false
    }
    else{

        var correctBoolean = true

        val guessArr = guess.split("")
        val correctArr = correct.split("")
        var returnArr = arrayOfNulls<Char>(5)

        for(i in 1..5){

            var guessChar = guessArr[i]

            //checking if the characters are exact matches
            if(guessChar == correctArr[i]){
                returnArr[i-1] = 'C'
            }
            //checking if any of the other characters are matches
            else{
                returnArr[i-1] = 'X'
                correctBoolean = false

                for(j in 1..5){
                    if(guessChar == correctArr[j]){
                        returnArr[i-1] = 'O'
                    }
                }
            }
        }

        var returnString = ""
        for(char in returnArr){
            returnString += char
        }
        println(returnString)

        return correctBoolean;
    }
}