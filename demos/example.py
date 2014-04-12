#!/usr/bin/env python
# encoding: utf-8
import sys

from genderpredictor import GenderPredictor


def main():
    gp = GenderPredictor()
    accuracy = gp.trainAndTest()
    print 'Accuracy: %f' % accuracy
    print 'Most Informative Features'
    feats = gp.getMostInformativeFeatures(10)
    for feat in feats:
        print '\t%s = %s'% feat
    
    print '\nStephen is classified as %s' % gp.classify('Stephen')


if __name__ == '__main__':
    sys.exit(main())
