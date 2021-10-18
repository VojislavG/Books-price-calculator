import itertools
neu=[]
wort = ""
A = ["a","b","a","b","c","c","d","e"]
#A = ["a","b","a","b","c","c"]
#A = ["a","b","a","b","c","c","d","e","a","c"]

book_preis = 8




def machen_string(arr):  
    str1 = ""     
    for ele in arr:  
        str1 += ele     
    return str1  

for i in range(len(A)):
	wort+=A[i]
sortiert_string = machen_string(sorted(wort))



def subset_machen(arr):
	n=len(arr)
	neu = []
	_list = []
	for i in range (2**n):
		subset = ""
		for j in range(n):
			if (i & (1 << j)) !=0:
				subset += arr[j]
		if subset not in _list and len(subset) > 0:
			_list.append(subset)

	return(_list)




def gib_mir_rabatt(x):
	if len(x)==1:
		return 0
	if len(x)==2:
		return 0.05
	elif len(x)==3:
		return 0.1
	elif len(x)==4:
		return 0.2
	elif len(x)==5:
		return 0.25
	
	
		

M=subset_machen(A)



def strings_ohne_wiederholung(strin):    #strings ohne wiederholung
	return len(strin)==len(set(strin))

def geeignetes_array(lis):      	#array ohne wiederholung und mit maximaler Länge von 5 (Es gibt fünf verschiedene Bücher)
	neu=[]
	k=len(lis)
	for i in range(k):
		if (len(lis[i])<=5):
			if (strings_ohne_wiederholung(str(lis[i]))):
				neu.append(lis[i])
	return(neu)



O = geeignetes_array(M)
O.sort(key=len)
O = O[::-1]
#print(O)





def alle_kombinationen_und_rabatte(arr,x):
	j=0
	p=0
	max_rabatt=0
	for l in range(len(arr)+1):
	
		for subset in itertools.combinations(arr,l) :

			sum=0
			for i in subset:
				
				

				rabatt = 0
				sum+=len(i)
			if sum==x and machen_string(sorted(machen_string((list(map("".join, subset))))))==sortiert_string:
				for i in subset:
					l+=len(i)
					j+=1
					rabatt += book_preis * gib_mir_rabatt(i)* len(i)

				if rabatt>max_rabatt:
					max_rabatt=rabatt
				if j>=20:	
				
					print("Bestpreis: ")
					print(book_preis*len(A)-max_rabatt)
					quit()
					

	



alle_kombinationen_und_rabatte(O,len(A))
