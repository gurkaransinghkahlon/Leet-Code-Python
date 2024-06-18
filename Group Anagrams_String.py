from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_map = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            anagram_map[sorted_str].append(str)

        res.extend(anagram_map.values())
        return res
