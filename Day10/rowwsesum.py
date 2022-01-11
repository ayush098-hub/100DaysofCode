def rowwisesum(array):

    largestsum=[]

    maxi=array[0][0]

    for i in range(len(array)):
        sum=0
        for j in range(len(array[i])):
            sum+=array[i][j]
        print("Row wise sum",sum)
        largestsum.append(sum)

        if sum>maxi:
            maxi=sum

    # print("Largest sum is:",max(largestsum)) 
    print(maxi)
    
    # for j in range(len(array[i])):
    #     sum=0
    #     for i in range(len(array)):
    #         sum+=array[i][j]
    #     print("column wise sum",sum)





array=[[24,1,2],[26,1,2],[25,1,2]]

rowwisesum(array)
