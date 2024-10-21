import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
sin_x = np.sin(x)

def print_table(x, sin_x):
    for x, y in zip(x, sin_x):
        print(f"{x} {y}")
def main():
    print_table(x, sin_x)
if __name__=="__main__":
    main()