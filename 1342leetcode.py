class Solution:

    def numberOfSteps(self, ar: int, count=0) -> int:
        if ar == 0:
            return count
        count += 1
        if ar % 2 == 0:
            return Solution.numberOfSteps(self, ar // 2, count)
        else:
            ar -= 1
            return Solution.numberOfSteps(self, ar, count)
