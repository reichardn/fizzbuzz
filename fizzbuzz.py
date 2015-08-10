
n = raw_input("Enter a number!")
n = int(n)
print "Fizz buzz counting up to", n
for i in range(1, n+1):
    if i % 3 != 0 and i % 5 != 0:
        print i
    if i % 3 == 0 and i % 5 != 0: 
        print "fizz"
    if i % 3 != 0 and i % 5 == 0: 
        print "buzz"
    if i % 3 == 0 and i % 5 == 0:
        print "fizz buzz"
        