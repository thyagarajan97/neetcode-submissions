class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp_stack = []
        if len(tokens) < 2:
            return int(tokens[0])
        for token in tokens:
            if token in ('+', '*', '-', '/'):
                #print(f'Encountered sign - {token}')
                item_2 = temp_stack.pop()
                item_1 = temp_stack.pop()
                if token == '+':
                    temp_stack.append(int(item_1 + item_2))
                elif token == '-':
                    temp_stack.append(int(item_1 - item_2))
                elif token == '*':
                    temp_stack.append(int(item_1 * item_2))
                elif token == '/':
                    temp_stack.append(int(item_1 / item_2))
                #print(f'Stack-State: {temp_stack}')
            else:
                temp_stack.append(int(token))
                #print(f'Appended {int(token)} , stack-state: {temp_stack}')
            #end if
        #end for
        return temp_stack[0]
    #end def
#end for