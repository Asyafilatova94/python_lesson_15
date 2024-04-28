import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
isHuman = []
isRobot = []
for item in lst:
    if item == 'robot':
      isRobot += [True]
    else:
      isRobot += [False]

    if item == 'human':
      isHuman += [True]
    else:
      isHuman += [False]
data = pd.DataFrame({'whoAmI':lst})
dataOneHot = pd.DataFrame({'human':isHuman, 'robot':isRobot})
dataOneHot.head(20)
