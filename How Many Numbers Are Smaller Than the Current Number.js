/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let output=[];
    for(let k=0;k<nums.length;k++){
        output[k]=0;
    }
    for(let i=0;i<nums.length;i++){
        for(let j=0; j<nums.length;j++){
            if(nums[i]!=nums[j] && nums[i]>nums[j]){
                output[i]++;
            }
        }
    }
    return output;
    
};
