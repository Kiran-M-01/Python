class Solution:
    def maxArea(self, height: List[int]) -> int:

        # BRUTE FORCE APPROACH
        # res = 0
        # for l in range(len(height)):
        #     for r in range(len(height)):
        #         area = (r - 1) * min(height[l],height[r])  ==> A=Width×Height
        #         res = max(res, area)
        # return res


        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l],height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res












        l,r = 0,len(height)-1
        maxW = 0
        while l < r:
            area = (r - l) * min(height[l], height(r))
            maxW = max(maxW, area)
            
            if height[l] < height[r]:
                l += 1
            else :
                r += 1
        return maxW
