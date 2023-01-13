def lis():
  
    lis1=[1,2,3,4,5,6,8]
    lis2=["s","h","o","b","h","i","t"]
    print("first list is :- ", lis1,"second list is :- ", lis2)
    lis1, lis2 = lis2, lis1
    print("\n")
    return print("second list is :- ",lis1, "first list is :- ",lis2)
    lis()
    
lis()



----------------------------------------------------------------------
Question:-
   print(proximity_lists([5, 8, 8, 9, 17, 21, 24, 27, 31, 41]))


def proximity_lists(values):
    def _recursion(values, list1, list2):
        if len(values) == 0:
            return list1, list2
        head, tail = values[0], values[1:]
        r1, r2 = _recursion(tail, list1 + [head], list2)
        s1, s2 = _recursion(tail, list1, list2 + [head])
        if abs(sum(r1) - sum(r2)) < abs(sum(s1) - sum(s2)):
            return r1, r2
        return s1, s2

    return _recursion(values, [], [])

values = [5, 8, 8, 9, 17, 21, 24, 27, 31, 41]
s1, s2 = proximity_lists(values)
print(sum(s1), sum(s2))
print(s1)
print(s2)

---------------------------------------------------------------------

Question:-
   print(proximity_lists([5, 8, 8, 9, 17, 21, 24, 27, 31, 41]))
    
    
from collections import Counter

def close_proximity(d, _dist = 1):
  def _valid(c, _original):
    return abs(sum(c) - sum([i for i in _original if i not in c])) <= _dist
  def combos(_d, current = []):
    if _valid(current, _d) and current:
      yield current
    else:
      for i in _d:
        _c1, _c2 = Counter(current+[i]), Counter(_d)
        if all(_c2[a] >= b for a, b in _c1.items()):
          yield from combos(_d, current+[i])
  return combos(d)

start = [5, 8, 8, 9, 17, 21, 24, 27, 31, 41]
t = next(close_proximity(start))
_c = [i for i in start if i not in t]
print(t, _c, abs(sum(t) - sum(_c)))
