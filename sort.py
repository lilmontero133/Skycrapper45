class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        return merge_sort(nums)


# ---- Test cases ----
sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))      # [1, 2, 3, 5]
print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # [0, 0, 1, 1, 2, 5]
