

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assignment):

    if len(assignment) == len(VARIABLES):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in ["Monday", "Tuesday", "Wednesday"]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if consistent(new_assignment):
            result = backtrack(new_assignment)
            if result is not None:
                return result
    return None


def select_unassigned_variable(assignment):

    """ Choose a variable not yet assigned, in order."""

    for variable in VARIABLES:
        if variable not in assignment:
            return variable
    return None


def consistent(assignment):
    """ Checks to see if an assignment is consistent"""
    for (x, y) in CONSTRAINTS:

        if x not in assignment or y not in assignment:
            continue

        if assignment[x] == assignment[y]:
            return False

    return True

solution = backtrack(dict())
print(solution)
