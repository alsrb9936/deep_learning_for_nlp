import numpy as np
import matplotlib.pyplot as plt

def sigmoid(k):
    return 1/(1 + np.exp(-k))

x = np.arange( -5.0, 5.0, 0.1)
y = sigmoid(x)

plt.title('Sigmoid Function')
plt.plot(x, y, 'g')
plt.plot([0,0], [1.0, 0.0], ':')
plt.show()

# W(가중치) 와 b(편향) 값이 시그모이드 함수에 미치는 영향 
y1 = sigmoid(0.5 * x)
y2 = sigmoid(2 * x)
plt.plot(x, y1, 'r', linestyle='--')
plt.plot(x, y, 'g')
plt.plot(x, y2, 'b', linestyle='--')
plt.title('Sigmoid Function')
plt.show()
# W 는 그래프 경사도 의미 작을수록 완만 = 쫙 펴짐

y1 = sigmoid(x+0.5)
y2 = sigmoid(x+1)
y3 = sigmoid(x+1.5)

plt.plot(x, y1, 'r', linestyle='--') # x + 0.5
plt.plot(x, y2, 'g') # x + 1
plt.plot(x, y3, 'b', linestyle='--') # x + 1.5
plt.plot(x, y)
plt.plot([0,0],[1.0,0.0], ':') # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()
# 마찬가지로 그래프의 이동