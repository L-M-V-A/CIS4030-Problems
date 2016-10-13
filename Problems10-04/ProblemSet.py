
# Problem 1:
# Write a function which takes a list of integers and returns it after a rearrangement.
# The rearrangement is that all even numbers occur first and the odd numbers come
# later but the relative order of both the even and the odd numbers should be preserved.
#
# For example:
# in_list = [3, 4, 2, 1, 7, 6, 8]
# out_list = rearrange_even_odd(in_list)
# print(out_list) # [4, 2, 6, 8, 3, 1, 7]


def rearrange_even_odd(L)
    evens = [x for x in L if x % 2 == 0]
    odds = [x for x in L if x % 2 != 0]
    return evens + odds



# Problem 2:
# https://bitbucket.org/piyush/pyquestions/issues/30/move-zeroes-in-an-array
def move_zeroes(L):
    return [x for x in L if x != 0] + [0]*L.count(0)


# Problem 3:
# https://bitbucket.org/piyush/pyquestions/issues/15/two-sum

def tar_sum(arg, args):
    summs = set()
    for x in args:
        if arg - x in args:
            summs.add(tuple(sorted([x,arg-x])))
    return summs


# Problem 4:
# Write a function which, given a list of d-dimensional points (tuples), returns
# the centroid (or the mean). d and n can be arbitrary.
def total_n_count(points):
    count, total = 0, 0
    recur = ()
    for point in points:
        if isinstance(point, tuple):
            recur = total_n_count(point)
        else:
            total += point
            count += 1
        if len(recur) != 0:
            total += recur[1]
            count += recur[0]
            recur = ()
    return (count, total)

def centroid(in_tuple):
    data = total_n_count(in_tuple)
    return float(data[1]) / float(data[0])



# Problem 5:
# Write a function which, given an input string of English sentences, returns the
# most frequently occurring word of length 4. You can consider the white space and
# usual punctuation symbols as the delimiters.
import string

def freq_four(in_eng):
    dic = dict()
    excluded = set(string.punctuation)
    no_punc = ''.join(chars for chars in in_eng if chars not in excluded)
    for word in no_punc.split():
        if len(word) == 4:
            dic[word] = dic.get(word, 0) + 1
    if len(dic) >= 1:
        return max(dic, key=dic.get)
    else:
        return None
