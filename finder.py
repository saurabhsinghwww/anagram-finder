# Class which provide which will return all strings from the list passed from constructor
# that contain the exact same characters as the string passed into it.
# @author Saurabh Singh
# @version 1.0
class Finder:

    # Constructor maintaining a list which contains all element in sorted order from the passed list.
    # Sorting the list in the constructor to improve the performance because in case of find then only need
    # to sort passed string and then search in already sorted list.
    def __init__(self, string_list):
        self.string_list = string_list
        self.string_sorted_list = [self.quick_sort(str) for str in string_list]

    # Function first sort the passed string, then check the indices in the sorted list
    # using the indices search and return the original elements from the original list.
    # Method return None in case no match.
    def find(self, str):
        sorted_str = self.quick_sort(str)
        if sorted_str not in self.string_sorted_list:
            return None
        indices = [i for i, x in enumerate(self.string_sorted_list) if x == sorted_str]
        return [self.string_list[i] for i in indices]

    # Implementation of Quick Sort for string
    def quick_sort(self, str):
        return ''.join(self.quick_sort_list(list(str)))

    # Implementation of Quick Sort for list of characters
    def quick_sort_list(self, lst):
        if not lst:
            return []
        return (self.quick_sort_list([x for x in lst[1:] if x < lst[0]])
                + [lst[0]] +
                self.quick_sort_list([x for x in lst[1:] if x >= lst[0]]))
