# What Are Some Good Debugging Techniques in Python?

Debugging is the process of identifying and resolving errors/bugs in code — examining the flow and using tools to pinpoint problems.

## 1. print() Function and f-strings
Printing values at various points helps you understand the flow and state of variables.

    def add(a, b):
        result = a + b
        print(f'Adding {a} and {b} gives {result}')
        return result

By printing `a`, `b`, and `result`, you can verify the function behaves as expected.

## 2. Interactive Debugging with pdb
Python's built-in `pdb` module allows interactive debugging.

    import pdb

    def divide(a, b):
        pdb.set_trace()
        return a / b

    print(divide(10, 2))

Setting a trace with `set_trace()` lets you step through code, inspect variables, and understand program behavior.

Running this shows the file location, the line where `set_trace()` was called, and an interactive prompt:

    > /Users/fcc/Desktop/debugging.py(5)divide()
    -> return a / b
    (Pdb)

### Useful pdb Commands
Type `help` to see all available commands:

    (Pdb) help

    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt      
    alias  clear      disable  ignore    longlist  r        source   until    
    args   commands   display  interact  n         restart  step     up       
    b      condition  down     j         next      return   tbreak   w        
    break  cont       enable   jump      p         retval   u        whatis   
    bt     continue   exit     l         pp        run      unalias  where    

    Miscellaneous help topics:
    ==========================
    exec  pdb

#### whatis
Check the type of a variable or object:

    (Pdb) whatis a
    <class 'int'>
    (Pdb) whatis divide
    Function divide

#### continue (or cont / c)
Resumes execution of the code:

    (Pdb) continue
    5.0

## 3. IDE Debugging Tools
IDEs offer advanced debugging tools: breakpoints, step execution, and variable inspection.

### Using the VS Code Debugger

**Step 1: Set up your code**

    def divide(a, b):
        result = a / b
        return result

    print(divide(10, 2))
    print(divide(15, 3))

**Step 2: Set a breakpoint**
Click in the gutter (left margin) next to the line `result = a / b` — a red dot marks the breakpoint.

**Step 3: Start debugging**
Press `F5` or go to **Run > Start Debugging**, then select "Python File" when prompted. Execution pauses at the breakpoint.

**Step 4: Inspect variables**
- Hover over variables to see current values
- Use the Variables panel to see all local variables
- Use the Debug Console to evaluate expressions

**Step 5: Step through code**
Use the debug toolbar:
- **Continue** (F5) — resume until the next breakpoint
- **Step Over** (F10) — execute current line, move to next
- **Step Into** (F11) — enter into function calls
- **Step Out** (Shift+F11) — exit the current function

IDE debugging tools give a visual interface to examine program state, often easier than relying on print statements alone.

---
Each technique has its place: `print()` for quick checks, `pdb` for interactive exploration, and IDE debuggers for visual inspection.