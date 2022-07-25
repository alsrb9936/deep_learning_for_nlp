from random import random
from re import S
import numpy as np

# 다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용됩니다 -> 속도도 더 빠르다
vec = np.array([1,2,3,4,5])
print(vec)

# 2차원 배열
mat = np.array([[1,2,3],[4,5,6]])
print(mat)

# 각 타입은 numpy.ndarray 동일
print("\nvec 타입: ",type(vec))
print("mat 타입: ",type(mat))

#numpy 배열에는 축의 개수(ndim)와 크기(shape)라는 개념이 존재하는데, 배열의 크기를 정확히 숙지하는 것은 딥 러닝에서 매우 중요합니다
print("\nvec 축의 개수: ",vec.ndim)
print("vec의 크기(shape)",vec.shape)

print("\nmat 축의 개수: ", mat.ndim)
print("mat 크기(shape): ",mat.shape)

# np.array 초기화
# 0 행열
zero_mat = np.zeros((2,3)) 
print("\n",zero_mat)
# 1로만 채우는 행렬
one_mat = np.ones((2,3))
print("\n",one_mat)
# 같은 수로 채우는 행렬
same_mat = np.full((2,3),7) 
print("\n",same_mat)
# 대각 행렬
diagonal_mat = np.eye(4)
print("\n",diagonal_mat)
# 임의의 값을 가지는 행렬
random_mat = np.random.random((2,3))
print("\n",random_mat)
# 0 ~ n-1 을 가지는 배열
range_vec = np.arange(4)
print("\n",range_vec)

# 다른 바리에이션 i 부터 j 까지 k 씩 증가 (i,j,k)
n = 2
range_n_vec = np.arange(1,10,n)
print("\n", range_n_vec)

# 배열 구조만 바꾸기 reshape 
reshape_map = np.arange(30).reshape(5,6)
print('\n',reshape_map)

# numpy 슬라이싱 기능
mat = np.array([[1,2,3],[4,5,6]])
print('\n',mat)
# 첫번째 행 출력
slice_mat = mat[0, :]
print('\n',slice_mat)
# 두번째 열 출력
slice_mat = mat[:,1]
print(slice_mat)

# numpy 정수 인덱싱
mat = np.array([[1, 2], [4, 5], [7, 8]])
print(mat)
# 1행 2열, 3행 1열 원소 모아서 새 배열 만들기 [1행 , 3행], [2열, 1열]
indexing_mat = mat[[0,2],[1,0]]
print('\n',indexing_mat)

# numpy 연산
# 원소 합과 곱, 나누기, 빼기
x = np.array([1,2,3])
y = np.array([4,5,6])
print('\n',np.add(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.subtract(x,y))
#행렬곱,벡터곱
mat = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
print('\n',np.dot(mat,mat2))