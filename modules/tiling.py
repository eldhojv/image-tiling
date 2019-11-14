import os
from PIL import Image

ROOT_DIR = ''
DEFAULT_SOURCE_DIR = os.path.join(ROOT_DIR, 'Images')
DEFAULT_TARGET_DIR = os.path.join(ROOT_DIR, 'TiledImages')
FILE_TYPE = ('jpg', 'jpeg', 'png')

def image_tiling(args):
    no_tiles = int(args.tile)

    if not args.target_dir:
        target_image_directory = DEFAULT_TARGET_DIR
    else:
        target_image_directory = os.path.join(args.target_dir,'TiledImages')
        if not os.path.exists(target_image_directory):
            os.makedirs(target_image_directory)

    if not args.source_dir:
        source_image_directory = DEFAULT_SOURCE_DIR
    else:
        source_image_directory = args.source_dir

    image_lists = [image_lists for image_lists in os.listdir(source_image_directory) if image_lists.endswith(FILE_TYPE)]
    
    for each_image in image_lists:
        im = Image.open(os.path.join(source_image_directory, each_image))
        dest_image = Image.new('RGB', (im.width*no_tiles, im.height*no_tiles))
        # tiling horizontally and vertically
        for x in range(no_tiles):
            for y in range(no_tiles):
                dest_image.paste(im, (im.width*x, im.height*y))
                
        dest_image.save(os.path.join(target_image_directory, each_image))

