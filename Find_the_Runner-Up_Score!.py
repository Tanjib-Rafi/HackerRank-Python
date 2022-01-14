if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = set(arr)
    new_arr.remove(max(new_arr))
    print(max(new_arr))
