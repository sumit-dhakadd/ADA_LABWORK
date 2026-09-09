from typing import List

# Binary Search
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Power Function
def myPow(x: float, n: int) -> float:
    result = 1

    if n < 0:
        x = 1 / x
        n = -n

    while n > 0:
        if n % 2 == 1:
            result = result * x

        x = x * x
        n = n // 2

    return result


# Driver Code
nums = list(map(int, input("Enter space separated integers: ").split()))
target = int(input("Enter target: "))

index = search(nums, target)
print("Index of", target, ":", index)

x = float(input("\nEnter base (x): "))
n = int(input("Enter exponent (n): "))

result = myPow(x, n)
print(f"{x}^{n} = {result}")
