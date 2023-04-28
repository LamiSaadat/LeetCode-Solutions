/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {   
    let i = 0;
    
    while(
        strs[0][i] && 
        strs.every((word) => {
            return word[i] === strs[0][i]
        }) 
        ){
        i++
    }
    return strs[0].substring(0, i)

};