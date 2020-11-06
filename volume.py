

import tkinter as tk

root = tk.Tk()

switch_frame = tk.Frame(root)
switch_frame.pack()

switch_variable = tk.StringVar(value="dec")

rad_button = tk.Radiobutton(switch_frame, text="Radical", variable=switch_variable,
                            indicatoron=False, value="rad", width=8)
dec_button = tk.Radiobutton(switch_frame, text="Decimal", variable=switch_variable,
                            indicatoron=False, value="dec", width=8)
rad_button.pack(side="right")
dec_button.pack(side="left")


root.mainloop()
# rad1 = 120
# workrad1 = rad1
# sqrnum = 1

# for i in range(2,rad1):
#   mexp = 1
#   while i**mexp<=workrad1:
#     if workrad1 % i**mexp == 0:
#       mexp = mexp+1
#     else:
#       break
#   if mexp > 2:
#     sqrfac = i**(int((mexp-1)/2))
#     sqrnum = sqrnum * sqrfac
#     workrad1 = workrad1/(sqrfac**2)
    
# outsidenum = int(sqrnum)
# insidenum = int(rad1/(sqrnum**2))
# print(" ")
# print("The square root of "+str(rad1)+" is"),
# if insidenum == 1:
#   print(outsidenum)
# else:
#   if outsidenum == 1:
#     print("√"+str(insidenum))
#   else:
#     print(str(outsidenum)+"√"+str(insidenum))

