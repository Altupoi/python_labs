import student_utils as stu
import tkinter as tk
#Students = input("Учні: ").strip().split(",")
Students = ["Anna","Ivan","Olha"]
def generate():
    count = E.get()
    if count.isdecimal():
        count = int(count)
        if count >= 1 or count <= 20:
            report = ""
            for i in range(len(Students)):
                Students[i] = Students[i].strip()
                grades = stu.generate_grades(count)
                avg = stu.average_grade(grades)
                level = stu.get_level(avg)
                report += f'{Students[i]}: {grades} → {avg} → {level} \n'
            print(report)
            T.delete("1.0", tk.END)
            T.insert(tk.END, report)
        else:
            T.delete("1.0", tk.END)
            T.insert(tk.END, "Error")
    else:
        T.delete("1.0", tk.END)
        T.insert(tk.END, "Error")

W = tk.Tk()
W.title("Статистика учнів")
L = tk.Label(W, text = 'Впишіть кількість 1-20 та натисність "Сформувати звіт"')
L.pack(pady = 10)
E = tk.Entry(W,width = 30)
E.pack(pady = 10)
B = tk.Button(W, text = "Згенерувати звіт", command = generate)
B.pack(pady = 10)
T = tk.Text(W, width = 30)
T.pack(pady = 10)
W.mainloop()