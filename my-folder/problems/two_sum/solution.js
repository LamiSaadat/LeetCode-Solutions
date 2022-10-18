/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //input: array
    //output: array of indeces
    
    //loop over nums array from the first index
        //loop over array from the next index
            //check if first loop's el and second loop's el add up to target
                //if yes, return the ideces
    
    for(let i=0; i<nums.length; i++) {
        for(let j=i+1; j<nums.length; j++) {
            if(nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }
    
};