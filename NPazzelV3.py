from queue import Queue
class Node:
    def __init__(self,father,action,root) -> None:
        self.father = father
        self.action = action
        self.root = list(root)
def problemActions(node):
    index = node.root.index('0')
    lis = []
    if((index - n) > -1):
        lis.append("U")
    if((index + 1) % n != 0):
        lis.append("R")
    if((index + n) < (n**2)):
        lis.append("D")
    if(index % n != 0):
        lis.append("L")
    return lis   
def newChildNode(node,action):
    index = node.root.index('0')
    temp = node.root
    if(action == "U"):
        temp[index] , temp[index - n] = temp[index - n] , temp[index]
        node1 = Node(node,action,temp)
        temp[index - n] , temp[index] = temp[index] , temp[index - n]
        return node1
    if(action == "D"):
        temp[index] , temp[index + n] = temp[index + n] , temp[index]
        node1 = Node(node,action,temp)
        temp[index + n] , temp[index] = temp[index] , temp[index + n]
        return node1
    if(action == "R"):
        temp[index] , temp[index + 1] = temp[index + 1] , temp[index]
        node1 = Node(node,action,temp)
        temp[index + 1] , temp[index] = temp[index] , temp[index + 1]
        return node1
    if(action == "L"):
        temp[index] , temp[index - 1] = temp[index - 1] , temp[index]
        node1 = Node(node,action,temp)
        temp[index - 1] , temp[index] = temp[index] , temp[index - 1]
        return node1
def checkExplored(child,explored):
    if child in explored:
        return True
    else:
        return False  
def solution(node):
    def slu(nodes):
        lia = ""
        if(nodes.father is not None):
            n = nodes.father
            lia = slu(n)
        if(nodes.action != None):
            lia += nodes.action + " "
        return lia
    soloList = slu(node)
    soloList = soloList[:-1]
    return soloList
def bfs(initialState,goalState):
    i = 0
    initialState = initialState.split(" ")
    goalState = goalState.split(" ")
    if(goalState == initialState):
        return 0
    nodeState = Node(None,None,initialState)
    explored = {"".join(nodeState.root)}
    frontier = Queue()
    frontier.put(nodeState)
    while not frontier.empty(): 
        nodeState = frontier.get()
        i += 1 
        for action in problemActions(nodeState):
            child = newChildNode(nodeState,action)
            if(child.root == goalState):
                return solution(child) , i
            if(not checkExplored("".join(child.root),explored)):
                explored.add("".join(child.root))
                frontier.put(child)
                                
    return "no solution found", i           
global n
n = int(input())
initialState = input()
goalState = input()
solution = bfs(initialState,goalState)
if(solution != 0):
    print(solution[1])
    print(str(solution[0]))
else:
    print(0)

