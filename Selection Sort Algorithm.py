def sort(seq):
    seq= list(seq)
    
    ln=len(seq)
    c=0
    for i in range(0,len(seq)):
        if i < ln-1:
            
            if seq[(i+1)] < seq[i]:
                seq[i+1],seq[i] = seq[i],seq[i+1]
                c+=1
                print(seq)
                
        elif c != 0:
            sort(seq)
            break
            
sort((-3,2,6,7,1,9,80))
