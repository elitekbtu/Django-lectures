# Python modules
from typing import (
    Union,
    Optional,
    Any,
    List,
    Tuple,
    Dict,
    Set,
    Sequence,
    Iterable,
    Mapping,
    Callable,
    TypeVar,
    TypedDict,
    NamedTuple,
    Literal,
    NoReturn,
)


name_or_age: Union[str, int] = 12
phone_number: Optional[str] = None
thing: Any = "something"
list_of_numbers = List[int] = [1, 2, 3, 4, 5]
tuple_of_number = Tuple[int, ...] = (1, 2, 3, 4, 5)
dict_of_users: Dict[str, int] = {
    "Turarbek": 19,
    "Beka": 19,
    "Aza": 100,
}
set_of_numbers: Set[int] = {1, 2, 3}

def greet(numbers:Sequence[int]) -> None:
    """
    Function for greeting a list of numbers

    :params: Sequence[int]
    :return: None
    """

    for number in numbers:
        print(f"{number}\n")


list_of_nums: Iterable[int] = [1, 2, 3]
next(list_of_numbers)
next(list_of_numbers)

users_info: Mapping[str, str] = {"name": "Turarbek", "surname": "Satbaldiyev"}

greet_func:Callable[[Sequence[int]], None] = greet
greet_func()

T = TypeVar("T")

def return_values(values:list[T]) -> list[T]:
    """
    Function for returns values of the list

    :params: list[T]
    :return: list[T]
    """

    return values


my_list = return_values([1, 2, 3, 4, 5])
my_list_2 = return_values(["Hello", "World"])
my_list_3 = return_values([True, False, True])

class MovieDict(TypedDict):
    """
    Function representing a movie with name and genre
    """

    name: str
    """
    Name of the movie
    """

    genre: str
    """
    Genre of the movie
    """


movies: Tuple[MovieDict] = (
    {"name": "Avatar", "genre": "fantastic"}, 
    {"name": "Tom and Jerry", "genre": "cartoon"},
)

class SearchMovieResult(NamedTuple):
    cur_movie:Optional[MovieDict]
    """
    Current movie
    """
    is_found:bool
    """
    A boolean indicates if movie was found
    """


def find_movie_by_name(movies: list[MovieDict], name: str) -> SearchMovieResult:
    """
    Find a movie by its name in a list of movies.

    :param movies: A list of MovieDict objects.
    :param name: The name of the movie to find.
    :return: The MovieDict object if found, otherwise None.

    """

    movie: MovieDict
    for movie in movies:
        if movie["name"] == name:
            return SearchMovieResult(
                cur_movie=movie,
                is_found=True
            )
    return SearchMovieResult(None, False)

one: Literal[1]


def fatal_error(msg: str) -> NoReturn:
    """
    Fatal error exception
    :params: msg
    :return: NoReturn
    """
    raise RuntimeError(f"Fatal error: {msg}")

