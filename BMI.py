import tkinter as tk
from tkinter import messagebox

def find_body_mass_index():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get())

        body_mass_index = weight / ((height/100)**2)
        output.configure(text='ค่าดัชนีมวลกาย(BMI)มีค่าเท่ากับ' + str("%.2f" %body_mass_index))
    except:
        messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง")

def reset():
    output.configure(text='')
    height_input.delete(0,'end')
    weight_input.delete(0,'end')


window = tk.Tk()
window.title('Body mass index(BMI)')
window.minsize(width=500, height=500)
window.maxsize(width=1920, height=1080)
window.config(bg='#fdebd0')
window.option_add('*Label.background', "#fdebd0")

welcome_to_program = tk.Label(master=window, text='โปรเเกรมคำนวณหาค่าดัชนีมวลกาย', font='prompt 16 bold')
welcome_to_program.pack()

weight_explain = tk.Label(master=window, text='กรอกน้ำหนัก(กิโลกรัม)', font='prompt 12')
weight_explain.pack(pady=30)

weight_input = tk.Entry(master=window)
weight_input.pack(pady=20)

height_explain = tk.Label(master=window, text='กรอกส่วนสูง(เซนติเมตร)', font='prompt 12')
height_explain.pack(pady=30)

height_input = tk.Entry(master=window)
height_input.pack(pady=20)

BMI_button = tk.Button(master=window, command=find_body_mass_index, text='คำนวณ')
BMI_button.pack(pady=30)

output = tk.Label(master=window, font='prompt 14')
output.pack(pady=30)

reset_button = tk.Button(master=window, command=reset, text='reset')
reset_button.pack(pady=20)

window.mainloop()


