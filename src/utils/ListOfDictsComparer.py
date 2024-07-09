class ListOfDictsComparer:
    @staticmethod
    def equals(list1, list2, comparator = None):
        """
        Compares two lists of dictionaries for equality based on a provided comparator function.
        
        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            comparator: A function to compare elements from the two lists. Default is None, in which case uses the == operator as comparator.

        Returns:
            True if the lists are equal based on the comparator, False otherwise.
        """
        if comparator is None:
            return list1 == list2
        else:
            if len(list1) != len(list2):
                return False
            for i in range(len(list1)):
                if not ListOfDictsComparer.__dict_comparer(list1[i], list2[i], comparator):
                    return False
            
            return True

    @staticmethod
    def equal_set(list1, list2, comparator = None):
        """
        Compares two lists of dictionaries for equality based on a provided comparator function, but doesn't consider the order of the dictionaries.

        Args:
            list1 (list): The first list of dictionaries to compare.
            list2 (list): The second list of dictionaries to compare.
            comparator (function, optional): A function to compare elements from the two lists. Defaults to None, in which case uses the == operator as comparator.

        Returns:
            bool: True if the lists are equal based on the comparator regardless of order, False otherwise.
        """
        if len(list1) != len(list2):
            return False
        
        for dict1 in list1:
            if comparator is None:
                if dict1 not in list2:
                    return False
            else:
                for dict2 in list2:
                    if not ListOfDictsComparer.__dict_comparer(dict1, dict2, comparator):
                        return False
        return True
    
    @staticmethod
    def includes(list1, list2, comparator = None):
        """
        Compares two lists to check if the second list is included in the first list based on a comparator function.
        
        Args:
            list1: The first list to compare.
            list2: The second list to compare for inclusion.
            comparator: A function to compare elements from the two lists. Default is None, which uses element equality.

        Returns:
            True if list2 is fully included in list1 based on the comparator, False otherwise.
        """
        for dict2 in list2:
            if comparator is None:
                if dict2 not in list1:
                    return False
            else:
                for dict1 in list1:
                    if not ListOfDictsComparer.__dict_comparer(dict1, dict2, comparator):
                        return False

        return True
    
    @staticmethod
    def __dict_comparer(dict1, dict2, comparator):
        # Compares two dictionaries using the given comparator function.
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            if not comparator(dict1[key], dict2[key]):
                return False
        
        return True