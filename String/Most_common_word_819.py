from string import punctuation
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = [word.strip(punctuation).lower() for word in paragraph.split()]
        counter = collections.Counter(paragraph)
        banned = set(banned)
        for word, count in counter.most_common():
            if word not in banned:
                return word
        return None
        
