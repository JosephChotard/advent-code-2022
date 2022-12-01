from pyspark.sql import SparkSession
import pyspark.sql.functions as F

def read_input():
    calories = [[]]
    with open('./input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                calories.append([])
                continue
            calories[-1].append(int(line))
    return calories

def a(calories):
    return max([sum(c) for c in calories])

def b(calories):
    pass

if __name__ == '__main__':
    calories = read_input()
    print(f"A: {a(calories)}")
    print(f"B: {b(calories)}")