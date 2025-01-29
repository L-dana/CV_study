import numpy as np
from ssigmoid import sigmoid_2, sigmoid_1

x = np.random.randn(10, 2)
W1 = np.random.randn(2, 4)
B1 = np.random.randn(4)

h = np.matmul(x, W1) + B1


print(W1, '\n')
print(B1, '\n')
print(x, '\n')
print(h, '\n')

x = np.random.randn(10, 2)

# Layer 1
W1 = np.random.randn(2, 4)
B1 = np.random.randn(4)

# Layer 2
W2 = np.random.randn(4, 3)
B2 = np.random.randn(3)

Layer_1 = sigmoid_1(np.matmul(x, W1) + B1)
Layer_2 = np.matmul(Layer_1, W2) + B2


# 최종 형상은 (10, 3), 10개의 데이터가 한번에 처리되었고
# 각 데이터는 3 차원 데이터로 변환됨(3가지 클래스로 분류되었다고 간주할 수 있음)
# 이 3차원 데이터는 각 클래스에 대응하는 점수로 간주할 수 있고, 점수가 가장 큰 클래스로 분류된 것
# 이 점수를 소프트맥스 함수에 대입하면 확률이 도출된다...
print("rufrhk")
print(Layer_2)