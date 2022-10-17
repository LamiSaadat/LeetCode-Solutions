/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    //input: string
    //output: boolean
   
    //create an array of alphabets
    const alphabets = [...Array(26)].map((_, i) => String.fromCharCode(i+97))
    
    //loop through the input string
    for(let i=0; i<alphabets.length; i++) {
        //if the input does not include an alphabet, return false
        if(!sentence.includes(alphabets[i])) return false
    }
    
    //otherwise, return true
    return true
};