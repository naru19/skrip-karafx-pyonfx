from pyonfx import *
import random

io = Ass("Insert_Akaniji_03.ass")
meta, styles, lines = io.get_data()


def romaji(line, l):

    for syl in Utils.all_non_empty(line.syls):
        if line.effect == "loli":
            if line.actor == "emma":
                warna = "&H3D8D22&"
            elif line.actor == "rina":
                warna = "&HC26076&"
            elif line.actor == "kanata":
                warna = "&HFF45DB&"
            elif line.actor == "kasumin":
                warna = "&H148DC6&"
            else:
                warna = line.styleref.color3

            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                syl.center, syl.middle, warna, syl.text)

            io.write_line(l)

            if line.actor == "emma":
                warna = "&H3D8D22&"
            elif line.actor == "rina":
                warna = "&HC26076&"
            elif line.actor == "kanata":
                warna = "&HFF45DB&"
            elif line.actor == "kasumin":
                warna = "&H148DC6&"
            elif line.actor == "semua":
                daftar_warna = ["&H3D8D22&", "&HC26076&",
                                "&HFF45DB&", "&H148DC6&"]
                warna = random.choice(daftar_warna)
            else:
                warna = line.styleref.color3

            l.layer = 1
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            l.text = "{\\blur3\\bord3\\an5\\pos(%.3f,%.3f)\\c%s\\3c&HFFFFFF&\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                syl.center, syl.middle, warna, durasi/3, durasi/3, durasi, syl.text)

            io.write_line(l)

            if line.actor == "emma":
                warna = "&H3D8D22&"
            elif line.actor == "rina":
                warna = "&HC26076&"
            elif line.actor == "kanata":
                warna = "&HFF45DB&"
            elif line.actor == "kasumin":
                warna = "&H148DC6&"
            else:
                warna = line.styleref.color3

            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\3c%s\\fad(0,200)}%s" % (
                syl.center, syl.middle, warna, syl.text)

            io.write_line(l)

        elif line.effect == "masuk":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.end_time
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                syl.center, syl.middle, line.styleref.color3, syl.text)

            io.write_line(l)

        elif line.effect == "masuk-li":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                syl.center, syl.middle, line.styleref.color3, syl.text)

            io.write_line(l)

        elif line.effect == "li":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)

        elif line.effect == "efek":
            l.layer = 1
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            l.text = "{\\blur3\\bord3\\an5\\pos(%.3f,%.3f)\\c%s\\3c&HFFFFFF&\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                syl.center, syl.middle, line.styleref.color3, durasi/3, durasi/3, durasi, syl.text)

            io.write_line(l)

        elif line.effect == "lo":
            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)

        elif line.effect == "lo-keluar":
            l.layer = 0
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)

        elif line.effect == "keluar":
            l.layer = 0
            l.start_time = line.start_time
            l.end_time = line.end_time + 200
            l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                syl.center, syl.middle, syl.text)

            io.write_line(l)


def sub(line, l):
    # Translation Effect
    if line.actor == "emma":
        warna = "&H3D8D22&"
    elif line.actor == "rina":
        warna = "&HC26076&"
    elif line.actor == "kanata":
        warna = "&HFF45DB&"
    elif line.actor == "kasumin":
        warna = "&H148DC6&"
    else:
        warna = line.styleref.color3
    l.layer = line.i
    l.start_time = line.start_time
    l.end_time = line.end_time + 200
    l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\3c%s\\fad(200,200)}%s" % (
        line.center, line.middle, warna, line.text)

    io.write_line(l)


# Generating lines
for line in lines:
    if line.styleref.alignment >= 7:
        romaji(line, line.copy())
    else:
        sub(line, line.copy())
io.save()
io.open_aegisub()
