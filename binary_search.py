

def binary_search(search_list, target, low=None, high=None):
    low = 0 if low == None else low
    high = len(search_list) - 1 if high == None else high
    midpoint = (low + high) // 2

    if search_list[midpoint] == target:
        print(f'index = {midpoint}')
        print(f'target = {search_list[midpoint]}')
        return midpoint
    elif target < search_list[midpoint]:
        return binary_search(search_list, target, low, midpoint-1)
    else:
        return binary_search(search_list, target, midpoint+1, high)


if __name__ == '__main__':

    test_list = [3, 5, 10, 13, 24, 25, 47, 59, 63, 64, 65, 78, 91, 99, 115]
    target = int(input('Insert a target to search: '))

    try:
        binary_search(test_list, target)
    except:
        print(f'{target} is not on the list!')
    