import sys, os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.util.validation import verify_biac_path


verify_biac_path("/Volumes/lj146/Documents/CBT.01/")

