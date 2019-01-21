import re
def reverse(st):
    arr = st.split(" ")
    arr.reverse()
    st = " ".join(arr)
    st = re.sub(' +', ' ',st)
    st = st.strip()
    return st