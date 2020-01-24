


max=0

m1 = 999
m2 = 999


while m1 > 100:
    m2=999
    while m2 > 100:
        x = m1 * m2
       
        if x // 100000!=0:
            a = x // 1000
            b = (x%10)*100 + ((x%100) - (x%10)) + ((x%1000)-(x%100))/100

        elif x // 10000!=0:
            a = x // 1000
            b = (x%10)*10 + ((x%100) - (x%10))/10

        if a == b and x > max:
            print(str(m1) + " * " + str(m2) + " = " + str(x))
            max=x
       
        m2-=1
    m1-=1

print("Ответ " + str(max))
