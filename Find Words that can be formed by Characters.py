def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result = 0
        char_count = [0]*26

        for c in chars:
            char_count[ord(c)-ord('a')] += 1

        for word in words:
            valid_chars = 0
            tmp_chars = char_count[:]

            for c in word:
                index = ord(c) - ord('a')
                if tmp_chars[index] > 0:
                    valid_chars += 1
                    tmp_chars[index] -= 1

            if valid_chars == len(word):
                result += len(word)

        return result