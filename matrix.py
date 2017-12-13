import pyspark

import re
def get_vector(str):
    if str:
        dict = {'Action':0,'Adventure':1,'Animation':2,'Children':3,'Comedy':4,'Crime':5,'Documentary':6,'Drama':7,'Fantasy':8,
                'Film-Noir':9,'Horror':10,'IMAX':11,'Musical':12,'Mystery':13,'(no genres listed)':14,'Romance':15,
                'Sci-Fi':16,'Thriller':17,'War':18,'Western':19}
        rsplit = re.split(r '|', str)
        vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for item in rsplit:
            vec[dict['item']]= 1
    #return _compile(pattern, flags).split(string, maxsplit)
        return vec