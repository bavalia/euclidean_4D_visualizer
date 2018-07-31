
4D Visualizer 
http://eusebeia.dyndns.org/4d/


3D Visualizer
(1) Blender - multifunctionality 
(2) Mayavi - python based, light weight, python support
(3) Vispy - high-performance interactive 2D/3D data visualization library.
(4) matplotlib/mplot http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

#Mayavi http://docs.enthought.com/mayavi/mayavi/index.html
 -- mlab section - http://docs.enthought.com/mayavi/mayavi/mlab.html#simple-scripting-with-mlab
 -- numpy - http://docs.enthought.com/mayavi/mayavi/auto/examples.html#example-gallery
 -- tutorial - http://docs.enthought.com/mayavi/mayavi/application.html#using-the-mayavi-application

#mlab - mayavi python 
http://docs.enthought.com/mayavi/mayavi/mlab.html
ipython --gui=wx # When using IPython with mlab
mesh() : Plot a surface described by three 2D arrays, x, y, z
triangular_mesh() : fully specified by x, y and z coordinates of its vertices, and the (n, 3) array of the indices of the triangles.


# File format to store data
#.obj http://www.scratchapixel.com/lessons/3d-advanced-lessons/obj-file-format/obj-file-format/
v 0 0 0
v 1 0 1
v 0 1 1
vp
l 

#.igs

#.vtk
http://www.vtk.org/VTK/img/file-formats.pdf



# Storage/Representation of 4D bounded object

--use surface blocks, triangles 
--use volume blocks 



# python key detect, Tkinter app

import Tkinter as tk

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
#root.geometry('300x200')
#text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
#text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()


### OR http://www.ster.kuleuven.be/~pieterd/python/html/plotting/interactive.html

plt.ion() #to enable interactive mode
show(block=False) #in option

# at end, to prevent execution from finishing
show()

### OR interctive key input (most useful)
def ontype(event):
 """Deal with keyboard events"""
 print("You pressed key {:s}".format(event.key))
 global x

fig.canvas.mpl_connect('key_press_event',ontype)
plt.show()

# key mapping 
You pressed key dec
You pressed key enter
You pressed key 0
You pressed key dec
You pressed key enter
You pressed key home
You pressed key pageup
You pressed key home
You pressed key pageup
You pressed key pagedown
You pressed key end
You pressed key pagedown
You pressed key end
You pressed key /
You pressed key *
You pressed key -
You pressed key up
You pressed key down
You pressed key left
You pressed key right

