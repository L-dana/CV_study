import numpy as np

class MatMul:
    '''
    행렬 곱 클래스
    '''
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
    

class Sigmoid:
    '''
    시그모이드 활성화 함수 클래스
    '''

    def __init__(self):
        self.params = []
        self.grads = []
        self.out = None
    
    def forward(self, x):
        out = 1 / (1+np.exp(-x))
        self.out = out
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx
        

class Affine:
    '''
    아핀(완전연결계층) 클래스
    '''
    def __init__(self, W, b):
        self.params = [W, b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.x = None

    def forward(self, x):
        W, b = self.params
        out = np.matmul(x, W) + b
        self.x = x
        return out
    
    def backward(self, dout):
        W, b = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        db = np.sum(dout, axis=0)

        self.grads[0][...] = dW
        self.grads[1][...] = db
        return dx