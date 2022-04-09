class Country:
    def __init__(self, name, population, area):

        # write your code below
        self.name = name
        self.population = population
        self.area = area


    
    def is_larger(self, other):

        # write your code below
        ans = 0
        if self.area > other.area :
            ans = True
        else :
            ans = False
            
        return ans
            

    
    def population_density(self):

        # write your code below
        density = self.population/self.area
        
        return density
        
       
       