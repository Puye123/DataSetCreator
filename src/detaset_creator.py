# -*- coding: utf-8 -*-
import cv2
import datetime
import os
import sys
from progressbar import ProgressBar, Percentage, Bar, CurrentTime, Counter, ETA
from argparse import ArgumentParser

# Generate a unique name based on the current time
def get_unique_name():
    date = datetime.datetime.now()
    unique_name = date.strftime("%Y%m%d_%H%M%S%f")
    return unique_name

# Make a directory
def make_directory(dir_name):
    if not os.path.isdir('./' + dir_name):
        try:
            os.mkdir(dir_name)
        except:
            print("cannot make a directory: " + dir_name)
            sys.exit(1)

# Parse command line arguments
def parser():
    usage = 'python [--dir <dir_name>] [--num <num_of_pictures>] [--size <size_of_pictures>] [--format <jpg | png | bmp>] [--help]'.format(__file__)
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('-d', '--dir', help='directory name', type=str, default='images', metavar='<dir_name>')
    argparser.add_argument('-n', '--num', help='number of pictures', type=int, default=10, metavar='<num_of_pictures>')
    argparser.add_argument('-s', '--size', help='size of pictures', type=int, default=224, metavar='<size_of_pictures>')
    argparser.add_argument('-f', '--format', help='image format [jpg | png | bmp]', type=str, default='jpg', metavar='<image_format>')
    args = argparser.parse_args()
    return args

def main():
    args = parser()
    if args.format != 'jpg' and args.format != 'png' and args.format != 'bmp':
        print("illegal format: " + args.format)
        print("You can use [jpg | png | bmp]")
        sys.exit(1)

    make_directory(args.dir)
    p = ProgressBar(0, args.num, widgets=[
        CurrentTime(), ':','(', Counter(), ' of {}) '.format(args.num), Bar(), ' ', ETA(),
    ])

    # count down
    cap = cv2.VideoCapture(0)
    ready = 59
    while ready > 0:
        ret, frame = cap.read()
        cv2.putText(frame, str(int(ready/10)), (200, 300), cv2.FONT_HERSHEY_COMPLEX, 10, (0, 0, 255))
        cv2.imshow('camera capture', frame)
        ready -= 1
        k = cv2.waitKey(100)
    cv2.destroyAllWindows()

    # capture images
    count = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow('camera capture', frame)
        frame = cv2.resize(frame, (args.size, args.size)) 
        cv2.imwrite('./' + args.dir + '/' + get_unique_name() + '.jpg', frame)
        p.update(count)
        count += 1
        if(count >= args.num):
            break
        k = cv2.waitKey(30)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()