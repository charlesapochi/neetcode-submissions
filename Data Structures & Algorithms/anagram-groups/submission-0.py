class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # this creates a default hashmap to group anagrams 

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(s) # using tuple because list cant have keys
        
        return list(result.values())

        # the time ccomplexity for this is O(m*n) where m is the inputs given and n is the lenght of each string 