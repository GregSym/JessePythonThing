import numpy as np

A_1 = [0,0]
A_2 = [0,1]
A_3 = [0,2]

B_1 = [1,0]
B_2 = [1,1]
B_3 = [1,2]

A = np.vstack([A_1, A_2, A_3])
B = np.vstack([B_1, B_2, B_3])

class MatrixMerge:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        

    def createMerge(self):
        self.C = []
        new_row = []
        for i, row in enumerate(A, 0):   # gets both index and object at index for legibility
            for j, element in enumerate(B[i], 0):
                #print(element)
                np.append(row, element)
            self.C.append(row.flatten())
            print(self.C)
            new_row.clear()
        return self.C

    def createMergeTheSequel(self):
        """
        desired product: a new matrix of arrays combining the rows of A and B such that calling C[0][1] returns [A[0],B[1]].flatten()
        - currently works only for C[0][0]
        """
        #size = len(self.A)*len(self.B)
        new_row = []
        new_matrix = []
        for i, row in enumerate(A, 0):
            new_row = np.concatenate((row,B[i]))
            new_matrix.append(new_row)

        # create new vstack with the elements in B shuffled

        # add new matrix combo

        # create new vstack with the elements in A shuffled

        # add new matrix combo

        return new_matrix        

if __name__=="__main__":
    print(A[0])
    print(MatrixMerge(A=A, B=B).createMergeTheSequel()) 