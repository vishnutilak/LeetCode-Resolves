def twoSum(self, nums:List[int], target:int)->List[int]:
    store_dict ={}

    for j, num in enumerate(nums):
        #nums[i]+nums[j] == target
        if target- nums[j] in store_dict:
            return (store_dict[target- nums[j]], j)
        store_dict[num] =j