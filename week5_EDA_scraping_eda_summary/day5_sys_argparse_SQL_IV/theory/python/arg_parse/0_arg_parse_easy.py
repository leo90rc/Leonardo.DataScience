import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int, help="the base")
parser.add_argument("-y", "--y", type=int, help="the exponent", required=True)
parser.add_argument("-v", "--v", default=0, type=int, help="the result will be multiplied by 'v'")
args = vars(parser.parse_args())

print("####################\n")
print(type(args))
print(args)
x = args["x"]
y = args["y"]
v = args["v"]

print("x:", x)
print("type(x):", type(x))
print("y:", y)
print("v:", v)