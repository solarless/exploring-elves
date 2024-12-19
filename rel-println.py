import os


def main() -> None:
    contents = bytearray(0x0328)

    # >>>>>>>> ELF HEADER <<<<<<<<

    # e_ident[EI_MAG0..=EI_MAG3]
    contents[0x0000] = 0x7f
    contents[0x0001] = 0x45
    contents[0x0002] = 0x4c
    contents[0x0003] = 0x46

    # e_ident[EI_CLASS]
    contents[0x0004] = 0x02

    # e_ident[EI_DATA]
    contents[0x0005] = 0x01

    # e_ident[EI_VERSION]
    contents[0x0006] = 0x01

    # e_ident[EI_OSABI]
    contents[0x0007] = 0x00

    # e_ident[EI_ABIVERSION]
    contents[0x0008] = 0x00

    # e_ident[EI_PAD..EI_NIDENT]
    contents[0x0009] = 0x00
    contents[0x000a] = 0x00
    contents[0x000b] = 0x00
    contents[0x000c] = 0x00
    contents[0x000d] = 0x00
    contents[0x000e] = 0x00
    contents[0x000f] = 0x00

    # e_type
    contents[0x0010] = 0x01
    contents[0x0011] = 0x00

    # e_machine
    contents[0x0012] = 0x3e
    contents[0x0013] = 0x00

    # e_version
    contents[0x0014] = 0x01
    contents[0x0015] = 0x00
    contents[0x0016] = 0x00
    contents[0x0017] = 0x00

    # e_entry
    contents[0x0018] = 0x00
    contents[0x0019] = 0x00
    contents[0x001a] = 0x00
    contents[0x001b] = 0x00
    contents[0x001c] = 0x00
    contents[0x001d] = 0x00
    contents[0x001e] = 0x00
    contents[0x001f] = 0x00

    # e_phoff
    contents[0x0020] = 0x00
    contents[0x0021] = 0x00
    contents[0x0022] = 0x00
    contents[0x0023] = 0x00
    contents[0x0024] = 0x00
    contents[0x0025] = 0x00
    contents[0x0026] = 0x00
    contents[0x0027] = 0x00

    # e_shoff
    contents[0x0028] = 0x68
    contents[0x0029] = 0x01
    contents[0x002a] = 0x00
    contents[0x002b] = 0x00
    contents[0x002c] = 0x00
    contents[0x002d] = 0x00
    contents[0x002e] = 0x00
    contents[0x002f] = 0x00

    # e_flags
    contents[0x0030] = 0x00
    contents[0x0031] = 0x00
    contents[0x0032] = 0x00
    contents[0x0033] = 0x00

    # e_ehsize
    contents[0x0034] = 0x40
    contents[0x0035] = 0x00

    # e_phentsize
    contents[0x0036] = 0x00
    contents[0x0037] = 0x00

    # e_phnum
    contents[0x0038] = 0x00
    contents[0x0039] = 0x00

    # e_shentsize
    contents[0x003a] = 0x40
    contents[0x003b] = 0x00

    # e_shnum
    contents[0x003c] = 0x07
    contents[0x003d] = 0x00

    # e_shstrndx
    contents[0x003e] = 0x06
    contents[0x003f] = 0x00

    # >>>>>>>> CODE <<<<<<<<

    # println:

    # push rdi
    contents[0x0040] = 0x57

    # call strlen
    contents[0x0041] = 0xe8
    contents[0x0042] = 0x28
    contents[0x0043] = 0x00
    contents[0x0044] = 0x00
    contents[0x0045] = 0x00

    # mov rdx, rax
    contents[0x0046] = 0x48
    contents[0x0047] = 0x89
    contents[0x0048] = 0xc2

    # mov eax, 0x01
    contents[0x0049] = 0xb8
    contents[0x004a] = 0x01
    contents[0x004b] = 0x00
    contents[0x004c] = 0x00
    contents[0x004d] = 0x00

    # mov rdi, 0x01
    contents[0x004e] = 0x48
    contents[0x004f] = 0xc7
    contents[0x0050] = 0xc7
    contents[0x0051] = 0x01
    contents[0x0052] = 0x00
    contents[0x0053] = 0x00
    contents[0x0054] = 0x00

    # pop rsi
    contents[0x0055] = 0x5e

    # syscall
    contents[0x0056] = 0x0f
    contents[0x0057] = 0x05

    # mov eax, 0x01
    contents[0x0058] = 0xb8
    contents[0x0059] = 0x01
    contents[0x005a] = 0x00
    contents[0x005b] = 0x00
    contents[0x005c] = 0x00

    # lea rsi, [rip + newline]
    contents[0x005d] = 0x48
    contents[0x005e] = 0x8d
    contents[0x005f] = 0x35
    contents[0x0060] = 0x00
    contents[0x0061] = 0x00
    contents[0x0062] = 0x00
    contents[0x0063] = 0x00

    # mov rdx, 0x01
    contents[0x0064] = 0x48
    contents[0x0065] = 0xc7
    contents[0x0066] = 0xc2
    contents[0x0067] = 0x01
    contents[0x0068] = 0x00
    contents[0x0069] = 0x00
    contents[0x006a] = 0x00

    # syscall
    contents[0x006b] = 0x0f
    contents[0x006c] = 0x05

    # ret
    contents[0x006d] = 0xc3

    # strlen:

    # mov rax, 0x00
    contents[0x006e] = 0x48
    contents[0x006f] = 0xc7
    contents[0x0070] = 0xc0
    contents[0x0071] = 0x00
    contents[0x0072] = 0x00
    contents[0x0073] = 0x00
    contents[0x0074] = 0x00

    # .Lloop:

    # mov dl, byte ptr [rdi]
    contents[0x0075] = 0x8a
    contents[0x0076] = 0x17

    # cmp dl, 0x00
    contents[0x0077] = 0x80
    contents[0x0078] = 0xfa
    contents[0x0079] = 0x00

    # je .Lreturn
    contents[0x007a] = 0x74
    contents[0x007b] = 0x08

    # inc rax
    contents[0x007c] = 0x48
    contents[0x007d] = 0xff
    contents[0x007e] = 0xc0

    # inc rdi
    contents[0x007f] = 0x48
    contents[0x0080] = 0xff
    contents[0x0081] = 0xc7

    # jmp .Lloop
    contents[0x0082] = 0xeb
    contents[0x0083] = 0xf1

    # .Lreturn:

    # ret
    contents[0x0084] = 0xc3

    # >>>>>>>> DATA <<<<<<<<

    # newline

    # "\n"
    contents[0x0085] = 0x0a

    # >>>>>>>> SYMBOL TABLE <<<<<<<<

    # Null

    # st_name
    contents[0x0088] = 0x00
    contents[0x0089] = 0x00
    contents[0x008a] = 0x00
    contents[0x008b] = 0x00

    # st_info
    contents[0x008c] = 0x00

    # st_other
    contents[0x008d] = 0x00

    # st_shndx
    contents[0x008e] = 0x00
    contents[0x008f] = 0x00

    # st_value
    contents[0x0090] = 0x00
    contents[0x0091] = 0x00
    contents[0x0092] = 0x00
    contents[0x0093] = 0x00
    contents[0x0094] = 0x00
    contents[0x0095] = 0x00
    contents[0x0096] = 0x00
    contents[0x0097] = 0x00

    # st_size
    contents[0x0098] = 0x00
    contents[0x0099] = 0x00
    contents[0x009a] = 0x00
    contents[0x009b] = 0x00
    contents[0x009c] = 0x00
    contents[0x009d] = 0x00
    contents[0x009e] = 0x00
    contents[0x009f] = 0x00

    # ========================

    # .rodata

    # st_name
    contents[0x00a0] = 0x00
    contents[0x00a1] = 0x00
    contents[0x00a2] = 0x00
    contents[0x00a3] = 0x00

    # st_info
    contents[0x00a4] = 0x03

    # st_other
    contents[0x00a5] = 0x00

    # st_shndx
    contents[0x00a6] = 0x03
    contents[0x00a7] = 0x00

    # st_value
    contents[0x00a8] = 0x00
    contents[0x00a9] = 0x00
    contents[0x00aa] = 0x00
    contents[0x00ab] = 0x00
    contents[0x00ac] = 0x00
    contents[0x00ad] = 0x00
    contents[0x00ae] = 0x00
    contents[0x00af] = 0x00

    # st_size
    contents[0x00b0] = 0x00
    contents[0x00b1] = 0x00
    contents[0x00b2] = 0x00
    contents[0x00b3] = 0x00
    contents[0x00b4] = 0x00
    contents[0x00b5] = 0x00
    contents[0x00b6] = 0x00
    contents[0x00b7] = 0x00

    # ========================

    # newline

    # st_name
    contents[0x00b8] = 0x01
    contents[0x00b9] = 0x00
    contents[0x00ba] = 0x00
    contents[0x00bb] = 0x00

    # st_info
    contents[0x00bc] = 0x01

    # st_other
    contents[0x00bd] = 0x00

    # st_shndx
    contents[0x00be] = 0x03
    contents[0x00bf] = 0x00

    # st_value
    contents[0x00c0] = 0x00
    contents[0x00c1] = 0x00
    contents[0x00c2] = 0x00
    contents[0x00c3] = 0x00
    contents[0x00c4] = 0x00
    contents[0x00c5] = 0x00
    contents[0x00c6] = 0x00
    contents[0x00c7] = 0x00

    # st_size
    contents[0x00c8] = 0x01
    contents[0x00c9] = 0x00
    contents[0x00ca] = 0x00
    contents[0x00cb] = 0x00
    contents[0x00cc] = 0x00
    contents[0x00cd] = 0x00
    contents[0x00ce] = 0x00
    contents[0x00cf] = 0x00

    # ========================

    # println

    # st_name
    contents[0x00d0] = 0x09
    contents[0x00d1] = 0x00
    contents[0x00d2] = 0x00
    contents[0x00d3] = 0x00

    # st_info
    contents[0x00d4] = 0x12

    # st_other
    contents[0x00d5] = 0x00

    # st_shndx
    contents[0x00d6] = 0x01
    contents[0x00d7] = 0x00

    # st_value
    contents[0x00d8] = 0x00
    contents[0x00d9] = 0x00
    contents[0x00da] = 0x00
    contents[0x00db] = 0x00
    contents[0x00dc] = 0x00
    contents[0x00dd] = 0x00
    contents[0x00de] = 0x00
    contents[0x00df] = 0x00

    # st_size
    contents[0x00e0] = 0x2e
    contents[0x00e1] = 0x00
    contents[0x00e2] = 0x00
    contents[0x00e3] = 0x00
    contents[0x00e4] = 0x00
    contents[0x00e5] = 0x00
    contents[0x00e6] = 0x00
    contents[0x00e7] = 0x00

    # ========================

    # strlen

    # st_name
    contents[0x00e8] = 0x11
    contents[0x00e9] = 0x00
    contents[0x00ea] = 0x00
    contents[0x00eb] = 0x00

    # st_info
    contents[0x00ec] = 0x12

    # st_other
    contents[0x00ed] = 0x00

    # st_shndx
    contents[0x00ee] = 0x01
    contents[0x00ef] = 0x00

    # st_value
    contents[0x00f0] = 0x2e
    contents[0x00f1] = 0x00
    contents[0x00f2] = 0x00
    contents[0x00f3] = 0x00
    contents[0x00f4] = 0x00
    contents[0x00f5] = 0x00
    contents[0x00f6] = 0x00
    contents[0x00f7] = 0x00

    # st_size
    contents[0x00f8] = 0x17
    contents[0x00f9] = 0x00
    contents[0x00fa] = 0x00
    contents[0x00fb] = 0x00
    contents[0x00fc] = 0x00
    contents[0x00fd] = 0x00
    contents[0x00fe] = 0x00
    contents[0x00ff] = 0x00

    # >>>>>>>> STRING TABLE <<<<<<<<

    # "\0"
    contents[0x0100] = 0x00

    # "newline\0"
    contents[0x0101] = 0x6e
    contents[0x0102] = 0x65
    contents[0x0103] = 0x77
    contents[0x0104] = 0x6c
    contents[0x0105] = 0x69
    contents[0x0106] = 0x6e
    contents[0x0107] = 0x65
    contents[0x0108] = 0x00

    # "println\0"
    contents[0x0109] = 0x70
    contents[0x010a] = 0x72
    contents[0x010b] = 0x69
    contents[0x010c] = 0x6e
    contents[0x010d] = 0x74
    contents[0x010e] = 0x6c
    contents[0x010f] = 0x6e
    contents[0x0110] = 0x00

    # "strlen\0"
    contents[0x0111] = 0x73
    contents[0x0112] = 0x74
    contents[0x0113] = 0x72
    contents[0x0114] = 0x6c
    contents[0x0115] = 0x65
    contents[0x0116] = 0x6e
    contents[0x0117] = 0x00


    # >>>>>>>> RELOCATION ENTRIES <<<<<<<<

    # 0x0020: .rodata - 0x04

    # r_offset
    contents[0x0118] = 0x20
    contents[0x0119] = 0x00
    contents[0x011a] = 0x00
    contents[0x011b] = 0x00
    contents[0x011c] = 0x00
    contents[0x011d] = 0x00
    contents[0x011e] = 0x00
    contents[0x011f] = 0x00

    # r_info
    contents[0x0120] = 0x02
    contents[0x0121] = 0x00
    contents[0x0122] = 0x00
    contents[0x0123] = 0x00
    contents[0x0124] = 0x01
    contents[0x0125] = 0x00
    contents[0x0126] = 0x00
    contents[0x0127] = 0x00

    # r_addend
    contents[0x0128] = 0xfc
    contents[0x0129] = 0xff
    contents[0x012a] = 0xff
    contents[0x012b] = 0xff
    contents[0x012c] = 0xff
    contents[0x012d] = 0xff
    contents[0x012e] = 0xff
    contents[0x012f] = 0xff

    # >>>>>>>> SECTION HEADER STRING TABLE <<<<<<<<

    # "\0"
    contents[0x0130] = 0x00

    # ".text\0"
    contents[0x0131] = 0x2e
    contents[0x0132] = 0x74
    contents[0x0133] = 0x65
    contents[0x0134] = 0x78
    contents[0x0135] = 0x74
    contents[0x0136] = 0x00

    # ".rela.text\0"
    contents[0x0137] = 0x2e
    contents[0x0138] = 0x72
    contents[0x0139] = 0x65
    contents[0x013a] = 0x6c
    contents[0x013b] = 0x61
    contents[0x013c] = 0x2e
    contents[0x013d] = 0x74
    contents[0x013e] = 0x65
    contents[0x013f] = 0x78
    contents[0x0140] = 0x74
    contents[0x0141] = 0x00

    # ".rodata\0"
    contents[0x0142] = 0x2e
    contents[0x0143] = 0x72
    contents[0x0144] = 0x6f
    contents[0x0145] = 0x64
    contents[0x0146] = 0x61
    contents[0x0147] = 0x74
    contents[0x0148] = 0x61
    contents[0x0149] = 0x00

    # ".symtab\0"
    contents[0x014a] = 0x2e
    contents[0x014b] = 0x73
    contents[0x014c] = 0x79
    contents[0x014d] = 0x6d
    contents[0x014e] = 0x74
    contents[0x014f] = 0x61
    contents[0x0150] = 0x62
    contents[0x0151] = 0x00

    # ".strtab\0"
    contents[0x0152] = 0x2e
    contents[0x0153] = 0x73
    contents[0x0154] = 0x74
    contents[0x0155] = 0x72
    contents[0x0156] = 0x74
    contents[0x0157] = 0x61
    contents[0x0158] = 0x62
    contents[0x0159] = 0x00

    # ".shstrtab\0"
    contents[0x015a] = 0x2e
    contents[0x015b] = 0x73
    contents[0x015c] = 0x68
    contents[0x015d] = 0x73
    contents[0x015e] = 0x74
    contents[0x015f] = 0x72
    contents[0x0160] = 0x74
    contents[0x0161] = 0x61
    contents[0x0162] = 0x62
    contents[0x0163] = 0x00

    # >>>>>>>>>> SECTION HEADER TABLE <<<<<<<<<<

    # Null

    # sh_name
    contents[0x0168] = 0x00
    contents[0x0169] = 0x00
    contents[0x016a] = 0x00
    contents[0x016b] = 0x00

    # sh_type
    contents[0x016c] = 0x00
    contents[0x016d] = 0x00
    contents[0x016e] = 0x00
    contents[0x016f] = 0x00

    # sh_flags
    contents[0x0170] = 0x00
    contents[0x0171] = 0x00
    contents[0x0172] = 0x00
    contents[0x0173] = 0x00
    contents[0x0174] = 0x00
    contents[0x0175] = 0x00
    contents[0x0176] = 0x00
    contents[0x0177] = 0x00

    # sh_addr
    contents[0x0178] = 0x00
    contents[0x0179] = 0x00
    contents[0x017a] = 0x00
    contents[0x017b] = 0x00
    contents[0x017c] = 0x00
    contents[0x017d] = 0x00
    contents[0x017e] = 0x00
    contents[0x017f] = 0x00

    # sh_offset
    contents[0x0180] = 0x00
    contents[0x0181] = 0x00
    contents[0x0182] = 0x00
    contents[0x0183] = 0x00
    contents[0x0184] = 0x00
    contents[0x0185] = 0x00
    contents[0x0186] = 0x00
    contents[0x0187] = 0x00

    # sh_size
    contents[0x0188] = 0x00
    contents[0x0189] = 0x00
    contents[0x018a] = 0x00
    contents[0x018b] = 0x00
    contents[0x018c] = 0x00
    contents[0x018d] = 0x00
    contents[0x018e] = 0x00
    contents[0x018f] = 0x00

    # sh_link
    contents[0x0190] = 0x00
    contents[0x0191] = 0x00
    contents[0x0192] = 0x00
    contents[0x0193] = 0x00

    # sh_info
    contents[0x0194] = 0x00
    contents[0x0195] = 0x00
    contents[0x0196] = 0x00
    contents[0x0197] = 0x00

    # sh_addralign
    contents[0x0198] = 0x00
    contents[0x0199] = 0x00
    contents[0x019a] = 0x00
    contents[0x019b] = 0x00
    contents[0x019c] = 0x00
    contents[0x019d] = 0x00
    contents[0x019e] = 0x00
    contents[0x019f] = 0x00

    # sh_entsize
    contents[0x01a0] = 0x00
    contents[0x01a1] = 0x00
    contents[0x01a2] = 0x00
    contents[0x01a3] = 0x00
    contents[0x01a4] = 0x00
    contents[0x01a5] = 0x00
    contents[0x01a6] = 0x00
    contents[0x01a7] = 0x00

    # ========================

    # .text

    # sh_name
    contents[0x01a8] = 0x01
    contents[0x01a9] = 0x00
    contents[0x01aa] = 0x00
    contents[0x01ab] = 0x00

    # sh_type
    contents[0x01ac] = 0x01
    contents[0x01ad] = 0x00
    contents[0x01ae] = 0x00
    contents[0x01af] = 0x00

    # sh_flags
    contents[0x01b0] = 0x06
    contents[0x01b1] = 0x00
    contents[0x01b2] = 0x00
    contents[0x01b3] = 0x00
    contents[0x01b4] = 0x00
    contents[0x01b5] = 0x00
    contents[0x01b6] = 0x00
    contents[0x01b7] = 0x00

    # sh_addr
    contents[0x01b8] = 0x00
    contents[0x01b9] = 0x00
    contents[0x01ba] = 0x00
    contents[0x01bb] = 0x00
    contents[0x01bc] = 0x00
    contents[0x01bd] = 0x00
    contents[0x01be] = 0x00
    contents[0x01bf] = 0x00

    # sh_offset
    contents[0x01c0] = 0x40
    contents[0x01c1] = 0x00
    contents[0x01c2] = 0x00
    contents[0x01c3] = 0x00
    contents[0x01c4] = 0x00
    contents[0x01c5] = 0x00
    contents[0x01c6] = 0x00
    contents[0x01c7] = 0x00

    # sh_size
    contents[0x01c8] = 0x45
    contents[0x01c9] = 0x00
    contents[0x01ca] = 0x00
    contents[0x01cb] = 0x00
    contents[0x01cc] = 0x00
    contents[0x01cd] = 0x00
    contents[0x01ce] = 0x00
    contents[0x01cf] = 0x00

    # sh_link
    contents[0x01d0] = 0x00
    contents[0x01d1] = 0x00
    contents[0x01d2] = 0x00
    contents[0x01d3] = 0x00

    # sh_info
    contents[0x01d4] = 0x00
    contents[0x01d5] = 0x00
    contents[0x01d6] = 0x00
    contents[0x01d7] = 0x00

    # sh_addralign
    contents[0x01d8] = 0x01
    contents[0x01d9] = 0x00
    contents[0x01da] = 0x00
    contents[0x01db] = 0x00
    contents[0x01dc] = 0x00
    contents[0x01dd] = 0x00
    contents[0x01de] = 0x00
    contents[0x01df] = 0x00

    # sh_entsize
    contents[0x01e0] = 0x00
    contents[0x01e1] = 0x00
    contents[0x01e2] = 0x00
    contents[0x01e3] = 0x00
    contents[0x01e4] = 0x00
    contents[0x01e5] = 0x00
    contents[0x01e6] = 0x00
    contents[0x01e7] = 0x00

    # ========================

    # .rela.text

    # sh_name
    contents[0x01e8] = 0x07
    contents[0x01e9] = 0x00
    contents[0x01ea] = 0x00
    contents[0x01eb] = 0x00

    # sh_type
    contents[0x01ec] = 0x04
    contents[0x01ed] = 0x00
    contents[0x01ee] = 0x00
    contents[0x01ef] = 0x00

    # sh_flags
    contents[0x01f0] = 0x40
    contents[0x01f1] = 0x00
    contents[0x01f2] = 0x00
    contents[0x01f3] = 0x00
    contents[0x01f4] = 0x00
    contents[0x01f5] = 0x00
    contents[0x01f6] = 0x00
    contents[0x01f7] = 0x00

    # sh_addr
    contents[0x01f8] = 0x00
    contents[0x01f9] = 0x00
    contents[0x01fa] = 0x00
    contents[0x01fb] = 0x00
    contents[0x01fc] = 0x00
    contents[0x01fd] = 0x00
    contents[0x01fe] = 0x00
    contents[0x01ff] = 0x00

    # sh_offset
    contents[0x0200] = 0x18
    contents[0x0201] = 0x01
    contents[0x0202] = 0x00
    contents[0x0203] = 0x00
    contents[0x0204] = 0x00
    contents[0x0205] = 0x00
    contents[0x0206] = 0x00
    contents[0x0207] = 0x00

    # sh_size
    contents[0x0208] = 0x18
    contents[0x0209] = 0x00
    contents[0x020a] = 0x00
    contents[0x020b] = 0x00
    contents[0x020c] = 0x00
    contents[0x020d] = 0x00
    contents[0x020e] = 0x00
    contents[0x020f] = 0x00

    # sh_link
    contents[0x0210] = 0x04
    contents[0x0211] = 0x00
    contents[0x0212] = 0x00
    contents[0x0213] = 0x00

    # sh_info
    contents[0x0214] = 0x01
    contents[0x0215] = 0x00
    contents[0x0216] = 0x00
    contents[0x0217] = 0x00

    # sh_addralign
    contents[0x0218] = 0x08
    contents[0x0219] = 0x00
    contents[0x021a] = 0x00
    contents[0x021b] = 0x00
    contents[0x021c] = 0x00
    contents[0x021d] = 0x00
    contents[0x021e] = 0x00
    contents[0x021f] = 0x00

    # sh_entsize
    contents[0x0220] = 0x18
    contents[0x0221] = 0x00
    contents[0x0222] = 0x00
    contents[0x0223] = 0x00
    contents[0x0224] = 0x00
    contents[0x0225] = 0x00
    contents[0x0226] = 0x00
    contents[0x0227] = 0x00

    # ========================

    # .rodata

    # sh_name
    contents[0x0228] = 0x12
    contents[0x0229] = 0x00
    contents[0x022a] = 0x00
    contents[0x022b] = 0x00

    # sh_type
    contents[0x022c] = 0x01
    contents[0x022d] = 0x00
    contents[0x022e] = 0x00
    contents[0x022f] = 0x00

    # sh_flags
    contents[0x0230] = 0x02
    contents[0x0231] = 0x00
    contents[0x0232] = 0x00
    contents[0x0233] = 0x00
    contents[0x0234] = 0x00
    contents[0x0235] = 0x00
    contents[0x0236] = 0x00
    contents[0x0237] = 0x00

    # sh_addr
    contents[0x0238] = 0x00
    contents[0x0239] = 0x00
    contents[0x023a] = 0x00
    contents[0x023b] = 0x00
    contents[0x023c] = 0x00
    contents[0x023d] = 0x00
    contents[0x023e] = 0x00
    contents[0x023f] = 0x00

    # sh_offset
    contents[0x0240] = 0x85
    contents[0x0241] = 0x00
    contents[0x0242] = 0x00
    contents[0x0243] = 0x00
    contents[0x0244] = 0x00
    contents[0x0245] = 0x00
    contents[0x0246] = 0x00
    contents[0x0247] = 0x00

    # sh_size
    contents[0x0248] = 0x01
    contents[0x0249] = 0x00
    contents[0x024a] = 0x00
    contents[0x024b] = 0x00
    contents[0x024c] = 0x00
    contents[0x024d] = 0x00
    contents[0x024e] = 0x00
    contents[0x024f] = 0x00

    # sh_link
    contents[0x0250] = 0x00
    contents[0x0251] = 0x00
    contents[0x0252] = 0x00
    contents[0x0253] = 0x00

    # sh_info
    contents[0x0254] = 0x00
    contents[0x0255] = 0x00
    contents[0x0256] = 0x00
    contents[0x0257] = 0x00

    # sh_addralign
    contents[0x0258] = 0x01
    contents[0x0259] = 0x00
    contents[0x025a] = 0x00
    contents[0x025b] = 0x00
    contents[0x025c] = 0x00
    contents[0x025d] = 0x00
    contents[0x025e] = 0x00
    contents[0x025f] = 0x00

    # sh_entsize
    contents[0x0260] = 0x00
    contents[0x0261] = 0x00
    contents[0x0262] = 0x00
    contents[0x0263] = 0x00
    contents[0x0264] = 0x00
    contents[0x0265] = 0x00
    contents[0x0266] = 0x00
    contents[0x0267] = 0x00

    # ========================

    # .symtab

    # sh_name
    contents[0x0268] = 0x1a
    contents[0x0269] = 0x00
    contents[0x026a] = 0x00
    contents[0x026b] = 0x00

    # sh_type
    contents[0x026c] = 0x02
    contents[0x026d] = 0x00
    contents[0x026e] = 0x00
    contents[0x026f] = 0x00

    # sh_flags
    contents[0x0270] = 0x00
    contents[0x0271] = 0x00
    contents[0x0272] = 0x00
    contents[0x0273] = 0x00
    contents[0x0274] = 0x00
    contents[0x0275] = 0x00
    contents[0x0276] = 0x00
    contents[0x0277] = 0x00

    # sh_addr
    contents[0x0278] = 0x00
    contents[0x0279] = 0x00
    contents[0x027a] = 0x00
    contents[0x027b] = 0x00
    contents[0x027c] = 0x00
    contents[0x027d] = 0x00
    contents[0x027e] = 0x00
    contents[0x027f] = 0x00

    # sh_offset
    contents[0x0280] = 0x88
    contents[0x0281] = 0x00
    contents[0x0282] = 0x00
    contents[0x0283] = 0x00
    contents[0x0284] = 0x00
    contents[0x0285] = 0x00
    contents[0x0286] = 0x00
    contents[0x0287] = 0x00

    # sh_size
    contents[0x0288] = 0x78
    contents[0x0289] = 0x00
    contents[0x028a] = 0x00
    contents[0x028b] = 0x00
    contents[0x028c] = 0x00
    contents[0x028d] = 0x00
    contents[0x028e] = 0x00
    contents[0x028f] = 0x00

    # sh_link
    contents[0x0290] = 0x05
    contents[0x0291] = 0x00
    contents[0x0292] = 0x00
    contents[0x0293] = 0x00

    # sh_info
    contents[0x0294] = 0x03
    contents[0x0295] = 0x00
    contents[0x0296] = 0x00
    contents[0x0297] = 0x00

    # sh_addralign
    contents[0x0298] = 0x08
    contents[0x0299] = 0x00
    contents[0x029a] = 0x00
    contents[0x029b] = 0x00
    contents[0x029c] = 0x00
    contents[0x029d] = 0x00
    contents[0x029e] = 0x00
    contents[0x029f] = 0x00

    # sh_entsize
    contents[0x02a0] = 0x18
    contents[0x02a1] = 0x00
    contents[0x02a2] = 0x00
    contents[0x02a3] = 0x00
    contents[0x02a4] = 0x00
    contents[0x02a5] = 0x00
    contents[0x02a6] = 0x00
    contents[0x02a7] = 0x00

    # ========================

    # .strtab

    # sh_name
    contents[0x02a8] = 0x22
    contents[0x02a9] = 0x00
    contents[0x02aa] = 0x00
    contents[0x02ab] = 0x00

    # sh_type
    contents[0x02ac] = 0x03
    contents[0x02ad] = 0x00
    contents[0x02ae] = 0x00
    contents[0x02af] = 0x00

    # sh_flags
    contents[0x02b0] = 0x00
    contents[0x02b1] = 0x00
    contents[0x02b2] = 0x00
    contents[0x02b3] = 0x00
    contents[0x02b4] = 0x00
    contents[0x02b5] = 0x00
    contents[0x02b6] = 0x00
    contents[0x02b7] = 0x00

    # sh_addr
    contents[0x02b8] = 0x00
    contents[0x02b9] = 0x00
    contents[0x02ba] = 0x00
    contents[0x02bb] = 0x00
    contents[0x02bc] = 0x00
    contents[0x02bd] = 0x00
    contents[0x02be] = 0x00
    contents[0x02bf] = 0x00

    # sh_offset
    contents[0x02c0] = 0x00
    contents[0x02c1] = 0x01
    contents[0x02c2] = 0x00
    contents[0x02c3] = 0x00
    contents[0x02c4] = 0x00
    contents[0x02c5] = 0x00
    contents[0x02c6] = 0x00
    contents[0x02c7] = 0x00

    # sh_size
    contents[0x02c8] = 0x18
    contents[0x02c9] = 0x00
    contents[0x02ca] = 0x00
    contents[0x02cb] = 0x00
    contents[0x02cc] = 0x00
    contents[0x02cd] = 0x00
    contents[0x02ce] = 0x00
    contents[0x02cf] = 0x00

    # sh_link
    contents[0x02d0] = 0x00
    contents[0x02d1] = 0x00
    contents[0x02d2] = 0x00
    contents[0x02d3] = 0x00

    # sh_info
    contents[0x02d4] = 0x00
    contents[0x02d5] = 0x00
    contents[0x02d6] = 0x00
    contents[0x02d7] = 0x00

    # sh_addralign
    contents[0x02d8] = 0x01
    contents[0x02d9] = 0x00
    contents[0x02da] = 0x00
    contents[0x02db] = 0x00
    contents[0x02dc] = 0x00
    contents[0x02dd] = 0x00
    contents[0x02de] = 0x00
    contents[0x02df] = 0x00

    # sh_entsize
    contents[0x02e0] = 0x00
    contents[0x02e1] = 0x00
    contents[0x02e2] = 0x00
    contents[0x02e3] = 0x00
    contents[0x02e4] = 0x00
    contents[0x02e5] = 0x00
    contents[0x02e6] = 0x00
    contents[0x02e7] = 0x00

    # ========================

    # .shstrtab

    # sh_name
    contents[0x02e8] = 0x2a
    contents[0x02e9] = 0x00
    contents[0x02ea] = 0x00
    contents[0x02eb] = 0x00

    # sh_type
    contents[0x02ec] = 0x03
    contents[0x02ed] = 0x00
    contents[0x02ee] = 0x00
    contents[0x02ef] = 0x00

    # sh_flags
    contents[0x02f0] = 0x00
    contents[0x02f1] = 0x00
    contents[0x02f2] = 0x00
    contents[0x02f3] = 0x00
    contents[0x02f4] = 0x00
    contents[0x02f5] = 0x00
    contents[0x02f6] = 0x00
    contents[0x02f7] = 0x00

    # sh_addr
    contents[0x02f8] = 0x00
    contents[0x02f9] = 0x00
    contents[0x02fa] = 0x00
    contents[0x02fb] = 0x00
    contents[0x02fc] = 0x00
    contents[0x02fd] = 0x00
    contents[0x02fe] = 0x00
    contents[0x02ff] = 0x00

    # sh_offset
    contents[0x0300] = 0x30
    contents[0x0301] = 0x01
    contents[0x0302] = 0x00
    contents[0x0303] = 0x00
    contents[0x0304] = 0x00
    contents[0x0305] = 0x00
    contents[0x0306] = 0x00
    contents[0x0307] = 0x00

    # sh_size
    contents[0x0308] = 0x34
    contents[0x0309] = 0x00
    contents[0x030a] = 0x00
    contents[0x030b] = 0x00
    contents[0x030c] = 0x00
    contents[0x030d] = 0x00
    contents[0x030e] = 0x00
    contents[0x030f] = 0x00

    # sh_link
    contents[0x0310] = 0x00
    contents[0x0311] = 0x00
    contents[0x0312] = 0x00
    contents[0x0313] = 0x00

    # sh_info
    contents[0x0314] = 0x00
    contents[0x0315] = 0x00
    contents[0x0316] = 0x00
    contents[0x0317] = 0x00

    # sh_addralign
    contents[0x0318] = 0x01
    contents[0x0319] = 0x00
    contents[0x031a] = 0x00
    contents[0x031b] = 0x00
    contents[0x031c] = 0x00
    contents[0x031d] = 0x00
    contents[0x031e] = 0x00
    contents[0x031f] = 0x00

    # sh_entsize
    contents[0x0320] = 0x00
    contents[0x0321] = 0x00
    contents[0x0322] = 0x00
    contents[0x0323] = 0x00
    contents[0x0324] = 0x00
    contents[0x0325] = 0x00
    contents[0x0326] = 0x00
    contents[0x0327] = 0x00

    os.makedirs("bin", exist_ok=True)
    with open("bin/rel-println.o", "wb") as file:
        file.write(contents)


if __name__ == "__main__":
    main()
