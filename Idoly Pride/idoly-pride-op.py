from pyonfx import *
import random

io = Ass("idoly-pride-op.ass")
meta, styles, lines = io.get_data()

circle = Shape.ellipse(20, 20)

def romaji(line, l):
	
	l.start_time = line.start_time - 300
	l.end_time = line.start_time
	l.text = "{\\blur1\\fscx5\\bord1.5\\an4\\pos(%.3f,%.3f)\\c&HFFFFFF&\\t(0,300,\\fscx100)\\p1}%s" % (
			line.left, line.top,Shape.rectangle(line.width,2))
	
	io.write_line(l)
	
	l.start_time = line.start_time
	l.end_time = line.start_time + 300
	l.text = "{\\blur1\\fscx100\\bord1.5\\an6\\pos(%.3f,%.3f)\\c&HFFFFFF&\\t(0,300,\\fscx5)\\p1}%s" % (
			line.right, line.top,Shape.rectangle(line.width,2))
	
	io.write_line(l)
	
	
	for syl in Utils.all_non_empty(line.syls):
		# Leadin Effect
		l.layer = 0
		if line.actor == "split":
			mulai = syl.start_time
			if mulai <=2240:
				ledi = 0 if line.leadin < 300 else 300
				l.start_time = line.start_time - ledi
				l.end_time = line.start_time + syl.start_time
				l.dur = l.end_time - l.start_time
				l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
					syl.center, syl.middle, ledi, syl.text)

				io.write_line(l)
			else:
				
				ledi = 0 if line.leadin < 300 else 300
				l.start_time = line.start_time - ledi
				l.end_time = line.start_time + 2240
				l.dur = l.end_time - l.start_time
				l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
					syl.center, syl.middle, ledi, syl.text)

				io.write_line(l)
				
				l.start_time = line.start_time + 2240
				l.end_time = line.start_time + syl.start_time
				l.dur = l.end_time - l.start_time
				
				l.text = "{\\3c&H3E79B1&\\blur1\\an5\\pos(%.3f,%.3f)}%s" % (
					syl.center, syl.middle, syl.text)

				io.write_line(l)
		else:
			ledi = 0 if line.leadin < 300 else 300
			l.start_time = line.start_time - ledi
			l.end_time = line.start_time + syl.start_time
			l.dur = l.end_time - l.start_time
			
			l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
				syl.center, syl.middle, ledi, syl.text)

			io.write_line(l)
		# Main Effect
		if l.effect == "fx1":
		
			l.layer = 1

			FU = FrameUtility(line.start_time + syl.start_time, line.start_time + syl.end_time)
			rand = random.uniform(-10, 10)
		
		
			# Starting to iterate over the frames
			for s, e, i, n in FU:
				l.layer = 1

				l.start_time = s
				l.end_time = e
				
				if i <= n/2:
					warna = Utils.interpolate(i/(n/2),line.styleref.color3,"&HFFFFFF&")
				else:
					warna = Utils.interpolate((i-(n/2))/(n/2),"&HFFFFFF&",line.styleref.color3)
				
				fsc = 100
				fsc += FU.add(0, syl.duration/3, 20)
				fsc += FU.add(syl.duration/3, syl.duration, -20)

				alpha = 255
				alpha -= FU.add(syl.duration/2, syl.duration, 255)
				alpha = Convert.coloralpha(alpha)

				l.text = "{\\blur1\\3c%s\\an9\\pos(%.3f,%.3f)\\fscx%.3f\\fscy%.3f}%s" % (
					warna, syl.right, syl.top,
					fsc, fsc, syl.text)

				io.write_line(l)

				l.text = "{\\an5\\pos(%.3f,%.3f)\\fscx%.3f\\fscy%.3f\\1c%s\\bord0\\shad0\\blur2\\alpha%s\\clip(%s)\\p1}%s" % (
					syl.center + rand, syl.middle + rand,
					fsc, fsc, line.styleref.color3, alpha, Convert.text_to_clip(syl, an=9, fscx=fsc, fscy=fsc),
					circle)

				io.write_line(l)
		else:
			l.layer = 1
			
			if line.actor == "split":
				mulai = syl.start_time
				if mulai <= 2140:
					l.start_time = line.start_time + syl.start_time
					l.end_time = line.start_time + syl.end_time
					l.dur = l.end_time - l.start_time
					
					l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)"\
							 "\\t(0,%d,0.5,\\3c&HFFFFFF&\\fscx125\\fscy125)"\
							 "\\t(%d,%d,1.5,\\fscx100\\fscy100\\1c%s\\3c%s)}%s" % (
						syl.center, syl.middle,
						l.dur/3, l.dur/3, l.dur, line.styleref.color1, line.styleref.color3, syl.text)
					
					io.write_line(l)
				else:
					l.start_time = line.start_time + syl.start_time
					l.end_time = line.start_time + syl.end_time
					l.dur = l.end_time - l.start_time
					
					l.text = "{\\3c&H3E79B1&\\blur1\\an5\\pos(%.3f,%.3f)"\
							 "\\t(0,%d,0.5,\\3c&HFFFFFF&\\fscx125\\fscy125)"\
							 "\\t(%d,%d,1.5,\\fscx100\\fscy100\\1c%s\\3c&H3E79B1&)}%s" % (
						syl.center, syl.middle,
						l.dur/3, l.dur/3, l.dur, line.styleref.color1, syl.text)
					
					io.write_line(l)
				
			else:	
				l.start_time = line.start_time + syl.start_time
				l.end_time = line.start_time + syl.end_time
				l.dur = l.end_time - l.start_time
				
				l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)"\
						 "\\t(0,%d,0.5,\\3c&HFFFFFF&\\fscx125\\fscy125)"\
						 "\\t(%d,%d,1.5,\\fscx100\\fscy100\\1c%s\\3c%s)}%s" % (
					syl.center, syl.middle,
					l.dur/3, l.dur/3, l.dur, line.styleref.color1, line.styleref.color3, syl.text)
				
				io.write_line(l)
	
		io.write_line(l)

		# Leadout Effect
		l.layer = 0
		if line.actor == "split":
			mulai = syl.start_time
			if mulai <= 2240:
				l.start_time = line.start_time + syl.end_time
				l.end_time = line.start_time + 2240
				l.dur = l.end_time - l.start_time
				
				l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)}%s" % (
					syl.center, syl.middle, syl.text)

				io.write_line(l)
				
				ledo = 0 if line.leadout < 300 else 300
				l.start_time = line.start_time + 2240
				l.end_time = line.end_time + ledo
				l.dur = l.end_time - l.start_time
				
				l.text = "{\\3c&H3E79B1&\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
					syl.center, syl.middle, ledo, syl.text)

				io.write_line(l)
				
			else:
				ledo = 0 if line.leadout < 300 else 300
				l.start_time = line.start_time + syl.end_time
				l.end_time = line.end_time + ledo
				l.dur = l.end_time - l.start_time
				
				l.text = "{\\3c&H3E79B1&\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
					syl.center, syl.middle, ledo, syl.text)

				io.write_line(l)
		else:
			ledo = 0 if line.leadout < 300 else 300
			l.start_time = line.start_time + syl.end_time
			l.end_time = line.end_time + ledo
			l.dur = l.end_time - l.start_time
			
			l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
				syl.center, syl.middle, ledo, syl.text)

			io.write_line(l)


def sub(line, l):
	# Translation Effect
	
	l.start_time = line.start_time - 300
	l.end_time = line.start_time
	l.text = "{\\blur1\\fscx5\\bord1.5\\an6\\pos(%.3f,%.3f)\\c&HFFFFFF&\\t(0,300,\\fscx100)\\p1}%s" % (
			line.right, line.bottom+5,Shape.rectangle(line.width,2))
	
	io.write_line(l)
	
	l.start_time = line.start_time
	l.end_time = line.start_time + 300
	l.text = "{\\blur1\\fscx100\\bord1.5\\an4\\pos(%.3f,%.3f)\\c&HFFFFFF&\\t(0,300,\\fscx5)\\p1}%s" % (
			line.left, line.bottom+5,Shape.rectangle(line.width,2))
	io.write_line(l)
	
	l.layer = 2
	if line.actor == "split":
		ledi1 = 0 if line.leadin < 300 else 300
		
		l.start_time = line.start_time - ledi1
		l.end_time = line.start_time + 2240
		l.dur = l.end_time - l.start_time
		l.text = "{\pos(%.3f,%.3f)\\blur1\\fad(%d,0)}%s" % (
		line.center, line.bottom, ledi1, line.text)

		io.write_line(l)
		
		ledo1 = 0 if line.leadout < 300 else 300
		
		l.start_time = line.start_time + 2240
		l.end_time = line.end_time + ledo1
		l.dur = l.end_time - l.start_time
		l.text = "{\\3c&H3E79B1&\pos(%.3f,%.3f)\\blur1\\fad(0,%d)}%s" % (
		line.center, line.bottom, ledo1, line.text)

		io.write_line(l)
	
	else:
		ledi2 = 0 if line.leadin < 300 else 300
		ledo2 = 0 if line.leadout < 300 else 300
		
		l.start_time = line.start_time - ledi2
		l.end_time = line.end_time + ledo2
		l.dur = l.end_time - l.start_time
		if line.style == "OP2-kanan - TL":
		
			l.text = "{\pos(%.3f,%.3f)\\blur1\\fad(%d,%d)}%s" % (
			line.right, line.bottom, ledi2, ledo2, line.text)

			io.write_line(l)
		
		else:
			l.text = "{\pos(%.3f,%.3f)\\blur1\\fad(%d,%d)}%s" % (
			line.center, line.bottom, ledi2, ledo2, line.text)

			io.write_line(l)
	


# Generating lines
for line in lines:
	if line.styleref.alignment >= 7:
		romaji(line, line.copy())
	else:
		sub(line, line.copy())
io.save()
io.open_aegisub()