Question_Link: https://www.codingninjas.com/codestudio/problems/print-like-a-wave_893268
    
    
def wavearray(list,nrows,ncols):
    ans=[]

    for j in range(ncols):
     if j%2==0:       
        for i in range(nrows):
            ans.append(list[i][j])
     else:
        for i in reversed(range(nrows)):
            ans.append(list[i][j])
    
    print(ans)


list=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

wavearray(list,5,3)






            
