#!/usr/bin/python3

import sys

#get the next lexan in tokenItr
def lexan():
	global tokenItr
	try:
		return next(tokenItr)
	except:
		return ''

#match the input string with the nextToken Print error if not a match
def match(ch):
	global nextToken
	if ch == nextToken:
		nextToken = lexan()
	else:
		print("Syntax Error")
		exit()

#Axillary fucntion to check datatype match
def typeCheck(data, vtype):
	if not isinstance(data, vtype):
		print("ERROR: Datatype mismatch")
		exit()

#Axillary function to cast a string into a number, also checks for datatype mismatch
def getNum(str, vtype):
	#attempt to convert str into a number
	try:
		#return an int if number is an integer or a float if number is a real
		if str.find(".") == -1:
			return int(str)
		else:
			return float(str)
	#report that str is not a number
	except:
		print("ERROR: Number expected. '" + str + "' not number.")
		exit()

#program start symbol <prog>
def prog():
	#Try to execture code
	try:
		global_decl()
		let_in_end()
		while(nextToken == "let"):
			let_in_end()
	#Report Unspecified errro
	except:
		print("ERROR: Unspedified")
		exit()

#global declarations <global-decl>
def global_decl():
	global gdict

	#for the variable type
	vtype = type()

	#list of identifers
	varlist = id_list()

	match("=")

	#list of expressions valuses
	vallist = expr_list(vtype) #vtype for checking variable type

	#check for mismatched number of variables and values
	if len(varlist) != len(vallist):
		print("ERROR: Number of variables does not equal number of values")
		exit()

	#fill the global dictionary with variables and data
	for i in range(len(varlist)):
		gdict[varlist[i]] = vallist[i]

	match(";")

#Let in end block <let-in-end>
def let_in_end():
	global nextToken

	match("let")

	#dictionary for local variables
	local = decl()
	match("in")

	#get the datatype
	vtype = type()
	match("(")

	#get the expression value
	hold = expr(vtype, local)

	#match the end of the block syntax
	match(")")
	match("end")
	match(";")

	#print result
	print(hold)

#get local declarations <decl>
def decl():
	#dictionary for local variables
	local = {}
	#get datatype
	vtype =  type()

	#list for identifers
	varList = id_list()
	match("=")

	#list for expression values
	valList = expr_list(vtype)

	#check that number of variables match the number of expressions
	if len(varList) != len(valList):
		print("ERROR: Number of variables does not equal the number of values")
		exit()

	#create local dictionary
	for i in range(len(varList)):
		local[varList[i]] = valList[i]

	match(";")
	return local

#Get list of identifers <id-list>
def id_list():
	global nextToken

	#list for identifers
	list = [nextToken]
	nextToken = lexan()

	#read in all the identifers
	while nextToken == ",":
		match(",")
		list.append(nextToken)
		nextToken = lexan()

	return list

#Get list of expression values <expr-list>
def expr_list(vtype):
	global nextToken

	#list for expr values
	exprlist = [expr(vtype, {})]
	while nextToken == ",":
		match(",")
		exprlist.append(expr(vtype,{}))

	return exprlist

#Get the data type <type>
def type():
	global nextToken

	if nextToken == "int":
		match("int")
		return int
	elif nextToken == "real":
		match("real")
		return float
	else:
		print("ERROR: Datatype not specifide")
		exit()

#Get value of an expression <expr>
def expr(vtype, local):
	global nextToken

	#variable for the sum of terms
	sum = term(vtype, local)
	while  nextToken == "+" or nextToken == "-":
		if nextToken == "+":
			match("+")
			sum += term(vtype, local)
		else:
			match("-")
			sum -= term(vtype, local)
	return sum

#Get value of a term <term>
def term(vtype, local):
	global nextToken

	#variable for the product or quotient
	product = factor(vtype, local)
	while nextToken == "*" or nextToken == "/":
		if nextToken == "*":
			match("*")
			product *= factor(vtype, local)
		else:
			match("/")
			product /= factor(vtype, local)
	return product

#Get a factor value <factor>
def factor(vtype, local):
	global nextToken
	#hold the value of the factor before returning it
	hold = None

	#if factor is and expression
	if nextToken == "(":
		match("(")
		hold = expr(vtype, local)
		match(")")

	#if factor is a local identifer
	elif nextToken in local:
		#check for datatype mismatch
		hold = local[nextToken]
		nextToken = lexan()

	#if factor is a global identifer
	elif nextToken in gdict:
		#Check data type
		hold = gdict[nextToken]
		nextToken = lexan()

	#if there is a type casted identifer
	elif nextToken == "int" or nextToken == "real":
		#Keep the type cast
		cast = nextToken
		nextToken = lexan()
		match("(")

		#look for identifer in local dictionary
		if nextToken in local:
			hold = local[nextToken]
		#Else assume identifer is in global dictionary
		else:
			hold = gdict[nextToken]

		nextToken = lexan()
		match(")")
		if cast == "int":
			hold = int(hold)
		else:
			hold = float(hold)
	#if number literal
	else:
		#cast the string to an int or real
		hold = getNum(nextToken, vtype)
		nextToken = lexan()

	#check for datatype mismatch
	typeCheck(hold, vtype)

	#return the value of the factor
	return hold

#open .tiny file and create an iterator for the .tiny tokens
tokenItr = iter(open(sys.argv[1],"r").read().split())

#A dictionary for global identifers
gdict = {}

#get first token
nextToken = lexan()

#Start program
prog()
