import pytest
import numpy as np
import pandas as pd
from decimal import Decimal
from framework.wrapconfig import Config

def test_frame():
	pass

list1=['a','b','c']
list2=[1,2,3]
list3=[0.5,0.3,0.1]
my_dict_3 = dict(zip(list1, zip(list2, list3)))

print(my_dict_3)

r1 = 3.4
r2 = 4
r3 = 4.5
n1 = 1000
n2 = 100
n3 = 10
list1 = (29, 39, 49)
weights1 = (r1, r2, r3)
axis1 = (n1, n2, n3)
wa = (r1*n1+r2*n2+r3*n3)/(n1+n2+n3)
print("weighted average = %s" % wa)
print("average ", (np.average(list1, weights=axis1)))

print(4.6)

