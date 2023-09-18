class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Count every row.
        for row in range(len(mat)):
            sold_count: int = 0
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    sold_count += 1
                    continue
                break
            mat[row] = [sold_count, row]
        # Sort by soldiers, ascending.
        mat.sort()
        # Can be changed to return mat[:k], with change of first k elements of mat for O(1).
        # But, then I need to change input|out annotations. So it's extra O(k) space for a new list.
        # Assume we're not allowed to do that.
        return [row[1] for row in mat[:k]]
        