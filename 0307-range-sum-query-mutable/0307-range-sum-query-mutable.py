class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree= [0]*(4*self.n)
        self.build(1,0,self.n-1)
    def build(self, node, start, end):
        if start == end :
            self.tree[node] = self.nums[start]
            return
        mid = (start + end ) // 2
        self.build (node*2,start,mid)
        self.build(node*2 +1 , mid + 1, end)

        self.tree[node] = self.tree[node*2]+ self.tree[node*2 +1]
    def updateTree(self,node, start, end, idx, val):
        if start == end :
            self.tree[node] = val
            self.nums[idx]  = val
        
            return
        mid = (start + end) //2
        if idx<= mid:
            self.updateTree(node*2,start,mid, idx, val)
        else:
            self.updateTree(node*2+1,mid+1, end, idx, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, start, end, left, right):
        
        if right < start or left > end:
            return 0

        
        if left <= start and end <= right:
            return self.tree[node]

      
        mid = (start + end) // 2

        left_sum = self.query(node * 2, start, mid, left, right)
        right_sum = self.query(node * 2 + 1, mid + 1, end, left, right)
        return left_sum + right_sum 
 
    def update(self, index: int, val: int) -> None:
        self.updateTree(1,0,self.n-1, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1,0,self.n-1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)