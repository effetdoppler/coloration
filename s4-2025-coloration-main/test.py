from coloration_program import *
from testcolor import *

if __name__ == '__main__':
    files = "files"

    print("greedy")
    print(run_verif_coloration(color_greedy, files))

    print("dsatur")
    print(run_verif_coloration(color_dsatur, files))

    print("weslsh_powell")
    print(run_verif_coloration(color_weslsh_powell, files))

    print("rlf")
    print(run_verif_coloration(color_rlf, files))