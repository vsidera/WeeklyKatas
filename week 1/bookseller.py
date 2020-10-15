def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    return " - ".join(
        "({} : {})".format(
            category,
            sum(int(item.split()[1]) for item in stocklist if item[0] == category))
        for category in categories)