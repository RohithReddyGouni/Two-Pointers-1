#Time Complexity: O(n2)
#Space Complexity: O(1) or O(n)(If library stores the sorted values)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[];
        nums.sort();
        for index,value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue;
            low=index+1;
            high=len(nums)-1;
            while low < high:
                Sum=value+nums[low]+nums[high];
                if Sum >0:
                    high=high-1;
                elif Sum <0:
                    low=low+1;
                else:
                    result.append([value,nums[low],nums[high]]);
                    low+=1;
                    while nums[low]==nums[low-1] and low<high:
                        low+=1;
        return result;



#Second Solution:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[];
        nums.sort();
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue;
            low=i+1;
            high=len(nums)-1;
            while low<high:
                sum=nums[i]+nums[low]+nums[high];
                if sum>0:
                    high-=1;
                elif sum<0:
                    low+=1;
                else:
                    result.append([nums[i],nums[low],nums[high]]);
                    while low<high and nums[low]==nums[low+1] :
                        low+=1;
                    while low<high and nums[high]==nums[high-1]:
                        high-=1;
                    low+=1;
                    
        return result;