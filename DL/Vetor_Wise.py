import numpy as np
import os


def vector_add(np_1: np, np_2: np) -> np:
    if(np_1.shape != np_2.shape): 
        raise Exception(f'행렬1의 크기({np_1.shape})와 행렬2의 크기({np_2.shape})가 일치하지 않습니다.')
    return np_1 + np_2

def vector_multiply(np_1: np, np_2: np) -> np:
    if(np_1.shape != np_2.shape): 
        raise Exception(f'행렬1의 크기({np_1.shape})와 행렬2의 크기({np_2.shape})가 일치하지 않습니다.')
    return np_1 * np_2

def vector_broadcast(np_1: np, np_2: np) -> np:
    # 두 배열의 차원을 맞추기 위해 shape 정보를 정리
    shape1 = np_1.shape
    shape2 = np_2.shape

    # 두 배열의 최종 shape 계산
    result_shape = []
    # reversed() 는 반복가능한 자료형의 순서를 뒤집어 새로운 객체를 생성
    # zip() 는 두 리스트를 짝지어 묶지만 짧은 리스트의 길이만큼만 동작, 길이 2, 길이6인 리스트를 묶으면 길이 2의 묶음이 나오고 길이 6은  4만큼의 길이가 무시됨
    for dim1, dim2 in zip(reversed(shape1), reversed(shape2)):
        if dim1 == dim2:
            result_shape.append(dim1)
        elif dim1 == 1:
            result_shape.append(dim2)
        elif dim2 == 1:
            result_shape.append(dim1)
        else:
            raise ValueError("Shapes are not compatible for broadcasting.")

    # 앞쪽 차원이 부족한 배열에 대해 1로 패딩
    result_shape = list(reversed(result_shape))


    ## 뒷자리가 0 이하일 경우 빈 튜플 () 이 됨 -> 파이썬 연산방식 때문, * 연산자는 반복을 의미하게 되는데 0 이하일 경우 반복하지 않아서 빈 튜플이 되버린다.
    print((1,) * (-1))

    ## 빈 튜플에다가 임의의 튜플을 더하면 결과물은 임의의 튜플 원본.
    print(shape1)
    print(() + shape1)

    # (1,) (2 - 5) + shape1 = shape1 , (1,) (2 - 5)이 (1,) * -3 으로 ()빈 튜플이 되므로 + shape1 원본이 결과가 됨
    arr1 = np_1.reshape((1,) * (len(result_shape) - len(shape1)) + shape1) 
    # (1,) (2 - 2) + shape2 = shape2 , (1,) (2 - 2)이 (1,) * 0 으로 ()빈 튜플이 되므로 + shape2 원본이 결과가 됨
    arr2 = np_2.reshape((1,) * (len(result_shape) - len(shape2)) + shape2)
    
    # 결과 배열 초기화
    result = np.zeros(result_shape, dtype=arr1.dtype)
    
    # 브로드캐스팅을 따라 값 복사 및 연산
    for idx in np.ndindex(tuple(result_shape)):  # 결과 배열의 모든 인덱스를 순회
        val1 = arr1
        val2 = arr2
        for dim, ind in enumerate(idx):  # 각 차원의 인덱스에 따라 값 가져오기
            if arr1.shape[dim] > 1:
                val1 = val1[ind]
            if arr2.shape[dim] > 1:
                val2 = val2[ind]
        result[idx] = val1 + val2  # 더한 값을 결과에 저장
    
    return result

W = np.array([[1, 2, 3], [4, 5, 6]])
X = np.array([[0, 1, 2], [3, 4, 5]])
Y = np.array([0, 1, 2])
Z = np.array([0, 1])
print(W + X)
print(W * X)
print()
print(vector_add(W, X))
print(vector_multiply(W, X))

print()
print(vector_broadcast(W,X))