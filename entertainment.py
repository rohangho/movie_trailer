##First we have to import the media and website file
import media
import website
toy_story=media.Movie("Toy Story",
                      "A story about a boy and his toys suddenly become living thing",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=Bj4gS1JQzjk")




avatar=media.Movie("Avatar",
                   "A US marine in an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")




pirate_of_caribbean_at_worlds_end=media.Movie("Pirates of Caribbean At World End",
                                              "Story about captain Jack Sparrow and his encounter with different people",
                                              "http://www.hans-zimmer.com/fr/disco/potc3/potc3.jpg",
                                              "https://www.youtube.com/watch?v=HKSZtp_OGHY")




assasin_Creed=media.Movie("Assasin -Creed",
                          "A story about spanish inquisition",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Assassin%27s_Creed_Logo.svg/296px-Assassin%27s_Creed_Logo.svg.png",
                          "https://www.youtube.com/watch?v=4haJD6W136c&t=92s")


Dhol=media.Movie("Dhol",
                 "A story about four guys and their life",
                 "https://upload.wikimedia.org/wikipedia/en/2/20/Dhol1.jpg",
                 "https://www.youtube.com/watch?v=bPzSfN8sWWE")



Fantastic_beast=media.Movie("Fantastic-Beast",
                            "A Harry Potter prequel",
                            "http://vignette2.wikia.nocookie.net/harrypotter/images/0/01/FBWTFT_Poster.png/revision/latest?cb=20151215162644",
                            "https://www.youtube.com/watch?v=Vso5o11LuGU")


movies= [toy_story, avatar,pirate_of_caribbean_at_worlds_end, assasin_Creed, Dhol, Fantastic_beast ]
website.open_movies_page(movies)
