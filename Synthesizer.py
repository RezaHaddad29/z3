from z3 import *
import sys

MAX_STEPS=10

def SelectOp(R,s):
    return If(s==0, R[0], 
            If(s==1, R[1], 
            If(s==2, R[2], 
            If(s==3, R[3], 
            If(s==4, R[4], 
            If(s==5, R[5], 
            If(s==6, R[6], 
            If(s==7, R[7], 
            If(s==8, R[8], 
            If(s==9, R[9], 
                0))))))))))

def operation(R, op, opl_reg, opr_reg, opr_imm):
    leftOperand = SelectOp(R, opl_reg)
    return If(op==0, leftOperand + SelectOp(R, opr_reg),
           If(op==1, leftOperand - SelectOp(R, opr_reg),
           If(op==2, leftOperand << opr_imm,
               0)))

# reza
def Eval(R, s, m, STEPS, op, op1_reg, op2_reg, op2_imm):
    op_n=m[op[s]].as_long()
    op1_reg_tmp=m[op1_reg[s]].as_long()
    op1_val=R[op1_reg_tmp]
    op2_reg_tmp=m[op2_reg[s]].as_long()
    op2_imm_tmp=m[op2_imm[s]].as_long()
    if op_n==0:
        op2_val=R[op2_reg_tmp]
        return op1_val+op2_val

    elif op_n==1:
        op2_val=R[op2_reg_tmp]
        return op1_val-op2_val

    elif op_n==2: 
        return op1_val << op2_imm_tmp

def resultValue(input, m, STEPS, op, op1_reg, op2_reg, op2_imm):
    R=[None]*STEPS
    R[0]=input

    for s in range(1,STEPS):
        R[s]=Eval(R, s, m, STEPS, op, op1_reg, op2_reg, op2_imm)

    return R[STEPS-1] 

def testAnswer(m, STEPS, op, opl_reg, opr_reg, opr_imm):
    result0=resultValue(0, m, STEPS, op, opl_reg, opr_reg, opr_imm)
    result1=resultValue(1, m, STEPS, op, opl_reg, opr_reg, opr_imm)
    result123=resultValue(123, m, STEPS, op, opl_reg, opr_reg, opr_imm)

    if 0*multiplier==result0 and 1*multiplier==result1 and 123*multiplier==result123:
        print ("tests are passed")
    else:
        print ("tests are NOT passed")
        print ("result0",result0)
        print ("result1",result1)
        print ("result123",result123)

OpStr=["ADD", "SUB", "SHL"]

def print_model(m, STEPS, op, opl_reg, opr_reg, opr_imm):
    for s in range(1,STEPS):
        op_n=m[op[s]].as_long()
        op_s=OpStr[op_n]
        opl_reg_n=m[opl_reg[s]].as_long()

        if op_n in [0, 1]:
            print (f"r{s}={op_s} r{opl_reg_n}, r{ m[opr_reg[s]].as_long()}")
        else:
            print ("r%d=%s r%d, %d" % (s, op_s, opl_reg_n, m[opr_imm[s]].as_long()))

def Synthesis(Steps):
    print(f"####Try {Steps} Steps")
    sr = Solver()
    
    R=[BitVec(f'S_s{s}', 32) for s in range(MAX_STEPS)]
    op=[Int(f'op_s{s}') for s in range(MAX_STEPS)]
    opl_reg=[Int(f'op1_reg_s{s}') for s in range(MAX_STEPS)]
    opr_reg=[Int(f'op2_reg_s{s}') for s in range(MAX_STEPS)]
    opr_imm=[BitVec(f'op2_imm_s{s}', 32) for s in range(MAX_STEPS)]

    for s in range(1, Steps):
        
        sr.add(And(op[s]>=0, op[s]<=2))
        sr.add(And(opl_reg[s]>=0, opl_reg[s]<s))
        sr.add(And(opr_reg[s]>=0, opr_reg[s]<s))
        sr.add(And(opr_imm[s]>=1, opr_imm[s]<=31))
    
    sr.add(R[0]==1)
    sr.add(R[Steps-1]==multiplier)

    for s in range(1, Steps):
        sr.add(R[s]==operation(R, op[s], opl_reg[s], opr_reg[s], opr_imm[s]))

    tmp=sr.check()

    if tmp==sat:
        print ("Result:")
        m=sr.model()
        print_model(m, Steps, op, opl_reg, opr_reg, opr_imm)
        testAnswer(m, Steps, op, opl_reg, opr_reg, opr_imm)
        exit(0)
    else:
        print (f"unsat in {Steps} steps")



multiplier = int(input('Please Enter Multiplier: '))
print ("Multiplier :", multiplier)
for s in range(2, MAX_STEPS):
    Synthesis(s)