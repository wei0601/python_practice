def top_k(nums,k):
    if not nums or k<=0:
        return []
    visited= {}
    for num in nums:
        if num in visited:
            visited[num]+=1
        else:
            visited[num]=1
    sorted_nums= sorted(visited.items(),key=lambda x:x[1],reverse=True)
    if k>len(sorted_nums):
        return [num[0] for num in sorted_nums]
    else:
        return [num[0] for num in sorted_nums[:k]]