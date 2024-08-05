class List:
    def remove_(self, integer_list, values_list):
        c = []
        for i in integer_list:
            if i not in values_list:
                c.append(i)
        return c
