#Define a procedure, union,#that takes as inputs two lists.#It should modify the first input#list to be the set union of the two#lists.#a = [1,2,3]#b = [2,4,6]#union(a,b)#a => [1,2,3,4,6]#b => [2,4,6]def union(data_a,data_b):    for each in data_b:        if each not in data_a:            data_a.append(each)a = [1,2,3,10,11,15,7,4,6]b = [2,4,6,5,3]union(a,b)print aprint b