/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let newArr = []
    newArr[0] = nums[0]
    for(let i=1; i<nums.length; i++) {
        newArr.push(nums[i]+=nums[i-1])
    }
    return newArr
};