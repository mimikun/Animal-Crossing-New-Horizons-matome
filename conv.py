from typing import *

def get_list(file: Any) -> list:
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data

en_list = get_list("./en_file")
jp_list = get_list("./jp_file")

for i,j in zip(en_list,jp_list):
    print(i)
    print(j)
