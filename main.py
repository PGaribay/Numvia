from tkinter import *
import tkinter as tk
import requests


app = tk.Tk()
app.title('Numvia')
app.resizable(False, False)

ht = 400  # app native height
wd = 500  # app native width


def get_numtrivia(numsearch):
    # function that will initialize the request from API after clicking search button
    # this line makes the tk.Label to show output with every click of the search button
    category = display_selected(drop)
    url = "https://numbersapi.p.rapidapi.com/%s/%s" % (numsearch, category)
    # i.e https://numbersapi.p.rapidapi.com/100/math
    print(url)  # to check for the url with the variables
    querystring = {"fragment": "true", "json": "true"}  # RapidAPI snippet
    headers = {
        "X-RapidAPI-Key": "68b907eb71msh431ec6ff46df5cdp1170b9jsn5dc4a211d44a",
        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    number_json = response.json()
    print(number_json)
    if category == 'math' or 'trivia':
        results['text'] = format_response(response.json())
        if category == 'year':
            results['text'] = format_response_year(response.json())


def format_response(number_json):
    # formats the values from json to Tk.Label output for math and trivia categories
    num = number_json['number']
    conditions = number_json['text']
    final_str = f'\nNumber: {num} \n\nTrivia:   {conditions}'
    return final_str


def format_response_year(number_json):
    # formats the values from json to Tk.Label output for year category
    num = number_json['number']
    conditions = number_json['text']
    final_str = f'\nYear: {num} \n\nTrivia:   {conditions}'
    return final_str


def display_selected(category):
    # gets input from the dropdown list and returns a variable for get_numtrivia function use
    category = numtype.get()
    return category


Canvas = tk.Canvas(app, height=ht, width=wd)  # 2nd layer after the app(root)
background_image = tk.PhotoImage(
    file='./images/backG.png')  # unable to read jpg images
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Canvas.pack()

# layer"master" for the textbox, dropdown list and search button
frame = tk.Frame(app,  bg='#638686', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

textbox = tk.Entry(frame, font=('Malgun Gothic', 15),
                   justify='center', borderwidth=10, relief=tk.FLAT)
textbox.place(rely=0, relwidth=0.67, relheight=.53)

menu = ["math", "trivia", "year"]
numtype = tk.StringVar()
numtype.set(menu[0])
drop = OptionMenu(frame, numtype, *menu, command=display_selected)
drop.place(rely=.5, relwidth=0.67, relheight=.47)

search = tk.Button(frame, text='Search', font=('Stencil', 18),
                   command=lambda: get_numtrivia(textbox.get()))
search.place(relx=0.68, relheight=1, relwidth=0.32)

# layer for the label or output panel
lower_frame = tk.Frame(app, bg='#638686', bd=5)
lower_frame.place(relx=0.5, rely=0.29, relwidth=0.75,
                  relheight=0.6, anchor='n')

results = tk.Label(lower_frame, anchor='nw', justify='left',
                   bd=4, wraplength=330, padx=20)
results.config(font=('Elephant', 13), bg='white')
results.place(relwidth=1, relheight=1)


app.mainloop()
