import io, os
import pandas as pd
import pstats


def read_and_convert(file):
    result = io.StringIO()
    pstats.Stats(file ,stream=result).strip_dirs().print_stats()
    result=result.getvalue()

    # chop the string into a csv-like buffer
    result='ncalls'+result.split('ncalls')[-1]
    result='\n'.join([','.join(line.rstrip().split(None,5)) for line in result.split('\n')])
    
    # return result
    with open(f'{file}.csv', 'w+') as f:
        #f=open(result.rsplit('.')[0]+'.csv','w')
        f.write(result)
        f.close()

def stats_to_df(file):
    read_and_convert(file)
    df = pd.read_csv(f'{file}.csv')
    os.remove(f'{file}.csv')
    return df

if __name__ == "__main__":
    df = stats_to_df('BinarySearchMain.prof')
    print(df)