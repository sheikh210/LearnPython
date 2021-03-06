try:
    import tkinter
except ImportError:
    import tkinter as tkinter


def parabola(num: int) -> int:
    product = num*num
    return product


def draw_axis(canv: tkinter.Tk):
    canv.update()
    x_origin = canv.winfo_width()/2
    y_origin = canv.winfo_height()/2
    canv.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canv.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canv.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canv, x, y):
    canv.create_line(x, y, x+1, y+1, fill="black")


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

main_window.mainloop()

