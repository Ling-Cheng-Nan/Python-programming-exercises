'''
Question15 Description:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
'''
def question15add(n):
	n1 = int("%s%s%s%s", (n,n,n,n))
	n2 = int("%s%s%s", (n,n,n))
	n3 = int("%s%s", (n,n))
	n4 = int("%s", (n))

	return n1+n2+n3+n4
'''
a = input("Enter a given digit as the value of a:\n")

n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )

print (n1+n2+n3+n4)

#question15add(inp)