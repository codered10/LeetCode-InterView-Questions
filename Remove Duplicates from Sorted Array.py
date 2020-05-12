class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        extraNums = 0
        if len(nums) is 0:
            return 0
        uniqueNum = nums[0]
        #print(nums[0])
        for i in range(1,len(nums)):
            if nums[i] != uniqueNum:
                uniqueNum = nums[i]
                nums[i- extraNums] = uniqueNum
            else:
                extraNums += 1
        return(len(nums)-extraNums)
        
