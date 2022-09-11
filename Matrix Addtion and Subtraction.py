# mat1=[[1,2],[3,4]]

# mat2=[[1,2],[3,4]]

# res=[[0,0],[0,0]]

mat1=[1,2,3,4]
mat2=[1,2,3,4]
res=[0,0,0,0]

for i in range(4):
    res[i]+=mat1[i]+mat2[i]
print(res)