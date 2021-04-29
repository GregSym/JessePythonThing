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
        self.matrixOfMatrices()        

    def createMerge(self):
        """
        desired product: a new matrix of arrays combining the rows of A and B such that calling C[0][1] returns [A[0],B[1]].flatten()
        - currently works only for C[0][0]
        """
        #size = len(self.A)*len(self.B)
        new_row = []
        new_matrix = []
        for i, row in enumerate(self.A, 0):
            new_row = np.concatenate((row,self.B[i]))
            new_matrix.append(new_row)

        # create new vstack with the rows in B shuffled

        #np.roll(self.B, 1)

        # add new matrix combo

        # create new vstack with the rows in A shuffled

        # add new matrix combo

        return new_matrix

    def matrixOfMatrices(self): 
        """Assemble the final product
        - shape: [[A0B*],[A1B*],[A2B*]]
        """
        self.C = []
        # row 0 (A0)
        for _, _ in enumerate(self.A, 0):
            row_0 = self.createMerge()
            np.roll(self.B, 1)
            self.C.append(row_0)
                        

if __name__=="__main__":
    print(A[0])
    print(MatrixMerge(A=A, B=B).C[0][1]) 