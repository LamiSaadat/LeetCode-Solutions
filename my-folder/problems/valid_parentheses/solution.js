/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    //create a Map of the parantheses
    const map = new Map([["(", ")"], ["{", "}"], ["[", "]"]])
    
    //create an empty stack
    const stack = []
    
    //loop over string
    for(let i=0; i<s.length; i++) {
        //if current char exists in the map
            //push it to stack
        if(map.has(s[i])) {
            stack.push(map.get(s[i]))
        }
        //otherwise if the current element is corresponding closing bracket of the opening bracket in stack
            //remove the opening bracket from stack
        else if(stack.length > 0 && stack[stack.length -1] === s[i]) {
            stack.pop()
        }
        //otherwise
            //return false
        else {
            return false
        }
    }
    
    //at the end, if stack is empty, return true
    return stack.length === 0
    
};