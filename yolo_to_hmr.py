import sys
import argparse
from yolo import YOLO, detect_video 
from PIL import Image
import glob 
import time 


def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

def to_hmr(yolo, args): 

    path = args.path_to_images
    files = glob.glob(path + '*.jpg')
    for file in files:

        image = Image.open(file)
        r_image = yolo.to_hmr(image, args.target_class_name)
        r_image.show()

        time.sleep(0.5)
        r_image.close() 
        # input('Press enter to process next image')
    
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''

    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help = "[Optional] Video output path"
    )

    parser.add_argument('--path_to_images', default = "./../dataset/")
    parser.add_argument('--target_class_name', default = "Name")

    FLAGS = parser.parse_args()

    to_hmr(YOLO(**vars(FLAGS)), FLAGS)
    # to_hmr(None, FLAGS)

    # if FLAGS.image:
    #     """
    #     Image detection mode, disregard any remaining command line arguments
    #     """
    #     print("Image detection mode")
    #     if "input" in FLAGS:
    #         print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
    #     detect_img(YOLO(**vars(FLAGS)))
    # elif "input" in FLAGS:
    #     detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    # else:
    #     print("Must specify at least video_input_path.  See usage with --help.")
