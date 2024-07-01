class ListOfDictsComparer:
    @staticmethod
    def equals(list1, list2):
        return list1 == list2        

    @staticmethod
    def equal_set(list1, list2):
        if len(list1) != len(list2):
            return False
        
        for item in list1:
            if item not in list2:
                return False

        return True

        return sorted_list1 == sorted_list2
    
    @staticmethod
    def includes(list1, list2):
        for item in list2:
            if item not in list1:
                return False

        return True