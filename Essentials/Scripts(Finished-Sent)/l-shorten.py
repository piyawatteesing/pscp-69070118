"""Range compressor"""

def main():
    """Compresses int"""
    nums = []
    while True:
        val = int(input().strip())
        if val == -1:
            break
        nums.append(val)
    if not nums:
        return
    ranges = []
    start = nums[0]
    prev = nums[0]
    for num in nums[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{prev}")
            start = num
            prev = num
    if start == prev:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{prev}")
    print(", ".join(ranges))
main()
