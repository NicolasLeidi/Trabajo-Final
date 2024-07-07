class ListOfDictsComparer:
    @staticmethod
    def equals(list1, list2, comparator = None):
        if comparator is None:
            return list1 == list2
        else:
            return comparator(list1, list2)

    @staticmethod
    def equal_set(list1, list2, comparator = None):
        if len(list1) != len(list2):
            return False
        
        for item1 in list1:
            if comparator is None:
                if item1 not in list2:
                    return False
            else:
                item_found = False
                for item2 in list2:
                    if comparator(item1, item2):
                        item_found = True
                        break
                if not item_found:
                    return False

        return True
    
    @staticmethod
    def includes(list1, list2, comparator = None):
        for item2 in list2:
            if comparator is None:
                if item2 not in list1:
                    return False
            else:
                item_found = False
                for item1 in list1:
                    if comparator(item1, item2):
                        item_found = True
                        break
                if not item_found:
                    return False

        return True