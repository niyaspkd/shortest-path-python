import re

# graph = {'Mysore': ['Mandya', '66', 'Chennapatna', '28', 'Nanjangud', '60', 'Bandipur', '34', 'Nagarhole', '34', 'Somnathpur', '3', 'Bylakuppe', '108'], 'Mandya': ['Chennapatna', '22', 'Nanjangud', '12', 'Bandipur', '91', 'Nagarhole', '121', 'Somnathpur', '111', 'Bylakuppe', '71'], 'Chennapatna': ['Nanjangud', '39', 'Bandipur', '113', 'Nagarhole', '130', 'Somnathpur', '35', 'Bylakuppe', '40'], 'Nanjangud': ['Bandipur', '63', 'Nagarhole', '21', 'Somnathpur', '57', 'Bylakuppe', '83'], 'Bandipur': ['Nagarhole', '9', 'Somnathpur', '50', 'Bylakuppe', '60'], 'Nagarhole': ['Somnathpur', '27', 'Bylakuppe', '81'], 'Somnathpur': ['Bylakuppe', '90']}

my_dict = {}

def create_graph():
    global places_list
    global places_set


    f = open("input.txt", 'r')
    data = f.read()
    
    remove_symbols = re.sub(r'to|= | \n', '', data)
    cleaned_str = remove_symbols.replace('\n', " ")
    
    places_string = ''.join([i for i in cleaned_str if not i.isdigit()])
    
    places_list = places_string.split()
    places_set = set(places_list)
    

    data = remove_symbols.replace('/n', " ")
    
    open('output.txt', 'w').write(data)

    with open('output.txt', 'r') as f:

        for line in f:
            items = line.split()

            try:

                key = items[0]
                values = {items[1]: int(items[2])}

                my_dict.setdefault(key, {}).update(values)

            except:


                print ("finished")
                


def dijkstra(graph, start, goal):


    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
   
    infinity = 9999999
    path = []



    for node in places_list:
        shortest_distance[node] = infinity
        
        
    shortest_distance[start] = 0
   

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        



        for childNode, weight in graph[minNode].items():
            # import pdb
            # pdb.set_trace()
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                

                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)

            currentNode = predecessor[currentNode]
            
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))

create_graph()
print(places_set)
starting_point = input("Start Journey from any of above location : ")
ending_station = input("Ending location for Journey : ")

print (dijkstra(my_dict, starting_point, ending_station))
