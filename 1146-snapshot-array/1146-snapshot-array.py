class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [[(0, 0)] for _ in range(length)]
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    def get(self, index: int, snap_id: int) -> int:
        values = self.arr[index]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return values[right][1]