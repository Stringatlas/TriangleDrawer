try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk
	from Tkinter import ttk
import turtle 
import triangle

# creating window
window = tk.Tk()

# configuring window
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 650
window.geometry("+{}+{}".format(int((window.winfo_screenwidth() - WINDOW_WIDTH) / 2), 
                                int((window.winfo_screenheight() - WINDOW_HEIGHT) / 2)))

window.title("Triangle Drawer")
window.configure(background="black")
window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
window.resizable(0, 0)

# adding icon
icon = tk.PhotoImage(file=r"Images\triangle.png")
window.iconphoto(False, icon)

window.overrideredirect(0)  # OVERRIDE

DEGREES = "°" 
# style of tabs
tab_selected_color = "#FA991C"
tab_background = "#1C7690"


tab_theme = ttk.Style()
tab_theme.theme_create("tab_theme", parent="classic", settings={
						"TNotebook": {"configure": {"tabmargins": [] } },

						"TNotebook.Tab": {
						"configure": {"padding": [20, 5], "font": ("Roboto", "18", "bold"),
						"background": tab_background},

						"map": {"background": [("selected", tab_selected_color)],
                        	"expand": [("selected", [1, 1, 1, 0])] } }
                        })


tab_theme.theme_use("tab_theme")


# app (Notebook)
app_bg = "#032539"
app_fg = "#38D5E6"
app_font = "verdana"

application = ttk.Notebook()
application.pack()

# elements in each tab
class App():
	def __init__(self, master, input1, input2, input3, type):
		self.input1 = input1
		self.inpu2 = input2
		self.input3 = input3
		self.type = type

		# master frame
		frame = tk.Frame(master, bg=app_bg)
		frame.grid(row=0, column=0)

		# canvas
		self.canvas = tk.Canvas(frame, width=600, height=400)
		self.canvas.grid(row=0, column=0) 

		# all input frames
		input_frames = tk.Frame(frame, bg=tab_background)
		input_frames.grid(row=0, column=1, sticky="s")

		# first input var
		input1_frame = tk.Frame(input_frames, bg=tab_background)
		input1_frame.grid(row=0, column=0)

		input1_label = tk.Label(input1_frame, text=input1, bg=app_bg, font="roboto 18 bold", fg=app_fg)
		input1_label.grid(row=0, column=0)

		self.input1_entry = tk.Entry(input1_frame, bg=tab_background, fg=app_fg, font="roboto 18", width=10, insertbackground=app_fg)
		self.input1_entry.grid(row=0, column=1)

		# second input var
		input2_frame = tk.Frame(input_frames, bg=tab_background)
		input2_frame.grid(row=2, column=0)

		input2_label = tk.Label(input2_frame, text=input2, bg=app_bg, font="roboto 18 bold", fg=app_fg)
		input2_label.grid(row=0, column=0, sticky="w")

		self.input2_entry = tk.Entry(input2_frame, bg=tab_background, fg=app_fg, font="roboto 18", width=10, insertbackground=app_fg)
		self.input2_entry.grid(row=0, column=1)

		# third input var
		input3_frame = tk.Frame(input_frames, bg=tab_background)
		input3_frame.grid(row=4, column=0)

		input3_label = tk.Label(input3_frame, text=input3, bg=app_bg, font="roboto 18 bold", fg=app_fg)
		input3_label.grid(row=0, column=0, sticky="w")

		self.input3_entry = tk.Entry(input3_frame, bg=tab_background, fg=app_fg, font="roboto 18", width=10, insertbackground=app_fg)
		self.input3_entry.grid(row=0, column=1)

		# reference image
		panel = tk.Label(frame, compound="top", bg=app_bg, fg=app_fg, font="roboto 18")
		panel.reference = tk.PhotoImage(file="Images/reference_tri.gif")
		panel["text"] = "Parameters"
		panel["image"] = panel.reference

		panel.grid(row=0, column=1, sticky="n")

		# spaces
		tk.Label(frame, text='\n' * 2, bg=app_bg).grid(row=1, column=0)
		tk.Label(input_frames, text='', bg=tab_background).grid(row=1, column=0)
		tk.Label(input_frames, text='', bg=tab_background).grid(row=3, column=0)
		tk.Label(frame, text="", bg=app_bg).grid(row=4, column=0)
		tk.Label(frame, text="       " * 5, bg=app_bg).grid(row=0, column=5)
		tk.Label(frame, text="       " * 11, bg=app_bg).grid(row=5, column=5)
		# button
		draw_button = tk.Button(frame, text="Draw", font="arial 26 bold", width=20, command=self.draw)
		draw_button.grid(row=2, column=0)

		# results
		results_frame = tk.Frame(frame, bg=tab_background, borderwidth=5)
		results_frame.place(x=650, y=425)

		results_text = tk.Label(results_frame, text=" Results: ", font="roboto 18 underline", fg=app_fg, bg=tab_background)
		results_text.grid(row=0, column=0, sticky="w")

		# angle A
		result_AngleA_frame = tk.Frame(results_frame, bg=tab_background)
		result_AngleA_frame.grid(row=1, column=0)

		result_AngleA_text = tk.Label(result_AngleA_frame, text="Angle A: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_AngleA_text.grid(row=0, column=0)

		self.angleA = tk.Text(result_AngleA_frame, width=10, height=1)
		self.angleA.grid(row=0, column=1)

		# Angle B
		result_AngleB_frame = tk.Frame(results_frame, bg=tab_background)
		result_AngleB_frame.grid(row=2, column=0)

		result_AngleB_text = tk.Label(result_AngleB_frame, text="Angle B: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_AngleB_text.grid(row=0, column=0)

		self.angleB = tk.Text(result_AngleB_frame, width=10, height=1)
		self.angleB.grid(row=0, column=1)

		# Angle C
		result_AngleC_frame = tk.Frame(results_frame, bg=tab_background)
		result_AngleC_frame.grid(row=3, column=0)

		result_AngleC_text = tk.Label(result_AngleC_frame, text="Angle C: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_AngleC_text.grid(row=0, column=0)

		self.angleC = tk.Text(result_AngleC_frame, width=10, height=1)
		self.angleC.grid(row=0, column=1)

		# Side A
		result_SideA_frame = tk.Frame(results_frame, bg=tab_background)
		result_SideA_frame.grid(row=1, column=1)

		result_SideA_text = tk.Label(result_SideA_frame, text="  Side A: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_SideA_text.grid(row=0, column=0)

		self.sideA = tk.Text(result_SideA_frame, width=10, height=1)
		self.sideA.grid(row=0, column=1)

		# Side B
		result_SideB_frame = tk.Frame(results_frame, bg=tab_background)
		result_SideB_frame.grid(row=2, column=1)

		result_SideB_text = tk.Label(result_SideB_frame, text="  Side B: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_SideB_text.grid(row=0, column=0)

		self.sideB = tk.Text(result_SideB_frame, width=10, height=1)
		self.sideB.grid(row=0, column=1)

		# Side A
		result_SideC_frame = tk.Frame(results_frame, bg=tab_background)
		result_SideC_frame.grid(row=3, column=1)

		result_SideC_text = tk.Label(result_SideC_frame, text="  Side A: ", bg=tab_background, fg=app_fg, font="roboto 12")
		result_SideC_text.grid(row=0, column=0)

		self.sideC = tk.Text(result_SideC_frame, width=10, height=1)
		self.sideC.grid(row=0, column=1)

		# drawing variable (to prevent clicking button while turtle is drawing)
		self.drawing = False

	def draw(self):
		if not self.drawing:
			self.canvas.delete("all")
	
			# pen attributes
			self.pen = turtle.RawTurtle(self.canvas)
			self.pen.pensize(5)
			self.pen.speed("fastest")
	
			try:
				self.drawing = True
				# gets attributes of the triangle
				param = "{}, {}, {}".format(self.input1_entry.get(), self.input2_entry.get(), self.input3_entry.get())
		
				triangle1 = (f"self.tri = triangle.{self.type}({param})")
				exec(triangle1)
				attributes = self.tri.all()
				print(attributes)
				# calculates relative size of triangle
				relative = 350 / max(attributes[0], attributes[1], attributes[2])
				print([(attributes[0] + attributes[1] > attributes[2]), (attributes[1] + attributes[2] > attributes[0]), (attributes[0] + attributes[2] > attributes[1])])
	
				if not ((attributes[0] + attributes[1] > attributes[2]) and (attributes[1] + attributes[2] > attributes[0]) and (attributes[0] + attributes[2] > attributes[1])):
					print(1 + "1")		
		
				# moves pen in position
				self.pen.penup()
				self.pen.setheading(180)
				self.pen.forward(0.5 * attributes[2] * relative)
				self.pen.setheading(270)
				self.pen.forward((attributes[6] / attributes[2]) * relative * 0.75)
		
				# draws triangle
				self.pen.pendown()
				self.pen.setheading(0)
		
				self.pen.left(attributes[3])
				self.pen.forward((attributes[0]) * relative * 0.5)
				self.pen.write("b ", move=False, align="right", font=("Roboto", 20, "bold"))
				self.pen.forward((attributes[0]) * relative * 0.5)
				
				self.pen.right(180 - attributes[4])
				self.pen.forward(attributes[1] * relative * 0.5)
				self.pen.write(" a", move=False, align="left", font=("Roboto", 20, "bold"))
				self.pen.forward(attributes[1] * relative * 0.5)
				
				self.pen.right(180 - attributes[5])
				self.pen.forward(attributes[2] * relative * 0.5)
				self.pen.write("c", move=False, align="center", font=("Roboto", 20, "bold"))
				self.pen.forward(attributes[2] * relative * 0.5)

				self.pen.hideturtle()

				self.drawing = False

				# insert Angle A
				self.angleA.delete(1.0, tk.END)
				self.angleA.insert(tk.INSERT, round(attributes[4], 13))

				# insert Angle A
				self.angleB.delete(1.0, tk.END)
				self.angleB.insert(tk.INSERT, round(attributes[5], 13))

				# insert Angle C
				self.angleC.delete(1.0, tk.END)
				self.angleC.insert(tk.INSERT, round(attributes[3], 13))

				# insert Side A
				self.sideA.delete(1.0, tk.END)
				self.sideA.insert(tk.INSERT, round(attributes[1], 13))

				# insert Side B
				self.sideB.delete(1.0, tk.END)
				self.sideB.insert(tk.INSERT, round(attributes[0], 13))

				# insert Side C
				self.sideC.delete(1.0, tk.END)
				self.sideC.insert(tk.INSERT, round(attributes[2], 13))


				del triangle1
				del attributes
				del self.tri
			except:
				# insert Angle A
				self.angleA.delete(1.0, tk.END)
				self.angleA.insert(tk.INSERT, "NaN")

				# insert Angle A
				self.angleB.delete(1.0, tk.END)
				self.angleB.insert(tk.INSERT, "NaN")

				# insert Angle C
				self.angleC.delete(1.0, tk.END)
				self.angleC.insert(tk.INSERT, "NaN")

				# insert Side A
				self.sideA.delete(1.0, tk.END)
				self.sideA.insert(tk.INSERT, "NaN")

				# insert Side B
				self.sideB.delete(1.0, tk.END)
				self.sideB.insert(tk.INSERT, "NaN")

				# insert Side C
				self.sideC.delete(1.0, tk.END)
				self.sideC.insert(tk.INSERT, "NaN")

				self.pen.write("Invalid parameters", move=False, align="left", font=("Arial", 18, "normal"))
				self.drawing = False


# adding tabs
Sss_frame = tk.Frame(application, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=app_bg)
Asa_frame = tk.Frame(application, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=app_bg)
Sas_frame = tk.Frame(application, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=app_bg)
Aas_frame = tk.Frame(application, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=app_bg)
Hl_frame = tk.Frame(application, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=app_bg)

application.add(Sss_frame, text="SSS")
application.add(Asa_frame, text="ASA")
application.add(Sas_frame, text="SAS")
application.add(Aas_frame, text="AAS")
application.add(Hl_frame, text=" HL ")


App(Sss_frame, "Side b: ", "Side a: ", "Side c: ", "Sss")
App(Asa_frame, "Angle A: ", "  Side c:  ", "Angle B: ", "Asa")
App(Sas_frame, "  Side b:  ", "Angle A: ", "  Side c:  ", "Sas")
App(Aas_frame, "Angle A: ", "Angle C: ", "  Side c:  ", "Aas")


window.mainloop()