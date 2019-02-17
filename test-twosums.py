# class Solution(object):
def twoSum(nums, target):  # self,
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    nums = [2,3,4,5,7,10,34,56,17]
    target = [7,9,17,37,50]
    print(nums)
    for t in target:
        result = twoSum(nums, t)
        if result:
            print(t, result, '=', nums[result[0]], '+', nums[result[1]])
        else:
            print(t, ' not in ', nums)
            
