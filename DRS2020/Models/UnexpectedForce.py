from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Models.Block import Block, BlockType
import random
import sys

from Models.Block import RotateDegrees


class Force(Block):
    x = 0
    y = 0
    effect = 0
    picture = 'resources/unexpected.png'
    deactivateForce = pyqtSignal()
    activateForce = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent.x, parent.y)
        parent.BType = BlockType.Force
        parent.RDegrees = RotateDegrees.Right