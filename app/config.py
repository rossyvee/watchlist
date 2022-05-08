class Config:
    pass

    MOVIE_API_KEY = "45b6ac0139fcfd1988133dfa47162c99"
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key='+MOVIE_API_KEY

class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG = True
