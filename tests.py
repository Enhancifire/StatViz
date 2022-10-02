## Unit tests for individual modules


def converter_test():

    from statviz import converter

    print("Converter Test")

    df = converter.stats_to_df("BinarySearchMain.prof")
    df.to_csv("test.csv")
    print(df)


def jsonizer_test():
    from statviz import jsonizer
    from pstats import Stats

    print("Jsonizer Test")
    json = jsonizer.json_stats(Stats("BinarySearchMain.prof"))
    print(json)


if __name__ == "__main__":
    converter_test()
    jsonizer_test()
