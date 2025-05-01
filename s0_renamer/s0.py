from clause import Clause
from literal import Literal
from phi import Phi

def is_s0(phi:Phi)->bool:
    """
    Checks if the formula is in S0 form.
    """
    if len(phi.clauses) == 0:
        return True
    elif len(phi.clauses) == 1:
        return phi.clauses[0].is_horn()
    ## Step 1: Remove all Horn clauses from the formula
    phi.remove_horn_clauses()
    ## Check empty
    if len(phi.clauses) == 0:
        return True
    ## Step 2: Check if all the remaining clauses have at least one literal in common
    common_literals = phi.positive_literal_in_common()
    if len(common_literals) == 0:
        return False
    ## Step 3: Remove such literal from the formula
    target = common_literals[0]
    phi.remove_literal(target)
    return is_s0(phi)
    

def main():
    with open("cnfs/0.cnf") as f:
        formula = f.read()
    phi = Phi.from_string(formula)

    print(phi)
    print("Is S0:",is_s0(phi))

    with open("cnfs/1.cnf") as f:
        formula = f.read()
    phi_2 = Phi.from_string(formula)
    print(phi_2)
    print("Is S0:",is_s0(phi_2))

    with open("cnfs/2.cnf") as f:
        formula = f.read()
    phi_3 = Phi.from_string(formula)
    print(phi_3)
    print("Is S0:",is_s0(phi_3))
    


if __name__ == "__main__":
    main()