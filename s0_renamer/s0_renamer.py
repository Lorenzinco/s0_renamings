from clause import Clause
from literal import Literal
from phi import Phi
from s0 import is_s0

def find_renamings(phi:Phi)->list[Literal]:
    if len(phi.clauses) == 0:
        return []
    if len(phi.clauses) == 1:
        return phi.clauses[0].all_positive_literals()
    
    ## Step 1: Remove all Horn clauses from the formula
    phi.remove_horn_clauses()
    ## Check empty
    if len(phi.clauses) == 0:
        return []
    ## Step 2: Check if all the remaining clauses have at least one literal in common
    common_literals = phi.positive_literal_in_common()
    if len(common_literals) > 0:
        phi.remove_literal(common_literals[0])
        return find_renamings(phi)
    else:
        target_relax = phi.positive_literal_with_most_occurrences()
        phi.remove_literal(target_relax)
        return find_renamings(phi)


def main():
    with open("cnfs/0.cnf") as f:
        formula = f.read()
    phi = Phi.from_string(formula)

    print(phi)
    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)

    print("Is S0:",is_s0(phi.clone()))
    renamings = find_renamings(phi.clone())
    print("Renamings:")
    stringed = [str(renaming) for renaming in renamings]
    print(stringed)
    for literal in renamings:
        phi.rename(literal)
    
    


if __name__ == "__main__":
    main()
