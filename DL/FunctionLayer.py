import numpy as np

class Sigmoid:
    def __init__(self):
        self.params = []

    def forward(self, x):
        return 1 / (1 + np.exp(-x))


# 완전연결계층(FC레이어 = 아핀레이어)
# 완전연결 계층에 의한 변환은 기하학의 아핀 변환에 해당한다...
class Affine:
    def __init__(self, W, B):
        self.params = [W, B]

    def forward(self, x):
        W, B = self.params
        return np.matmul(x, W) + B
    

class TwoFunctionLayer_Net:
    def __init__(self, input_size, hidden_size, output_size):
        
        # 가중치와 편향 초기화
        W1 = np.random.randn(input_size, hidden_size)
        B1 = np.random.randn(hidden_size)
        W2 = np.random.randn(hidden_size, output_size)
        B2 = np.random.randn(output_size)

        self.layers = [
            Affine(W1, B1),
            Sigmoid(),
            Affine(W2, B2)
        ]

        # 모든 레이어의 가중치를 리스트에 모은다. (리스트의 뒤에 이어붙인다.)
        self.params = []
        for layer in self.layers:
            self.params += layer.params

        def predict(self, x):
            for layer in self.layers:
                x = layer.forward(x)
            return x