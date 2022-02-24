#!/usr/bin/python

import sys\


def main(argv):
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', (argv))  
    #TODO
    # convert images to array with 3 rgb values per pixel -- ideally 5000 correct images and 2500 incorrect images
    # create test datasets based on each of the 10 CIFAR-10 classes
    # instantiate a perceptron object
    # run training for each of the 10 image classes
    # pick a random 9 images from the dataset in a recaptcha style question
    # run perceptron.classify method on each of the 9 images


if __name__ == "__main__":
    main(sys.argv)