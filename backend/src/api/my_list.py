from fastapi import APIRouter, HTTPException, Depends
from src.db.db_mananger import Db_manager
from src.schemas.user import UserDB
from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.movies import MovieModel, MovieList
from src.schemas.tv_series import TVSeriesModel, TVSeriesList
from src.schemas.generics import GenericMediaModel, GenericMediaList
from src.api.login import get_logged_user
from typing import Annotated, Union


router = APIRouter()

my_list_db = {}
database = Db_manager("http://localhost:4000")


@router.get('/', status_code=200, response_model=GenericMediaList, tags=["my-list"])
def get_my_list(current_user: Annotated[UserDB, Depends(get_logged_user)]):
    # profile_list = database.
    profiles_list = my_list_db.get(current_user.email, {})

    profile_list = profiles_list.get(current_user.active_profile, [])
    return {'medias': profile_list}


@router.post(
    '/movie',
    status_code=201,
    response_model=GenericMediaModel,
    tags=['my-list']
)
def add_movie_to_mylist(
    movie: MovieModel,
    current_user: Annotated[UserDB, Depends(get_logged_user)]
):
   
    profiles_lists = my_list_db.setdefault(current_user.email, {})

    profile_lists = profiles_lists.setdefault(
        current_user.active_profile, []
    )

    if movie not in profile_lists:
        profile_lists.append(movie)

    return GenericMediaModel(**movie.model_dump())


@router.post(
    '/tv-series',
    status_code=201,
    response_model=GenericMediaModel,
    tags=['my-list']
)
def add_tv_series_to_mylist(
    tv_series: TVSeriesModel,
    current_user: Annotated[UserDB, Depends(get_logged_user)]
):

    profile_lists = my_list_db.setdefault(current_user.email, {})

    my_list = profile_lists.setdefault(
        current_user.active_profile, []
    )

    if tv_series not in my_list:
        my_list.append(tv_series)

    return GenericMediaModel(**tv_series.model_dump(), title=tv_series.name)


@router.delete(
    '/',
    status_code=200,
    response_model=GenericMediaList,
    tags=["my-list"]
)
def remove_from_my_list(
    media: Union[TVSeriesModel, MovieModel],
    current_user: Annotated[UserDB, Depends(get_logged_user)]
):
    profiles_list = my_list_db.get(current_user.email, {})

    profile_list = profiles_list.get(current_user.active_profile, [])

    if media in profile_list:
        profile_list.remove(media)

    return {'medias': profile_list}
