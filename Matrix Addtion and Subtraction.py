#Matrix Addition/Subtraction

def mat_add(mat1,mat2):
    res=[0,0,0,0]
    for i in range(4):
        res[i]+=mat1[i]+mat2[i]
    return res


def mat_sub(mat1,mat2):
    res=[0,0,0,0]
    for i in range(4):
        res[i]-=mat1[i]-mat2[i]
    return res



mat1=[5,2,3,4]
mat2=[1,2,3,4]

print(mat_add(mat1,mat2))

print(mat_sub(mat1,mat2))
