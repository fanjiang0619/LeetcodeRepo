class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^A-Za-z ]+', ' ', paragraph)
        paragraph = paragraph.split()
        count = {}
        for i in paragraph:
            count[i.lower()] = count.get(i.lower(), 0) + 1
        for j in banned:
            count.pop(j, None)
        return sorted(count.items(), key=lambda x: x[1], reverse=True)[0][0]