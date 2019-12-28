def check(g_input,A,B,p):
    i1=0
    x=y=z=i2=0
    i3=0  
    r=False
    r2=False
    a=b=c=r3=False
    for i in [1,2,3]:
        if g_input==i:
            i1=1
            A[i-1]=p
            display()
            
    for i in [4,5,6]:      
        if g_input==i:
            i2=1
            B[i-4]=p
            display()  
    for i in [7,8,9]:          
        if g_input==i:
            i3=1
            C[i-7]=p
            display()
            
        #Checking if the row is same 
        
    if i1!=0 and (A[0] ==A[1] == A[2]):
                  r=True
        
    elif i2!=0 and (B[0]==B[1]==B[2]):
        r=True
            
    elif i3!=0 and (C[0]==C[1]==C[2]):
        r=True
            #Checking columns is same or not
            
    for i in [0,1,2]:
            if A[i]==B[i]==C[i]:
                r2=True
                    
                    
            #Check diagonally 
    if (A[0]==B[1]==C[2]) or (A[2]==B[1]==C[0]):
        r3=True
                
    
    #Check if array is full
    for i in [1,2,3]:
        if A[i-1]!=i:
            x+=1
    if x==2:
        a=True

        
    for i in [4,5,6]:
        if B[i-4]!=i:
            y+=1
    if y==2:
        b=True

        
    for i in [7,8,9]:
        if C[i-7]!=i:
            z+=1
    if z==2:
         c=True

                      
    if (a and b and c):
        flag=1
        print('Tie and No space available')
        return True
    
    return (r or r2 or r3)


def display():
        print (f'   {A[0]}   |    {A[1]}    |    {A[2]}      \n')
        print('--------------------------------------------\n')
        print (f'   {B[0]}   |    {B[1]}    |    {B[2]}       \n')
        print('---------------------------------------------\n')
        print(f'    {C[0]}   |    {C[1]}    |    {C[2]}        \n')




play_cont=True
while play_cont==True:
    player1=input('Do you want to be X or O? \n')
    if player1=='X':
        player2='O'
    elif player1=='O':
        player2='X'
    t=False

    A=[1,2,3]
    B=[4,5,6]
    C=[7,8,9]
    i=0
    count=1
    t1=t2=False
    flag=0
    while t==False and count<10:
        if i%2==0:
            g_input=int(input('P1 Pick you position from 1 to 9 \n'))
            t=check(g_input,A,B,player1)
            t1=t
        else:
            g_input=int(input('P2 Pick you position from 1 to 9 \n'))
            t=check(g_input,A,B,player2) 
            t2=t 
        i+=1
        count+=1
    else:
        if t1==True:
            print('Congrats player1 !! you won')
        elif t2==True:
            print('Congrats player2 !! you won')
        elif count==10:
            print('Tie')

    p=input('Do you wanna play again? Y or N\n')
    if p=='Y':
        play_cont=True
    else:
        print('\n Good Bye and have a good day!!')
        play_cont=False


