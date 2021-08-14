from math import sqrt, pow

examples = [1, 2, 1, 2, 1, 1, 1, 2, 5, 1]

mean = sum(examples) / len(examples)

sum_mean = 0
for example in examples:
    sum_mean += pow((example - mean), 2)

std = sqrt(sum_mean / len(examples))

print(std)
