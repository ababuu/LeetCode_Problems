/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let output=[];
    let temp=0;
    for(let i=0;i<nums.length; i++){
        for(let j=0;j<nums.length;j++){
            if(nums[i]<nums[j]){
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
            }
        }
    }
    for(let i=0;i<nums.length; i++){
        if(nums[i]==target){
            output.push(i);
        }
    }
    
    return output;
    
};
