class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string : int = 1 #start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<=2
            if nucleotide == "A": #change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": #chang"e last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G": #cahnge last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T": #change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))