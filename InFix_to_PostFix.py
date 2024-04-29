from abc import ABC, abstractmethod


class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, element):
        self.array.append(element)
    
    def pop(self):
        if len(self.array) == 0:
            raise ValueError("Stack is empty")
        return self.array.pop()
    
    def get_top(self):
        if len(self.array) == 0:
            raise ValueError("Stack is empty")
        return self.array[-1]
    
    def is_empty(self):
        return len(self.array) == 0
    
    def is_full(self):
        # Python lists don't have a fixed capacity
        return False
    
    def get_size(self):
        return len(self.array)
    
    def display(self):
        return self.array


# An Abstract Base Class for Evaluators


class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, expression):
        pass


class InfixEvaluator(Evaluator):

    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def valid(self, expression):
        stack = []
        for char in expression:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or '([{'.index(stack.pop()) != ')]}'.index(char):
                    return False
        return not stack


    def infixToPostfix(self, expression):
        if not self.valid(expression):
            raise ValueError("Invalid expression")

        postfix = []
        for char in expression:
            if char.isdigit():
                postfix.append(char)
            elif char in '+-*/^':
                while (not self.stack.is_empty() and self.stack.get_top() != '(' and self.precedence.get(self.stack.get_top(), 0) >= self.precedence.get(char, 0)):
                    postfix.append(self.stack.pop())
                self.stack.push(char)
            elif char == '(':
                self.stack.push(char)
            elif char == ')':
                while (not self.stack.is_empty() and self.stack.get_top() != '('):
                    postfix.append(self.stack.pop())
                self.stack.pop()  # Discard the '('
        while not self.stack.is_empty():
            postfix.append(self.stack.pop())

        postfix_str = ''.join(postfix)
        print(f"The Post Fix Expression is: {postfix_str}")

        return postfix


    def evaluate(self, expression):
        try:
            for token in expression:
                if token.isdigit():
                    self.stack.push(int(token))
                else:
                    operand2 = self.stack.pop()
                    operand1 = self.stack.pop()
                    if token == '+':
                        result = operand1 + operand2
                    elif token == '-':
                        result = operand1 - operand2
                    elif token == '*':
                        result = operand1 * operand2
                    elif token == '/':
                        result = operand1 // operand2
                        remainder = operand1 % operand2
                    elif token == '^':
                        result = operand1 ** operand2
                    else:
                        raise ValueError("Invalid operator")
                    self.stack.push(result)
                    if token == '/':
                        self.stack.push(remainder)
            if '/' in expression:
                return self.stack.pop(), self.stack.pop()  # Returning Both Result and Remainder
            else:
                return self.stack.pop()
        except (ValueError):
            return "Invalid Expression"


def run():
    while True:
        infix_evaluator = InfixEvaluator()

        exp = input("Enter an Expression(To Exit write exit): ")
        if exp == "exit":
            break
        exp = infix_evaluator.infixToPostfix(exp)

        result = infix_evaluator.evaluate(exp)
        
        if isinstance(result, tuple):
            quotient, remainder = result
            print(f"\nThe Quotient is: {remainder}")
            print(f"The Remainder is: {quotient}\n")
        else:
            print(f"\nThe Result is: {result}\n")

# run()



class PostfixEvaluator(Evaluator):
    def __init__(self):
        self.stack = Stack()
    
    def evaluate(self, expression):
        try:
            for token in expression:
                if token.isdigit():
                    self.stack.push(int(token))
                else:
                    operand2 = self.stack.pop()
                    operand1 = self.stack.pop()
                    if token == '+':
                        result = operand1 + operand2
                    elif token == '-':
                        result = operand1 - operand2
                    elif token == '*':
                        result = operand1 * operand2
                    elif token == '/':
                        result = operand1 // operand2
                        remainder = operand1 % operand2
                    elif token == '^':
                        result = operand1 ** operand2
                    else:
                        raise ValueError("Invalid operator")
                    self.stack.push(result)
                    if token == '/':
                        self.stack.push(remainder)
            if '/' in expression:
                return self.stack.pop(), self.stack.pop()  # Return Both Result and Remainder
            else:
                return self.stack.pop()
        except (ValueError):
            return "Invalid Expression"


def run():
    while True:
        postfix_evaluator = PostfixEvaluator()

        exp = input("Enter an Expression(To Exit write exit): ")
        if exp == "exit":
            break

        result = postfix_evaluator.evaluate(exp)
        
        if isinstance(result, tuple):
            quotient, remainder = result
            print(f"\nThe Quotient is: {remainder}")
            print(f"The Remainder is: {quotient}\n")
        else:
            print(f"\nThe Result is: {result}\n")

# run()
