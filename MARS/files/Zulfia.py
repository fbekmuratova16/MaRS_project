from hashlib import md5
from bitstring import BitArray
from ..config import ACTIVE_BITS,bs_slice


def get_bitstring(descriptors):
    d = {}
    result = []
    for i in descriptors.columns:
        a = md5(i.encode()).digest()
        xx = BitArray(a)
        l = []
        for j in range(ACTIVE_BITS):
            s = xx[j*bs_slice:(j+1)*bs_slice].uint
            l.append(s)
        d[i] = l
    for _, i in descriptors.iterrows():
        hfp = BitArray(2 ** bs_slice)
        for k, v in i.items():
            if v:
                hfp.set(True, d[k])
        result.append(hfp)

    return result

