import llvmlite.ir as llvm_ir


def constant_folding(function):
    for block in function.blocks:
        for inst in block.instructions:
            if isinstance(inst, llvm_ir.BinaryOperator) and \
              len(inst.operands) >= 2 and \
              isinstance(inst.operands[0], llvm_ir.Constant) and \
              isinstance(inst.operands[1], llvm_ir.Constant):
                op1 = inst.operands[0].constant
                op2 = inst.operands[1].constant
                if inst.opcode == "add":
                    folded_val = op1 + op2
                elif inst.opcode == "sub":
                    folded_val = op1 - op2
                elif inst.opcode == "mul":
                    folded_val = op1 * op2
                elif inst.opcode == "udiv":
                    
                    folded_val = op1 // op2
                elif inst.opcode == "sdiv":
                    folded_val = op1 / op2
                else:
                    continue  # skip other instructions
                const_inst = llvm_ir.Constant(inst.type, folded_val)
                block.instructions[0:0] = [llvm_ir.Assign(inst.dest, const_inst)]
                block.instructions.remove(inst)



# create an example function to optimize
function = llvm_ir.Function("example", [], llvm_ir.VoidType())
block = function.append_basic_block("entry")
x = block.add_instruction(llvm_ir.AllocaInstr(llvm_ir.IntType(32), "x"))
y = block.add_instruction(llvm_ir.AllocaInstr(llvm_ir.IntType(32), "y"))
z = block.add_instruction(llvm_ir.AllocaInstr(llvm_ir.IntType(32), "z"))
store1 = block.add_instruction(llvm_ir.StoreInstr(x, llvm_ir.Constant(llvm_ir.IntType(32), 10)))
store2 = block.add_instruction(llvm_ir.StoreInstr(y, llvm_ir.Constant(llvm_ir.IntType(32), 20)))
load1 = block.add_instruction(llvm_ir.LoadInstr(x))
load2 = block.add_instruction(llvm_ir.LoadInstr(y))
add = block.add_instruction(llvm_ir.BinaryOperator("add", llvm_ir.IntType(32), load1, load2))
store3 = block.add_instruction(llvm_ir.StoreInstr(z, add))
ret = block.add_instruction(llvm_ir.ReturnInst())

print("Before optimization:")
print(function)  # view function before optimization

# perform constant folding and constant propagation
constant_folding(function)
# constant_propagation(function)

print("\nAfter optimization:")
print(function)  # view function after optimization