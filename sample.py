A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
B=[[7,8],[9,10],[11,12]]
result=[]
#First i'm going to take into consideration the number of rows present
#in the result which is equal to the length of the first element
class isosceles_right_triangle(isosceles_triangle,right_triangle):
    def __init__(self, x):
        self.x=x

    def check_isosceles(self):
        if len(set(self.x)) ==2:
            return True
        else:
            return False
        
    def check_right_angle(self):
        x_sorted=sorted(self.x)
        small=(x_sorted[0]**2)+(x_sorted[1]**2)
        return True if small==x_sorted[3]**2 else False