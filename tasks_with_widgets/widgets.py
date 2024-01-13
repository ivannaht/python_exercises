from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from  IPython.display import display


def func(x):
    return x


interact(func, x=10)
interact(func, x=True)
interact(func, x="Text")
interact(func, x=["Option1", "Option2"])
interact(func, x={"Option1":10, "Option2":20})
interact(func, x=fixed("Text"))
interact(func, x=widgets.IntSlider(min=-100,max=100,step=1,value=0))
interact(func, x=(-100,100,1))


def func_2(a, b):
    display(a + b)
    return a + b


w = interactive(func_2, a=10, b=20)
display(w)
w.children
