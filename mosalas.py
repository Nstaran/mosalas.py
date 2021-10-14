print (' enter the three numbers you intend for the sides of your triangle az n ,m ,z :\n')
n=int(input())
m=int(input())
z=int(input())

if n+m>z:
    if n+z>m:
        if m+z>n:
            print("it's a triangle" )
            
else:
    print("it's not a triangle ")