import os
import random
import sys
import subprocess
from scipy.optimize import minimize

DATA_DIRNAME = "data/"
D_MIN = -100
D_MAX = 100
FUZZY_R_MIN = -100
FUZZY_R_MAX = 100

def curry_executable(f, a):
    def curried(b):
        arg_a = str(a)
        arg_b = str(b[0])
        result = float(subprocess.run(["python3", f, str(a), str(b[0])], capture_output=True, text=True).stdout)
        print(f'({arg_a : <20}, {arg_b: >20}) |---> {result}')
        return result
    return curried

def prep_data_dir():
    if not os.path.isdir(DATA_DIRNAME):
        os.mkdir(DATA_DIRNAME)

def generate_data(exec_name, data_file_name, n):
    out_path = DATA_DIRNAME + data_file_name
    with open(out_path, "w") as out_file:
        out_file.write("a\tb\tscore\n")
        for _ in range(n):
            x = random.uniform(D_MIN, D_MAX)
            y0 = random.uniform(FUZZY_R_MIN, FUZZY_R_MAX)
            f = curry_executable(exec_name, x)
            m = minimize(f, y0, method='Nelder-Mead')
            msg = f'{x}\t{m.x[0]}\t{m.fun}'
            print(f'Writing: {msg} to {out_path}.')
            out_file.write(f'{msg}\n')
            out_file.flush()

def main():
    args = sys.argv
    if len(args) == 2:
        prep_data_dir()
        generate_data(args[1], "data.tsv", 10)
    else:
        print("Please provide exactly one function to the training routine.")

if __name__ == '__main__':
    main()
