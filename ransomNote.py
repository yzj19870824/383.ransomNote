__author__ = 'jerry'

import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # for item in ransomNote:
        #     if magazine.count(item) == 0:
        #         return False
        #
        # return True
        # if magazine.count(ransomNote) == 0:
        #     return False
        # return True

        ransomNoteCnt = collections.Counter(ransomNote)
        magazineCnt = collections.Counter(magazine)
        return not ransomNoteCnt - magazineCnt

if __name__ == "__main__":
    so = Solution()
    ransomNote = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"

    print(so.canConstruct(ransomNote,magazine))
