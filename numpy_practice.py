import numpy as np

'''Initalizing - 1D,2D,3D,etc.'''
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
b = np.array([[1,2,3,4,5,6],
              [8,9,10,11,12,13]])

'''getting dimension,shape,type,itemsize,bytes,indexing in array'''
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(a[[1,2,8]]) #prints elements on index 1,2 and 8

'''Accessing or Changing specific row or column'''
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a[1,5]) # a[1,-2] = 13
print(a[0,:]) # complete row
print(a[:,2]) #complete column
print(a[0,1:6:2]) #step indexing #Another way - a[0,1:-1:2]
a[1,5] = 20 #changing a element
a[:,2] = [1,2] #changing more than one element at a time

'''Initializng Diff types of Arrays'''
a = np.zeros((2,3)) #A zero matrix of specific dimension
a = np.ones((2,3)) #For all ones matrix
a = np.full((2,3), 13) #For any other number(here 13)
a = np.full_like(b, 4) #Using the shape of a existing matrix
a = np.full(b.shape, 4) #Same as above
a = np.random.rand(2,5) #A random array of size 2 by 5
#Random.rand gives number btw 0 and 1
a = np.random.random_sample(b.shape) #For using existing shape
a = np.random.randint(2,9, size = (2,5)) #For integers
a = np.identity(5) #Identity matrix is a square matrix by default
a = np.repeat(b,3,axis=0) # repeat b matrix 3 times row wise
print(a) # axis = 0 to duplicate rows and 1 to duplicate columns

## Copying an array
a = np.array([1,2,3,4,5])
b = a #Not a good method❎
#Bcoz they point to the same memory, so if data is changed in a then it will reflect in b also and vice versa
b = a.copy() # Good method, bcoz it creates a diff copy so thry act independently

'''Mathematics in Arrays'''
a = np.array([1,2,3,4])
b = np.array([2,2,3,5])
a += 2 # adds two to each element same for -,*,/,**
print(a)
b += a # adding two arrays
print(b)
#Taking sin,cos,tan,etc
c = np.sin(a)
print(c)

'''Linear Algebra'''
a = np.ones((2,3))
b = np.full((3,2), 2)
c = np.matmul(a,b) #Matrix multiplication
c = np.identity(3)
print(np.linalg.det(c)) #Determinant of c

'''Reorganizing Array'''
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((4,2)) #changing the shape of a given matrix
#shape = number of elements, i.e if number of elements = 8
#then shape should be like 4x2, 2x2x2, 8x1, etc (mult of each is 8)

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v3 = np.vstack([v1,v2]) #vertically stacking array,v3 can have many rows
#can be [v1,v2,v1,v2,v1....]

h1 = np.ones((2,4))
h2 = np.zeros((2,2))
h3 = np.hstack((h1,h2))

'''Statistics'''
stats = np.array([[1,2,3,4],[5,6,7,8]])
print(np.min(stats)) #can have attr like axis = 1 for ros and 0 for columns
print(np.max(stats)) #can have same attr as min
print(np.sum(stats)) #same as min

'''Load Data from file'''
filedata = np.genfromtxt("data.txt", delimiter=",")
filedata = filedata.astype("int32")
print(filedata)

'''Boolena Masking and Advanced Indexing'''
print(filedata>50) #give an array of true and false based on condition
print(filedata[filedata>50]) #gives all the elements >50
print(np.any(filedata>50,axis=0)) #check column wise
#np.all in above case when all the values in a given column >50
#can have multiple conditions also