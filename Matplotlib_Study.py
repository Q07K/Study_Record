# Import to matplotlib
import matplotlib.pyplot as plt

# Draw bar plot
bar_x = [0, 1]
bar_y = [10, 0]

plt.figure(figsize=(6,6))

# bar setting 
bar_set = {
    'edgecolor' : 'skyblue',
    'fill' : False,
    'width' : 0.4,
}

# line stting
line_set = {
    'arrowstyle' : '-',
    'connectionstyle' : 'arc3, rad=0',
    'color' : 'skyblue',
}

# pointer_setting
pointer_set = {
    'arrowstyle' : '->',
    'connectionstyle' : 'arc3, rad=0',
    'color' : 'red',
}

# Draw bar, line, pointer
plt.bar(bar_x, bar_y, **bar_set)

for line_ in range(0, 8+1, 2):
    plt.annotate('', xy=(-0.2, line_), xytext=(0.21, line_),
                  arrowprops=line_set,
                  ) 

plt.annotate('point', xy=(0, 9), xytext=(0.5, 8),
              arrowprops=pointer_set,
              )
