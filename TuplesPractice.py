# tuples
tup1 = ('string', 4.5, 10) # tuple with string, float, and int
print("tuple 1:",tup1)

#Tuples are immutable, which means you cannot update or change the values of tuple elements. 
def tupleOperation(stri, fl, i):
	tup2 = (stri,fl,i)
	print("tuple 2:",tup2)
	
	newTup = tup1 + tup2
	print("New tuple:",newTup)

tupleOperation("passed string", 3.2, 5)

# compound interest

initialInvestment = 500.00 # initial starting investment (P)
monthlyContribution = 100.50 # monthly contribution 
annualContribution = monthlyContribution * 12 # annual contribution (N)
growth = 0.07 # percent of growth (G)
rate = 12 # rate of contributions per year
time = 30 # time - 30 years

interestTuple = (initialInvestment, growth, rate, time)
print("\n\nInterest tuple properties: ", interestTuple)
print("Initial investment:", interestTuple[0], 
	  "\nAnnual interest rate:", interestTuple[1],
	  "\nRate of contributions per year:", interestTuple[2], 
	  "\nTime span:", interestTuple[3])


def compoundInterest(P, r, n,t):
	# Compound interest formula - A = P(1 + r/n)^(nt)
	# A = future value	
	# P = initial investment - P
	# r = annual interest rate - G
	# n = number of times interest is compounded per time - 12
	# t = time - 30
	
#	A = (P * ((1 + r/n))**(n*t))
#	print(A)
	
	Z = (1 + r/n)
	Y = (n*t)
	C = annualContribution
	
#	Balance(Y)   =   P(1 + r)Y   +   c[ ((1 + r)Y - 1) / r ]
	Total = P*(Z**Y) + C*((Z**Y) -1 / r)
	print("Year 0 : $", P*(Z**Y))

	
	for x in range(1,31):
		T = 0
		T += P*(Z**Y) + C*(Z**(n*x))

		outputTuple = (x, T)
		print("Year", outputTuple[0], ": $", outputTuple[1])

# Function call
compoundInterest(initialInvestment, growth, rate, time)