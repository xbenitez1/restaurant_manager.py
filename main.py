from tkinter import *
import datetime
from tkinter import filedialog, messagebox

# Star Tkinter
restaurant = Tk()

food_price = [12.8, 34, 23, 21, 45, 32, 16.8, 28]
drink_price = [2, 1.5, 3, 2, 1.5, 3, 2, 3]
dessert_price = [5, 7, 8, 6.7, 5.8, 7.3, 8, 5.7]


# Result Display
def result_display(name, row_location, column_location, var_cost):
    cost_food = Label(result_panel,
                      text=name,
                      font=("arial", 12, "bold"),
                      fg="white",
                      bg="azure4")
    cost_food.grid(row=row_location,
                   column=column_location
                   )

    text_cost_food = Entry(result_panel,
                           font=("arial", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_cost,
                           bg="azure4")
    text_cost_food.grid(row=row_location,
                        column=column_location + 1,
                        padx=41)


# Check Function
def check_function():
    x = 0
    for item in box_food:
        if menu_variable_food[x].get() == 1:
            box_food[x].config(state=NORMAL)
            if box_food[x].get() == 0:
                box_food[x].delete(0, END)
            box_food[x].focus()
        else:
            box_food[x].config(state=DISABLED)
            text_food[x].set("0")
        x += 1

    x = 0
    for item in box_drink:
        if menu_variable_drink[x].get() == 1:
            box_drink[x].config(state=NORMAL)
            if box_drink[x].get() == 0:
                box_drink[x].delete(0, END)
            box_drink[x].focus()
        else:
            box_drink[x].config(state=DISABLED)
            text_drink[x].set("0")
        x += 1

    x = 0
    for item in box_dessert:
        if menu_variable_dessert[x].get() == 1:
            box_dessert[x].config(state=NORMAL)
            if box_dessert[x].get() == 0:
                box_dessert[x].delete(0, END)
            box_dessert[x].focus()
        else:
            box_dessert[x].config(state=DISABLED)
            text_dessert[x].set("0")
        x += 1


# Calculator function
def button_calculator_function(num):
    global calculator_string
    calculator_string = calculator_string + num
    visual_calculator.delete(0, END)
    visual_calculator.insert(END, calculator_string)


def clean_button():
    global calculator_string
    calculator_string = ""
    visual_calculator.delete(0, END)


def total_cal():
    global calculator_string
    result_cal = str(eval(calculator_string))
    visual_calculator.delete(0, END)
    visual_calculator.insert(0, result_cal)
    calculator_string = ""


# subtotals, tax and total calculation
def total_meel():
    sub_total_food = 0
    index_price = 0
    for price in text_food:
        sub_total_food = sub_total_food + (float(price.get()) * food_price[index_price])
        index_price += 1

    sub_total_dinks = 0
    index_price = 0
    for price in text_drink:
        sub_total_dinks = sub_total_dinks + (float(price.get()) * drink_price[index_price])
        index_price += 1

    sub_total_desserts = 0
    index_price = 0
    for price in text_dessert:
        sub_total_desserts = sub_total_desserts + (float(price.get()) * dessert_price[index_price])
        index_price += 1

    sub_total = sub_total_food + sub_total_dinks + sub_total_desserts
    tax = sub_total * 0.2
    total_dinner = sub_total_food + tax

    var_cost_food.set(f"$ {round(sub_total_food, 2)}")
    var_cost_drink.set(f"$ {round(sub_total_dinks, 2)}")
    var_cost_dessert.set(f"$ {round(sub_total_desserts, 2)}")
    var_cost_subtotal.set(f"$ {round(sub_total, 2)}")
    var_cost_tax.set(f"$ {round(tax, 2)}")
    var_cost_total.set(f"$ {round(total_dinner, 2)}")


# ticket text
def ticket_text():
    text_ticket.delete(1.0, END)
    number_ticket = 1
    date = datetime.datetime.now()
    date_ticket = f'\n{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    text_ticket.insert(END, F'Data:\t{number_ticket}\t\t{date_ticket}\n')
    text_ticket.insert(END, (f'*' * 63) + '\n')
    text_ticket.insert(END, f'Items\t\tCantidad\t\tPrice\n')
    text_ticket.insert(END, (f'-' * 75) + '\n')

    x_counter = 0
    for food in text_food:
        if food.get() != '0':
            text_ticket.insert(END, f'{food_list[x_counter]}\t\t{food.get()}\t\t'
                                    f'$ {float(food.get()) * food_price[x_counter]}\n')
        x_counter += 1

    x_counter = 0
    for drink in text_drink:
        if drink.get() != '0':
            text_ticket.insert(END, f'{drink_list[x_counter]}\t\t{drink.get()}\t\t'
                                    f'$ {float(drink.get()) * drink_price[x_counter]}\n')
        x_counter += 1

    x_counter = 0
    for dessert in text_dessert:
        if dessert.get() != '0':
            text_ticket.insert(END, f'{dessert_list[x_counter]}\t\t{dessert.get()}\t\t'
                                    f'$ {float(dessert.get()) * dessert_price[x_counter]}\n')
        x_counter += 1

    text_ticket.insert(END, (f'-' * 75) + '\n')
    text_ticket.insert(END, F' Subtotal\t\t\t\t$ {var_cost_subtotal.get()}\n')
    text_ticket.insert(END, F' Tax\t\t\t\t$ {var_cost_tax.get()}\n')
    text_ticket.insert(END, F' Total\t\t\t\t$ {var_cost_total.get()}\n')
    text_ticket.insert(END, (f'*' * 63) + '\n')
    text_ticket.insert(END, " \tHAVE A NICE DAY")

    number_ticket += 1


# Save ticket
def save():
    info_text = text_ticket.get(1.0, END)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(info_text)
    file.close()
    messagebox.showinfo("informacion", f"{info_text}\nYOR TICKET HAVE BENN SAVE")


# Reset program
def reset():
    text_ticket.delete(0.1, END)

    for text in text_food:
        text.set("0")
    for text in text_drink:
        text.set("0")
    for text in text_dessert:
        text.set("0")

    for box in box_food:
        box.config(state=DISABLED)
    for box in box_drink:
        box.config(state=DISABLED)
    for box in box_dessert:
        box.config(state=DISABLED)

    for var in menu_variable_food:
        var.set(0)
    for var in menu_variable_drink:
        var.set(0)
    for var in menu_variable_dessert:
        var.set(0)

    var_cost_food.set("")
    var_cost_drink.set("")
    var_cost_dessert.set("")
    var_cost_subtotal.set("")
    var_cost_tax.set("")
    var_cost_total.set("")


# Window parameters: location and size
restaurant.geometry('1280x630+30+50')

# Avoid maximize
restaurant.resizable(0, 0)

# Title program
restaurant.title("Restaurant management")

# Window Backround
restaurant.config(bg="blue")

# Top panel
top_panel = Frame(restaurant,
                  bd=1,
                  relief="flat")
top_panel.pack(side="top")
title_name = Label(top_panel,
                   text="Restaurant management",
                   fg="white smoke",
                   font=("arial", 58),
                   bg="blue",
                   width=20)
title_name.grid(row=0,
                column=0)

# Left panel (Menu)
left_panel = Frame(restaurant,
                   bd=1,
                   relief="flat")
left_panel.pack(side="left")

# result panel in left panel
result_panel = Frame(left_panel,
                     bd=1,
                     relief="flat",
                     bg="azure4",
                     padx=130)
result_panel.pack(side="bottom")

# Food panel in left panel
food_panel = LabelFrame(left_panel,
                        text="Food",
                        font=("arial", 20, "bold"),
                        bd=1,
                        relief="flat",
                        fg="white smoke")
food_panel.pack(side="left")

# Drink panel in left panel
drink_panel = LabelFrame(left_panel,
                         text="Drink",
                         font=("arial", 20, "bold"),
                         bd=1,
                         relief="flat",
                         fg="white smoke")
drink_panel.pack(side="left")

# Dessert in left panel
desserts_panel = LabelFrame(left_panel,
                            text="Desserts",
                            font=("arial", 20, "bold"),
                            bd=1,
                            relief="flat",
                            fg="white smoke")
desserts_panel.pack(side="left")

# Right Panel
right_panel = Frame(restaurant,
                    bd=1,
                    relief="flat")
right_panel.pack(side="right")

# Calculator in Right panel
calculator_panel = Frame(right_panel,
                         bd=1,
                         relief="flat",
                         bg="blue")
calculator_panel.pack(side="top")

# Ticket in Right panel
ticket_panel = Frame(right_panel,
                     bd=1,
                     relief="flat",
                     bg="blue")
ticket_panel.pack(side="top")

# Button in Right panel
button_panel = Frame(right_panel,
                     bd=1, relief="flat",
                     bg="blue")
button_panel.pack(side="top")

# Product list
food_list = ["Pasta", "Meet", "Salad", "Soup", "Appetizers", "Pizza", "Hamburger", "Salmon"]
drink_list = ["Orangina", "Coca-cola", "Water", "limonade", "Coctail", "Milk-shake", "Wine", "Beer"]
dessert_list = ["Tiramisu", "Icecream", "Cake", "Flan", "Fruit", "Brownies", "Mousse", "Crème brulée"]

# Variable result display
var_cost_food = StringVar()
var_cost_drink = StringVar()
var_cost_dessert = StringVar()
var_cost_subtotal = StringVar()
var_cost_tax = StringVar()
var_cost_total = StringVar()

# Call display food
# variables Food menu
menu_variable_food = []
box_food = []
text_food = []
count = 0
for item in food_list:
    # Check list Products
    menu_variable_food.append("")
    menu_variable_food[count] = IntVar()
    item = Checkbutton(food_panel,
                       text=item.title(),
                       font=("arial", 16, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=menu_variable_food[count],
                       command=check_function)

    item.grid(row=count,
              column=1,
              sticky=W,
              padx=15)

    # Box Data entry
    box_food.append("")
    text_food.append("")
    text_food[count] = StringVar()
    text_food[count].set("0")
    box_food[count] = Entry(food_panel,
                            font=("arial", 18, "bold"),
                            bd=1,
                            width=6,
                            state=DISABLED,
                            textvariable=text_food[count])
    box_food[count].grid(row=count,
                         column=2)

    count += 1

# Call display drinks
# variables Food menu
menu_variable_drink = []
box_drink = []
text_drink = []
count = 0
for item in drink_list:
    # Check list Products
    menu_variable_drink.append("")
    menu_variable_drink[count] = IntVar()
    item = Checkbutton(food_panel,
                       text=item.title(),
                       font=("arial", 16, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=menu_variable_drink[count],
                       command=check_function)

    item.grid(row=count,
              column=3,
              sticky=W,
              padx=15)

    # Box Data entry
    box_drink.append("")
    text_drink.append("")
    text_drink[count] = StringVar()
    text_drink[count].set("0")
    box_drink[count] = Entry(food_panel,
                             font=("arial", 18, "bold"),
                             bd=1,
                             width=6,
                             state=DISABLED,
                             textvariable=text_drink[count])
    box_drink[count].grid(row=count,
                          column=4)

    count += 1

# Call display dessert
# variables Food menu
menu_variable_dessert = []
box_dessert = []
text_dessert = []
count = 0
for item in dessert_list:
    # Check list Products
    menu_variable_dessert.append("")
    menu_variable_dessert[count] = IntVar()
    item = Checkbutton(food_panel,
                       text=item.title(),
                       font=("arial", 16, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=menu_variable_dessert[count],
                       command=check_function)

    item.grid(row=count,
              column=5,
              sticky=W,
              padx=15)

    # Box Data entry
    box_dessert.append("")
    text_dessert.append("")
    text_dessert[count] = StringVar()
    text_dessert[count].set("0")
    box_dessert[count] = Entry(food_panel,
                               font=("arial", 18, "bold"),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=text_dessert[count])
    box_dessert[count].grid(row=count,
                            column=6)

    count += 1

# Call result display
result_display("Food cost", 1, 0, var_cost_food)
result_display("Drink cost", 3, 0, var_cost_drink)
result_display("Dessert cost", 5, 0, var_cost_dessert)

result_display("Sub-Total", 1, 2, var_cost_subtotal)
result_display("Tax", 3, 2, var_cost_tax)
result_display("Total", 5, 2, var_cost_total)

# Button Variables
buttons = ["Total", "Ticket", "Save", "Reset"]
buttons_created = []
count_columns = 0

# Create button
for button in buttons:
    button = Button(button_panel,
                    text=button.title(),
                    font=("arial", 12, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)

    buttons_created.append(button)

    button.grid(row=0,
                column=count_columns)
    count_columns += 1

buttons_created[0].config(command=total_meel)
buttons_created[1].config(command=ticket_text)
buttons_created[2].config(command=save)
buttons_created[3].config(command=reset)

# Ticket
text_ticket = Text(ticket_panel,
                   font=("arial", 12, "bold"),
                   bd=1,
                   width=42,
                   height=10)
text_ticket.grid(row=0,
                 column=0)

# Calculator variable
calculator_string = ""

# Calculator Result
visual_calculator = Entry(calculator_panel,
                          font=("arial", 12, "bold"),
                          width=32,
                          bd=1)
visual_calculator.grid(row=0,
                       column=0,
                       columnspan=4)

# Calculator buttons
buttons_calculator = ["7", "8", "9", "+", "4", "5", "6", "-",
                      "1", "2", "3", "x", "=", "Clean", "0", "/"]
visual_operation = []

count_row_cal = 1
count_columns_cal = 0

# Create button calculator
for button in buttons_calculator:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=("arial", 16, "bold"),
                    fg="white",
                    bd=1,
                    bg="azure4",
                    width=8)

    visual_operation.append(button)

    button.grid(row=count_row_cal,
                column=count_columns_cal)

    if count_columns_cal == 3:
        count_row_cal += 1

    count_columns_cal += 1

    if count_columns_cal == 4:
        count_columns_cal = 0

visual_operation[0].config(command=lambda: button_calculator_function("7"))
visual_operation[1].config(command=lambda: button_calculator_function("8"))
visual_operation[2].config(command=lambda: button_calculator_function("9"))
visual_operation[3].config(command=lambda: button_calculator_function("+"))
visual_operation[4].config(command=lambda: button_calculator_function("4"))
visual_operation[5].config(command=lambda: button_calculator_function("5"))
visual_operation[6].config(command=lambda: button_calculator_function("6"))
visual_operation[7].config(command=lambda: button_calculator_function("-"))
visual_operation[8].config(command=lambda: button_calculator_function("1"))
visual_operation[9].config(command=lambda: button_calculator_function("2"))
visual_operation[10].config(command=lambda: button_calculator_function("3"))
visual_operation[11].config(command=lambda: button_calculator_function("*"))
visual_operation[12].config(command=total_cal)
visual_operation[13].config(command=clean_button)
visual_operation[14].config(command=lambda: button_calculator_function("0"))
visual_operation[15].config(command=lambda: button_calculator_function("/"))

# Window dont close
restaurant.mainloop()
