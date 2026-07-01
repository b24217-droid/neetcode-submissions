class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        match = {
                "{" : "}",
                "(" : ")",
                "[" : "]"
        }
        for char in s:
            if char in "{[(":
                st.append(char)
            else:
                if not st:
                    return False
                bracket = st.pop()
                if char != match[bracket]:
                    return False

        return len(st) == 0