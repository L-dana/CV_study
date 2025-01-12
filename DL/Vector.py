import numpy as np

# 벡터와 행렬

x = np.array([2, 4, 6])

print(x.__class__) # 클래스명
print(x.shape) # 행렬(벡터)의 모양
print(x.ndim) # 행렬의 차원 수

W = np.array([[1, 2, 3], [4, 5, 6]])
print(W.shape)
print(W.ndim)