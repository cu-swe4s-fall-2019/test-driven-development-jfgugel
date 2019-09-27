import sys
import math
import argparse



def list_mean(L):
    
    if L is None:
        return None
        sys.exit(1)
    
    if len(L) == 0:
        return None
        sys.exit(1)
             
    else: 
        mean = sum(L)/len(L)
        return mean
    

def list_stdev(V):
    
    if len(L) == 0:
    return None
    sys.exit(1)
        
    else:
        stdev = math.sqrt(sum([(mean(V)-x)**2 for x in L]) / len(L))
        return stdev



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    parser.add_argument('--column_number',
                        type=int,
                        help='The name of the column',
                        required=True)

    args = parser.parse_args()

    try: 
        file = open(args.file_name, 'r')
    except FileNotFoundError:
        print('Could not find' + args.file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open' + args.file_name)
        sys.exit(1)

    L = []

    for col in file:
        try: 
            A = [int(x) for x in col.split()]
        except ValueError:
            print('Check column values')
            sys.exit(1)
        try: V.append(int(A[args.column_number]))
        except IndexError:
            print('Problem with column number')
            sys.exit (1)



    print('mean:', mean(V))
    print('stdev:', stdev(V))
