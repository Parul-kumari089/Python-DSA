class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)
        ans = []
        for height, name in people:
            ans.append(name)
        return ans