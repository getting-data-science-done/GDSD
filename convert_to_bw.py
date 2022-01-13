from PIL import Image
import sys

def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

if __name__ == '__main__':  
    if len(sys.argv) < 3:
        print("Error you need to supply input and output paths")
    else:
        black_and_white( sys.argv[1], sys.argv[2])


