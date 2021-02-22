# importing a method from a module allows us to call the method without referencing the module name
from turtle import forward, right, circle, done

# If we just imported turtle (import turtle), we would call this as "turtle.forward(150)"
forward(150)
right(250)
forward(150)
circle(285)

done()
