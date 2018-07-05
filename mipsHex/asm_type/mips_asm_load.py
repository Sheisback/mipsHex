# mips_asm_load.py

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from mips_asm import *

# load the data to register
class MIPS_Asm_Load(MIPS_Asm):
	def __init__(self, addr):
		super(MIPS_Asm_Load, self).__init__(addr)

	# lbu instruction 
	def do_lbu(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != lbu".format(hex(self.addr), self.ins), self.ins == 'lbu')

		var_name = self.opr2.convert(o_reg)

		if o_func.get_local_var(var_name) is not None:
			var = o_func.get_local_var(var_name)
		else:
			var = var_name

		o_reg.set_register(self.opr1.value, '((uint8_t)' + var + ')')

		comment = o_func.get_comment(opr1=self.opr1.value, opr2='((uint8_t)' + var + ')')

		return comment, None

	# lhu instruction 
	def do_lhu(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != lhu".format(hex(self.addr), self.ins), self.ins == 'lhu')

		var_name = self.opr2.convert(o_reg)

		if o_func.get_local_var(var_name) is not None:
			var = o_func.get_local_var(var_name)
		else:
			var = var_name

		o_reg.set_register(self.opr1.value, '((uint16_t)' + var + ')')

		comment = o_func.get_comment(opr1=self.opr1.value, opr2='((uint16_t)' + var + ')')

		return comment, None

	# load word instruction
	def do_lw(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != lw".format(hex(self.addr), self.ins), self.ins == 'lw')

		var_name = self.opr2.convert(o_reg)

		if o_func.get_local_var(var_name) is not None:
			var = o_func.get_local_var(var_name)
		else:
			var = var_name

		o_reg.set_register(self.opr1.value, var)

		comment = o_func.get_comment(opr1=self.opr1.value, opr2=var)

		return comment, None

	# load immediate instruction
	def do_li(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != li".format(hex(self.addr), self.ins), self.ins == 'li')
		check_assert("[-] Check opr2 type, current({0}) : {1} != {2}".format(self.addr, self.opr2.type, ASM_TYPE['Imm']), self.opr2.type == ASM_TYPE['Imm'])

		o_reg.set_register(self.opr1.value, self.opr2.value)

		comment = o_func.get_comment(opr1=self.opr1.value, opr2=self.opr2.value)

		return comment, None

	# load unsigned immediate instruction
	def do_lui(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != lui".format(hex(self.addr), self.ins), self.ins == 'lui')
		check_assert("[-] Check opr2 type, current({0}) : {1} != {2}".format(self.addr, self.opr2.type, ASM_TYPE['Imm']), self.opr2.type == ASM_TYPE['Imm'])

		o_reg.set_register(self.opr1.value, self.opr2.value)

		comment = o_func.get_comment(opr1=self.opr1.value, opr2=self.opr2.value)

		return comment, None

	# load address instruction
	def do_la(self, o_reg, o_func):
		check_assert("[-] Check ins, current({0}) : {1} != la".format(hex(self.addr), self.ins), self.ins == 'la')
		check_assert("[-] Check opr2 type, current({0}) : {1} != {2}".format(hex(self.addr), self.opr2.type, ASM_TYPE['Imm']), self.opr2.type == ASM_TYPE['Imm'])

		o_reg.set_register(self.opr1.value, self.opr2.value)

		comment = o_func.get_comment(opr1=self.opr1.value, opr2=self.opr2.value)

		return comment, None
