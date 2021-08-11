#!/usr/bin/env python3

import PySimpleGUI as sg

DEFAULT_THEME = "SystemDefault"

def set_theme(theme_name=DEFAULT_THEME):
    sg.theme(theme_name)

def set_font(font_descr=("Arial", 14)):
    sg.set_options(font=font_descr)
    
def make_layout():
    return [ [ sg.Text("Name"),
               sg.Input(key="-NAME-")] ]

def make_window(title, layout):
    return sg.Window(title, layout)

def main():
    set_theme()
    set_font()
    layout = make_layout()
    window = make_window("Window Title", layout)

    while True:
        event, values = window.read()
        if event == WIN_CLOSED:
            break
        else:
            print(f"Event:  {event}")
            print(f"Values: {values}")

    window.close()

if __name__ == "__main__":
    main()
