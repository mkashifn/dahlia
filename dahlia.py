import argparse
import sys
from utils.dataset_verification import verify_dataset
from utils.env_verification import verify_environment
from utils.experiments import Experiment

SW_VER='0.1.0'
SW_DATE='26-Jan-2020'
VERSION_STR='Dahlia version {} {}'.format(SW_VER, SW_DATE)

def add_arguments(parser):
  parser.add_argument("-v", "--version", help="show program version", action="store_true")
  
  subparsers = parser.add_subparsers(help='dataset verification functions')
  
  vds = subparsers.add_parser('verifydataset', help='verify a dataset')
  vds.add_argument("-d", "--dataset", required=True, help="dataset name")
  vds.set_defaults(vds=True, func=verifydataset)
  
  venv = subparsers.add_parser('verifyenv', help='verify the environment')
  venv.set_defaults(venv=True, func=verifyenvironment)

def verifydataset(args):
  verify_dataset(args.dataset)
  sys.exit(0)

def verifyenvironment(args):
  verify_environment()
  sys.exit(0)

if __name__ == '__main__':

  #from multiprocessing import freeze_support
  #freeze_support()

  # initiate the parser
  parser = argparse.ArgumentParser()
  add_arguments(parser)

  # read arguments from the command line
  args = parser.parse_args()

  # check for --version or -V
  if args.version:
    print(VERSION_STR)

  if hasattr(args, 'func'):
    args.func(args)
