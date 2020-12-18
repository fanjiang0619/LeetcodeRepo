class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest, count = 0, 0
        maximum = len(set(s))
        visited = []
        for i in range(len(s)):
            if s[i] in visited:
                idx = "".join(visited).rindex(s[i])
                del visited[:idx+1]
                visited.append(s[i])
                longest = max(count, longest)
                count = len(visited)
            else:
                count += 1
                visited.append(s[i])
                if count == maximum:
                    return count
        return max(count, longest)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        length, start = 0, 0
        maximum = len(set(s))
        visited = {}
        for i, c in enumerate(s):
            if c in visited and start <= visited[c]:
                length = max(length, i - start)
                start = visited[c] + 1
            else:
                if i - start == maximum:
                    return maximum
            visited[c] = i
        return max(length, len(s) - start)