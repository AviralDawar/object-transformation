import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.all_coords = [x.copy() for x in A]
        self.all_coords_N = [x.copy() for x in A]
        self.new_lst = [x.copy() for x in A]
        pass
 
    
    def translate(self, dx = 0, dy = 0):
        Shape.translate(self , dx , dy)
        self.new_lst = []
        T = self.T_t
        for index0 in self.all_coords_N:
            result = np.matmul(T , index0)
            self.new_lst.append(result)
        self.new_lst = np.round_(self.new_lst , 2)
        self.new_lst = np.array(self.new_lst).tolist()

        self.all_coords_N = self.new_lst

        return [[x for (x,y,z) in self.new_lst], [y for (x,y,z) in self.new_lst]]

        
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        pass

    
    def scale(self, sx, sy):
        Shape.scale(self , sx , sy)
        self.new_lst = []
        T = self.T_s
        rx = np.mean([x for x,y,z in self.all_coords_N])
        ry = np.mean([y for x,y,z in self.all_coords_N])
        # rx,ry is centroid
        for index0 in self.all_coords_N:
            index0[0] -= rx
            index0[1] -= ry
            result = np.matmul(T , index0)
            result[0] += rx
            result[1] += ry
            self.new_lst.append(result)
        self.new_lst = np.round_(self.new_lst , 2)
        self.new_lst = np.array(self.new_lst).tolist()

        self.all_coords_N = self.new_lst

        return [[x for (x,y,z) in self.new_lst], [y for (x,y,z) in self.new_lst]]
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        pass
 
    
    def rotate(self, deg, rx = 0, ry = 0):

        Shape.rotate(self , deg)
        self.new_lst = []
        T = self.T_r
        for index4 in self.all_coords_N:
            index4[0] -= rx
            index4[1] -= ry
            result = np.matmul(T, index4)
            result[0] += rx
            result[1] += ry
            self.new_lst.append(result)
        self.new_lst = np.round_(self.new_lst , 2)
        self.new_lst = np.array(self.new_lst).tolist()

        self.all_coords_N = self.new_lst

        return [[x for (x,y,z) in self.new_lst], [y for (x,y,z) in self.new_lst]]
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        axis = plt.gca()
        for index2 in self.all_coords:
            index2.pop(2)
        polygon = plt.Polygon(self.all_coords , ls = '--' , fill = False)
        if self.new_lst != self.all_coords:
            for index3 in self.new_lst:
                index3.pop(2)
            polygon_N = plt.Polygon(self.new_lst , ls = '-' , fill = False)
            axis.add_artist(polygon_N)
        axis.add_artist(polygon)
        
        
        
        x_coord_lst = []
        y_coord_lst = []
        for index3 in self.new_lst:
            x_coord_lst.append(index3[0])
            y_coord_lst.append(index3[1])
        xlimit = max(max(abs(x) for x,y,in self.all_coords) , max(abs(x) for x,y in self.new_lst))
        ylimit = max(max(abs(y) for x,y in self.all_coords) , max(abs(y) for x,y in self.new_lst))
        Shape.plot(self , xlimit , ylimit)
        
        pass


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        
        '''
        Initializations here
        '''
        self.centreX = x
        self.centreY = y
        self.centreX_N1 = x
        self.centreY_N1 = y
        self.radius_N = radius
        self.centreX_N = x
        self.centreY_N = y
        self.radius = radius
        self.radius_N1 = radius
        
        pass

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        #make matrix
        #multiply with self.T_t
        Shape.translate(self , dx , dy)
        V = [[self.centreX_N1] , [self.centreY_N1] , [1]]
        T = self.T_t
        tv = np.matmul(T,V)
        self.centreX_N = tv[0][0]
        self.centreY_N = tv[1][0]
        self.radius_N = self.radius_N1
        (self.centreX_N , self.centreY_N , self.radius_N) = np.round_((self.centreX_N , self.centreY_N , self.radius_N), 2)

        self.centreX_N1, self.centreY_N1, self.radius_N1 = (self.centreX_N , self.centreY_N , self.radius_N)
        return (self.centreX_N , self.centreY_N , self.radius_N)
        
        
    def scale(self, sx):
        Shape.scale(self , sx , sx)
        V = [[self.centreX_N1] , [self.centreY_N1] , [0]]
        T = self.T_s
        tv = np.matmul(T,V)
        self.radius_N = self.radius_N1 * (tv[0][0]/self.centreX_N1)
        self.centreX_N = self.centreX_N1
        self.centreY_N = self.centreY_N1
        (self.centreX_N , self.centreY_N , self.radius_N) = np.round_((self.centreX_N , self.centreY_N , self.radius_N), 2)

        self.centreX_N1, self.centreY_N1, self.radius_N1 = (self.centreX_N , self.centreY_N , self.radius_N)
        return (self.centreX_N , self.centreY_N , self.radius_N)
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        Shape.rotate(self , deg)
        V = [[self.centreX_N1-rx] , [self.centreY_N1-ry] , [0]]
        T = self.T_r
        tv = np.matmul(T,V)
        self.centreX_N = tv[0][0] + rx
        self.centreY_N = tv[1][0] + ry
        self.radius_N = self.radius_N1
        (self.centreX_N , self.centreY_N , self.radius_N) = np.round_((self.centreX_N , self.centreY_N , self.radius_N), 2)

        self.centreX_N1, self.centreY_N1, self.radius_N1 = (self.centreX_N , self.centreY_N , self.radius_N)
        return (self.centreX_N , self.centreY_N , self.radius_N)
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        pass
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''


        circle = plt.Circle((self.centreX , self.centreY) , self.radius , ls = '--' , fill = False)
        circle_N = plt.Circle((self.centreX_N , self.centreY_N) , self.radius_N , ls = '-' , fill = False)
        axis = plt.gca() 
        axis.add_artist(circle)
        axis.add_artist(circle_N)
        xlimit = max(abs(self.centreX_N) + self.radius_N , abs(self.centreX) + self.radius)
        ylimit = max(abs(self.centreY_N) + self.radius_N , abs(self.centreY) + self.radius)
        Shape.plot(self , xlimit , ylimit)

        pass

        

        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    veribose = int(input('verbose? 1 to plot, 0 otherwise: '))
    test_cases = int(input('Enter the number of test cases: ')) # add a for loop as number of test cases denote the amount of shapes taken
    for index60 in range(test_cases):
        shape = int(input('Enter type of shape (polygon/circle):'))
        if shape == 0:
            n = int(input('Enter the number of sides: ')) # For the number of sides in a polygon
            coord_lst = []
            for no_sides in range(n):
                coords = input('enter(x' + str(no_sides+1) + ',y' + str(no_sides+1) + ') ')
                coords = coords.split()
                x_coord = int(coords[0])
                y_coord = int(coords[1])
                coord_lst.append([x_coord , y_coord , 1])
            polygon = Polygon(coord_lst)  
            no_queries = int(input('Enter the number of queries: '))
            print('''Enter Query:
1) R deg (rx) (ry) 
2) T dx (dy)
3) S sx (sy)
4) P)''')
            updated_self_coords = []
            for index6 in range(no_queries):
                query = input()
                query = query.split()
                if query[0] == 'T':
                    
                    if len(query) == 2:
                        translate = polygon.translate(int(query[1]) , int(query[1]))
                    elif len(query) == 3:
                        translate = polygon.translate(int(query[1]) , int(query[2]))
                    if index6 == 0:
                        for index9 in coord_lst:
                            print(index9[0] , end = ' ')
                        for index10 in coord_lst:
                            print(index10[1] , end = ' ')
                    else:
                        for index52 in updated_self_coords:
                            print(index52[0] , end = ' ')
                        for index53 in updated_self_coords:
                            print(index53[1] , end = ' ')
                    print()
                    for index7 in translate:
                        for index8 in index7:
                            print(index8 , end = ' ')
                    if veribose == 1:
                        polygon.plot()
                    print()
                    updated_self_coords = []
                    for index17 in range(len(translate[0])):
                        updated_self_coords.append([translate[0][index17] , translate[1][index17] , 1])
                    polygon = Polygon(updated_self_coords)
                if query[0] == 'S':
                    if len(query) == 2:
                        scale = polygon.scale(int(query[1]),int(query[1]))
                    elif len(query) == 3:
                        scale = polygon.scale(int(query[1],int(query[2])))
                    if index6 == 0:
                        for index53 in coord_lst:
                            print(index53[0] , end = ' ')
                        for index54 in coord_lst:
                            print(index54[1] , end = ' ')
                    else:
                        for index55 in updated_self_coords:
                            print(index55[0] , end = ' ')
                        for index56 in updated_self_coords:
                            print(index56[1] , end = ' ')
                    print()
                    for index57 in scale:
                        for index58 in index57:
                            print(index58 , end = ' ')
                    if veribose == 1:
                        polygon.plot()
                    print()
                    updated_self_coords = []
                    for index59 in range(len(translate[0])):
                        updated_self_coords.append([translate[0][index59] , translate[1][index59] , 1])
                    polygon = Polygon(updated_self_coords)
                if query[0] == 'R':
                    
                    if len(query) < 4:
                        rotate = polygon.rotate(float(query[1]))
                    else:
                        rotate = polygon.rotate(float(query[1]), float(query[2]), float(query[3]))

                    if index6 == 0:
                        for index9 in coord_lst:
                            print(index9[0] , end = ' ')
                        for index10 in coord_lst:
                            print(index10[1] , end = ' ')
                    else:
                        for index50 in updated_self_coords:
                            print(index50[0] , end = ' ')
                        for index51 in updated_self_coords:
                            print(index51[1] , end = ' ')
                    print()
                    for index11 in rotate:
                        for index12 in index11:
                            print(index12 , end = ' ')
                    print()
                    if veribose == 1:
                        polygon.plot()
                    for index18 in range(len(rotate[0])):
                        updated_self_coords.append([rotate[0][index18] , rotate[1][index18] , 1])
                    polygon = Polygon(updated_self_coords)
                if query[0] == 'P':
                    polygon.plot()
        if shape == 1:
            dimensions = input('Enter the x co-ordinate of the centre ,y co-ordinate of the centre , radius (space seperated): ')
            dimensions = dimensions.split()
            no_queries = int(input('Enter the number of queries: '))
            print('''Enter Query:
1) R deg (rx) (ry) 
2) T dx (dy)
3) S sr
4) P)''')
            circle = Circle(int(dimensions[0]) , int(dimensions[1]) , int(dimensions[2]))
            for index13 in range(no_queries):
                query = input()
                query = query.split()
                
                if query[0] == 'T':
                    
                    if len(query) == 2:
                        translate = circle.translate(int(query[1]) , int(query[1]))
                    elif len(query) == 3:
                        translate = circle.translate(int(query[1]) , int(query[2]))
                    if index13 == 0:
                        print(int(dimensions[0]) ,' ', int(dimensions[1]) , ' ' , int(dimensions[2]))
                    else:
                        print(a,' ' , b, ' ' , c)
                    for index14 in translate:
                        print(index14 , end = ' ')
                    if veribose == 1:
                        circle.plot()
                    for index21 in translate:
                        a = translate[0]
                        b = translate[1]
                        c = translate[2]
                    circle = Circle(a , b , c)             
                if query[0] == 'S':
                    
                    scale = circle.scale(int(query[1]))
                    if index13 == 0:
                        print(int(dimensions[0]) ,' ', int(dimensions[1]) , ' ' , int(dimensions[2]))
                    else:
                        print(a,' ' , b, ' ' , c)
                    for index15 in scale:
                        print(index15 , end = ' ')
                    if veribose == 1:
                        circle.plot()
                    for index22 in rotate:
                        a = rotate[0]
                        b = rotate[1]
                        c = rotate[2]
                    circle = Circle(a , b , c)
                if query[0] == 'R':
                    
                    rotate = circle.rotate(int(query[1]))
                    if index13 == 0:
                        print(int(dimensions[0]) ,' ', int(dimensions[1]) , ' ' , int(dimensions[2]))
                    else:
                        print(a,' ' , b, ' ' , c)
                    for index15 in rotate:
                        print(index15 , end = ' ')
                    print()
                    if veribose == 1:
                        circle.plot()
                    for index20 in rotate:
                        a = rotate[0]
                        b = rotate[1]
                        c = rotate[2]
                    circle = Circle(a , b , c)
                if query[0] == 'P':
                    circle.plot()

