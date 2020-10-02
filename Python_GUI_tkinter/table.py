#To run this program
#Call gen_truth_table(exp) where exp='((a+b).c)'
#exp = any valid boolean expression with no. of variables=2 or 3 or 4 only


from tkinter import *
  
lst=[]
class Table:
	def __init__(self,root,total_rows,total_columns): 
		print(lst)        
		print('sssssssssssssssss')
		print(total_rows)
			# code for creating table 
		for i in range(total_rows): 
			for j in range(total_columns):
				self.e = Entry(root, width=15, fg='black', font=('Arial',16,'bold'))
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j]) 

def findOpenParen(text, closePos):
	print(closePos)
	openPos = closePos
	counter = 1
	while counter > 0:
		openPos-=1
		c = text[openPos]
		if(c == '('):
			counter-=1
		elif(c == ')'):
			counter+=1
	return openPos;


def f(a,b,c,s):
	print('sss',s)
	return s

def truth_table_2(s):
	table = {}
	for a in [0, 1]:
		for b in [0, 1]:
			lst.insert(len(lst)-1,(a,b,eval(s)))
			table[(a, b)] =  eval(s)
	return table


def truth_table_3(s):
	table = {}
	for a in [0, 1]:
		for b in [0, 1]:
			for c in [0,1]:
				lst.insert(len(lst)-1,(a,b,c,eval(s)))
				table[(a, b, c)] =  eval(s)
	return table


def truth_table_4(s):
	table = {}
	for a in [0, 1]:
		for b in [0, 1]:
			for c in [0,1]:
				for d in [0,1]:
					lst.insert(len(lst)-1,(a,b,c,d,eval(s)))
					table[(a, b, c, d)] =  eval(s)
	return table


def gen_truth_table(exp):

	s=""
	lst.clear()
	print(exp)
	print(type(exp))
	for i in range(len(exp)):
		if(exp[i]=='.'):
			s+=" and "
		elif(exp[i]=='+'):
			s+=" or "	
		else:
			s+=exp[i]

	print(s)

		
	for i in range(len(s)):
		#print(i)
		if(s[i]=='\''):
			pos=i-1
			#print(pos)
			p=findOpenParen(s,pos)
			
			s1=s[0:p]
			s2="not"
			s3=s[p:i]
			s4=s[(i+1):len(s)]
			s=s1+s2+s3+s4
			
			
	print(s)

	for i in range(len(s)):
		#print(i)
		if(s[i]=='\''):
			pos=i-1
			#print(pos)
			p=findOpenParen(s,pos)
			
			s1=s[0:p]
			s2="not"
			s3=s[p:i]
			s4=s[(i+1):len(s)]
			s=s1+s2+s3+s4
			
			
	print(s)


	p=[]

	for i in range(len(exp)):
		if(exp[i]>='a' and exp[i]<='z'):
			p.append(exp[i])

	if(len(p)==3):
		truth_table_3(s)
		lst.insert(0,(p[0],p[1],p[2],'X='+exp))
	elif(len(p)==2):
		truth_table_2(s)
		lst.insert(0,(p[0],p[1],'X='+exp))
	elif(len(p)==4):
		truth_table_4(s)
		lst.insert(0,(p[0],p[1],p[2],p[3],'X='+exp))



	total_rows = len(lst)
	print(total_rows) 
	total_columns = len(lst[0]) 
	print(total_columns)
	print('*************************')
	print(lst)
	# create root window 
	s_table = Tk()
	s_table.title("Truth Table")
	t = Table(s_table,total_rows,total_columns) 
	s_table.mainloop()

	return lst
	
#Example
gen_truth_table('((a+b).c)')


    