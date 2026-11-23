class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Search on the smaller array so the search is on the shorter array
        if len(nums1) <= len(nums2):
            n1, n2 = nums1, nums2
        else:
            n1, n2 = nums2, nums1

        len1 = len(n1)
        len2 = len(n2)
        left_size = (len1+len2+1)//2
        l=0 #At a minimum how many elements need to be considered from n1 on the left-side
        r=len1 #At a maximum how many elements need to be considred from n2 on the left-side
        #print(f'left-size: {left_size}, l = {l}, r = {r}, n1: {n1}, n2: {n2}')
        while (l<=r):
            m1=(l+r)//2 #No of elements from l1 to be considered on the left
            m2=left_size-m1 #No of elements from l2 to be considered on the left
            #print(f'm1: {m1}, m2: {m2}')
            #print(f'l = {l}, r = {r}')
            l1 = n1[m1-1] if m1>0 else -float('inf') #if 0 elements need to considered: -inf else m1-1
            l2 = n2[m2-1] if m2>0 else -float('inf') #if 0 elements need to considered: -inf else m2-1
            r1 = n1[m1] if m1<len(n1) else float('inf')
            r2 = n2[m2] if m2<len(n2) else float('inf')
            #print(f'l1 = {l1}, l2 = {l2}, r1={r1}, r2={r2}')
            if l1<=r2 and l2<=r1:
                #can find median
                #print(f'Can find median')
                if (len1 + len2)%2 == 0:
                    return (max(l1,l2)+min(r1, r2))/2
                return max(l1,l2)
            elif l2>r1:
                #search in right-space
                l=m1+1
            else:
                r=m1-1
            #end if
        #end while