class SelectionSort:
    def selection_sort(self, array):
        for i in range(0, len(array)-1):
            curr_min = array[i]
            for j in range (i+1, len(array)-1):
                if array[j] < curr_min:
                    curr_min = array[j]
            array[i], array[j] = array[j], array[i]