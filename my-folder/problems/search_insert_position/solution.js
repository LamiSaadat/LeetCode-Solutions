/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    for (let i=0; i<nums.length; i++) {
        if (nums[i] != target && nums[i] < target) {
            if(nums[i+1] > target) {
                return i+1
            }
            else if (i == nums.length-1) {
                return i+1
            }
        } else {
            return i
            }
    }
};