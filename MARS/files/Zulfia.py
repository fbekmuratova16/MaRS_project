from hashlib import md5
from bitstring import BitArray
from pandas import DataFrame

ACTIVE_BITS = 2
BITSTRING_SIZE = 0
bs_slice = BITSTRING_SIZE+6


# holi=('NewYear', 'MothersDay', 'FathersDay', 'VictoryDay', 'ValentineDay')

df = DataFrame([[1, 2, 3, 4, 0], [0, 1, 2, 0, 3]], columns=holi)

def get_bitstring (descriptors):
    d = {}
    result = []
    for i in descriptors.columns:
        a=md5(i.encode()).digest()
        xx=BitArray(a)
        l=[]
        for j in range(ACTIVE_BITS):
            s=xx[j*bs_slice:(j+1)*bs_slice].uint
            l.append(s)
        d[i]=l
    for _, i in df.iterrows():
        hfp = BitArray(2 ** bs_slice)
        for k, v in i.items():
            if v:
                hfp.set(True, d[k])
        result.append(hfp)

    return result

print(get_bitstring(df))
