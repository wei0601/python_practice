class QickSort:
    def quickSort(self,nums):
        if len(nums)<=1:
            return nums
        else:
            pivot = nums[0]
            Left = [x for x in nums[1:] if x <= pivot]
            Right = [x for x in nums[1:] if x > pivot]
            return self.quickSort(Left)+[pivot]+self.quickSort(Right)
def main():
    OickSort = QickSort()
    nums = [3,6,8,10,1,2,1]
    print(OickSort.quickSort(nums))
if __name__ == "__main__":
    main()