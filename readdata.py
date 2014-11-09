"""
this function check if a string is a real number or integer
It is not used in our current preprocessing function, 
but it may be useful in the future
"""
import re
def IsFloat(s):
	return re.match(r"[-+]?\d+(\.\d*)?$", s) is not None


"""
this function reads the training sample file,
removes the features of hash values,
convert 'YES' to '1', 'NO' to '-1' , '' to '0',
convert all features into float
"""

def preprocess():
	train=[item.strip().split(',') for item in open('train.csv').readlines()[1:]]
	pos=[]
	for i, item in enumerate(train[0]):
		if len(item)!=44:
			pos.append(i)
        pos.remove(0)
	X=[[row[i].replace('YES','1').replace('NO','-1') for i in pos] for row in train]
        for row in X:
		for i, item in enumerate(row):
			if item=='':
				row[i]='0'
	X=[[float(item) for item in row] for row in X]	
	return X
	
	
	
if __name__=="__main__":
	preprocess()
	X=preprocess()
	
