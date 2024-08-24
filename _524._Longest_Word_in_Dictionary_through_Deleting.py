class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        answer = ""
        for word in dictionary:
            if len(word) >= len(answer):
                if len(answer) == len(word) and sorted([answer,word])[0] == answer:
                    continue
                else:
                    current = s
                    for letterCount, letter in enumerate(word):
                        if letter not in current:
                            break
                        else:
                            current = current[current.index(letter)+1:]
                            if letterCount == len(word)-1: answer = word
        return answer
                        
print(Solution().findLongestWord("abce",["abe","abc"]))
