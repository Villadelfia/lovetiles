import zlib
import base64
import struct

decoded1 = base64.b64decode("eJyTYmBg4CUTSwMxNxD7kYm5oPp9ycSj+kf1SwIxJ5TPDsQcJGAJIAYAsckszg==")
decompressed1 = zlib.decompress(decoded1)
decoded2 = base64.b64decode("eJxjYBgFowACnIHYBYhdieSjA38gDgDiQCL5yEAZiKOBOAaIY6FihPjIQB+3t/ACAC2zCMM=")
decompressed2 = zlib.decompress(decoded2)
decoded3 = base64.b64decode("eJxjYBgFo2DkAgADAAAB")
decompressed3 = zlib.decompress(decoded3)
decoded4 = base64.b64decode("eJxjZGBgYKQQkwtG9Y/qp4Z+Rix8YjEAUTAANA==")
decompressed4 = zlib.decompress(decoded4)

length = len(decompressed1)/4
fmt = 'i'*length
output1 = struct.unpack(fmt, decompressed1)

length = len(decompressed2)/4
fmt = 'i'*length
output2 = struct.unpack(fmt, decompressed2)

length = len(decompressed3)/4
fmt = 'i'*length
output3 = struct.unpack(fmt, decompressed3)

length = len(decompressed4)/4
fmt = 'i'*length
output4 = struct.unpack(fmt, decompressed4)

strout = """map[0] = Room.new{
    -- background
    layer0 =
    {   {"""

i = 0
j = 0
for k in output1:
    i += 1
    if i % 16 == 0:
        j += 1
        strout = strout + str(k).rjust(4)
        if j != 12:
            strout = strout + "},\n        {"
        else:
            strout = strout + "}},\n"
    else:
        strout = strout + str(k).rjust(4) + ", "

strout = strout + """
    -- middle layer
    layer1 =
    {   {"""

i = 0
j = 0
for k in output2:
    i += 1
    if i % 16 == 0:
        j += 1
        strout = strout + str(k).rjust(4)
        if j != 12:
            strout = strout + "},\n        {"
        else:
            strout = strout + "}},\n"
    else:
        strout = strout + str(k).rjust(4) + ", "

strout = strout + """
    -- foreground
    layer2 =
    {   {"""

i = 0
j = 0
for k in output3:
    i += 1
    if i % 16 == 0:
        j += 1
        strout = strout + str(k).rjust(4)
        if j != 12:
            strout = strout + "},\n        {"
        else:
            strout = strout + "}},\n"
    else:
        strout = strout + str(k).rjust(4) + ", "

strout = strout + """
    -- clipping mask
    clippingmask =
    {   {"""

i = 0
j = 0
for k in output4:
    i += 1
    if i % 16 == 0:
        j += 1
        strout = strout + str(k).rjust(4)
        if j != 12:
            strout = strout + "},\n        {"
        else:
            strout = strout + "}},\n"
    else:
        strout = strout + str(k).rjust(4) + ", "

strout = strout + """
    -- the tileset
    tileset = tiles["normal"],

    -- the quads
    quads = quads["normal"]
}"""

print strout
