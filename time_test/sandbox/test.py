import pytest

from main import MoneyBox


@pytest.fixture()
def create_moneybox_instance():
    capacity = 50
    money_box = MoneyBox(capacity)
    return money_box


def test_capacity(create_moneybox_instance: MoneyBox):
    money_box = create_moneybox_instance
    assert money_box.can_add(49) == True, 'Монеты должны поместиться в копилку'
    assert money_box.can_add(50) == True, 'Монеты должны поместиться в копилку'
    assert money_box.can_add(51) == False, 'Монеты не должны поместиться в копилку'
    print('Тест проверки вместимости успешно пройден')


def test_add(create_moneybox_instance: MoneyBox):
    money_box = create_moneybox_instance
    money_box.add(5)
    assert money_box.can_add(45) == True, 'Монеты должны поместиться в копилку'
    money_box.add(44)
    assert money_box.can_add(1) == True, 'Монеты должны поместиться в копилку'
    assert money_box.can_add(2) == False, 'Монеты не должны поместиться в копилку'
    money_box.add(1)
    assert money_box.can_add(1) == False, 'Монеты не должны поместиться в копилку'


# @pytest.mark.parametrize("idx, value",
#                          [(0, "Fomichev A.V."),
#                           (1, "fisher"),
#                           (2, 55),
#                           (3, 32_237),
#                           (4, 35)])
# def test_set_value_by_index(create_person_instance, idx, value):
#     person = create_person_instance
#     person[idx] = value
#     assert person[idx] == value
#     with pytest.raises(IndexError) as ex:
#         person[idx + 5] = "new_value"
#     assert 'неверный индекс' in str(ex.value)
#
#
# def test_person_as_iterator(create_person_instance, monkeypatch):
#     person = create_person_instance
#     outp = io.StringIO()
#     monkeypatch.setattr("sys.stdout", outp)
#     for field in person:
#         print(field)
#     assert outp.getvalue() == """Балакирев С.М.
# бизнесмен
# 61
# 1000000
# 46
# """
