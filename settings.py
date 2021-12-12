# -*- coding: utf-8 -*-
#
# gdb-frontend is a easy, flexible and extensionable gui debugger
#
# https://github.com/rohanrhu/gdb-frontend
# https://oguzhaneroglu.com/projects/gdb-frontend/
#
# Licensed under GNU/GPLv3
# Copyright (C) 2019, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

"""
If enabled, it sets your CWD to executable's directory when you load an executable.
"""
SET_CWD_TO_EXECUTABLE: bool

"""
Most of GDBFrontend functions are thread-safe and work on GDB's main-thread.
So, if you run something that is blocking on the GDB shell, GDBFrontend functions have to wait it until finish.
This setting is seconds to wait for print warning.
"""
GDB_MT_WARNING_TIME: int

"""
Maximum recursion number of recursive functions that are used in somewhere like backtracing.
"""
MAX_RECURSIONS: int

"""
Height and width synchronizing tresholds in enhanced collabration mode. (In pixels.)
"""
ENHANCED_COLLABRATION_RESOLUTION_TRESHOLD: int

"""
If enabled, interrupts the process and call the function that is given to @threadSafe(no_interrupt=True)
@threadSafe(no_interrupt=True) skips this setting if no_interrupt is True.
"""
INTERRUPT_FOR_THREAD_SAFETY: bool

def init():
    global SET_CWD_TO_EXECUTABLE
    SET_CWD_TO_EXECUTABLE = True

    global GDB_MT_WARNING_TIME
    GDB_MT_WARNING_TIME = 3

    global MAX_RECURSIONS
    MAX_RECURSIONS = 100
    
    global ENHANCED_COLLABRATION_RESOLUTION_TRESHOLD
    ENHANCED_COLLABRATION_RESOLUTION_TRESHOLD = 10
    
    global INTERRUPT_FOR_THREAD_SAFETY
    INTERRUPT_FOR_THREAD_SAFETY = True