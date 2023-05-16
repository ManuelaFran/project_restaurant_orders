from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    strogonoff = Dish("strogonoff", 25.00)
    pasta_with_cheese = Dish("macarrão com queijo", 24.50)

    assert strogonoff.name == "strogonoff"
    assert strogonoff.price == 25.00

    assert strogonoff.__repr__() == "Dish('strogonoff', R$25.00)"
    assert strogonoff.__eq__(strogonoff) == True  # noqa E712
    assert strogonoff.__eq__(pasta_with_cheese) == False  # noqa E712
    assert strogonoff.__hash__() == hash("Dish('strogonoff', R$25.00)")

    strogonoff.add_ingredient_dependency(Ingredient("creme de leite"), 1)
    strogonoff.add_ingredient_dependency(Ingredient("frango"), 1)

    assert strogonoff.recipe == {
        Ingredient("creme de leite"): 1,
        Ingredient("frango"): 1,
    }
    assert len(strogonoff.get_restrictions()) == 3

    assert strogonoff.get_ingredients() == {
        Ingredient("creme de leite"),
        Ingredient("frango"),
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("strogonoff", "25.00")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("strogonoff", -25.00)
