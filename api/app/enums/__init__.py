from enum import Enum


class Scopes(Enum):
    GUEST = ["recos:public"]
    REGIS = ["recos:write", "recos:read", "recos:public"]
    ADMIN = [
        "user:write",
        "user:read",
        "recos:write",
        "recos:read",
        "recos:public",
    ]


class RecosCategory(Enum):
    MOVIE = "movie"
    SHOW = "show"
    BOOK = "book"
    MUSIC = "music"
    GAME = "game"
    PODCAST = "podcast"
    APP = "app"
    OTHER = "other"


class ShowCategory(Enum):
    ACTION = "action"
    ADVENTURE = "adventure"
    COMEDY = "comedy"
    CRIME = "crime"
    DRAMA = "drama"
    FANTASY = "fantasy"
    HISTORICAL = "historical"
    HORROR = "horror"
    MYSTERY = "mystery"
    PHILOSOPHICAL = "philosophical"
    POLITICAL = "political"
    ROMANCE = "romance"
    SAGA = "saga"
    SATIRE = "satire"
    SCIENCE = "science"
    SOCIAL = "social"
    SPECULATIVE = "speculative"
    THRILLER = "thriller"
    URBAN = "urban"
    WESTERN = "western"


class BookCategory(Enum):
    FICTION = "fiction"
    NON_FICTION = "non_fiction"
    MYSTERY = "mystery"
    SCIFI = "science_fiction"
    FANTASY = "fantasy"
    ROMANCE = "romance"
    HORROR = "horror"
    BIOGRAPHY = "biography"
    SELF_HELP = "self_help"
    OTHER = "other"


class MusicCategory(Enum):
    SONG = "song"
    ARTIST = "artist"
    ALBUM = "album"
    OTHER = "other"


class GamePlatform(Enum):
    PC = "PC"
    PLAYSTATION = "PlayStation"
    XBOX = "Xbox"
    NINTENDO = "Nintendo"
    MOBILE = "Mobile"
    OTHER = "Other"


class GameCategory(Enum):
    ACTION = "action"
    ADVENTURE = "adventure"
    RPG = "role_playing_game"
    STRATEGY = "strategy"
    SPORTS = "sports"
    HORROR = "horror"
    SIMULATION = "simulation"
    OTHER = "other"


class PodcastCategory(Enum):
    COMEDY = "comedy"
    EDUCATION = "education"
    NEWS = "news"
    POLITICS = "politics"
    SPORTS = "sports"
    TRUE_CRIME = "true_crime"
    OTHER = "other"


class AppCategory(Enum):
    SOCIAL_MEDIA = "social_media"
    PRODUCTIVITY = "productivity"
    ENTERTAINMENT = "entertainment"
    HEALTH_FITNESS = "health_fitness"
    EDUCATION = "education"
    UTILITIES = "utilities"
    GAMING = "gaming"
    SOFTWARE_DEVELOPMENT = "software_development"
    OTHER = "other"
