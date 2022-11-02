/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    //input: array
    //output: number
    
    //record number of unique elements to track the length of the unique elements
    
    //loop over the array
        //check if current element is the same as the previous element
            //if not, set the current element to the current record to the current element
            //increment the record
    
    //return the record
    
    let k = 0
    
    for(let i=0; i< nums.length; i++) {
        if(nums[i] !== nums[i-1]){
            nums[k] = nums[i];
            k++
        }
        
    }
    return k
    
};