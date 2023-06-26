"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Constants
OPERATORS = "+-*/"
# Imports
from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()

    while not source.is_empty():
        target1.push(source.pop())
        if not source.is_empty():
            target2.push(source.pop())

    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = []
    for _ in source:
        lst.append(source.pop())

    for x in lst:
        source.push(x)
    return


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns‌​‌​‌‌‌​‌:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    lst = string.split(" ")
    for value in lst:
        if value in OPERATORS:
            if not stack.is_empty():
                num2 = stack.pop()
                if not stack.is_empty():
                    num1 = stack.pop()
                if value == OPERATORS[0]:
                    num = num1 + num2
                    stack.push(num)
                elif value == OPERATORS[1]:
                    num = num1 - num2
                    stack.push(num)
                elif value == OPERATORS[2]:
                    num = num1 * num2
                    stack.push(num)
                elif value == OPERATORS[3]:
                    num = num1 / num2
                    stack.push(num)
        else:
            stack.push(float(value))
    if not stack.is_empty():
        answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    s = Stack()
    key = list(maze)[0]
    s.push(maze[key][0])
    path = []
    exit = False

    while not s.is_empty():
        node = s.pop()
        if node in path:
            continue
        path.append(node)
        if node in maze:
            for nodechild in maze[node]:
                s.push(nodechild)
                if nodechild in maze:
                    if len(maze[nodechild]) == 0:
                        s.pop()
                else:
                    break

        else:
            exit = True
            break
    if exit is False:
        path = None
    return path
