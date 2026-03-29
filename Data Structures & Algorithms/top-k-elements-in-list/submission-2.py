class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        top = defaultdict(list)
        res = []
        for value, freq in count_nums.items():
            top[freq].append(value)
        s_top = sorted(top.items(), key=lambda x:x[0])
        print(s_top)
        while len(res)<k:
            res.extend(s_top.pop()[1])
        return res