class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):

                if j >= len(strs[i]):
                    return prefix

                if strs[i][j] != strs[0][j]:
                    return prefix

            prefix += strs[0][j]

        return prefix


a = Solution()

print(a.longestCommonPrefix(["flower", "flow", "flower"]))