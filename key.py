#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
import pyatspi
import sys

KEY_CODE = {
    '1': 10, '2': 11, '3': 12, '4': 13, '5': 14, '6': 15,
    '7': 16, '8': 17, '9': 18, '0': 19, 'dash': 20, '=': 21,
    'q': 24, 'w': 25, 'e': 26, 'r': 27, 't': 28, 'y': 29,
    'u': 30, 'i': 31, 'o': 32, 'p': 33, '[': 34, ']': 35,
    'a': 38, 's': 39, 'd': 40, 'f': 41, 'g': 42, 'h': 43,
    'j': 44, 'k': 45, 'l': 46, ';': 47, 'z': 52, 'x': 53,
    'c': 54, 'v': 55, 'b': 56, 'n': 57, 'm': 58, ',': 59,
    '.': 60, '/': 61, '\'': 48, '\\': 51, '`': 49, '|': 52,
    'esc': 9, 'back': 22, 'enter': 36, 'space': 65, 'tab': 23,
    'ins': 118, 'del': 119, 'home': 110, 'end': 115, 'pgup': 112,
    'pgdown': 117, 'up': 111, 'left': 113, 'right': 114, 'down': 116,
    'f1': 67, 'f2': 68, 'f3': 69, 'f4': 70,
    'f5': 71, 'f6': 72, 'f7': 73, 'f8': 74,
    'f9': 75, 'f10': 76, 'f11': 95, 'f12': 96,
    'alt': 64,
    'alt_r': 105,
    'ctrl': 37,
    'ctrl_r': 108,
    'shift': 50,
    'shift_r': 62,
    'super': 133,
    'caps': 66,
    'menu': 135,
    'pause': 127,
    'num_lock': 77,
    'scroll_lock': 78,
    }


def key_events(argv):
    reg = pyatspi.Registry.generateKeyboardEvent
    if not isinstance(argv, (list, tuple)):
        argv = [argv]
    for key_set in argv:
        keys = key_set.split('-')
        print(keys)
        if keys[0] == '00':
            keys.pop(0)
            for index, key_name in enumerate(keys):
                if key_name not in KEY_CODE:
                    print(key_name, "not found")
                    continue
                key = KEY_CODE[key_name]
                event = pyatspi.KEY_PRESS
                print(key_name, ':', key, event)
                reg(key, None, event)
        elif keys[0] == '99':
            keys.pop(0)
            for index, key_name in enumerate(keys):
                if key_name not in KEY_CODE:
                    print(key_name, "not found")
                    continue
                key = KEY_CODE[key_name]
                event = pyatspi.KEY_RELEASE
                print(key_name, ':', key, event)
                reg(key, None, event)
        else:
            count = len(keys) - 1
            reverse_keys = keys[:]
            reverse_keys.reverse()
            keys.extend(reverse_keys)
            keys.pop(count)
            for index, key_name in enumerate(keys):
                if key_name not in KEY_CODE:
                    print(key_name, "not found")
                    continue
                key = KEY_CODE[key_name]
                if index < count:
                    event = pyatspi.KEY_PRESS
                elif index > count:
                    event = pyatspi.KEY_RELEASE
                else:
                    event = pyatspi.KEY_PRESSRELEASE
                print(key_name, ':', key, event)
                reg(key, None, event)


def mouse_event(x, y, event):
    reg = pyatspi.Registry.generateMouseEvent
    reg(x, y, event)

if sys.argv[0] == __file__ and len(sys.argv) > 1:
    argv = sys.argv[:]
    argv.pop(0)
    key_events(argv)
