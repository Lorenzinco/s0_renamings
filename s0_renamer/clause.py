from literal import Literal

class Clause:
    def __init__(self,literals:list[Literal]):
        self.literals = literals

    def __str__(self):
        """
        Returns a string representation of the clause.
        """
        clause = " \033[94mv\033[0m ".join([str(literal) for literal in self.literals])
        return f"\033[93m(\033[0m{clause}\033[93m)\033[0m"
    def relax(self,literal:Literal):
        """
        Adds a literal to the clause.
        """
        self.literals.append(literal)
    def clone(self):
        """
        Returns a clone of the clause.
        """
        return Clause([literal.clone() for literal in self.literals])
    
    def is_horn(self):
        """
        Checks if the clause is a Horn clause.
        """
        return len(self.literals) == 1 or all(literal.negated for literal in self.literals[:-1])
    
    def all_positive_literals(self)->list[Literal]:
        """
        Returns a list of all positive literals in the clause.
        """
        return [literal for literal in self.literals if not literal.negated]
    