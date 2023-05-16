from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese_ingredient = Ingredient("queijo mussarela")
    sugar_ingredient = Ingredient("sugar")

    assert sugar_ingredient.__hash__() == hash(sugar_ingredient.name)
    assert sugar_ingredient.__eq__(sugar_ingredient) == True  # noqa E712
    assert sugar_ingredient.__eq__(cheese_ingredient) == False  # noqa E712
    assert sugar_ingredient.__repr__() == "Ingredient('sugar')"
    assert len(cheese_ingredient.restrictions) == 2
