/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    //modify nums1 in place 
    
    //length of nums1 is m+n but m elements should be merged
        //splice nums1 at m
    //loop over nums2 and push each element into nums1

    nums1.splice(m)
    
    nums2.forEach(num => nums1.push(num))
    
    nums1.sort((a,b) => a-b)

};