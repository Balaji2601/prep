class DSU:
    def __init__(self):
        self.V = 10
        self.parent = [i for i in range(self.V)]
        self.size = [1]*self.V
    
    def find_parent(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]

    def size(self, x, y):
        parent_of_x = self.find_parent(x)
        parent_of_y = self.find_parent(y)

        if parent_of_x == parent_of_y:
            return

        if self.size[parent_of_x] > self.size[parent_of_y]:
            self.parent[parent_of_y] = parent_of_x # x is becoming parent of y, so x size should increase
            self.size[parent_of_x] += self.size[parent_of_y]
        elif self.size[parent_of_x] < self.size[parent_of_y]:
            self.parent[parent_of_x] = parent_of_y # y is becoming parent of x, so y size should increase
            self.size[parent_of_y] += self.size[parent_of_x]
        else:
            self.parent[parent_of_x] = parent_of_y # y is becoming parent of x, so y size should increase
            self.size[parent_of_y] += self.size[parent_of_x]
