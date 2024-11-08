from LinkedList import *
from manim import *


scene = LinkedList([1,2,3,4,7,3,8,9,0,2,3])
scene.delete(3)
scene.delete(8)
# interface.create_linked_list()
scene.render()