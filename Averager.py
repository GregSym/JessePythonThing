import numpy as np

example_list = [[1,1],[1,2,3],[1,2]]

class Targets:
    """Relate the targets for listing
    """
    def __init__(self, loc: int, val):
        self.loc = loc
        self.val = val
    
    def __repr__(self):
        return f"{self.loc}, {self.val}"

def averager():
    target_list = [] # define list of targets for averaging
    valid_pos = []
    for nested_list in example_list:
        for i, target_num in enumerate(nested_list):
            target = Targets(loc=i, val=target_num) # create objects
            target_list.append(target) # append the defined target with the location
    for target in target_list: # get the full list of valid locations
        if target.loc not in valid_pos:
            valid_pos.append(target.loc)
    output_array = np.zeros(len(valid_pos))
    for pos in valid_pos:
        accumulator = [] # local accumulator
        for target in target_list:
            if target.loc==pos:
                accumulator.append(target.val)
        #avg_target = Targets(loc=pos, val=np.mean(accumulator)) # new average value at position
        output_array[pos] = np.mean(accumulator)
    return output_array

if __name__=="__main__":
    print(averager())
