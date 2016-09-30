def threegram(s):
    dic = dict()
    s = ''.join(s.lower().split())
    for i in range(len(s)-3):
        temp = s[i:i+3]
        dic[temp]= dic.get(temp, 0) + 1
        #temp = space_rm[i:i+3]
        #if temp not in dic:
          #  dic[temp] = 0
        #dic[temp] += 1
    return dic

strang = input("enter a string: ")
diction = threegram(strang)
for i in diction:
    print(i, diction[i])
