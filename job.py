import os
from pyats.easypy import run

def main(runtime):
    run(
        testscript='testscript.py',
        testbed=runtime.testbed
    )
