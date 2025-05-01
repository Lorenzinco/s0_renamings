class Literal:
    """
    A python class representing a literal in propositional logic.
    """
    def __init__(self,literal:str,negated:bool):
        self.literal = literal
        self.negated = negated
    def __str__(self):
        """
        Returns a string representation of the literal.
        """
        if self.negated:
            return f"¬{self.literal}"
        else:
            return self.literal
    def __eq__(self,other):
        """
        Compares two literals for the same name, negated or not.
        """
        if isinstance(other,Literal):
            return self.literal == other.literal
        else:
            return False
    def clone(self):
        """
        Returns a clone of the literal.
        """
        return Literal(self.literal,self.negated)
    def negate(self):
        """
        Negates the literal.
        """
        self.negated = not self.negated
        return self
