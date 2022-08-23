#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max=0;
        low=0;
        high=len(height)-1;
        while low< high:
            area=(high-low)*min(height[low],height[high]);
            Max=max(Max,area);
            if height[low]<height[high]:
                low+=1;
            else:
                high-=1;
        return Max;