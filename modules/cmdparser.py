import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Image tiling")
    parser.add_argument("--source_dir", required=False 
                        ,help="source directory where images are present")
    parser.add_argument("--tile", required=True, metavar="4"
                        , help="No of times the image is to be tiled")
    parser.add_argument("--target_dir", required=False, metavar="target-directory/TiledImages"
                        , help="Target directory where images is to be saved" )
    return parser.parse_args()


parse_arguments()