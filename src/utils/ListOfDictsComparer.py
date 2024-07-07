class ListOfDictsComparer:
    @staticmethod
    def equals(list1, list2, comparator = None):
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
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            if not comparator(dict1[key], dict2[key]):
                return False
        
        return True