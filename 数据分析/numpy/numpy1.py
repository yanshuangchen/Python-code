import numpy as np 
a = np.array([1,2,3])  
print (a)

import numpy as np 
b = np.array([[1,  2],  [3,  4]])  
print (b)

import numpy as np 
a = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print (a)

# dtype 参数 复数 
import numpy as np 
a = np.array([1,  2,  3], dtype = complex)  
print (a)

import numpy as np
# 使用标量类型 查询变量类型
dt = np.dtype(np.int32)
print(dt)

import numpy as np
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

