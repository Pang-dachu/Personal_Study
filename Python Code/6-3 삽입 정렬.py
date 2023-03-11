array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array) ) :
    print("i의 값 :", i)
    for j in range(i,0,-1) : 
        print("j의 값 :", j)
        if array[j] < array[j-1] : 
            # 한칸씩 왼쪽이동 
            array[j], array[j-1] = array[j-1], array[j]
            print( array )
        else :
            # 왼쪽이 더 작은 경우 
            break
        

print( array )