class Number:
    def __init__(self,list1,reverse=False):
        self.list1=list1
        self.reverse=reverse

    def shortF(self):
        sizeO=len(self.list1)
        for i in range(0,sizeO-1):
            for j in range(i+1,sizeO):
                state = self.list1[i]<self.list1[j] if self.reverse else self.list1[i]>self.list1[j]
                if state:
                    aux=self.list1[i]
                    self.list1[i]=self.list1[j]
                    self.list1[j]=aux
    
    def printF(self):
        for i in self.list1:
            print(i , end=' ')
        print()

class TupleF:
    def __init__(self,list1,reverse=False,indexF=0):
        self.list1=list1
        self.indexF=indexF
        self.reverse=reverse

    def shortF(self):
        sizeO = len(self.list1)
        for i in range(0, sizeO-1):
            for j in range(i+1, sizeO):
                state = self.list1[i][self.indexF]<=self.list1[j][self.indexF] if self.reverse else self.list1[i][self.indexF]>=self.list1[j][self.indexF]
                if state:
                    if self.indexF==1 and self.list1[i][self.indexF]==self.list1[j][self.indexF]:
                        if self.list1[i][0]>self.list1[j][0]:
                            aux = self.list1[i]
                            self.list1[i] = self.list1[j]
                            self.list1[j] = aux
                    else:
                        aux = self.list1[i]
                        self.list1[i] = self.list1[j]
                        self.list1[j] = aux

    def printF(self):
        for i in self.list1:
            print(i , end=' ')
        print()
       
def shortF(objectF):
    objectF.shortF()

def printF(objectF):
    objectF.printF()

numbers =[645.41, 37.59, 76.41, 5.31, -34.23, 1.11, 1.10, 23.46, 635.47, -876.32, 467.83, 62.25]
people=[("Hal", 20), ("Susann", 31), ("Dwight", 19), ("Kassandra", 21), ("Lawrence", 25), 
("Cindy", 22), ("Cory", 27), ("Mac", 19), ("Romana", 27), ("Doretha", 32), ("Danna", 20),
 ("Zara", 23), ("Rosalyn", 26), ("Risa", 24), ("Benny", 28), ("Juan", 33), ("Natalie", 25)]

numbers=Number(numbers)
people=TupleF(people)

#1. short numbers in ascending order
print("Short numbers in ascending order")
shortF(numbers)
printF(numbers)

#2. short people in alphabetical order (lexicographically) per name
print("\n\nOrder people in alphabetical order (lexicographically) per name")
shortF(people)
printF(people)

#3. Order people in descending order per age, where a person with the same age shoulf be ordered alphabetical by name (lexicographically)"
print("\n\nOrder people in descending order per age, where a person with the same age shoulf be ordered alphabetical by name (lexicographically)")
people.indexF=1
people.reverse=True
shortF(people)
printF(people)

