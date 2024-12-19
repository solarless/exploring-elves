import os


def main() -> None:
    contents = bytearray(0x5a)

    # >>>>>>>> ELF HEADER <<<<<<<<

    # e_ident[EI_MAG0..=EI_MAG3]
    contents[0x00] = 0x7f
    contents[0x01] = 0x45
    contents[0x02] = 0x4c
    contents[0x03] = 0x46

    # e_ident[EI_CLASS]
    contents[0x04] = 0x01

    # e_ident[EI_DATA]
    contents[0x05] = 0x01

    # e_ident[EI_VERSION]
    contents[0x06] = 0x01

    # e_ident[EI_OSABI]
    contents[0x07] = 0x00

    # e_ident[EI_ABIVERSION]
    contents[0x08] = 0x00

    # e_ident[EI_PAD..EI_NIDENT]
    contents[0x09] = 0x00
    contents[0x0a] = 0x00
    contents[0x0b] = 0x00
    contents[0x0c] = 0x00
    contents[0x0d] = 0x00
    contents[0x0e] = 0x00
    contents[0x0f] = 0x00

    # e_type
    contents[0x10] = 0x02
    contents[0x11] = 0x00

    # e_machine
    contents[0x12] = 0x03
    contents[0x13] = 0x00

    # e_version
    contents[0x14] = 0x01
    contents[0x15] = 0x00
    contents[0x16] = 0x00
    contents[0x17] = 0x00

    # e_entry
    contents[0x18] = 0x54
    contents[0x19] = 0x80
    contents[0x1a] = 0x04
    contents[0x1b] = 0x08

    # e_phoff
    contents[0x1c] = 0x34
    contents[0x1d] = 0x00
    contents[0x1e] = 0x00
    contents[0x1f] = 0x00

    # e_shoff
    contents[0x20] = 0x00
    contents[0x21] = 0x00
    contents[0x22] = 0x00
    contents[0x23] = 0x00

    # e_flags
    contents[0x24] = 0x00
    contents[0x25] = 0x00
    contents[0x26] = 0x00
    contents[0x27] = 0x00

    # e_ehsize
    contents[0x28] = 0x34
    contents[0x29] = 0x00

    # e_phentsize
    contents[0x2a] = 0x20
    contents[0x2b] = 0x00

    # e_phnum
    contents[0x2c] = 0x01
    contents[0x2d] = 0x00

    # e_shentsize
    contents[0x2e] = 0x00
    contents[0x2f] = 0x00

    # e_shnum
    contents[0x30] = 0x00
    contents[0x31] = 0x00

    # e_shstrndx
    contents[0x32] = 0x00
    contents[0x33] = 0x00

    # >>>>>>>> PROGRAM HEADER TABLE <<<<<<<<

    # p_type
    contents[0x34] = 0x01
    contents[0x35] = 0x00
    contents[0x36] = 0x00
    contents[0x37] = 0x00

    # p_offset
    contents[0x38] = 0x54
    contents[0x39] = 0x00
    contents[0x3a] = 0x00
    contents[0x3b] = 0x00

    # p_vaddr
    contents[0x3c] = 0x54
    contents[0x3d] = 0x80
    contents[0x3e] = 0x04
    contents[0x3f] = 0x08

    # p_paddr
    contents[0x40] = 0x00
    contents[0x41] = 0x00
    contents[0x42] = 0x00
    contents[0x43] = 0x00

    # p_filesz
    contents[0x44] = 0x06
    contents[0x45] = 0x00
    contents[0x46] = 0x00
    contents[0x47] = 0x00

    # p_memsz
    contents[0x48] = 0x06
    contents[0x49] = 0x00
    contents[0x4a] = 0x00
    contents[0x4b] = 0x00

    # p_flags
    contents[0x4c] = 0x05
    contents[0x4d] = 0x00
    contents[0x4e] = 0x00
    contents[0x4f] = 0x00

    # p_align
    contents[0x50] = 0x01
    contents[0x51] = 0x00
    contents[0x52] = 0x00
    contents[0x53] = 0x00

    # >>>>>>>> CODE <<<<<<<<

    # mov al, 0x01
    contents[0x54] = 0xb0
    contents[0x55] = 0x01

    # mov bl, 0x00
    contents[0x56] = 0xb3
    contents[0x57] = 0x00

    # inc 0x80
    contents[0x58] = 0xcd
    contents[0x59] = 0x80

    os.makedirs("bin", exist_ok=True)
    with open("bin/exec-tiny", "wb") as file:
        file.write(contents)

    os.chmod("bin/exec-tiny", 0o755)


if __name__ == "__main__":
    main()