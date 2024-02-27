# -*- coding: utf-8 -*-            
# @Time : 2024/02/25 14:43
# @Author: yxli
# @FileName: correct_dc_model_31_256.py
# @Software: PyCharm
import subprocess
from unit_function_256 import *


class FunctionModel:
    def __init__(self, init_HW, steps, bounds, message_bound, message_differential, op0, op1, op2, op3, op4, op5, op6,
                 op7):
        self.__obj_value = init_HW

        self.__end_step = bounds
        self.__start_step = steps
        self.__message_bound = message_bound
        self.__message_differential = message_differential
        self.__block_size = 32

        self.__declare = []
        self.__constraints = []

        self.__op0 = op0
        self.__op1 = op1
        self.__op2 = op2
        self.__op3 = op3
        self.__op4 = op4
        self.__op5 = op5
        self.__op6 = op6
        self.__op7 = op7

    def save_variable(self, s):
        temp = s + ": BITVECTOR(1);\n"
        if temp not in self.__declare:
            self.__declare.append(temp)
        return s

    def check_assign(self, s):
        if s not in self.__declare:
            self.__declare.append(s)

    def assign_value(self):
        for i in range(self.__message_bound):
            if i not in self.__message_differential:
                for j in range(self.__block_size):
                    temp = "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("wv_" + str(i) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("wd_" + str(i) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)

        temp = "ASSERT BVGT(BVPLUS(10,"
        for i in range(len(self.__message_differential)):
            print(self.__message_differential[i])
            for j in range(self.__block_size):
                if len(self.__message_differential) - 1 == i and j == self.__block_size - 1:
                    temp += "0bin000000000@%s), 0bin%s);\n" % (
                        self.save_variable(
                            "wv_" + str(self.__message_differential[i]) + "_" + str(self.__block_size - 1 - j)),
                        bin(1)[2:].zfill(10))
                else:
                    temp += "0bin000000000@%s," % (
                        self.save_variable(
                            "wd_" + str(self.__message_differential[i]) + "_" + str(self.__block_size - 1 - j)))
        self.__constraints.append(temp)

        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) = 0bin%s;\n" % ("wd_" + str(18) + "_" + str(j), bin(2)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("wd_" + str(18) + "_" + str(j))
        self.__constraints.append(temp)
        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) = 0bin%s;\n" % ("wd_" + str(16) + "_" + str(j), bin(17)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("wd_" + str(16) + "_" + str(j))
        self.__constraints.append(temp)
        for step in range(self.__start_step - 4, self.__start_step):
            for i in range(self.__block_size):
                temp = "ASSERT xv_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                temp += "ASSERT xd_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                temp += "ASSERT yv_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                temp += "ASSERT yd_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                self.__constraints.append(temp)
        for step in range(self.__end_step - 8, self.__end_step):
            for i in range(self.__block_size):
                temp = "ASSERT xv_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                temp += "ASSERT xd_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                self.__constraints.append(temp)
        for step in range(self.__end_step - 4, self.__end_step):
            for i in range(self.__block_size):
                temp = "ASSERT yv_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                temp += "ASSERT yd_" + str(step) + "_" + str(i) + " = 0bin0;\n"
                self.__constraints.append(temp)
        ee = ["=u====n=u=nu===un===n=u=nn=u====",
              "==================u==========n==",
              "uuuu=======unnnnn=unnnnnnnnnnn==",
              "===u=====n==================nn==",
              "================n============n==",
              "================================",
              "================u============u=="]
        for i in range(len(ee)):
            for j in range(len(ee[i])):
                if ee[i][j] == "=":
                    temp = "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("yv_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("yd_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)
                elif ee[i][j] == "u":
                    temp = "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("yv_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("yd_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)
                elif ee[i][j] == "n":
                    temp = "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("yv_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("yd_" + str(i + 8) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)
        aa = ["===================u========n=u=",
              "================================",
              "===u==n===n========n==========nn",
              "================================",
              "================================",
              "================u============u=="]
        for i in range(len(aa)):
            for j in range(len(aa[i])):
                if aa[i][j] == "=":
                    temp = "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("xv_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("xd_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)
                elif aa[i][j] == "u":
                    temp = "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("xv_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("xd_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)
                elif aa[i][j] == "n":
                    temp = "ASSERT %s = 0bin0;\n" % (
                        self.save_variable("xv_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    temp += "ASSERT %s = 0bin1;\n" % (
                        self.save_variable("xd_" + str(i + 5) + "_" + str(self.__block_size - 1 - j)))
                    self.__constraints.append(temp)

        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) =  0bin%s;\n" % ("yd_" + str(14) + "_" + str(j), bin(2)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("yd_" + str(14) + "_" + str(j))
        self.__constraints.append(temp)
        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) =  0bin%s;\n" % ("yd_" + str(12) + "_" + str(j), bin(2)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("yd_" + str(12) + "_" + str(j))
        self.__constraints.append(temp)
        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) =  0bin%s;\n" % ("yd_" + str(13) + "_" + str(j), bin(0)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("yd_" + str(13) + "_" + str(j))
        self.__constraints.append(temp)
        for i in range(32):
            temp = "ASSERT (%s | %s) = %s;\n" % (
                self.save_variable("yd_" + str(11) + "_" + str(31 - i)),
                self.save_variable("yd_" + str(12) + "_" + str(31 - i)),

                self.save_variable("flag_" + str(31 - i)))
            self.__constraints.append(temp)
        temp = "ASSERT BVPLUS(10,"
        for j in range(32):
            if j == 31:
                temp += "0bin000000000@%s) = 0bin%s;\n" % ("flag_" + str(j), bin(5)[2:].zfill(10))
            else:
                temp += "0bin000000000@%s," % ("flag_" + str(j))
        self.__constraints.append(temp)

        temp = "ASSERT BVPLUS(10,"
        for i in range(self.__message_bound):
            for j in range(32):
                if i == self.__message_bound - 1 and j == 31:
                    temp += "0bin000000000@%s) = 0bin%s;\n" % ("wd_" + str(i) + "_" + str(j), bin(48)[2:].zfill(10))
                else:
                    temp += "0bin000000000@%s," % ("wd_" + str(i) + "_" + str(j))
        self.__constraints.append(temp)

    def main(self):
        for i in range(self.__start_step, self.__end_step):
            variable_e, constrain_e = sha_e(self.__block_size, self.__op0[i], self.__op1[i], self.__op2[i], i)
            self.__constraints.append("".join(constrain_e))
            for var in variable_e:
                self.check_assign(var)
            variable_a, constrain_a = sha_a(self.__block_size, self.__op3[i], self.__op4[i], self.__op5[i], i)
            self.__constraints.append("".join(constrain_a))
            for var in variable_a:
                self.check_assign(var)
            if self.__op7[i]:
                variable, constrain = sha2_value(32, "IF", "MAJ", i)
                self.__constraints.append("".join(constrain))
                for var in variable:
                    self.check_assign(var)

        for i in range(self.__message_bound):
            if i > 15:
                variable_w, constrain_w = message_expand(self.__block_size, self.__op6[i], i)
                self.__constraints.append("".join(constrain_w))
                for var in variable_w:
                    self.check_assign(var)

    def obj_value(self, obj):
        temp = "ASSERT BVPLUS(10,"
        for i in range(self.__start_step, self.__end_step):
            for j in range(32):
                if i == self.__end_step - 1 and j == 31:
                    temp += "0bin000000000@%s) = 0bin%s;\n" % ("yd_" + str(i) + "_" + str(j), bin(obj)[2:].zfill(10))
                else:
                    temp += "0bin000000000@%s," % ("yd_" + str(i) + "_" + str(j))
        return temp

    def solver(self):
        self.main()
        self.assign_value()
        constrain = "".join(self.__constraints)
        variable = "".join(self.__declare)
        query = '\n' + 'QUERY FALSE;\nCOUNTEREXAMPLE;'
        kk = -1
        for obj_val in range(self.__obj_value, -1, -1):
            file_write = open("find_dc_model.cvc", "w")
            obj = self.obj_value(obj_val)
            file_write.write(variable)
            file_write.write(constrain)
            #file_write.write(obj)
            file_write.write(query)
            file_write.close()
            stp_parameters = ["stp", "find_dc_model.cvc", "--cryptominisat", "--threads", "26"]
            R = subprocess.check_output(stp_parameters)
            if "Valid.\n" != R.decode():
                file = open("res2_dc_solution_" + str(obj_val) + ".out", "w")
                file.write(R.decode())
                file.close()
                print("The number of HW in a differential characteristic is %s: valid" % obj_val)
                kk = obj_val

            else:
                print("The number of HW in a differential characteristic is %s: invalid" % obj_val)
                break
        if kk != -1:
            for temp in read_differential_characteristic(self.__block_size,
                                                         "res2_dc_solution_" + str(kk) + ".out",
                                                         self.__message_bound):
                print(temp)


if __name__ == '__main__':
    start_step = 5
    end_step = 19
    message_bound = 31
    init_HW = 60
    message_differential = [5, 6, 7, 8, 9, 16, 18]
    op0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    op7 = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    FunctionModel(init_HW, start_step, end_step, message_bound, message_differential, op0, op1, op2, op3, op4, op5, op6,
                  op7).solver()
