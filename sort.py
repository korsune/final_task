def sort(nums):
    length = len(nums)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


