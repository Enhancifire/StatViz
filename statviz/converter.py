import pandas as pd


def read_and_convert(file):
    """Converts a .prof file into JSON Data"""
    from .jsonizer import json_stats
    import pstats

    f = pstats.Stats(file)

    return json_stats(f)


def json_to_df(data) -> pd.DataFrame:
    """Converts the JSON data to Dataframe"""
    import pandas as pd

    df = pd.json_normalize(data)
    df.dropna(inplace=True)
    df = df.rename(
        columns={"name": "Function Name", "callees": "Callee"},
    )
    return df


def stats_to_df(file) -> pd.DataFrame:
    """Converts a .prof file to a dataframe"""
    f = read_and_convert(file)
    df = json_to_df(f)
    return df


if __name__ == "__main__":
    df = stats_to_df("BinarySearchMain.prof")
    print(df)
