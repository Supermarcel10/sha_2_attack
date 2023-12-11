"""
modadd_model_constrain = ['0000000000', '0000010100', '0000111100', '0001000100', '0001010001', '0001110000',
                          '0011001100', '0011010000', '0011110011', '0100000100', '0100010001', '0100110000',
                          '0101000001', '0101010101', '0101110100', '0111000000', '0111010100', '0111111100',
                          '1100001100', '1100010000', '1100110011', '1101000000', '1101010100', '1101111100',
                          '1111000011', '1111011100', '1111111111']
"""
modadd_model_constrain = ['1---1-01--', '-0--011---', '1--01----0', '-1-0-1-1--', '1-1--0---0', '--010-1---',
                          '------10--', '1--0--01--', '1-1--10---', '--10------', '01--0-1---', '--1-1-0-0-',
                          '----1---01', '---01-01--', '-1-1-0-1--', '----01--1-', '1-1-1---0-', '-0-----1-1',
                          '01--01-0-0', '01010----0', '1-------01', '0-01--1---', '-1-1-1-0--', '----10----',
                          '-0-1-1-1--', '--01----1-', '---0-0---1', '10--------', '01------1-', '--0101-0-0',
                          '-0-0-1-0--', '-1-0-0-0--', '-0-0-0-1--', '--1--001--', '--------10', '-0-1-0-0--',
                          '--1-----01']
"""
expand_model_contsrain_1 = ['00011101', '01110000', '00010100', '11010000', '11001100', '11000111', '00111100',
                            '11110011', '00000000', '01001101', '01000100', '00110111', '01010001']
expand_model_contsrain_2 = ['00000000', '00110101', '00010100', '00111100', '00011111', '11000100', '01000101',
                            '11001111', '01001100', '01110001', '01010000', '11110000', '11010011']
"""
expand_model_contsrain_1 = ['----10--', '-0-0---1', '-0-1-0--', '----0101', '--01--1-', '0101---0', '01--1--0',
                            '01----1-', '--011--0', '------10', '----1-1-', '1---01-0', '-1-1-1--', '--1-01-0',
                            '10------', '-0-0-1--', '1-----01', '1-1---0-', '-1-0-0--', '--10----', '--1---01']

expand_model_contsrain_2 = ['--10----', '01----1-', '1-01--0-', '--1-01-0', '1---1-0-', '1-----01', '----10--',
                            '----011-', '-0-0-1--', '--011--0', '10------', '--01--01', '-0-1-0--', '------10',
                            '01--01-0', '----1-01', '011----0', '-1-1-1--', '-0---0-1', '-1-0-0--', '--1---1-']
"""
fast_boolean_xor_contsrain = ['01110000', '11110000', '11010111', '01111101', '00110011', '11110101', '00010001',
                              '01010101', '01000001', '11000100', '01011111', '00010011', '00000111', '01010000',
                              '00001101', '00110001', '11011101', '01110111', '00000101', '01000100', '01001100',
                              '00000000', '00001111', '00110100', '00010100', '11010000', '01000011', '11001100',
                              '00011100', '11000001', '11000011', '00111100', '11111111']
"""
xor_fast_constrain = ['-0-1-0-0', '-1-0-1-1', '-0-0-1-0', '1-1-0-1-', '0-1-0101', '0-1-1-1-', '-1-1-0-1',
                      '----10--', '1-01010-', '1-0-1-1-', '0-01011-', '-0-0-0-1', '010-1-01', '-1-0-0-0',
                      '10------', '-1-1-1-0', '--10----', '-0-1-1-1', '------10', '1-1-1-0-']
"""

maj_fast_constrain = ["00000000", "00001100", "00000100", "00110000", "00111111", "00110100", "00110011", "00010000",
                      "00011100", "00010101", "00010001", "00001111", "00000101", "11000000", "11001111", "11000100",
                      "11000011", "11110011", "11111111", "11110111", "11010000", "11011111", "11010101", "01000000",
                      "01001100", "01000101", "01000001", "01110000", "01111111", "01110101", "01010001", "01011101",
                      "01010101"]
"""
maj_fast_constrain = ['0101---0', '------10', '--1--001', '--1-1-0-', '-0--1-01', '01--01-0', '0-01--1-',
                      '1---1-0-', '1--0--01', '10------', '-01---01', '1-1---0-', '0---011-', '---01-01',
                      '-0-0-0-1', '--010-1-', '--0101-0', '--10----', '1----001', '010---1-', '----10--',
                      '01---01-', '---0011-']

"""
if_fast_constrain = ["00000000", "00001111", "00000101", "00110000", "00111111", "00110101", "00010000", "00011111",
                     "00010101", "11000000", "11001100", "11000101", "11000001", "11110011", "11111111", "11110100",
                     "11110000", "11010000", "11011100", "11010101", "11010001", "11000011", "11001111", "11000100",
                     "01000000", "01001111", "01000100", "01000011", "01110000", "01111111", "01110100", "01110011",
                     "01010001", "01011100", "01010101", "01010000", "01000001", "01001100", "01000101", "00001100",
                     "00000100", "00110011", "00110111", "00010001", "00011101"]
"""
if_fast_constrain = ['--1--001', '-101--1-', '-1--1-01', '--1-1-0-', '--0-011-', '----10--', '---01-01', '------10',
                     '--10----', '--010-1-', '-1--011-', '10------', '-0-1-1-0', '-11---01', '-0-0-0-1', '--0101-0']

xor_full_constrain = ['-01---1-0-1', '10---------', '---0010110-', '1-1-1-0----', '-1-1-1-0---', '-1-0-0-0---',
                      '01-0--01-10', '-0--011-11-', '1-1-0-1----', '-0--1-0111-', '0-1-1-1----', '--01-0010-1',
                      '1----01--01', '-0--010101-', '1----001-11', '-001--1-0-0', '---01-1-01-', '-0-0-1-0---',
                      '1--0--01-00', '-0--011-00-', '-0-1-0-0---', '01---01--11', '--01-0011-0', '-0-1-1-1---',
                      '-0-0-0-1---', '1-0-1-1----', '--1--0011-1', '------10---', '1----01--10', '--10-------',
                      '-01---1-1-0', '0-1-0101---', '1-010-01---', '01-0--1--00', '-001--1-1-1', '-1-1-0-1---',
                      '----10-----', '01---001-01', '---01-1-10-', '01011-0----', '-01---010-0', '-1-0-1-1---',
                      '---01-0100-', '01010-1----']

ifz_full_constrain = ['-01-01-00--', '-01-1--01--', '---00101-1-', '010-01-0-0-', '-1---0-0--1', '-0--1-1-0--',
                      '010-1--0-1-', '0101---0---', '-0--01010--', '0---011-1--', '--0-011--0-', '--1---01--0',
                      '-0--1-011--', '1--01-0--0-', '-0-0-1-010-', '01---11----', '1-----01--1', '--0-1-1--1-',
                      '--01-11----', '--10-------', '--01--1---0', '01----1---1', '---0-0-1--0', '1--001-0-1-',
                      '0-011--00--', '1-1----0---', '1----101---', '-00101-01--', '---1-0-0--0', '-0-0-1-001-',
                      '------10---', '-0---0-1--1', '10---------', '--1--101---', '----10-----', '---01-01-0-']

maj_full_constrain = ['-0-0-1-010-', '-0--011----', '1-1---0----', '--010-1----', '-0-1-0-01-0', '-1-0-0-0-10',
                      '-0---0-10-0', '------10---', '----10-----', '01--0-1----', '-01---01---', '--0101-0---',
                      '0-01--1----', '--1--001---', '---01-01---', '1--0--01---', '--10-------', '--1-1-0----',
                      '-0-0---111-', '01--01-0---', '-0---0-11-1', '1----001---', '010---1----', '--0-011----',
                      '1---1-0----', '-1-0-0-0-01', '-0-1-0-00-1', '---0-0-1-11', '10---------', '-0--1-01---',
                      '---0-0-1-00', '-0-0---100-', '-0-0-1-001-', '0101---0---']
addexp_model_constrain = ['01--01---0', '-1-0-0-0--', '-0-1-1-1--', '-1-1-1-0--', '01--0---1-', '--0---1-1-',
                          '1-----010-', '------10--', '--010---1-', '---01-1--1', '--1---010-', '0-01----1-',
                          '-01---1--1', '1-----0-01', '----01-01-', '-----00101', '--0101---0', '-1-0-1-1--',
                          '010-011---', '0101-----0', '0-----1-1-', '--1---0-01', '--------10', '01-----01-',
                          '--01--1--0', '1----01--1', '----1-0-01', '-0-0-0-1--', '-0--01--1-', '----011--0',
                          '-1-1-0-1--', '-0-0---0-1', '10--------', '---0--0101', '1-1-1-0---', '-0-0-1-0--',
                          '----1-010-', '01----1--0', '----10----', '1-1-----0-', '--10------', '----0-1-1-',
                          '-0-1-0-0--', '--1-1---0-', '1---1---0-']
xor = ['1000', '1110', '0111', '1011', '0010', '1101', '0100', '0001']
ifx = ['0-01', '0-10', '10-1', '11-0']
maj = ['1-10', '-110', '0-01', '11-0', '00-1', '-001']
modadd_model = ['0001-', '1-1-0', '1--00', '11--0', '-00-1', '0-0-1', '-0-11', '0--11', '--011', '1110-',
                '--100', '-1-00', '-11-0', '00--1']
k_constant = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538,
              0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe,
              0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235,
              0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
              0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab,
              0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725,
              0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed,
              0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
              0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218,
              0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
              0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373,
              0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
              0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c,
              0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6,
              0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc,
              0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]
derive_cond_constrain = ['-10', '101', '01-']