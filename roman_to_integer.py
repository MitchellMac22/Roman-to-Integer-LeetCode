class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {}
        # Store the known conversions
        mapping["I"] = 1
        mapping["V"] = 5
        mapping["X"] = 10
        mapping["L"] = 50
        mapping["C"] = 100
        mapping["D"] = 500
        mapping["M"] = 1000

        total = 0
        for i in range(len(s)):
            if i < len(s)-1:
                if(mapping[s[i]] < mapping[s[i+1]]):
                    total-=mapping[s[i]]
                else:
                    total+=mapping[s[i]]
            else:
                total+=mapping[s[i]]
        return total
