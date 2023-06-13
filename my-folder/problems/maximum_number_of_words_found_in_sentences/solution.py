class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentence_lengths = []

        for sentence in sentences:
            sentence_lengths.append(len(sentence.split(' ')))
        
        return max(sentence_lengths)


