#!/usr/bin/env python3

import PySimpleGUI as sg
from collections.abc import Iterable
from typing import Tuple

DEFAULT_THEME:str = "DarkGreen"

def set_theme(theme_name:str=DEFAULT_THEME) -> None:
    sg.theme(theme_name)

def set_font(font_descr:Tuple[str, int]=("Arial", 14)) -> None:
    sg.set_options(font=font_descr)
    
def make_layout() -> Iterable[Iterable[sg.Element]]:
    return [ [ sg.Text("Name"),
               sg.Input(key="-NAME-")] ]

def make_window(title: str, layout: Iterable[Iterable[sg.Element]]) \
        -> sg.Window:
    return sg.Window(title, layout, finalize=True)

def main() -> None:
    set_theme()
    set_font()
    layout: Iterable[Iterable[sg.Element]]= make_layout()
    window: sg.Window = make_window("Window Title", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            print(f"Event:  {event}")
            print(f"Values: {values}")

    window.close()

if __name__ == "__main__":
    main()
