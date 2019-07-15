import sys

sys.stderr.write("This is stderr text\n")
sys.stderr.flush()
sys.stdout.write("This is stdout text\n")

#argv used to make arguments available to python
def main(arg):
    print(arg)

main(sys.argv[1])
