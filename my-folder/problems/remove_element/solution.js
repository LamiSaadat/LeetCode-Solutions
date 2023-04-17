/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for(let i=0; i<nums.length; i++) {
        if(nums[i] === val) {
            nums.splice(i, 1, "_")
        }
    }

    nums.sort()

    for(let i=0; i<nums.length; i++) {
        if(nums[i] === "_") {
            nums.splice(i)
        }
    }
    
};