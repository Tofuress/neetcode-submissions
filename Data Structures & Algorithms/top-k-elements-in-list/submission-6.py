class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        dct = defaultdict(list)

        for i in nums:
            dct[i] = dct.get(i, 0) + 1
        for key, val in dct.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
