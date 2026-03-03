def longestEmptySequence(stalls:list):
    max_len = 0
    longest_range = (0,0)
    i = 0
    while i < len(stalls):
        if not stalls[i]:
            start = i
            while i < len(stalls) and not stalls[i]:
                i += 1
            length = i - start
            if length > max_len:
                max_len = length
                longest_range = (start, i - 1)
        else:
            i += 1
    
    return longest_range if max_len > 0 else None
                
    
    
#main code
stalls = [False for _ in range(10)]

lowerBound = 0
upperBound = len(stalls)-1

for _ in range(10):
    seq = longestEmptySequence(stalls)
    if not seq:    
        print("No empty stalls left")
        break
    lowerBound, upperBound = seq
    stalls[(lowerBound + upperBound)//2] = True
    
    print(stalls)
