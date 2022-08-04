from pyonfx import *

io = Ass("insert01.ass")
meta, styles, lines = io.get_data()


def romaji(line, l):

    for syl in Utils.all_non_empty(line.syls):
        # Leadin Effect
        l.layer = 0
        l.start_time = line.start_time - 200 + (syl.i*20)
        l.end_time = line.start_time + syl.start_time
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
            syl.center, syl.middle, line.styleref.color3, syl.text)

        io.write_line(l)

        # Main Effect

        l.layer = 2
        l.style = line.style
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time
        durasi = l.end_time - l.start_time
        l.text = "{\\blur3\\bord3\\an5\\pos(%.3f,%.3f)\\c&H4F2C62&\\3c&HFFFFFF&\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
            syl.center, syl.middle, durasi/3, durasi/3, durasi, syl.text)

        io.write_line(l)

        # Leadout Effect
        l.layer = 1
        l.start_time = line.start_time + syl.end_time
        l.end_time = line.end_time + 200
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
            syl.center, syl.middle,  syl.text)

        io.write_line(l)


def sub(line, l):
    # Translation Effect
    for chara in Utils.all_non_empty(line.chars):
        l.layer = 0
        l.start_time = line.start_time - 300 + (chara.i*10)
        l.end_time = line.end_time + 200
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            chara.center, chara.middle, chara.text)

        io.write_line(l)


# Generating lines
for line in lines:
    if line.styleref.alignment >= 7:
        romaji(line, line.copy())
    else:
        sub(line, line.copy())
io.save()
io.open_aegisub()
