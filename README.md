# Image Tiling
Script to generate and save a tiled image from an input image

## Usage

````
usage: run.py [-h] [--source_dir source-directory/Images] 
                    --tile <number>
                   [--target_dir target-directory/TiledImages]

Image tiling

optional arguments:
  -h, --help            show this help message and exit
  --source_dir source-directory/Images
                        source directory where images are present
  --tile <number>       No of times the image is to be tiled horizontally and vertically
  --target_dir target-directory/TiledImages
                        Target directory where images is to be saved
````
## Example

  Generate a tile image 
  ````
  python run.py --source_dir "E:\image-tiling\SourceImages" --tile 3 --target_dir "E:\image-tiling\TargetImages"
  ````  
  Or you can run simply with defualt config
  (source image directory should be present in the root directory with folder name Images)
  ````
  python run.py --tile 4
  ````
## Tiled Images 
  Image for tiling
  
  <img src="https://github.com/eldhojv/image-tiling/blob/master/Images/cat_image_1.jpg" width="250">
  
  Image tiled both horizontally and vertically (tile number - 3)
  
  <img src="https://github.com/eldhojv/image-tiling/blob/master/TiledImages/cat_image_1.jpg" width="250">
  
