import statistics
def max_min(nums):
    min_n = min(nums)
    max_n = max(nums)
    print('Minimum:', min_n)
    print('Maximum:', max_n)


def mean(nums):
    mean = sum(nums) / len(nums)
    print(f'Mean: {mean:.1f}')


def is_palindrome(nums):
    rev = nums[::-1]
    if nums == rev:
        print('Palindrome: True')
    else:
        print('Palindrome: False')

def median(nums):
    if len(nums) % 2 == 1:
        med = len(nums) // 2
        print(f'Median: {nums[med]}')


def mode_set(nums):
    print(f'Mode: {statistics.mode(nums)}')

nums = [int(n) for n in input().split()]
max_min(nums)
mean(nums)
is_palindrome(nums)
median(nums)
# Sort list
nums.sort()
mode_set(nums)