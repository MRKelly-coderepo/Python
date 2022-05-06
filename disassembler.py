import pefile
from capstone import *

class Disasm:
    ARCH = CS_ARCH_X86
    MODE_32 = CS_MODE_32
    MODE_64 = CS_MODE_64

    def __init__(self, binary):
        self.binary = binary
        self.pe = pefile.PE(self.binary)
        self.entry = self.pe.OPTIONAL_HEADER.AddressOfEntryPoint
        self.entry_address = self.entry+self.pe.OPTIONAL_HEADER.ImageBase
        self.binary = self.pe.get_memory_mapped_image()[self.entry:]

    def dump(self):
        try:
            asm = Cs(self.ARCH,self.MODE_32)
            for inst in asm.disasm(self.binary,self.entry_address):
                print(f"0x{inst.address}\t{inst.mnemonic}\t{inst.op_str}")
        except CsError as e:
            print(f"ERROR: {e}")
