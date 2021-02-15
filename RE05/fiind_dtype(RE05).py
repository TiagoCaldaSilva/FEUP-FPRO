def find_dtype(atuple, data_type):
    result = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            result += (i,)
    return result
