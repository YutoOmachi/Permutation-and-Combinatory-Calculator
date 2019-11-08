import tkinter as tk

# INITIATING GUI
root = tk.Tk()
root.title("Permutation and Combinetorics Calculator")
root.geometry("370x400")

# INSTANCES
text = tk.StringVar()
display = ""  # variable holding displayed numbers and signs
calc_num = ""  # variable holding calculation values


# FUNCTIONS
def factorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def permutation(n: int, r: int):
    """
    Precondition: n >= r
    """
    return factorial(n) // factorial(n - r)


def combination(n: int, r: int):
    """
    Precondition: n >= r
    """
    return int(factorial(n) // factorial(r) // factorial(n - r))


def btn_click(x):
    global calc_num
    calc_num = calc_num + str(x)
    global display
    display = display + str(x)
    text.set(display)


def btn_factorial():
    global calc_num
    global display
    display = display + "!"
    text.set(display)
    i = 0
    index = 0
    while i < len(calc_num):
        if not (calc_num[len(calc_num) - i - 1].isnumeric or calc_num[len(calc_num) - i - 1] == "."):
            index = len(calc_num) - i - 1
            break
        i += 1
    try:
        calc_num = calc_num[:index] + str(factorial(int(calc_num[index:len(calc_num)])))
    except:
        text.set("Error... Invalid use of '!'")
        display = ""
        calc_num = ""


def process_permutation_combination():
    global calc_num
    global display
    errorP = "Invalid use of 'P'... Please try again"
    errorC = "Invalid use of 'C'... Please try again"
    calc_sign = ["+", "-", "÷", "×"]
    i = 0
    while i < len(calc_num):
        index_before = i
        index_after = i
        if calc_num[i] == "P":
            if i == 0 or i == len(calc_num)-1:
                display = errorP
                text.set(display)
                return False
            for j in range(1, i + 1):
                if calc_num[i - j].isnumeric():
                    index_before -= 1
                elif calc_num[i - j] in calc_sign and i != index_before:
                    break
                else:
                    display = errorP
                    text.set(display)
                    return False

            for j in range(1, len(calc_num) - i):
                if calc_num[i + j].isnumeric():
                    index_after += 1
                elif calc_num[i+j] in calc_sign and i != index_after:
                    break
                else:
                    display = errorP
                    text.set(display)
                    return False

            if int(calc_num[index_before:i]) < int(calc_num[i + 1:index_after + 1]):
                display = errorP
                text.set(display)
                return False
            calc_num = calc_num[:index_before] + str(
                permutation(int(calc_num[index_before:i]), int(calc_num[i + 1: index_after + 1]))) \
                       + calc_num[index_after + 1:]

        elif calc_num[i] == "C":
            if i == 0 or i == len(calc_num)-1:
                display = errorC
                text.set(display)
                return False
            for j in range(1, i + 1):
                if calc_num[i - j].isnumeric():
                    index_before -= 1
                elif calc_num[i - j] in calc_sign and i != index_before:
                    break
                else:
                    display = errorC
                    text.set(display)
                    return False

            for j in range(1, len(calc_num) - i):
                if calc_num[i + j].isnumeric():
                    index_after += 1
                elif calc_num[i + j] in calc_sign and i != index_after:
                    break
                else:
                    display = errorC
                    text.set(display)
                    return False
            if int(calc_num[index_before:i]) < int(calc_num[i + 1:index_after + 1]):
                display = errorC
                text.set(display)
                return False

            calc_num = calc_num[:index_before] + str(
                combination(int(calc_num[index_before:i]), int(calc_num[i + 1:index_after + 1]))) \
                       + calc_num[index_after + 1:]
        i = index_before + 1
    return True


def valid_calc(statement: str):
    global display
    calc_sign = ["+", "-", "/", "*"]
    for i in range(len(statement)-1):
        if statement[i] in calc_sign and statement[i+1] in calc_sign:
            display = "Invalid Syntax... Please Try Again"
            text.set(display)
            return False
    return True


def btn_clear():
    global calc_num
    global display
    calc_num = ""
    display = ""
    text.set(display)


def btn_calc():
    global calc_num
    global display
    calc_num = calc_num.replace("×", "*")
    calc_num = calc_num.replace("÷", "/")
    if process_permutation_combination() and calc_num != "" and valid_calc(calc_num):
        try:
            display = str(round(eval(calc_num), 6))
        except:
            display = "Invalid Syntax... Please Try Again"
    text.set(display)
    display = ""
    calc_num = ""


# CREATE FRAMES
background_image = tk.PhotoImage(file="blue_background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

high_frame = tk.Frame(root, bg="red", bd=3)
high_frame.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.15, anchor="n")
low_frame = tk.Frame(root, bg="green", bd=5)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.7, anchor="n")

# CREATE HIGH_FRAME
text_box = tk.Label(high_frame, textvariable=text, font=("arial", 20, "bold"))
text_box.place(relwidth=1, relheight=1)

# CREATE LOW_FRAME BUTTONS
button_fact = tk.Button(low_frame, text="!", command=lambda: btn_factorial())
button_fact.place(relx=0, rely=0, relwidth=0.25, relheight=0.2)
button_perm = tk.Button(low_frame, text="nPr", command=lambda: btn_click("P"))
button_perm.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.2)
button_comb = tk.Button(low_frame, text="nCr", command=lambda: btn_click("C"))
button_comb.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.2)
button_clear = tk.Button(low_frame, text="AC", fg="#B52E31", command=lambda: btn_clear())
button_clear.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.2)

button1 = tk.Button(low_frame, text="1", command=lambda: btn_click(1))
button1.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)
button2 = tk.Button(low_frame, text="2", command=lambda: btn_click(2))
button2.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)
button3 = tk.Button(low_frame, text="3", command=lambda: btn_click(3))
button3.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)
button_mul = tk.Button(low_frame, text="×", command=lambda: btn_click("×"))
button_mul.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)

button4 = tk.Button(low_frame, text="4", command=lambda: btn_click(4))
button4.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)
button5 = tk.Button(low_frame, text="5", command=lambda: btn_click(5))
button5.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)
button6 = tk.Button(low_frame, text="6", command=lambda: btn_click(6))
button6.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)
button_div = tk.Button(low_frame, text="÷", command=lambda: btn_click("÷"))
button_div.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)

button7 = tk.Button(low_frame, text="7", command=lambda: btn_click(7))
button7.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)
button8 = tk.Button(low_frame, text="8", command=lambda: btn_click(8))
button8.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)
button9 = tk.Button(low_frame, text="9", command=lambda: btn_click(9))
button9.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)
button_plus = tk.Button(low_frame, text="+", command=lambda: btn_click("+"))
button_plus.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)

button_dig = tk.Button(low_frame, text=".", command=lambda: btn_click("."))
button_dig.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)
button0 = tk.Button(low_frame, text="0", command=lambda: btn_click(0))
button0.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.2)
button_equal = tk.Button(low_frame, text="=", command=lambda: btn_calc())
button_equal.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)
button_minus = tk.Button(low_frame, text="-", command=lambda: btn_click("-"))
button_minus.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

root.mainloop()
