# @Time    : 2018/10/25 22:04
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 测试.py

def twoSum_60ms(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_mapping = dict()

    for i in range(len(nums)):
        other = target - nums[i]
        if other in num_mapping:
            return [num_mapping[other], i]
        num_mapping[nums[i]] = i

if __name__ == '__main__':
    num_mapping = dict()
    print(type(num_mapping))