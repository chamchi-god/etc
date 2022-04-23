# 채점을 위해 sys library 는 불러와야 합니다.
import sys

# pplinfo : 대기하는 인원 리스트 
def solution(pplinfo):
    arr1= [] 
    arr2= []
    arr3= []
    arr4= []
    arr5= []
    arr6= []
    arrX= [] #각각 1부, 2부, 3부, 4부, 5부, 6부, 입장불가
    i= two= four= six= 0 #각각 2개짜리 테이블, 4개짜리 테이블, 6개짜리 테이블
    def check(table, tableN, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i):
        if table//tableN ==0:
            arr1.append(i)
        elif table//tableN ==1: 
            arr2.append(i)
        elif table//tableN ==2:  
            arr3.append(i)
        elif table//tableN ==3:  
            arr4.append(i)
        elif table//tableN ==4:   
            arr5.append(i)
        elif table//tableN ==5:
            arr6.append(i)
        else:
            arrX.append(i) 

    def check4(table, tableSix, tableN, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i):
        if table//tableN ==0:
            arr1.append(i)
        elif table//tableN ==1:
            check(tableSix,1 ,arr1, arr2, arr2, arr2, arr2, arr2, arr2, i)
        elif table//tableN ==2:  
            check(tableSix,1 ,arr1, arr2, arr3, arr3, arr3, arr3, arr3, i)
        elif table//tableN ==3:  
            check(tableSix,1 ,arr1, arr2, arr3, arr4, arr4, arr4, arr4, i)
        elif table//tableN ==4: 
            check(tableSix,1 ,arr1, arr2, arr3, arr4, arr5, arr5, arr5, i)  
        elif table//tableN ==5:
            check(tableSix,1 ,arr1, arr2, arr3, arr4, arr5, arr6, arr6, i)
        else:
            arrX.append(i)         
    # TODO
    for j in range(0, len(pplinfo)):
        if pplinfo[j] == '1':
            i=i+1
            check(two, 4, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            two = two+1  
        if pplinfo[j] == '2':
            i=i+1
            check(two, 4, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            two = two+1       
        if pplinfo[j] == '3':
            i=i+1
            check(four, 2, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            four = four+1    
        if pplinfo[j] == '5':
            i=i+1
            check(six, 1, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            six = six+1
        if pplinfo[j] == '6':
            i=i+1
            check(six, 1, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            six = six+1
        if pplinfo[j] == '4':
            i = i+1
            check4(four,six, 2, arr1, arr2, arr3, arr4, arr5, arr6, arrX, i)
            if four//2 > six:
                six = six+1
            else: 
                four = four+1                                 
    ans = {}
    ans['1부'] = arr1
    ans['2부'] = arr2
    ans['3부'] = arr3
    ans['4부'] = arr4
    ans['5부'] = arr5
    ans['6부'] = arr6
    ans['입장불가'] = arrX
    return ans


# 채점을 위해 아래 코드는 수정하지 마세요.
if __name__ == '__main__':
    input_DIR = sys.argv[1]
    with open(input_DIR, "r") as input_file:
        pplinfo = input_file.read()

    submission = solution(pplinfo)
    print(submission)
