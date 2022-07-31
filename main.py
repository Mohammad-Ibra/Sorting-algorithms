from sorting import Sorting

def main():
    arr = [64,25,17,34,90,12]
    s = Sorting()
    s.selection_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()