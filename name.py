
def full_names(first_name, last_name, min_length=0):
    """
    :param List of first and last names and optional number
    :returns integration of all names that can be
    """
    if min_length == 0:
        names = [(first,last) for first in first_name for last in last_name]
    else:
        names = [(first, last) for first in first_name for last in last_name if len(first)+len(last) + 1 >= min_length]
    full = []
    for i in names:
        a = i[0][0].upper() + i[0][1:]
        b = i[1][0].upper() + i[1][1:]
        full.append(" ".join([a,b]))
    return full


if __name__=="__main__":
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names) == ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi',
                                            'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(first_names, last_names))