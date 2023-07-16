"""
Question 9: AdoptAPet
An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home. 
Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; 
they are assigned the animal of that species that has been in the shelter longest. If there are no animals
 available of the desired species, they must take the other species. You are given a list of pets in the 
 shelter with their names, species, and time in the shelter at the start of a week. You receive a sequence 
 of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time. Print the 
 names and species of the pets as they are adopted out.

Example (input and output forms one sequence of sample input):
Initial Input:
Sadie, dog, 4 days
Woof, cat, 7 days
Chirpy, dog, 2 days
Lola, dog, 1 day

Input: Bob, person, dog
Output: Sadie, dog

Input: Floofy, cat
Output:

Input: Sally, person, cat
Output: Woof, cat

Input: Ji, person, cat
Output: Floofy, cat

Input: Ali, person, cat
Output: Chirpy, dog

"""

# Strategy: multiple queues

# IDEA: have hashmap/dictionary of pet category --> max heap
# addAnimal: time -- O(log(n)), space -- O(n) (n = number of pets)
# adoptAPet: time -- O(k+log(n)) (k=number of species), space -- O(1) if adding pet

from collections import defaultdict
from heapq import heapify, heappop, heappush

class Shelter:
    def __init__(self) -> None:
        self.animals = defaultdict(lambda: []) # maps each type of animal (time_spent, name) to max heap organized by age
        
    def addAnimal(self, name:str, breed:str, days:int) -> None: 
        heappush(self.animals[breed], (-1*days, name)) # max heap, but heapify is min-heap by default so negate all days
        return
    
    def adoptOldest(self): 
        oldestAge, oldestName, oldestBreed = 0, None, None

        for breed in self.animals:
            if self.animals[breed]: # if heap is nonempty
                age, name = self.animals[breed][0]
                if age < oldestAge: # since "max" heap is actually min heap with ages negated
                    oldestAge, oldestName, oldestBreed = age, name, breed

        return (oldestName, oldestBreed)


    def adoptAPet(self, input:tuple):
        if len(input) == 2: # inputting animal
            petname, breed = input
            self.addAnimal(petname, breed, 0)
            return

        # otherwise, inputting adoptee w/ 3 inputs
        if len(input) != 3:
            raise Exception("Invalid input, must be tuple of length 2 or 3")
        
        _, _, breed = input # only care about needed breed

        # shelter has breed, take oldest of dog out
        if len(self.animals[breed]) > 0: 
            _, adoptedName = heappop(self.animals[breed]) 
            
        else:        
            # if shelter doesn't have breed, adopt oldest of all species O(k) operation
            adoptedName, breed = self.adoptOldest()

        return(f"{adoptedName}, {breed}")


"""
------------------------------
            TESTS
------------------------------
"""

def exampleTest():
    # initial input
    shelter = Shelter()
    shelter.addAnimal("Sadie", "dog", 4)
    shelter.addAnimal("Woof", "cat", 7)
    shelter.addAnimal("Chirpy", "dog", 2)
    shelter.addAnimal("Lola", "dog", 1)

    # check heap
    assert(shelter.animals == {'dog': [(-4, 'Sadie'), (-2, 'Chirpy'), (-1, 'Lola')], 'cat': [(-7, 'Woof')]})

    # generic AdoptAPet input
    assert(shelter.adoptAPet(("Bob", "person", "dog")) == "Sadie, dog")
    assert(shelter.adoptAPet(("Floofy", "cat")) == None)
    assert(shelter.adoptAPet(("Sally", "person", "cat")) == "Woof, cat")
    assert(shelter.adoptAPet(("Ji", "person", "cat")) == "Floofy, cat")
    assert(shelter.adoptAPet(("Ali", "person", "cat")) == "Chirpy, dog")
    
exampleTest()


        

