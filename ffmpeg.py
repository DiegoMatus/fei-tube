#!/usr/bin/env python2
#Change this:
videoconvertpath='/mnt/opslag/server/mediaconvert/'
videooutputpath='/mnt/opslag/server/media/Video/'
videocodec='mpeg4'
videotag='xvid'
videobitrate='3000k'
audiocodec='libmp3lame'
outputcontainer='avi'
supportedcontainers=['mkv','avi','mov','ts']
#End of variables, start of code
for arg in argv[1:]:
	arg=path.abspath(arg)
	print(arg)
	if not path.exists(arg):
		print("Path doesn't exist. Exiting...")
		exit(1)
	if not path.splitext(arg)[1][1:] in supportedcontainers:
		print("Unsupported file. Exiting...")
		exit(1)
	if path.isfile(arg):
		series=path.dirname(arg.split(videoconvertpath)[1])
	elif path.isdir(arg):
		series=path.dirname(arg.split(videoconvertpath)[1]+'/')
	outputpath=path.join(videooutputpath,series)
	if series!='' and not path.exists(outputpath):
		call(['mkdir','-p', '%s'%outputpath])
	if path.isfile(arg):
		outputname=path.splitext(path.basename(arg))[0]
		if path.isfile(path.splitext(arg)[0]+'.srt'):
			call(['cp',path.splitext(arg)[0]+'.srt',path.join(outputpath,outputname)+'.srt'])
		call(['ffmpeg','-i',arg,'-vcodec',videocodec,'-vtag', videotag,'-acodec',audiocodec,'-ac','2','-b:v',videobitrate,'-y',path.join(outputpath,outputname)+'.'+outputcontainer])
	elif path.isdir(arg):
		files=listdir(arg)
		todo=[]
		for i in files:
			i=path.abspath(path.join(arg,i))
			if path.splitext(i)[1][1:] in supportedcontainers:
				todo.append(path.join(arg,i))
				outputname=path.splitext(path.basename(i))[0]
				if path.isfile(path.splitext(i)[0]+'.srt'):
					call(['cp',path.splitext(i)[0]+'.srt',path.join(outputpath,outputname)+'.srt'])
				call(['ffmpeg','-i',i,'-vcodec',videocodec,'-vtag', videotag,'-acodec',audiocodec,'-ac','2','-b:v',videobitrate,'-y',path.join(outputpath,outputname)+'.'+outputcontainer])


