from clause import Clause
from literal import Literal

class Phi:
    def __init__(self,clauses:list[Clause]):
        """
        A class representing a propositional formula in CNF.
        """
        self.clauses = clauses

    def from_string(formula:str):
        """
        Parses a formula from CNF standard format.
        """
        clauses = []
        for line in formula.splitlines():
            if line.startswith("c") or line.startswith("p"):
                continue
            clause = []
            for literal in line.split():
                if literal == "0":
                    break
                if literal.startswith("-"):
                    clause.append(Literal(literal[1:],True))
                else:
                    clause.append(Literal(literal,False))
            clauses.append(Clause(clause))
        return Phi(clauses)


    def __str__(self):
        """
        Returns a string representation of the formula.
        """
        return " \033[91m^ \033[0m".join([str(clause) for clause in self.clauses])
    
    def relax_all(self,literal:Literal):
        """
        Relaxes all the clauses in the formula that do not contain such literal with a given literal.
        """
        for clause in self.clauses:
            if literal not in clause.literals: # uses the __eq__ method of Literal, so it checks for the same name and not the negation
                self.relax(clause,literal)
            

    
    def relax(self,clause:Clause,literal:Literal):
        """
        Takes a clone of the clause and adds a literal with the same name but negated to it, the same literal is also added to the original clause.
        """
        negated_literal = literal.clone().negate()
        clone = clause.clone()

        #remove the original clause from the list of clauses
        self.clauses.remove(clause)

        clone.relax(negated_literal)
        clause.relax(literal)

        #add the new clause to the list of clauses
        self.clauses.append(clone)
        self.clauses.append(clone)
    
    def remove_horn_clauses(self):
        """
        Removes all Horn clauses from the formula.
        """
        self.clauses = [clause for clause in self.clauses if not clause.is_horn()]

    def literal_in_common(self)->list[Literal]:
        """
        Returns a list of literals that are in common between the clauses.
        """
        if len(self.clauses) == 0:
            return []
        if len(self.clauses) == 1:
            return self.clauses[0].literals
        
        common_literals = self.clauses[0].literals.copy()
        common_literals = [literal for literal in common_literals if all(any(literal == l for l in clause.literals) for clause in self.clauses[1:])]

        return common_literals
    
    def remove_literal(self,literal:Literal):
        """
        Removes a literal from the formula.
        """
        for clause in self.clauses:
            clause.literals = [l for l in clause.literals if l != literal]
        self.clauses = [clause for clause in self.clauses if len(clause.literals) > 0]

    def literal_with_most_occurrences(self)->Literal:
        """
        Returns the literal with the most occurrences in the formula.
        """
        if len(self.clauses) == 0:
            return None
        if len(self.clauses) == 1:
            return self.clauses[0].literals[0]
        
        literal_count = {}
        for clause in self.clauses:
            for literal in clause.literals:
                if literal.literal not in literal_count:
                    literal_count[literal.literal] = 0
                literal_count[literal.literal] += 1

        max_literal = max(literal_count, key=literal_count.get)
        return Literal(max_literal,False)
    
