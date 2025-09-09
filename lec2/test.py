from typing import Union
from typing import Optional
from typing import Any
from typing import (Sequence, 
                    Set,
                    Tuple, 
                    List, 
                    Iterable,
                    Callable,
                    TypedDict,
                    )


users_cnt_or_some_str: Union[int, str] = 1000   #Number of users
#Python 3.10+ 
users_cnt_or_some_str: int | str = 1000  

some_string_or_none: str | None = None  #Not valid

some_string_or_none: Optional[str] = None  #Valid

any_variable: Any = None

marks_list: list[int] = [1, 2, 3, 4, 5,]  # Valid
marks_tuple: tuple[int] = (1, 2, 3, 4, 5,)  #Invalid
marks_tuple: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5,)  #Valid
marks_tuple: tuple[int, ...] = (1, 2, 3, 4, 5,)  #Valid
name_age_dict: dict[str, int] = {
    "Temirbolat": 16, 
    "john": 15,
}
unique_names_set: set[str] = {1, 2, 3}

def greet(names: Sequence[str]) -> None:
    for name in names:
        print(f"Hello {name}!")
def greet(names) -> None:
    """
    print a names
    
    :param names: A sequense of the names 
    :return: None
    """
    name: str
    for name in names:
        print(f"Hello {name}!")

def greet(names):
    """
    print a names
    
    :param names: A sequense of the names 
    :return: None
    """
    name: str
    for name in names:
        print(f"Hello {name}!")
    return None

a: Iterable[str] = iter(["Temirbolat", "Turarbek"])
next(a)
next(a)
#next(a) it would raise StopIterable

class A:
    """
    Example of class A
    """

    def __getattribute__(self, name: str):
        return name

greet_func: Callable[[Sequence[str]], None] = greet

class MovieDict(TypedDict):
    name: str
    year: int

movies: list[MovieDict] = {
    
}


