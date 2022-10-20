/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    //input: integer
    //output: boolean
    
    //reverse the integer and store in a var
    //check if the input equals the reversed
        //if yes, return true
        //if not, return false
    
    const reversed = Number(x.toString().split('').reverse().join(''));
    
    const result = x === reversed ? true : false
    
    return result
};