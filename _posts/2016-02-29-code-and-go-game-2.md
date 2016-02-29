---
layout     : post
title      : "Code &amp; Go game Episode II"
categories : events
tags       : python getinvolved
author     : Adam
comments   : true
---

Due to there being no workshop during Thursday's code club session, Vince
decided that we would have another game of *Code & Go*.  This time, we only had
one game in which we had three turns at writing one line of code and we used
*Vince's Macbook*. As such Sam didn't dare attempt to mess up his machine.

Below is the code from the game:

```python
import random
import math
import ciw

ciw = False

import axelrod as ciw

ciw = math.factorial

math.sqrt = ciw

random.choice = lambda x: lambda y: y + len(x)

# print = del

import ciw as queue
print queue.Individual(2)
queue = random.choice([math.factorial, math.sqrt, math.floor])
ciw = random.choice([math, ciw, random])
math.exp = queue
print type(math.exp)
for i in random.sample(range(100), random.randint(1,20)):
    math.sqrt = random.choice([math.factorial, math.exp])
    j = math.sqrt(i)
    print i, j
    i = j / (i+1)
    print i, j
    if i%2 == 0:
        print 'ciw is {}'.format(str(ciw))
        print 2**j**i
    else:
        break
```
