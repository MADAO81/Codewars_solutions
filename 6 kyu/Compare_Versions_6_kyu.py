# https://www.codewars.com/kata/53b138b3b987275b46000115/train/python

# def compare_versions(version1,version2):
#     from distutils.version import LooseVersion, StrictVersion
#     return LooseVersion(version1) >= LooseVersion(version2)


# def compare_versions(version1, version2):
#     v1 = map(int, version1.split('.'))
#     v2 = map(int, version2.split('.'))
#     return list(v1) >= list(v2)



def compare_versions(version1,version2):
    return [int(i) for i in version1.split(".")] >= [int(j) for j in version2.split(".")]
