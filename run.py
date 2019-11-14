from modules.cmdparser import *
from modules.tiling import *

if __name__ == "__main__":
    args = parse_arguments()

    if args:
        image_tiling(args)
        # print("ok")
    else:
        exit(1)



