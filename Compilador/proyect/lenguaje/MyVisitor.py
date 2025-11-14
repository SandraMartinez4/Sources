from .GrammarVisitor import GrammarVisitor
from .GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

    # Visita nuestro programa
    def visitProgram(self, ctx: GrammarParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # Definimos la asignacion
    def visitAssing(self, ctx: GrammarParser.AssingContext):
        # Se obtiene el tipo de la variable (int, string)
        var_type = ctx.type_().getText()
        # Se obtiene el id o nombre de la variable
        name = ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una expresion
        value = self.visit(ctx.expr())

        # Validacion de tipos
        if var_type == 'int' and not isinstance(value, int):
            raise TypeError(f"Error en '{name}' ")
        if var_type == 'string' and not isinstance(value, str):
            raise TypeError(f"Error en '{name}' ")

        # Almacena en memoria el valor y su tipo
        self.memory[name] = {'value': value, 'type': var_type}

        # Se verifica que la variable exista
        if name not in self.memory:
            raise NameError(f"Variable '{name}' no ha sido definida.")

        # Se obtiene el tipo original
        var_type = self.memory[name]['type']

        # Se valida el nuevo valor
        if (var_type == 'int' and not isinstance(value, int)) or \
           (var_type == 'string' and not isinstance(value, str)):
            raise TypeError(f"No se puede asignar un {type(value).__name__} ")

        # Se actualiza el valor en memoria
        self.memory[name]['value'] = value

    # Definimos la impresión
    def visitPrint(self, ctx: GrammarParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)

    # Visitor para if
    def visitIf_statement(self, ctx: GrammarParser.If_statementContext):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.block())
        return None

    # Visitor para for
    def visitFor_statement(self, ctx: GrammarParser.For_statementContext):
        self.visit(ctx.assing(0))  # Inicializador

        while self.visit(ctx.expr()):
            self.visit(ctx.block())
            self.visit(ctx.assing(1))

    # Bloque
    def visitBlock(self, ctx: GrammarParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # Expresiones
    def visitExpr(self, ctx):
        # IDs
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no ha sido definida")
            return self.memory[name]["value"]

        # Número
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())

        # String
        elif ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]

        # Operadores
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))

            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                if right == 0:
                    raise ValueError("Division por cero")
                return left / right

            if ctx.op.text == ">":
                return left > right
            if ctx.op.text == "<":
                return left < right
            if ctx.op.text == ">=":
                return left >= right
            if ctx.op.text == "<=":
                return left <= right
            if ctx.op.text == "==":
                return left == right
            if ctx.op.text == "!=":
                return left != right
