__author__ = 'sunary'


import os


class Binary():

    def __init__(self):
        pass

    def hibit(self, num):
        num |= (num >>  1)
        num |= (num >>  2)
        num |= (num >>  4)
        num |= (num >>  8)
        num |= (num >> 16)
        return num - (num >> 1)

    def lowbit(selfself, num):
        return num & 1

    def lenbin(self, num):
        if not num:
            return 1

        len_bin = 0
        while num:
            num >>= 1
            len_bin += 1

        return len_bin

    def append_bin(self, num, bin):
        num <<= self.lenbin(bin)
        num |= bin
        return num

class HuffmanCoding():
    '''
    Huffman coding, read binary and write
    '''
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)

        self.bin_helper = Binary()

        self.letter_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
        self.letter_binary = [0b0, 0b10, 0b110, 0b1110, 0b11110, 0b111110, 0b1111110, 0b11111110, 0b111111110, 0b1111111110, 0b11111111110, 0b111111111110, 0b1111111111110, 0b11111111111110,
                              0b111111111111110, 0b1111111111111110, 0b11111111111111110, 0b111111111111111110, 0b1111111111111111110, 0b11111111111111111110, 0b111111111111111111110,
                              0b1111111111111111111110, 0b11111111111111111111110, 0b111111111111111111111110, 0b1111111111111111111111110, 0b11111111111111111111111110]

        self.letter_dict = {}
        for i in range(len(self.letter_frequency)):
            self.letter_dict[self.letter_frequency[i]] = self.letter_binary[i]

    def coding(self):
        text = 'asdsdsaz'
        self.binary = 1

        for char in reversed(text):
            self.binary <<= self.bin_helper.lenbin(self.letter_dict[char])
            self.binary |= self.letter_dict[char]

    def decoding(self):
        text = ''
        count_bit_1 = 1
        self.binary >>= 1
        while self.binary:
            if not self.binary & 0b1:
                text += self.letter_frequency[count_bit_1 - 1]
                count_bit_1 = 1
            else:
                count_bit_1 += 1
            self.binary >>= 1

        text += self.letter_frequency[count_bit_1 - 2]
        print text

    def coding_save(self):
        text = 'asdsdsaz'
        self.byte_arr = []
        bin_temp = 0
        len_bin_temp = 0
        for char in text:
            bin_temp <<= self.bin_helper.lenbin(self.letter_dict[char])
            bin_temp |= self.letter_dict[char]
            len_bin_temp += self.bin_helper.lenbin(self.letter_dict[char])
            while len_bin_temp >= 8:
                self.byte_arr.append(bin_temp >> (len_bin_temp - 8))
                bin_temp &= ((0b1 << (len_bin_temp - 8)) - 1)
                len_bin_temp -= 8

        if len_bin_temp:
            for i in range(8 - len_bin_temp):
                bin_temp <<= 1
                bin_temp |= 1
            self.byte_arr.append(bin_temp)

        ofb = open(self.current_dir + '/../resources/huffman.bin', 'wb')

        for byte in self.byte_arr:
            ofb.write(chr(byte))
        ofb.close()

    def read_decoding(self):
        self.byte_arr = []
        ofb = open(self.current_dir + '/../resources/huffman.bin', 'rb')
        byte = ofb.read(1)
        while byte != '':
            self.byte_arr.append(ord(byte))
            byte = ofb.read(1)
        ofb.close()

        text = ''
        count_bit_1 = 1
        bits_and = [0b10000000, 0b1000000, 0b100000, 0b10000, 0b1000, 0b100, 0b10, 0b1]
        for byte in self.byte_arr:
            for b in bits_and:
                if not byte & b:
                    try:
                        text += self.letter_frequency[count_bit_1 - 1]
                    except:
                        print count_bit_1
                    count_bit_1 = 1
                else:
                    count_bit_1 += 1

        print text

if __name__ == '__main__':
    huffman_coding = HuffmanCoding()
    huffman_coding.coding()
    huffman_coding.decoding()
    huffman_coding.coding_save()
    huffman_coding.read_decoding()