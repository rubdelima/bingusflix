from src.api.filmes_em_alta import read_filmesEmAlta
from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.library import library

@scenario(
    scenario_name='Ver lista de filmes Em alta',
    feature_name='../features/emalta.feature'
)
def test_sucessful_EmAlta():
    pass

