# pair problem
%matplotlib inline
import matplotlib.pyplot as plt

data = [2, 7, 1, 5, 10]

def Math(num_list, candidate):
    ans = []
    for n in data:
        result = (n - candidate)**2
        ans.append(result)
    final_ans = round(sum(ans), 2)
    return(final_ans)

Math(data, 8.2)

gen = [x * 0.1 for x in range(0, 101)]
gen
ans_list = []
for x in gen:
    ans_list.append(Math(data, x))
ans_list

final_ans = min(ans_list)
final_ans