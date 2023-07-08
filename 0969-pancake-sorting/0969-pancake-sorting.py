class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        num = 1
        if sorted(arr) == arr:
            return ans
        while num < n:
            flag = False
            for i in range(n - num):
                if arr[i] == num:
                    arr[:i + 1] = arr[:i + 1][::-1]
                    ans.append(i + 1)
                    flag = True
                    break
            if flag:
                arr[:n - num + 1] = arr[:n - num + 1][::-1]
                ans.append(n - num + 1)
            
            num += 1
        ans.append(n)
        return ans
