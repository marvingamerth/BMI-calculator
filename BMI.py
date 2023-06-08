import tkinter as tk

def find_body_mass_index():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get())

        body_mass_index = weight / (height**2)
        output.configure(text='ค่าดัชนีมวลกาย(BMI)มีค่าเท่ากับ' + str("%.2f" %body_mass_index))
    except ValueError:
        output.configure(text='กรุณากรอกข้อมูลที่ถูกต้อง')


window = tk.Tk()
window.title('Body mass index(BMI)')
window.minsize(width=500, height=500)
window.maxsize(width=1920, height=1080)

welcome_to_program = tk.Label(master=window, text='โปรเเกรมคำนวณหาค่าดัชนีมวลกาย')
welcome_to_program.pack()

weight_explain = tk.Label(master=window, text='กรอกน้ำหนัก(ไม่ต้องใส่หน่วย กรอกข้อมูลที่มีหน่วยเป็นกิโลกรัม)')
weight_explain.pack(pady=30)

weight_input = tk.Entry(master=window)
weight_input.pack(pady=20)

height_explain = tk.Label(master=window, text='กรอกส่วนสูง(ไม่ต้องใส่หน่วย กรอกข้อมูลที่มีหน่วยเป็นเมตร)')
height_explain.pack(pady=30)

height_input = tk.Entry(master=window)
height_input.pack(pady=20)

BMI_button = tk.Button(master=window, command=find_body_mass_index, text='คำนวณ')
BMI_button.pack(pady=30)

output = tk.Label(master=window)
output.pack(pady=30)

notice = tk.Label(master=window)
notice.pack(pady=30)

window.mainloop()


