/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let hash = {}

    for (let i=0; i<nums.length; i++) {
        if (!(nums[i] in hash)) {
            hash[nums[i]] = i
        } else {
            if (Math.abs(hash[nums[i]] - i) <= k) {
                return true
            } else {
                hash[nums[i]] = i
            }
        }
    }
        return false

};

// two distinct elements are the same and the difference of their indeces is less than equal to k
// hash = {}
// loop over the array to find two of the same element, and if found, check if their difference is less than or euqal to k