#coding=utf-8

class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

movie = Movie_MP4(u'D:/Workspace/OpenVideo/负样本（主码）.mp4')
movie.play()
