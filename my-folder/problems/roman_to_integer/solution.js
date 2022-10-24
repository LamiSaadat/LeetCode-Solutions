/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    //input: string
    //output: number
    
    //create a dictionary
    
    //initialize a result variable with 0
    
    //loop through the array
        //by using the dictionary, set the current and next elements to be values of the of the object's keys
        //check if the current element is smaller than the next element
            //if yes, subtract the current element from the next element and add it to the result, and move to the next iteration
            //if not, add the current element to the result
    //return result
   
    
    const romanNums = {I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
    
    let result = 0
    
    for(let i=0; i<s.length; i++) {
        let curr = romanNums[s[i]]
        let next = romanNums[s[i+1]]
        
        if(curr < next) {
            result += next - curr
            i++
        } else {
            result += curr
        }
    }
    
    
    return result
    
};