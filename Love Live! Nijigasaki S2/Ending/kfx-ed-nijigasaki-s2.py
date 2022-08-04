from pyonfx import *
import random

io = Ass("ed.ass")
meta, styles, lines = io.get_data()

# TEMPLATE KARA-FX ED NIJIGAKU S2 (Oleh: Naru@Melody)


def romaji(line, l):
    warna_acak = ["&HB8EDCB&", "&HEAECC9&", "&H99EAE5&", "&HE2E3FA&"]
    warna1 = random.choice(warna_acak)
    warna2 = random.choice(warna_acak)
    while (warna1 == warna2):
        warna2 = random.choice(warna_acak)
    n = len(line.syls)

    for syl in Utils.all_non_empty(line.syls):
        # Leadin Effect
        persen = syl.i / n
        if line.layer == 0:
            warna = Utils.interpolate(persen, warna1, warna2)
        else:
            warna = Utils.interpolate(persen, "&HB8EDCB&", "&HEAECC9&")
        if line.effect == "no-lo" and line.layer == 10:
            l.layer = 1
            l.start_time = line.start_time - 300
            l.end_time = line.end_time
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                    syl.center, syl.middle, line.styleref.color3, syl.text)
                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\c&HFFFFFF&\\t(0,200,\\3c%s\\c%s)}%s" % (
                    syl.center, syl.middle, line.styleref.color3, warna, syl.text)
                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)
        elif line.effect == "no-li" and line.layer == 1:
            l.layer = 1
            l.start_time = line.start_time
            l.end_time = line.start_time + syl.start_time
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)}%s" % (
                    syl.center, syl.middle, syl.text)

                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\c%s}%s" % (
                    syl.center, syl.middle, warna, syl.text)

                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)
        elif line.effect == "efek" or line.effect == "no-lo":
            l.layer = 1
            l.start_time = line.start_time - 300
            l.end_time = line.start_time + syl.start_time
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                    syl.center, syl.middle, line.styleref.color3, syl.text)

                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\c&HFFFFFF&\\t(0,200,\\3c%s\\c%s)}%s" % (
                    syl.center, syl.middle, line.styleref.color3, warna, syl.text)

                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)

        # Main Effect
        if line.layer != 10:
            l.layer = 2
            l.style = line.style
            l.start_time = line.start_time + syl.start_time
            l.end_time = line.start_time + syl.end_time
            durasi = l.end_time - l.start_time
            if line.actor == "warna":
                l.text = "{\\blur3\\bord4\\an5\\pos(%.3f,%.3f)\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                    syl.center, syl.middle, durasi/3, durasi/3, durasi, syl.text)

                io.write_line(l)

            else:
                l.text = "{\\blur3\\an5\\pos(%.3f,%.3f)\\c%s\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
                    syl.center, syl.middle, warna, durasi/3, durasi/3, durasi, syl.text)

                io.write_line(l)

        # Leadout Effect
        if line.effect == "no-li" and line.layer == 10:
            l.layer = 1
            l.start_time = line.start_time
            l.end_time = line.end_time + 300
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                    syl.center, syl.middle, syl.text)

                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,200)\\c%s}%s" % (
                    syl.center, syl.middle, warna, syl.text)

                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)
        elif line.effect == "no-lo" and line.layer == 1:
            l.layer = 1
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)}%s" % (
                    syl.center, syl.middle, syl.text)

                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\c%s}%s" % (
                    syl.center, syl.middle, warna, syl.text)

                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)
        elif line.effect == "efek" or line.effect == "no-li":
            l.layer = 1
            l.start_time = line.start_time + syl.end_time
            l.end_time = line.end_time + 300
            if line.actor != "warna":
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
                    syl.center, syl.middle, syl.text)

                io.write_line(l)
            else:
                l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,200)\\c%s}%s" % (
                    syl.center, syl.middle, warna, syl.text)

                io.write_line(l)

            l.layer = 0
            l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\fad(200,0)\\3c&HFFFFFF&\\c&HFFFFFF&)}%s" % (
                syl.center, syl.middle, syl.text)
            io.write_line(l)


def sub(line, l):
    # Translation Effect
    warna_acak = ["&HB8EDCB&", "&HEAECC9&", "&H99EAE5&", "&HE2E3FA&"]
    warna1 = random.choice(warna_acak)
    warna2 = random.choice(warna_acak)
    while (warna1 == warna2):
        warna2 = random.choice(warna_acak)
    n = len(line.chars)

    for chara in Utils.all_non_empty(line.chars):
        persen = chara.i / n
        warna = Utils.interpolate(persen, warna1, warna2)
        l.layer = line.i
        l.start_time = line.start_time - 300
        l.end_time = line.end_time + 300
        if line.actor == "warna":
            l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,200)\\3c&HFFFFFF&\\c&HFFFFFF&\\t(0,200,\\c%s\\3c%s)}%s" % (
                chara.center, chara.middle, warna, line.styleref.color3, chara.text)

            io.write_line(l)
        else:
            l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(200,200)\\3c&HFFFFFF&\\t(0,200,\\3c%s)}%s" % (
                chara.center, chara.middle, line.styleref.color3, chara.text)

            io.write_line(l)

        l.layer = line.i-1
        l.text = "{\\blur3\\bord6\\an5\\pos(%.3f,%.3f)\\fad(200,200)\\3c&HFFFFFF&\\c&HFFFFFF&}%s" % (
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
