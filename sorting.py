class Sorting:

    def selection_sort(self, arr: list) -> None:
        
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j

            arr[i] , arr[min_index] = arr[min_index], arr[i]

