from pyonfx import *

io = Ass("OPloplep_Super_2.ass")
meta, styles, lines = io.get_data()

bintang = "m 17.119 0 l 22.409 10.719 34.238 12.438 25.679 20.781 27.699 32.562 17.119 27 6.539 32.562 8.559 20.781 0 12.438 11.829 10.719 17.119 0"

warna_acak = ["&H49B5FC&", "&H8C65FA&", "&H91F3BC&"]


def romaji(line, l):
    mod_tiga = line.i % 3
    warna_bintang = warna_acak[mod_tiga]

    l.layer = 3
    l.start_time = line.start_time
    l.end_time = line.start_time + 500
    l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx140\\fscy140)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
        line.left+20, line.middle-20, warna_bintang, bintang)

    io.write_line(l)

    l.layer = 3
    l.start_time = line.start_time + 500
    l.end_time = line.start_time + 1000
    l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx140\\fscy140)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
        line.right-20, line.middle+20, warna_bintang, bintang)

    io.write_line(l)

    if line.end_time - line.start_time > 2000:

        l.layer = 3
        l.start_time = line.start_time + 1000
        l.end_time = line.start_time + 1500
        l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx120\\fscy120)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
            line.center-40, line.middle+20, warna_bintang, bintang)

        io.write_line(l)

        l.layer = 3
        l.start_time = line.start_time + 1500
        l.end_time = line.start_time + 2000
        l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx120\\fscy120)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
            line.center+40, line.middle-20, warna_bintang, bintang)

        io.write_line(l)

    for syl in Utils.all_non_empty(line.syls):
        # Leadin Effect
        l.layer = 0
        l.start_time = line.start_time + (syl.i*20)
        l.end_time = line.start_time + syl.start_time
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\c&HFFFFFF&\\t(0,1000,\\c&H6E00C3&)}%s" % (
            syl.center, syl.middle, syl.text)

        io.write_line(l)

        # Main Effect

        l.layer = 2
        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time
        durasi = l.end_time - l.start_time
        l.text = "{\\blur4\\bord4\\an5\\pos(%.3f,%.3f)\\c%s\\3c%s\\t(0,%d,\\fscx125,\\fscy125)\\t(%d,%d,\\fscx100,\\fscy100)}%s" % (
            syl.center, syl.middle, line.styleref.color3, line.styleref.color1, durasi/3, durasi/3, durasi, syl.text)

        io.write_line(l)

        # Leadout Effect
        l.layer = 1
        l.start_time = line.start_time + syl.end_time
        l.end_time = line.end_time + 200
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(0,200)}%s" % (
            syl.center, syl.middle,  syl.text)

        io.write_line(l)


def sub(line, l):
    # Translation Effect

    mod_tiga = line.i % 3
    warna_bintang = warna_acak[mod_tiga]

    l.layer = 3
    l.start_time = line.start_time
    l.end_time = line.start_time + 500
    l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx140\\fscy140)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
        line.left+20, line.middle-20, warna_bintang, bintang)

    io.write_line(l)

    l.layer = 3
    l.start_time = line.start_time + 500
    l.end_time = line.start_time + 1000
    l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx140\\fscy140)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
        line.right-20, line.middle+20, warna_bintang, bintang)

    io.write_line(l)

    if line.end_time - line.start_time > 2000:

        l.layer = 3
        l.start_time = line.start_time + 1000
        l.end_time = line.start_time + 1500
        l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx120\\fscy120)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
            line.center-40, line.middle+20, warna_bintang, bintang)

        io.write_line(l)

        l.layer = 3
        l.start_time = line.start_time + 1500
        l.end_time = line.start_time + 2000
        l.text = "{\\bord4\\1a&HFF&\\fad(100,100)\\blur1\\an5\\pos(%.3f,%.3f)\\t(0,166,0.5,\\frz-45\\fscx120\\fscy120)\\t(166,500,1.5,\\frz-90\\fscx100\\fscy100)\\3c%s\\p1}%s" % (
            line.center+40, line.middle-20, warna_bintang, bintang)

        io.write_line(l)

    for chara in Utils.all_non_empty(line.chars):
        l.layer = 0
        l.start_time = line.start_time + (chara.i*10)
        l.end_time = line.end_time + 200
        l.text = "{\\blur2\\an5\\pos(%.3f,%.3f)\\fad(0,200)\\c&HFFFFFF&\\t(0,1000,\\c&H6E00C3&)}%s" % (
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
