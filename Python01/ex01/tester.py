"""_summary_
Not same size error:
family = [[1.80, 78.4, 0],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

Not a list error:
x = 0
print(slice_me(x, 0, 0))
"""

from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
