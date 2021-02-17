# 그래프 그리기 2

import seaborn as sns
# 연습용 데이터와 가시화 툴을 제공하는 라이브러리
import matplotlib.pyplot as plt

# 그림 그려주는 라이브러리

tips = sns.load_dataset('tips')
print(tips)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


# 막대그래프
# ax1.hist(tips['total_bill'], bins=10)
# ax1.set_title('Histogram')
# ax1.set_xlabel('Frequency')
# ax1.set_ylabel('Total Bill')
# fig.show()

# 흩뿌리는 그래프
# ax1.scatter(tips['total_bill'], tips['tip'])
# fig.show()

def recode_sex(sex):
    if sex == "Female":
        return 0
    else:
        return 1


# 성별별로 색깔 달리해서 그리기
tips['sex_color'] = tips['sex'].apply(recode_sex)
ax1.scatter(tips['total_bill'], tips['tip'], s=tips['size'] * 10, c=tips['sex_color'], alpha=0.5)
fig.show()


