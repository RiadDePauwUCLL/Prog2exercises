# Write your code here
def double_dict_values(dictionary):
    double = {}
    for k, v in dictionary.items():
        double[k] = v * 2
    return double