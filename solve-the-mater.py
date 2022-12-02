if __name__ == '__main__':
    y=full_list=[]
    x=student_grad_list=[]
    i=new_y=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        y.append([name,score])


        
size=len(y)
y.sort(key= lambda col:(col[1],col[0]))
lowest=second_lowest=y[0][1]
t=updat_lowest= False
i=0
while 1<size:
   if lowest< y[i][1]:
       second_lowest=lowest
       update_lowest=1

    if t==1:
        print(y[i][0])
        
    if lowest !=second_lowest:
        bresk
    i+=1    
 
            

print(y)
#make a new repository in github
