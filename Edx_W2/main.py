class State(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
    def add_neighbor(self, neighbor, distance):
        self.neighbors.update({neighbor:distance})
    def get_neighbors(self):
        return(self.neighbors)
   
class Parse_path(object):
    def __init__(self, NomFic):
        self.states = dict()
        with open(NomFic, 'r') as entree:
            #path = set()
            #path is a set of tuples(city a, city b, distance))
            for line in entree:
                a = line.rstrip().split(';')
                #print a
                #path.add(tuple(a))
                self.add_path(tuple(a))
        
    def add_path(self, tuplevalue):
        (city_a, city_b, length) = tuplevalue
        #print city_a,city_b, length 
       
        if city_a not in self.states.keys():
            self.states[city_a] = State(city_a)
        if city_b not in self.states.keys():
            self.states[city_b] = State(city_b)
           
        self.states[city_a].add_neighbor(city_b, length)
        self.states[city_b].add_neighbor(city_a, length)
   
    def build_tree(self):
        while (self.path):
            self.add_path()
            
    def get_states(self):
        return self.states
   
    def get_state(self,state):
        return self.states[state]

class BFS(object):
    """
    BREADTH FIRST SEARCH implementation
    """
    def __init__(self, initial_state, goal_state, country):
        """
        initial_state: departure state
        goal_state: target state
        country: state dictionary
        frontier: next states to visit
        explored: states visited
        journey: calculated optimized path
        success : journey successfully calculated
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.country = country
        self.frontier = [initial_state]
        self.explored = []
        self.journey = []
        self.success = self.compute()
    
    
    def compute(self):
        while self.frontier:
            print ("Frontier :{}".format(self.frontier))
            print ("Explored :{}".format(self.explored))
            tmp_state = self.frontier.pop(0) #FIFO
            self.explored.append(tmp_state)
            
            if (tmp_state == self.goal_state): #is does not work: distinct objects
                return True
            
            #cast a sorted list instead of dict to always have same search result
            for neighbor in sorted(self.country.get_state(tmp_state).get_neighbors()):
                if neighbor not in (self.frontier + self.explored): #may have duplicates
                    self.frontier.append(neighbor)
        
        return False
        


#== main() ===================================================
#== Init
country = Parse_path("./usa_cities.txt")
bfs = BFS("Calgary", "Chicago", country)
print bfs.success
#print(bfs.success, bfs.frontier, bfs.explored )


#== Verif 
#print(country.get_states())
#print(country.get_state('Calgary').get_neighbors())
#print(country.get_state('Nashville').get_neighbors())


