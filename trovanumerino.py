def is_operator(item):
    return type(item) == str

def rpn_eval(stack):
    item = stack.pop()
    if is_operator(item):
        operand_b = rpn_eval(stack)
        operand_a = rpn_eval(stack)
        if item == '+':
            return operand_a + operand_b
        elif item == '-':
            return operand_a - operand_b
        elif item == '*':
            return operand_a * operand_b
        elif item == '/':
            if operand_b == 0:
                return None
            return operand_a / operand_b
        else:
            return None
    else:
        return item


def rpn(expr):
    temp = expr[:]
    val = rpn_eval(expr)
    if val == 24:
        print(str(temp) + ": " + str(val))
    return val

def check_valid(expr, expected_result):
    actual_result = rpn(expr)
    if actual_result != expected_result:
        print("Error! ", str(expr), " actual: ", actual_result, "; expected: ", expected_result)
    else:
        print("[OK]")


# Some UT's for the RPN evaluator
# check_valid([10, 10, '+'], 20)
# check_valid([1, 2, '+'], 3)
# check_valid([4, 2, '-'], 2)
# check_valid([5, 1, '/'], 5)
# check_valid([3, 5, '/'], 3/5)
# check_valid([5, 7, '*'], 35)
# check_valid([1.2, 1.3, '+'], 1.2 + 1.3)
# check_valid([10, 50, '-'], -40)

# check_valid([2, 4, '*', 8, '+'], 16)
# check_valid([2, 4, 8, '+', '*'], 24)
# check_valid([3, 2, '*', 11, '-'], -5)
# check_valid([2, 5, '*', 4, '+', 3, 2, '*', 1, '+', '/'], 2)

# check_valid([1, 1, 1, 1, '+', '+', '+'], 4)
# check_valid([1, 1, 1, '+', 1, '+', '+'], 4)
# check_valid([1, 1, '+', 1, 1, '+', '+'], 4)
# check_valid([1, 1, '+', 1, '+', 1, '+'], 4)


def permutation(list):
    if len(list) == 1:
        return [list]
 
    temp_list = []
 
    for i in range(len(list)):
       item = list[i]
       remaining_list = list[:i] + list[i+1:]
 
       for p in permutation(remaining_list):
           temp_list.append([item] + p)
    return temp_list

operands = [1, 3, 4, 6]
operands_permutations = permutation(operands)
# for p in operands_permutations:
#     print(p)

def combination_worker(list, prefix, n, k, combination_list):
    if k == 0:
        combination_list.append(prefix)
        return
    for i in range(n):
        new_prefix = prefix + [list[i]]
        combination_worker(list, new_prefix, n, k - 1, combination_list)

def combination(list, length):
    combination_list = []
    combination_worker(list, [], len(list), length, combination_list)
    return combination_list

operators = ['+', '-', '*', '/']
operators_combinations = combination(operators, 3)
# for p in operators_combinations:
#     print(p)

for i in operands_permutations:
    for j in operators_combinations:
        rpn([ i[0], i[1], i[2], i[3], j[0], j[1], j[2] ])
        rpn([ i[0], i[1], i[2], j[0], i[3], j[1], j[2] ])
        rpn([ i[0], i[1], j[0], i[2], i[3], j[1], j[2] ])
        rpn([ i[0], i[1], j[0], i[2], j[1], i[3], j[2] ])
        