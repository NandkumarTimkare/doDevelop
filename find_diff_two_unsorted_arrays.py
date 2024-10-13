l1 = [1,3,5,7,1,3]
l2 = [1,2,3,4,5,6,2]
#Diff = {2,4,6,7}

l1.sort()
l2.sort()
i = j = 0
out = []
prevRep = None
prevDiff = None
while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
        prevRep = l1[i]
        i += 1
        j += 1
        
    elif l1[i] < l2[j]:
        if prevRep != l1[i] and prevDiff != l1[i]:
            out.append(l1[i])
            prevDiff = l1[i]
        i += 1
    elif l2[j] < l1[i]:
        if prevRep != l2[j] and prevDiff != l2[j]:
            out.append(l2[j])
            prevDiff = l2[j]
        j += 1
        
if i < len(l1):
    out.extend(list(set(l1[i:])))
elif j < len(l2):
    out.extend(list(set(l2[j:])))
    
print(out)

