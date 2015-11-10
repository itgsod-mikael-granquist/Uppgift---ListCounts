def average(listofnumbers):
 result = 0
 tal = 0
 wow = 0
 for numbers in listofnumbers:
     result = result + numbers
     tal = len(listofnumbers)
     wow = result / tal
     return wow


average([1,2,3])

def sum(listofnumbers):
    result = 0
    for numbers in listofnumbers:
        result = result + numbers

    return result

sum([1,2,3])


def max(listofnumbers):
    sort= sorted(listofnumbers)
    längd = len(listofnumbers)
    return (sort[längd])

def min(listofnumbers):
    sort = sorted(listofnumbers)
    return(sort[0])


def median(listofnumbers):
    sort = sorted(listofnumbers)
    längd = len(sort)
    if not längd % 2:
        return (sort[längd / 2] + sort[längd / 2 - 1]) / 2.0

    return sort[längd / 2]



