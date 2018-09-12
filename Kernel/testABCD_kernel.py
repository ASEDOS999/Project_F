import kernel
import sys

sys.path.append("../Segmentation")
sys.path.append("../Recognition")
sys.path.append("../Interface")

set = []
set.append(('A', '../SET/A'))
set.append(('B', '../SET/B'))
set.append(('C', '../SET/C'))
set.append(('D', '../SET/D'))

main.text(set, 'Desktop/PROJECTS/Project_F/ABCD/T_3.gif')
