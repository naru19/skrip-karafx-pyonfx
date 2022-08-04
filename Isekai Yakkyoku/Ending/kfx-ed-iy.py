from pyonfx import *

io = Ass("EDyakyou.ass")
meta, styles, lines = io.get_data()
CU = ColorUtility(lines)


def romaji(line, l):

    for syl in Utils.all_non_empty(line.syls):

        if line.effect == "warna":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur3\\3c&H8F5E27&\\an5\\pos(%.3f,%.3f)\\fad(200,0)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)

        elif line.effect == "set-warna":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\fad(200,0)%s}%s" % (
                syl.center, syl.middle, CU.get_color_change(l), syl.text)

            io.write_line(l)
        else:
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\fad(200,0)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)

        if line.effect == "warna":

            l.layer = 2
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            l.text = "{\\blur3\\an5\\3c&H8F5E27&\\pos(%.3f,%.3f)\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                syl.center, syl.middle, durasi/3, durasi/3, durasi, syl.text)

            io.write_line(l)

        elif line.effect == "set-warna":
            l.layer = 2
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)%s}%s" % (
                syl.center, syl.middle, durasi/3, durasi/3, durasi, CU.get_color_change(l), syl.text)

            io.write_line(l)
        else:
            l.layer = 2
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                syl.center, syl.middle, durasi/3, durasi/3, durasi, syl.text)

            io.write_line(l)

        if line.effect == "warna":

            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur3\\3c&H8F5E27&\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)
        elif line.effect == "set-warna":
            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\fad(0,200)%s}%s" % (
                syl.center, syl.middle, CU.get_color_change(l), syl.text)

            io.write_line(l)

        else:
            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)


def sub(line, l):
    # Translation Effect
    if line.effect == "warna":
        l.layer = line.i
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur3\\3c&H8F5E27&\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            line.center, line.middle, line.text)

        io.write_line(l)
    elif line.effect == "set-warna":
        l.layer = line.i
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur3\\t(979,1229,\\3c&H8F5E27&)\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            line.center, line.middle, line.text)

        io.write_line(l)
    else:
        l.layer = line.i
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            line.center, line.middle, line.text)

        io.write_line(l)


# Generating lines
for line in lines:
    if line.styleref.alignment >= 7:
        romaji(line, line.copy())
    else:
        sub(line, line.copy())
io.save()
io.open_aegisub()
