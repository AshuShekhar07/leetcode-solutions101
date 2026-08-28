class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for x in s:
            stack.append(x)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        