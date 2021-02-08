lambda x: 3*x + 1

#给lamdba表达式一个名字
g = lambda x: 3*x + 1
print(g(2))

#combine first name and last name into a single "Full Name",含有两个参数的lambda表达式
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonhard", "EULER"))

s = 'hello,optimal'
print(enumerate(s))
for i in enumerate(s):
    print(i)