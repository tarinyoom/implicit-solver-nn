import sys
from scipy.optimize import rosen

def main():
    X = [ float(x) for x in sys.argv[1:] ]
    print(rosen(X))

if __name__ == '__main__':
    main()
