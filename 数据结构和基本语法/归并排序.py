class MergeSort:
    def merge(self,nums1,nums2):
        i,j = 0,0
        res=[]
        while i<len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < len(nums1):
            res.extend(nums1[i:])
        elif j < len(nums2):
            res.extend(nums2[j:])
        return res
    def merge_sort(self,nums):
        mid = len(nums)//2
        if mid >0:
            nums1 = self.merge_sort(nums[:mid])
            nums2 = self.merge_sort(nums[mid:])
            res = self.merge(nums1,nums2)
        else:
            res = nums
        return res
def main():
    nums = [1,2,3,4,5,6,7,8,9]
    print(MergeSort().merge_sort(nums))
if __name__ == '__main__':   
    main()