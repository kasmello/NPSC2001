import numpy as np

lol = np.array([[5,6,7],[8,9,10]])
print(lol)
print()



print('all ones matrix')
print(np.ones([5,5,5]))
print('any other number')
print(np.full([4,4,4],32))
print('now random array')
print(np.random.random_sample([5,4,4]))

print('just intergers?')
print(np.random.randint(5,size=(2,2)))

print()
print('numpy exercise from stupid utuber')

a=np.zeros([5,5])
a[(0,4),:] = 1
a[:,(0,4)] = 1
a[2,2] = 9
print(a)



print('multiply two matrices')
b= np.full([5,6],4)
c=np.full([6,3],10)
print(np.matmul(b,c))

print('vertical stacking')
xd = np.array([5,4,2,3])
xf = np.array([1,1,1,1])
print(np.vstack([xd,xf]))

print('horizontal stacking')
lmao = np.array([5,4,2,3])
lmao = lmao.reshape((4,1))
lmfao = np.array([1,1,1,1])
lmfao = lmfao.reshape((4,1))
print(np.hstack([lmao,lmfao]))
