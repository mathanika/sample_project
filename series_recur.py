#n=int(input("enter the value for n"))
#k=int(input("enter the value of k"))
n=20
k=4
c=0
def series(n,s,k,c):
    if((s>0)and(c==0)):
        s=s-k
        print(s)
        series(n,s,k,c)		
    else:
        c=1	
        if(s!=n):
            s=s+k
            print(s)
            series(n,s,k,c)			
        else:
            return 0
series(n,n,k,c)      
