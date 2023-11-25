# The RecoBase class is a subclass of the BaseModel class.
from pydantic import BaseModel
from api.enums import (
    AppCategory,
    BookCategory,
    GameCategory,
    GamePlatform,
    MusicCategory,
    PodcastCategory,
    RecosCategory,
    Scopes,
    ShowCategory,
)


class RecoBase(BaseModel):
    title: str
    description: str
    url: str
    tags: list
    image: str
    rating: int
    category: RecosCategory
    owner: str
    is_public: boolS


class RecoMovie(RecoBase):
    category: ShowCategory
    date_released: str
    director: list
    actors: list
    duration: int


class RecoShow(RecoBase):
    category: ShowCategory
    seasons: int
    episodes_per_season: int
    creators: list
    cast: list
    episode_duration: int


class RecoBook(RecoBase):
    category: BookCategory
    author: str
    publication_date: str
    pages: int
    language: str
    publisher: str
    isbn: str


class RecoSong(RecoBase):
    category: MusicCategory = MusicCategory.SONG
    artist: str
    album: str
    release_date: str
    duration: int


class RecoArtist(RecoBase):
    category: MusicCategory = MusicCategory.ARTIST
    genres: list
    albums: list
    popular_songs: list
    debut_year: int


class RecoGame(RecoBase):
    category: GameCategory
    platform: list[GamePlatform]
    release_date: str
    developers: list
    publishers: list
    rating: float


class RecoPodcast(RecoBase):
    category: PodcastCategory
    host: list
    episodes: int
    average_duration: int
    language: str
    release_frequency: str


class RecoApp(RecoBase):
    category: AppCategory
    platform: list[GamePlatform]
    release_date: str
    developers: list
    publishers: list
    rating: float


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    scopes: Scopes
    recos: list
