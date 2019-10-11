import random
from matplotlib import pyplot as plt

num_list = []


def nums_list():
    for i in (range(1, 1001)):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        num3 = random.randint(1, 6)
        num = num1 + num2 + num3

        num_list.append(num)

    return num_list


nums_list = nums_list()
print(nums_list.count(11))

from matplotlib import pyplot as plt

plt.figure()
bins = 1
group = int((max(nums_list) - min(nums_list)) / bins)
plt.hist(nums_list, group)
plt.grid(True,linestyle = "--",alpha = 0.2)
plt.show()
