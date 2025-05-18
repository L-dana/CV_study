import numpy as np

class MatMul:
    def __init__(self, W):
        self.params = [W] # 학습하는 매개변수
        self.grads = [np.zeros_like[W]] # 학습 시 사용되는 기울기
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.matmul(x, W)
        self.x = x
        return out
    
    def backward(self, dout):
        W, = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        self.grads[0][...] = dW # ... 은 생략 기호로 위치를 고정하고 덮어쓰기를 수행하도록 함(깊은 복사 수행).
        return dx