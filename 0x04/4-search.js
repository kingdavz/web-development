/**
 * a module that search and finds words in a sentence
 */

function findWord(sentence,search){
    let words = sentence.split(' ')
    for (let i = 0; i < words.length;i++){
        if (words[i] == search){
            console.log(words[i + 1])
            break
        }
    }
}



let sentence = "obi likes to play basketball during the weekend and play video games during weekdays"
findWord(sentence, 'weekend')