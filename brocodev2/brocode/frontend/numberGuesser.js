easyStreak = 0;
hardStreak = 0;
easyLives = 3;
hardLives = 5;
easyRandNum = 0;
hardRandNum = 0;

var myName;


window.onload=function(){


    myName=prompt("please enter a name","");

    document.getElementById("name").innerHTML=myName;
   
}

function guessNumber(isHard) {
    
    if (isHard != true) {
        // random number from 1 to 3 
        if (easyRandNum == 0) {
            randomNumber = Math.floor(Math.random() * 3) + 1;
            easyRandNum = randomNumber;
        }
        guessedNumber = document.getElementById("easyguess").value;
        console.log(easyRandNum)

        console.log(guessedNumber)
        
        
        
        if (guessedNumber == easyRandNum) {
            easyStreak++;
            easyRandNum = 0;
            document.getElementById("mystery-num").innerHTML = easyStreak;
            alert("You have " + easyStreak + " streak");
            
    
            
            return;
        }


        
        easyLives--;
        
        if (easyLives == 0) {
            alert("You lose");
            easyStreak = 0;
            easyRandNum = 0;
            easyLives = 3;
            tryAgainEasy()
            return;
        } else {
            alert("You have " + easyLives + " lives left");
        }
        return;
    }
    if (hardRandNum == 0) {
        randomNumber = Math.floor(Math.random() * 7) + 1;
        hardRandNum = randomNumber;
    }
    guessedNumber = document.getElementById("hardguess").value;
    console.log(hardRandNum)
    console.log(guessedNumber)
    if (guessedNumber == hardRandNum) {
        hardStreak++;
        hardRandNum = 0;
        document.getElementById("mystery-num").innerHTML = hardStreak;
        alert("You have " + hardStreak + " streak")
        return;
    }

    hardLives--;
    
    if (hardLives == 0) {
        alert("You lose");
        hardStreak = 0;
        hardRandNum = 0;
        hardLives = 5;
        tryAgainHard()
        return;
    } else {
        alert("You have " + hardLives + " lives left");
    }
}