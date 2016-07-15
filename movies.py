# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 11:47:12 2016

@author: Rblackshaw
"""

import class_lesson as cl
import fresh_tomatoes

miracle = cl.Movie('''Miracle''',
                   '''U.S. hockey team beats the unbeaten Soviet Union team'''
                   +'''amidst the Cold War''',
                   '''https://s-media-cache-ak0.pinimg.com/236x/29/dc/0d/'''
                   +'''29dc0d40463919524b4b508a18ea8a08.jpg''',
                   '''https://www.youtube.com/watch?v=v64ofT1rGOw''',
                   "7.7/10",
                   "2004")
            
fight_club = cl.Movie('''Fight Club''',
                      '''Guys start a fight club and things start'''
                      +'''getting weird''',
                      '''https://moviemaster1703.files.wordpress.com/2010/12/'''
                      +'''fight-club-movie-poster-1020270798.jpg''',
                      "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                      "8.8/10",
                      "1999")
                      
american_history_x = cl.Movie("American History X",
                              '''Edward Norton goes to prison for a hate crime'''
                              +'''and becomes a nicer person''',
                              '''http://www.movieposter.com/posters/archive/'''
                              +'''main/92/MPW-46054''',
                              "https://www.youtube.com/watch?v=JsPW6Fj3BUI",
                              "8.6/10",
                              "1998")
            
inglorious_basterds = cl.Movie("Inglorious Basterds",
                              '''American WWII soldiers form a group with'''
                              +'''the goal of killing nazis''',
                        '''https://questionablefilmreview.files.wordpress.'''
                        +'''com/2013/07/7736093674_2e8414a35c_o.jpg''',
                              "https://www.youtube.com/watch?v=KnrRy6kSFF0",
                              "8.3/10",
                              "2009")

team_america = cl.Movie("Team America: World Police",
                        "American Special Forces attempt to stop Kim Jong Il",
                        '''http://www.impawards.com/2004/posters/'''
                        +'''team_america_world_police.jpg''',
                        "https://www.youtube.com/watch?v=RPBX47zSktc",
                        "7.2/10",
                        "2004")

dazed_and_confused = cl.Movie("Dazed and Confused",
                              '''A day in the life of high school kids'''
                              +'''in the 1970s''',
                              "http://i43.tinypic.com/2ufr42x.jpg",
                              "https://www.youtube.com/watch?v=Mvj4Ng6yinA",
                              "7.7/10",
                              "1993")


movies = [miracle, fight_club, american_history_x, inglorious_basterds,
          team_america, dazed_and_confused]
fresh_tomatoes.open_movies_page(movies)
