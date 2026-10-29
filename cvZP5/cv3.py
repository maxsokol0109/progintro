values = [1,2,3,4,5,6,7,8,9,10]

def mean(values):
    num = 0
    sum = 0
    for i in values: # or you can do range(len(values))
        num += 1
        sum += i # += values[i]
    mean = round(sum / num , 2)
    return mean

print(mean(values))

def median(values):
    num = 0
    newlist = sorted(values)

    if(len(newlist) % 2 != 0):
        for i in range(len(newlist)):
            if(i == len(newlist) // 2):
                return newlist[i]
    else:
        for j in range(len(newlist)):
            if(j == len(newlist) // 2):
                num = (newlist[j-1] + newlist[j])/2
                return num 

# print(median([1,2,3,4,5,60,7,8,9,10]))


def median_beter(values):

    sorted_values = sorted(values)
    list_num = len(sorted_values)
    mid = list_num // 2

    if(list_num % 2 != 0):
        return sorted_values[mid]
    
    else:
        n = (sorted_values[mid] + sorted_values[mid - 1]) / 2
        return n

print(median_beter(values))

def std_dev(values):
    mean_num = mean(values)
    n = len(values)
    x = 0
    for i in values:
        x += (i - mean_num)**2
    y = x / n
    return round(y**0.5,2)

print(std_dev(values))

def min_max(values):
    sorted_list = sorted(values)
    list_num = len(sorted_list) - 1 # 9
    min = sorted_list[0]
    max = sorted_list[list_num]
    return [min,max]

print(min_max(values))

def summary(values):
    summary_dict = {
    
        "mean":mean(values),
        "median_beter":median_beter(values),
        "std_dev":std_dev(values),
        "min_max":min_max(values)
    }
    return summary_dict


print(summary(values))