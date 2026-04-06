# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python


# from textwrap import wrap

# def split_in_parts(s, part_length): 
# 	return " ".join(wrap(s,part_length))



def split_in_parts(s, part_length): 
    return " ".join([s[i:i + part_length] for i in range(0, len(s), part_length)])
