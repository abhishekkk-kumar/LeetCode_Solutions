class Solution:
    def average(self, salary: List[int]) -> float:
        ans=(sum(salary)-max(salary)-min(salary))/(len(salary)-2)
        return ans
        