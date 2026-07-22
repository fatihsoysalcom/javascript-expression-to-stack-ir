def generate_ir_from_js_expression(js_expression_str):
    """
    Simulates compilation of a simple JavaScript-like arithmetic expression
    into a stack-based Intermediate Representation (IR).
    This example hardcodes the IR for '10 + 5 * 2' to demonstrate the concept
    without implementing a full parser, focusing on the IR generation.
    """
    print(f"--- Simulating compilation of JS expression: '{js_expression_str}' ---")
    # In a real compiler (like one using LLVM), a parser would generate an Abstract Syntax Tree (AST),
    # and then an IR generator would traverse the AST to produce LLVM IR.
    # Here, we directly generate a simplified, stack-based IR for the expression '10 + 5 * 2'.
    # This IR represents operations for a minimalistic stack machine, avoiding complex runtime features.
    ir_instructions = [
        ('PUSH_INT', 10),  # Push integer 10 onto the stack
        ('PUSH_INT', 5),   # Push integer 5 onto the stack
        ('PUSH_INT', 2),   # Push integer 2 onto the stack
        ('MUL',),          # Pop 2, 5; push 5 * 2 = 10 (demonstrates operator precedence)
        ('ADD',),          # Pop 10, 10; push 10 + 10 = 20
        ('PRINT_TOP',)     # Pop top of stack and print it as the final result
    ]
    print("Generated IR (simplified LLVM-like stack instructions):")
    for instr in ir_instructions:
        print(f"  {instr}")
    print("--- End IR generation ---")
    return ir_instructions

def execute_ir(ir_instructions):
    """
    Executes the given Intermediate Representation (IR) using a simple
    stack-based virtual machine. This VM operates without a complex
    JavaScript runtime or garbage collector, mimicking the bare-metal
    execution concept for a minimal footprint.
    """
    print("\n--- Executing IR on a minimalistic VM (no JS runtime/GC) ---")
    stack = []
    for instruction in ir_instructions:
        opcode = instruction[0]

        if opcode == 'PUSH_INT':
            value = instruction[1]
            stack.append(value)
            print(f"  PUSH_INT {value} -> Stack: {stack}")
        elif opcode == 'ADD':
            if len(stack) < 2: raise Exception("Stack underflow for ADD")
            b = stack.pop()
            a = stack.pop()
            result = a + b
            stack.append(result)
            print(f"  ADD ({a} + {b}) -> Stack: {stack}")
        elif opcode == 'SUB':
            if len(stack) < 2: raise Exception("Stack underflow for SUB")
            b = stack.pop()
            a = stack.pop()
            result = a - b
            stack.append(result)
            print(f"  SUB ({a} - {b}) -> Stack: {stack}")
        elif opcode == 'MUL':
            if len(stack) < 2: raise Exception("Stack underflow for MUL")
            b = stack.pop()
            a = stack.pop()
            result = a * b
            stack.append(result)
            print(f"  MUL ({a} * {b}) -> Stack: {stack}")
        elif opcode == 'DIV':
            if len(stack) < 2: raise Exception("Stack underflow for DIV")
            b = stack.pop()
            a = stack.pop()
            if b == 0: raise Exception("Division by zero")
            result = a // b # Integer division for simplicity
            stack.append(result)
            print(f"  DIV ({a} / {b}) -> Stack: {stack}")
        elif opcode == 'PRINT_TOP':
            if not stack: raise Exception("Stack empty for PRINT_TOP")
            final_result = stack.pop()
            print(f"  PRINT_TOP -> Final Result: {final_result}")
        else:
            raise Exception(f"Unknown opcode: {opcode}")
    print("--- VM execution complete ---")
    if stack:
        print(f"Warning: Stack not empty at end of execution: {stack}")

if __name__ == "__main__":
    # The JavaScript-like expression we want to "compile" and "run"
    js_code = "10 + 5 * 2"

    # Step 1: Simulate compilation to IR
    intermediate_representation = generate_ir_from_js_expression(js_code)

    # Step 2: Execute the generated IR
    execute_ir(intermediate_representation)
