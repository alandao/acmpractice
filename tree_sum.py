import itertools

class Tree(object):
    def __init__(self, data, left, right):
        self.left = left 
        self.right = right 
        self.data = data 

# String ->  (Int, String)
def splitSumTree(xs):
    head, *tail = xs
    if head.isdigit():
        return head + splitSumTree(tail) 
    else:
        return '\n' + head + ''.join(tail)

def splitSumTree_1(xs):
    return tuple(filter(None, xs.split('\n')))

# String -> [String]
def splitInputIntoList(xs, prev_char):
    xs = list(filter(lambda x: x != ' ' and x != '\n', xs))
    head, *tail = xs 
    if tail == []:
        return head 
    if prev_char == ')' and  head.isdigit():
        return '\n' + head + splitInputIntoList(tail, head)
    return head + splitInputIntoList(tail, head)

# IO -> IO
def main():
    
    line = ""
    
    while True:
        try:
            line = line  + input() + '\n'
        except EOFError:
            break
    
    x = splitInputIntoList(line, None)
    tree_list = x.split('\n')
    tree_list = list(map(lambda a: (int(a[0]),a[1]),list(map(splitSumTree_1,list(map(splitSumTree, tree_list))))))
    tree_list = list(map(lambda a: (int(a[0]), convertListToTree(a[1])), tree_list))
    truth_list = list(map(isSum, tree_list))
    for x in truth_list:
        if x == True:
            print('yes')
        else:
            print('no')

def isSum(tup):
    (xsum, ytree) = tup
    xs = listOfSums(ytree) 
    xs = xs.split('\n')
    xs.pop()
    xs = list(map(int, xs))
    xs = list(map( lambda x: x == xsum, xs))
    return any(xs)

# Tree -> String
def treeStructure( node ):
    if node == None:
        return '()'
    else:
        return '(' + str(node.data)  + treeStructure(node.left) + treeStructure(node.right) + ')' 

# String -> String
def takeWhileDigit( xs ):
    head, *tail = xs
    if head.isdigit():
        return head + takeWhileDigit(tail)
    else:
        return ''

#string -> (string, string)
def breakwhenSym(xs):
    left_brack = 0
    right_brack = 0
    left = ''
    right = ''
    for x in xs:
        if x == '(':
            left_brack += 1
        if x == ')':
            right_brack += 1
        if left_brack == right_brack:
            for x in xs:
                right = right + x
        
        left = left + x

    return (left, right)

def convertListToTree(xs):
    xs = list(xs)
    xs.pop()
    return convertListToTree_Ex( xs, None)

def convertListToTree_Ex( xs, prevChar ):
    head, *tail = xs
    if tail == []:
        return None
    if head == ')' and prevChar == '(':
        return None 
    if head.isdigit() and prevChar == '(':
        (left, right) = breakwhenSym(itertools.dropwhile(lambda x: x != '(', tail))
        return Tree( int(takeWhileDigit(xs)), convertListToTree_Ex(left, None), convertListToTree_Ex(right, None)) 
    else:
        return convertListToTree_Ex(tail, head)

def listOfSums(tree, path= 0):
    if tree == None:
        return ''

    path += tree.data 

    if (tree.left == None and tree.right == None):
        return str(path) + '\n' 
    else:
        return listOfSums(tree.left, path)  +  listOfSums(tree.right, path)

main()
