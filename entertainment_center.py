import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Toys Come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("The Shawshank Redemption",
                     "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     "https://www.youtube.com/watch?v=6hB3S9bIaco")
god_father = media.Movie("The Godfather",
                         " godfather storyline balah",
                         "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                         "https://www.youtube.com/watch?v=sY1S34973zA")
forest_gump = media.Movie("Forrest Gump",
                         "Forrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny. His 'mama' teaches him the ways of life and leaves him to choose his destiny.",
                         "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                         "https://www.youtube.com/watch?v=uPIEn0M8su0")
dark_knight = media.Movie("The Dark Knight",
                         "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham",
                         "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                         "https://www.youtube.com/watch?v=EXeTwQWrcwY")
pulp_fiction = media.Movie("Pulp Fiction",
                         "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                         "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                         "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
saving_private_ryan = media.Movie("Saving Private Ryan",
                         "Drama · Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                         "https://www.youtube.com/watch?v=zwhP5b4tD6g")
titanic = media.Movie("Titanic",
                         "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                         "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                         "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
movies = [toy_story, avatar, god_father, forest_gump, dark_knight, pulp_fiction, saving_private_ryan, titanic]
fresh_tomatoes.open_movies_page(movies)
