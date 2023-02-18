# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys

# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
OPS = ['noop', 'add', 'mul', 'gt', 'or', 'nand', 'min', 'shift']
def process(line):
    # print(line)
    # Split operation/command
    op, args = split_op(line)
    
    # Execute operation
    if (op not in OPS) | (args == 'invalid') | (args == 'no args' and op != 'noop'):
        return f'invalid operation {line}\n'
    
    if op == 'noop':
        ret = '' if args == 'no args' else 'invalid'
    elif op == 'add':
        ret = add_op(args)
    elif op == 'mul':
        ret = mul_op(args)
    elif op == 'gt':
        ret = gt_op(args)
    elif op == 'or':
        ret = or_op(args)
    elif op == 'nand':
        ret = nand_op(args)
    elif op == 'min':
        ret = min_op(args)
    elif op == 'shift':
        ret = shift_op(args)
    else: return f'invalid operation {line}\n'
    
    # print(ret)
    return f'invalid operation {line}\n' if ret=='invalid' else ret
            
def split_op(line):
    ops_split = line.split(' ')
    
    if len(ops_split) == 1:
        return ops_split[0], 'no args'
    
    # separate the operation/command from the arguments
    op = ops_split.pop(0)
    args = []
    
    # checks and convert the arguments to integer if they are valid (integer)
    for a in ops_split:
        try:
            args.append(int(a))
        except Exception:
            return op, 'invalid'
    
    
    return str(op), args

# add operation
def add_op(args):
    return sum(args) if len(args) > 1 else 'invalid'

# multiplication operation
def mul_op(args):
    prod = 1
    for i in args:
        prod *= i
    return prod

# greater than operation
def gt_op(args):
    return int(args[0] > args[1]) if len(args) == 2 else 'invalid'

# or operation
def or_op(args):
    return int(bool(args[0]) or bool(args[1])) if len(args) == 2 else 'invalid'

# nand operation
def nand_op(args):
    return int(not(args[0] & args[1])) if len(args) == 2 else 'invalid'

# min operation
def min_op(args):
    return min(args)

# shift operation
def shift_op(args):
    return (args[0] << args[1]) if ((len(args) == 2) and (args[0] > 0)) else 'invalid'

# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line 
def run(filename):
    with open(filename, 'r') as file:
        for operation in file: #.readlines():
            process(operation.strip())

# This code will call the run function with a filename, if it's provided on the 
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [path/to/sample]")
    else:
        run(sys.argv[1])
