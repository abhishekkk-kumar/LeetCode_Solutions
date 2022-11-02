The logic:
​
we convert the input list into a dictionary where for every group size we list all members of a group of this size.
So for example for [3,3,3,3,3,1,3] it wil be { 1:[5], 3:[0,1,2,3,4,6]}
​
The code for that:
​
d = {}
for i,v in enumerate(groupSizes):
if v in d:
d[v].append(i)
else:
d[v] = [i]
Ok if number of members in a group is less then or equal to the size of the group - we can keep all those members in one group (like 1:[5] - we can just keep a group of one member 5). But if we get too many members - they can't fit. For example, 3:[0,1,2,3,4,6] - there are 6 members in the groups of size 3. That means that 'supergroup' needs to be split into multiple groups of size 3.
The way to do it is:
​
​
ret = []
for i in d:
for j in range(0,len(d[i]),i):
ret.append(d[i][j:j+i])
return ret