# plot 꾸미기

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# ax = sns.displot(tips['total_bill'], hist=False)
# ax = sns.displot(tips['total_bill'], rug=True)
# fig.show()

# a = sns.histplot(tips['total_bill'])
# fig.show()

# ax = sns.countplot('day', data=tips)
# ax.set_title("Count")
# ax.set_xlabel("Day")
# ax.set_ylabel("Frequency")
#
# sns.regplot(x='total_bill', y='tip', data=tips)

# sns.barplot(x='time', y='total_bill', data=tips)
# fig.show()

# sns.kdeplot(data=tips['total_bill'], data2=tips['tip'], shade=True)
# fig.show()

# sns.boxplot(x='time', y='total_bill', data=tips)
# fig.show()

# sns.violinplot(x='time', y='total_bill', data=tips)
# fig.show()

# sns.violinplot(x='time', y='total_bill', data=tips, hue='sex', split=True)
# fig.show()

# sns.pairplot(tips, hue='sex')
# fig.show()

# sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', fit_reg=False)
# fig.show()

#
# facet = sns.FacetGrid(tips, col='day', col_wrap=2)
# facet.map(plt.scatter, 'total_bill', 'tip')
# plt.show()

#
sns.set_style('whitegrid')
facet = sns.FacetGrid(tips, col='time', hue='sex', row='smoker')
facet.map(plt.scatter, 'total_bill', 'tip')
plt.show()