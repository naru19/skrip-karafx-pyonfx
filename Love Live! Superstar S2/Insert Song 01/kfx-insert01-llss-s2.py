from pyonfx import *
import random

io = Ass("Insertloplep_Super_2.ass")
meta, styles, lines = io.get_data()

bintang = "m 17.119 0 l 22.409 10.719 34.238 12.438 25.679 20.781 27.699 32.562 17.119 27 6.539 32.562 8.559 20.781 0 12.438 11.829 10.719 17.119 0"


def romaji(line, l):

    for syl in Utils.all_non_empty(line.syls):

        l.layer = 1
        l.start_time = line.start_time
        l.end_time = line.start_time + syl.start_time
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
            syl.center, syl.middle, line.styleref.color3, syl.text)

        io.write_line(l)

        l.layer = 2
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time
        durasi = l.end_time - l.start_time
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\c&HD5995B&\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
            syl.center, syl.middle, durasi/3, durasi/3, durasi, syl.text)

        io.write_line(l)

        # if line.effect == "ref":
        #     l.layer = 0
        #     l.start_time = line.start_time + syl.start_time
        #     l.end_time = line.start_time + syl.end_time
        #     durasi = l.end_time - l.start_time
        #     l.text = "{\\an5\\3c&HFFFFFF&\\fscx100\\fscy100\\p1\\c&H8721DF&\\pos(%.3f,%.3f)\\t(0,%d,0.5,\\frz-45\\fscx130\\fscy130)\\t(%d,%d,1.5,\\frz-90\\fscx100\\fscy100)}%s" % (
        #         syl.center, syl.middle, durasi/3, durasi/3, durasi, bintang)

        #     io.write_line(l)

        l.layer = 1
        l.start_time = line.start_time + syl.end_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
            syl.center, syl.middle, syl.text)

        io.write_line(l)


def sub(line, l):
    # Translation Effect
    if line.style == "Dialog":
        l.layer = line.i
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
            line.center, line.middle, line.text)

        io.write_line(l)
    else:
        l.layer = line.i
        l.start_time = line.start_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(200,200)}%s" % (
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
