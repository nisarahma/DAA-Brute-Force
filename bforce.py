def build(n):
    res = []
    for i in iter(range(n)):
        weight = int(input('weight : '))
        p = int (input('value :'))
        res.append((i, weight, p))
    return res

def powerset(i):
    res = [[]]
    for j in i:
        newset = [r+[j] for r in res]
        res.extend(newset) 
    return res

def bruteforce(items, weight):
    knapsack=[]
    best_weight=0
    best_value=0
    x= powerset(items)
    for item in x:
        set_weight = sum ([e[1] for e in item])
        set_value = sum ([e[2] for e in item])
        if (set_value > best_value) and (set_weight <= weight):
            best_value = set_value
            best_weight = set_weight
            knapsack = item
    return knapsack, best_weight, best_value


n = int (input('jumlah item :'))
max = int (input('jumlah kapasitas :'))
array = build(n) 
print ("Kombinasi :", bruteforce(array,max)[0])
print ("Jumlah bobot yang bisa ditampung :", bruteforce(array,max)[1])
print ("Keuntungan maksimum yang bisa diperoleh :", bruteforce(array,max)[2])                          