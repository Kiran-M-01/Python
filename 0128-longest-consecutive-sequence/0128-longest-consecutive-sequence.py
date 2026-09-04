class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longestSeq = 0

        # for num in numSet:
        #     if (num - 1) not in numSet:   # CHECKING FOR LEFT NEIGHBOUR
        #         length = 0
        #         while (num + length) in numSet: #STARTING THE SEQUENCE FROM CURRENT NUM ITSELF
        #             length += 1       # UPDATING LENGTH --> USED AS BOTH LENGTH OF SEQUENCE AND NEXT NUMBER
        #         longestSeq = max(length, longestSeq)
        # return longestSeq
        numSet = set(nums)
        maxLength = 0
        for num in numSet:
            if (num-1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                
                maxLength = max(maxLength, length)
        
        return maxLength
                









