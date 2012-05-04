# this is hacky as fuck, don't care to clean it up though.
import zlib
import base64
import struct
import xml.dom.minidom
import sys

if len(sys.argv) < 2:
    print "Usage:"
    print "python mapcreate.py infile roomnumber outfile"
    sys.exit()

f = open(sys.argv[1], "r")
data = f.read()
f.close()

dom = xml.dom.minidom.parseString(data)
data = dom.getElementsByTagName("data")
decompressed = []

for d in data:
    nodes = d.childNodes
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            decompressed.append(zlib.decompress(base64.b64decode(node.data)))

length = len(decompressed[0])/4
fmt = 'i'*length
output1 = struct.unpack(fmt, decompressed[0])

length = len(decompressed[1])/4
fmt = 'i'*length
output2 = struct.unpack(fmt, decompressed[1])

length = len(decompressed[2])/4
fmt = 'i'*length
output3 = struct.unpack(fmt, decompressed[2])

length = len(decompressed[3])/4
fmt = 'i'*length
output4 = struct.unpack(fmt, decompressed[3])

strout = """map["""+str(sys.argv[2])+"""] = Room.new{
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

f = open(sys.argv[3], "w")
f.write(strout)
