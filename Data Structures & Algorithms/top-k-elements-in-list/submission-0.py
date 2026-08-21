from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # this gives us the frequency count
        f: dict[int, int] = defaultdict(int)
        for n in nums:
            f[n] += 1
        
        # Now bucket sort!
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for num, count in f.items():
            buckets[count].append(num)

        results: list[int] = []

        i: int = len(buckets) - 1
        while len(results) < k:
            if len(buckets[i]) == 0:
                i -= 1
                continue
            r: int = buckets[i].pop()
            results.append(r)
        return results            