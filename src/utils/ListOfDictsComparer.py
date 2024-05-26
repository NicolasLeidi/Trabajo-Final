class ListOfDictsComparer:
    @staticmethod
    def equals(list1, list2):
        return list1 == list2        

    @staticmethod
    def equal_set(list1, list2):
        sorted_list1 = sorted([ListOfDictsComparer.__dict_to_sorted_tuple(item) if isinstance(item, dict) else item for item in list1])
        sorted_list2 = sorted([ListOfDictsComparer.__dict_to_sorted_tuple(item) if isinstance(item, dict) else item for item in list2])
        
        return sorted_list1 == sorted_list2
    
    @staticmethod
    def includes(list1, list2):
        sorted_list1 = sorted([ListOfDictsComparer.__dict_to_sorted_tuple(item) if isinstance(item, dict) else item for item in list1])
        sorted_list2 = sorted([ListOfDictsComparer.__dict_to_sorted_tuple(item) if isinstance(item, dict) else item for item in list2])
        
        return all(item in sorted_list1 for item in sorted_list2)

    @staticmethod
    def __dict_to_sorted_tuple(d):
        # Transforma los diccionarios a tuplas ordenadas
        return tuple(sorted(d.items()))