def mean(*args):
    nums = [x for x in args if type(x) in (int, float)]
    if not nums: # if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)