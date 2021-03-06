# ML 기초

import numpy as np  # 수치계산
import matplotlib.pyplot as plt

# AI (2.75, 69.9)
x1 = np.array(([2, 4, 6, 8]))
x2 = np.array(([1, 2, 1, 3]))
y = np.array([75, 85, 80, 95])

a1 = 0
a2 = 0
b = 0
lr = 0.0001

for i in range(80000):
    error = (a1 * x1 + a2 * x2 + b) - y

    a1_diff = sum(2 * error * x1)
    a2_diff = sum(2 * error * x2)
    b_diff = sum(2 * error * 1)

    a1 = a1 - a1_diff * lr
    a2 = a2 - a2_diff * lr
    b = b - b_diff * lr

    print('{}회 학습 // 기울기1 {} // 기울기2 {} // 절편 {}'.format(i + 1, a1, a2, b))

# plt.plot(x, y, 'o')
# plt.plot(x, a * x + b)

plt.plot(x1, y, 'o')
plt.plot(x1, a1*x1+a2*x2+b)
# 근접한 값에 다가가고 있다는 것을 확인가능하다.

plt.show()
