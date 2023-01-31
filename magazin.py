class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomList, magazineList = list(ransomNote), list(magazine)
        while True:
            for i in ransomList:
                if i in magazineList:
                    ransomList.remove(i)
                    magazineList.remove(i)
                    if len(ransomList) == 0:
                        return True
                else:
                    return False