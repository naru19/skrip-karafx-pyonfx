from pyonfx import *

io = Ass("Op-yakyoku.ass")
meta, styles, lines = io.get_data()


def romaji(line, l):

    for syl in Utils.all_non_empty(line.syls):

        gradasi = syl.i/(len(line.syls))
        warna = Utils.interpolate(gradasi, "&HE4AC0B&", "&H70A331&")

        l.layer = 0
        l.start_time = line.start_time
        l.end_time = line.start_time + syl.start_time
        l.text = "{\\blur5\\bord5\\3c&HFFFFFF&\\an5\\pos(%.3f,%.3f)\\fad(200,0)}%s" % (
            syl.center, syl.middle, syl.text)

        io.write_line(l)

        l.layer = 1
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c%s}%s" % (
            syl.center, syl.middle, warna, syl.text)

        io.write_line(l)

        l.layer = 2
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time
        durasi = l.end_time - l.start_time
        l.text = "{\\blur5\\an5\\bord5\\pos(%.3f,%.3f)\\c%s\\3c&HFFFFFF&\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
            syl.center, syl.middle, warna, durasi/3, durasi/3, durasi, syl.text)

        io.write_line(l)

        l.layer = 0
        l.start_time = line.start_time + syl.end_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur5\\bord5\\3c&HFFFFFF&\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
            syl.center, syl.middle, syl.text)

        io.write_line(l)

        l.layer = 1
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(0,200)\\3c%s}%s" % (
            syl.center, syl.middle, warna, syl.text)

        io.write_line(l)


def sub(line, l):
    # Translation Effect
    for chara in Utils.all_non_empty(line.chars):
        l.layer = 0
        gradasi = chara.i/(len(line.chars))
        warna = Utils.interpolate(gradasi, "&HE4AC0B&", "&H70A331&")
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur5\\bord5\\3c&HFFFFFF&\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            chara.center, chara.middle, chara.text)

        io.write_line(l)
        l.layer = 1
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(200,200)\\3c%s}%s" % (
            chara.center, chara.middle, warna, chara.text)

        io.write_line(l)


# Generating lines
for line in lines:
    if line.styleref.alignment >= 7:
        romaji(line, line.copy())
    else:
        sub(line, line.copy())
io.save()
io.open_aegisub()
