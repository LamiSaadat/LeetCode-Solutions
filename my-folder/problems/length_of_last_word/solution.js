/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    //split string into an array
    //get the last element
    //return length of the element

    let result = s.trim().split(' ').slice(-1)[0].split('').length;
    return result
};