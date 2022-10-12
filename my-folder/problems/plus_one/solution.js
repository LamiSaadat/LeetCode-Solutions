/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    //loop through the array backwards
    for(let i=digits.length - 1; i>=0; i--) {
        //if the current digit is 9, set it to 0
        if(digits[i] === 9) {
            digits[i] = 0
        } else {
            //otherwise increase it by 1 and return the array
            digits[i]++
            return digits
        }
    }
    //if all the values are 0, add a 1 to the beginning of the array
    return [1, ...digits]
};