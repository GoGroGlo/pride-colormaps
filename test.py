### Glo's test file - see what I'm working on right now ###

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np





def plot_examples(colormaps):
    '''
    Helper function to plot data with associated colormap.
    '''
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()





'''
Process to define single-color sequential colormaps 
(see https://jiffyclub.github.io/palettable/mycarta/ for examples)
'''

# define how many colors the colorway should have
N = 3

# create an np array pre-filled with 1's
vals = np.ones((N, 4))

# edit the np array to show correct rgb values
vals[:, 0] = np.linspace(245/256, 1, N)
vals[:, 1] = np.linspace(171/256, 1, N)
vals[:, 2] = np.linspace(185/256, 1, N)
# vals[:, 3] is the alpha which is the same all throughout because transparency doesn't matter here

#make the colormap
trans_pink_3 = ListedColormap(vals)

# print the colormap array to see how it changed
print(vals)

# plot examples to see the colormap in action
plot_examples([trans_pink_3])





'''
Process to define two-color diverging colormaps 
(see https://jiffyclub.github.io/palettable/cartocolors/diverging/ for examples)
'''

# define how many colors the colorway should have
N = 2

# create an np array pre-filled with 1's
vals = np.ones((N, 4))

# edit the np array to show correct rgb values
vals[0, :] = np.array([91/256, 207/256, 250/256, 1]) # trans blue
vals[1, :] = np.array([245/256, 171/256, 185/256, 1]) # trans pink
# vals[:, 3] is the alpha which is the same all throughout because transparency doesn't matter here

#make the colormap
trans_2 = ListedColormap(vals)

# print the colormap array to see how it changed
print(vals)

# plot examples to see the colormap in action
plot_examples([trans_2])





'''
Process to define three-color diverging colormaps 
(see https://jiffyclub.github.io/palettable/cartocolors/diverging/ for examples)
'''

# define how many colors the colorway should have
N = 3

# create an np array pre-filled with 1's
vals = np.ones((N, 4))

# edit the np array to show correct rgb values
vals[0, :] = np.array([91/256, 207/256, 250/256, 1]) # trans blue
#vals[1, :] = np.array([248/256, 24/256, 148/256, 1]) # middle color is white and no need to reassign because 1 is already white
vals[2, :] = np.array([245/256, 171/256, 185/256, 1]) # trans pink
# vals[:, 3] is the alpha which is the same all throughout because transparency doesn't matter here

#make the colormap
trans_3 = ListedColormap(vals)

# print the colormap array to see how it changed
print(vals)

# plot examples to see the colormap in action
plot_examples([trans_3])





'''
Process to define linear segmented colormaps (more versatile)
'''

cdict = {'red':   [[0.0,  0.0, 0.0],
                   [0.5,  1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'green': [[0.0,  0.0, 0.0],
                   [0.25, 0.0, 0.0],
                   [0.75, 1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'blue':  [[0.0,  0.0, 0.0],
                   [0.5,  0.0, 0.0],
                   [1.0,  1.0, 1.0]]}


def plot_linearmap(cdict):
    newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    rgba = newcmp(np.linspace(0, 1, 256))
    fig, ax = plt.subplots(figsize=(4, 3), constrained_layout=True)
    col = ['r', 'g', 'b']
    for xx in [0.25, 0.5, 0.75]:
        ax.axvline(xx, color='0.7', linestyle='--')
    for i in range(3):
        ax.plot(np.arange(256)/256, rgba[:, i], color=col[i])
    ax.set_xlabel('index')
    ax.set_ylabel('RGB')
    plt.show()

plot_linearmap(cdict)





'''
Process to define linear segmented colormaps (simpler)
'''

colors = ["darkorange", "gold", "lawngreen", "lightseagreen"]
cmap1 = LinearSegmentedColormap.from_list("mycmap", colors)