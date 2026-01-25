# CPU bound + sync

import time


def cpu_bound(num):
    return sum(i * i for i in range(num))


def find_sums(nums):
    result = []
    for num in nums:
        result.append(cpu_bound(num))
    return result

def main():
    nums= [3000000 + x for x in range(30)]
    print(nums)
    start_time = time.time()
    total = find_sums(nums)
    
    print(f'Total list: {total}')
    print(f'Sum: {sum(total)}')
    duration = time.time() - start_time
    print(f'Duration: {duration} seconds')

if __name__ == '__main__':
    main()