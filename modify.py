"""
Usage: python3 modify.py $apkfile.apk $modification_folder/
"""
###############################################################################

import subprocess
import sys
from time import sleep
import os
import struct
from enum import Enum
from math import (
    floor,
    sin,
)
from bitarray import bitarray

class Buffer(Enum):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

class H(object):
    _string = None
    _buffers = {
        Buffer.A: None,
        Buffer.B: None,
        Buffer.C: None,
        Buffer.D: None,
    }
    @classmethod
    def f(cls, string):
        cls._string = string
        preprocessed_bit_array = cls._step_2(cls._step_1())
        cls._step_3()
        cls._step_4(preprocessed_bit_array)
        return cls._step_5()
    @classmethod
    def _step_1(cls):
        bit_array = bitarray(endian="big")
        bit_array.frombytes(cls._string.encode("utf-8"))
        bit_array.append(1)
        while len(bit_array) % 512 != 448:
            bit_array.append(0)
        return bitarray(bit_array, endian="little")
    @classmethod
    def _step_2(cls, step_1_result):
        length = (len(cls._string) * 8) % pow(2, 64)
        length_bit_array = bitarray(endian="little")
        length_bit_array.frombytes(struct.pack("<Q", length))
        result = step_1_result.copy()
        result.extend(length_bit_array)
        return result
    @classmethod
    def _step_3(cls):
        for buffer_type in cls._buffers.keys():
            cls._buffers[buffer_type] = buffer_type.value
    @classmethod
    def _step_4(cls, step_2_result):
        F = lambda x, y, z: (x & y) | (~x & z)
        G = lambda x, y, z: (x & z) | (y & ~z)
        H = lambda x, y, z: x ^ y ^ z
        I = lambda x, y, z: y ^ (x | ~z)
        rotate_left = lambda x, n: (x << n) | (x >> (32 - n))
        modular_add = lambda a, b: (a + b) % pow(2, 32)
        T = [floor(pow(2, 32) * abs(sin(i + 1))) for i in range(64)]
        N = len(step_2_result) // 32
        for chunk_index in range(N // 16):
            start = chunk_index * 512
            X = [step_2_result[start + (x * 32) : start + (x * 32) + 32] for x in range(16)]
            X = [int.from_bytes(word.tobytes(), byteorder="little") for word in X]
            A = cls._buffers[Buffer.A]
            B = cls._buffers[Buffer.B]
            C = cls._buffers[Buffer.C]
            D = cls._buffers[Buffer.D]
            for i in range(4 * 16):
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    temp = F(B, C, D)
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    temp = G(B, C, D)
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    temp = H(B, C, D)
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    temp = I(B, C, D)
                temp = modular_add(temp, X[k])
                temp = modular_add(temp, T[i])
                temp = modular_add(temp, A)
                temp = rotate_left(temp, s[i % 4])
                temp = modular_add(temp, B)
                A = D
                D = C
                C = B
                B = temp
            cls._buffers[Buffer.A] = modular_add(cls._buffers[Buffer.A], A)
            cls._buffers[Buffer.B] = modular_add(cls._buffers[Buffer.B], B)
            cls._buffers[Buffer.C] = modular_add(cls._buffers[Buffer.C], C)
            cls._buffers[Buffer.D] = modular_add(cls._buffers[Buffer.D], D)
    @classmethod
    def _step_5(cls):
        A = struct.unpack("<I", struct.pack(">I", cls._buffers[Buffer.A]))[0]
        B = struct.unpack("<I", struct.pack(">I", cls._buffers[Buffer.B]))[0]
        C = struct.unpack("<I", struct.pack(">I", cls._buffers[Buffer.C]))[0]
        D = struct.unpack("<I", struct.pack(">I", cls._buffers[Buffer.D]))[0]
        return f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}"



# subprocess.call("run shell script here", shell=True)

def system(command: str, shell: str="/bin/bash"):
    subprocess.call(command, shell=True, executable=shell)

def coloredEcho(message: str, color: str):
    system("echo -e ${%s}%s${COLOREND}" % (color, message))


STEPS = [
    "Decode APK file",
    "Modify files in \"assets/\"",
    "Rebuild APK file",
    "Zipalign APK file",
    "Generate signature key, please set password to 123456 !!!",
    "Sign APK file"
]

def startSTEP(currentSTEP: int):
    coloredEcho("STEP {_step_}: {_stepMessage_}".format(
        _step_=currentSTEP,
        _stepMessage_=STEPS[currentSTEP - 1]
    ), "BG_BLUE")



###############################################################################

if __name__ == "__main__":
    system('export COLOREND="\x1b[0m"')
    system('export BLACK="\x1b[30m"')
    system('export RED="\x1b[31m"')
    system('export GREEN="\x1b[32m"')
    system('export YELLOW="\x1b[33m"')
    system('export BLUE="\x1b[34m"')
    system('export PURPLE="\x1b[35m"')
    system('export CYAN="\x1b[36m"')
    system('export WHITE="\x1b[37m"')
    system('export GRAY="\x1b[90m"')
    system('export BG_BLACK="\x1b[40m"')
    system('export BG_RED="\x1b[41m"')
    system('export BG_GREEN="\x1b[42m"')
    system('export BG_YELLOW="\x1b[43m"')
    system('export BG_BLUE="\x1b[44m"')
    system('export BG_PURPLE="\x1b[45m"')
    system('export BG_CYAN="\x1b[46m"')
    system('export BG_WHITE="\x1b[47m"')
    system('export BG_GRAY="\x1b[100m"')

    if len(sys.argv) < 3:
        coloredEcho("Please specify the name of apk flie you want to modify.", "RED")
        sys.exit() 

    apkFile = sys.argv[1]
    apkName = apkFile[:apkFile.find(".apk")]
    apkFileBuilded = "{}-builded.apk".format(apkName)
    apkFileAligned = "{}-aligned.apk".format(apkName)
    apkFileSigned = "{}-modified.apk".format(apkName)
    modificationFolder = sys.argv[2]
    stepCounter = 0
    publicVersion = len(sys.argv) > 3


    if not os.path.isfile(apkFile):
        coloredEcho("APK file does not exist.", "RED")
        sys.exit()

    #######################################################################
    # STEP 1: Decode APK file

    stepCounter += 1
    startSTEP(stepCounter)

    system("apktool d -f {}".format(apkFile), shell="/bin/fish")

    #######################################################################
    # STEP 2: Modify files in "assets/"

    stepCounter += 1
    startSTEP(stepCounter)

    for (currentPath, dirs, files) in os.walk(modificationFolder):
        for file in files:
            d = currentPath[currentPath.find("/"):]
            if ((H.f(d[:4]) == "dad344c5fc83cc325c3b7105da28ddfb"
                  and H.f(file[:5]) == "606156695511e4635e67f22add757948") or
                (H.f(d[:7]) == "571d4da7d9744abc1d11d0fdfea45317") or
                (H.f(d) == "c3012d1ca6b6e59263d6ec9d3a55c30f")):
                continue

            fileInMod = currentPath + "/" + file
            fileInAPK = apkName + "/assets" + fileInMod[fileInMod.find("/"):]

            if publicVersion and (
                d == "/Fonts" or
                file.startswith("shutter") or
                d == "/img/grade" or
                d == "/layouts"
            ):
                coloredEcho("[Public Version] Skipping {}".format(fileInMod), "YELLOW")
                continue

            if os.path.isfile(fileInAPK):
                coloredEcho("Modified file: {}".format(fileInAPK), "GRAY")
                system("cp {} {}".format(fileInMod, fileInAPK))

    #######################################################################
    # STEP 3: Rebuild APK file

    stepCounter += 1
    startSTEP(stepCounter)

    system("apktool b --use-aapt2 {_apkName_} -o {_apkFileBuilded_}".format(
        _apkName_=apkName,
        _apkFileBuilded_=apkFileBuilded
    ), shell="/bin/fish")

    #######################################################################
    # STEP 4: Zipalign APK file
    
    stepCounter += 1
    startSTEP(stepCounter)

    system("zipalign -v -p 4 {_apkFileBuilded_} {_apkFileAligned_}".format(
        _apkFileBuilded_=apkFileBuilded,
        _apkFileAligned_=apkFileAligned
    ), shell="/bin/fish")

    #######################################################################
    # STEP 5: Generate signature key, please set password to 123456 !!!
    
    stepCounter += 1
    startSTEP(stepCounter)

    system("keytool -genkey -v "
        "-keystore signature-key.jks "
        "-keyalg RSA -keysize 2048 -validity 10000 -alias my-alias",
            shell="/bin/fish")

    # STEP 6: Sign on APK file

    stepCounter += 1
    startSTEP(stepCounter)

    system("apksigner sign "
        "--ks signature-key.jks "
        "--ks-pass pass:123456 "
        "--out {_apkFileSigned_} {_apkFileAligned_}".format(
           _apkFileSigned_=apkFileSigned,
           _apkFileAligned_=apkFileAligned
    ), shell="/bin/fish")


    #######################################################################

    coloredEcho("Successfully modified your Arcaea APK File.", "GREEN")
    
    system("rm {_apkFileBuilded_}".format(_apkFileBuilded_=apkFileBuilded))
    system("rm {_apkFileAligned_}".format(_apkFileAligned_=apkFileAligned))
    system("rm signature-key.jks")
    system("rm {}.idsig".format(apkFileSigned))




