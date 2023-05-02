class Solution:
    def average(self, salary: List[int]) -> float:
        salary_sorted = sorted(salary)

        salary_sorted.remove(salary_sorted[0])
        salary_sorted.remove(salary_sorted[len(salary_sorted) - 1])

        sum = 0
        for item in salary_sorted:
            sum += item
        
        average = sum / len(salary_sorted)

        return average