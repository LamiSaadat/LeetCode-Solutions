/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let largestIndex = 0;
    
   for(let i=0; i<nums.length; i++) {
       if(nums[i] > nums[largestIndex]) {
           largestIndex = i
       } 
   }
    
    for(let i=0; i<nums.length; i++) {
        if(largestIndex !== i && (nums[i] * 2) > nums[largestIndex]) {
            return  -1
        } 
        
    }
    return largestIndex
};