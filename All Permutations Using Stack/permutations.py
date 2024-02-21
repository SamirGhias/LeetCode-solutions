from stack import Stack

def permutations(lst):
    """
    Returns a new list containing all permutations using
    all of the strings in <lst>
    """
    acc = []
    for word in lst:
        perm_helper(word, acc)
    for i in range(len(acc)):
        acc[i] = "".join(acc[i])
         
    return acc

def perm_helper(word, acc):
    if acc == []:
        acc.append([word])
        return
    s = Stack()
    while acc != []:
        s.push(acc.pop())
    while not s.is_empty():
        acc.extend(perm_insert(s.pop(), word))

def perm_insert(lst, word):
	result = []
	c = lst.copy()
	for i in range(len(lst) + 1):
		new = c.copy()
		new.insert(i, word)
		result.append(new)
	return result

if __name__ == "__main__":
     print("MAIN")
     lst1 = ["foo", "bar"]
     lst2 = ["foo", "bar", "hello"]
     lst3 = ["hello", "my", "name", "is", "samir"]
     lst4 = ["foo", "bar", "hello", "world", "my", "name", "is", "samir"]
     
