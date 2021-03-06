# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 13:19:20 2016

@author: Rblackshaw
"""
import webbrowser


class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,
                 trailer_youtube, imdb_rating, year_of_release):
        '''Initializes all the variables that will be used'''             
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating
        self.year_of_release = year_of_release
        
    def show_trailer(self):
        '''Uses the webbrowser function to open the youtube video trailer'''
        webbrowser.open(self.trailer_youtube_url)
