def rec_exceptions(alist):
    result = []
    for i in alist:
        try:
            if type(i()) == list:
                result.extend(rec_exceptions(i()))
        except Exception as x:
            result.append(x)
    return result