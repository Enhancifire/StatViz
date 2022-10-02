from itertools import chain
import os


def json_stats(s):
    """Converts the stats in the pstats module to a comprehensive JSON file"""

    nstats = s.stats

    stat_list = []

    for item, value in nstats.items():

        cc, nc, tt, ct, callees = value
        clz = {}

        if callees:
            for callee_name, callee_value in callees.items():

                clz["name"] = f"{callee_name[0]}:{callee_name[2]}()"
                ccc, cnc, ctt, cct = callee_value
                clz["cc"] = ccc
                clz["nc"] = cnc
                clz["tt"] = ctt
                clz["ct"] = cct

        sts = {}
        sts["name"] = f"{item[0]}:{item[2]}()"
        sts["cc"] = cc
        sts["nc"] = nc
        sts["tt"] = tt
        sts["ct"] = ct
        sts["callees"] = clz

        stat_list.append(sts)

    return stat_list


if __name__ == "__main__":
    import pstats
    import json

    s = pstats.Stats("BinarySearchMain.prof")

    jsons = json_stats(s)

    with open("test.json", "w") as f:
        json.dump(jsons, f)
