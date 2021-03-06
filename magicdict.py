class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        ans = []
        self.wordSet = set(words)
        for word in words:
            self.wordSet.remove(word)
            if self.search(word):
                ans.append(word)
            self.wordSet.add(word)
        return ans

    def search(self, word):
        if word in self.wordSet:
            return True
        for idx in range(1, len(word)):
            if word[:idx] in self.wordSet and self.search(word[idx:]):
                return True
        return False
val=Solution()
words=list(map(str,input().split()))
print(*val.findAllConcatenatedWordsInADict(words))
