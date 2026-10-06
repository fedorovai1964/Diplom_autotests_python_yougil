import allure
import pytest

pytestmark = [pytest.mark.api]

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Boards API")
@allure.title("Получение списка досок (вызов метода GET) на сайте YouGile")
def test_get_boards(api) -> None:
    board_list = api.get_all_boards()

    assert len(board_list['content']) == board_list['paging']['count']

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Boards API")
@allure.title("Получение доски по ID (вызов метода GET) на сайте YouGile")
def test_get_board_by_id(board, api) -> None:
    id_board, name = board
    data_board = api.find_board(id_board)
    with allure.step("Проверить, что заголовок"
                     " созданной доски совпадает с заданным"):
        assert data_board['title'] == name

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Boards API")
@allure.title("Создание доски  (вызов метода POST) на сайте YouGile")
def test_create_board(api) -> None:
    name = api.random_board_name()
    with allure.step(f"Отправить POST на создание доски {name}"):
        resp = api.create_board(name)
    with allure.step("Проверить, что API вернул id созданной доски"):
        assert "id" in resp
        id_board = resp["id"]
    with allure.step("Проверить, что заголовок совпадает"):
        assert api.find_board(id_board)["title"] == name
    with allure.step("Удалить созданную доску"):
        api.delete_board(id_board)

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Boards API")
@allure.title("Изменение доски (вызов метода PUT) на сайте YouGile")
def test_update_board(board, api) -> None:
    id_board, name = board

    new_name = f"{name} измененная"
    api.update_board(id_board, new_name)
    data_board = api.find_board(id_board)
    with allure.step("Проверить, что заголовок изменился"):
        assert data_board['title'] == new_name

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Boards API")
@allure.title("Удаление доски  (вызов метода PUT) на сайте YouGile")
def test_delete_board(board, api) -> None:
    id_board, name = board
    board_list_before = api.get_all_boards()

    api.delete_board(id_board)
    board_list_after = api.get_all_boards()

    id_after = [b['id'] for b in board_list_after['content']]
    with allure.step("Проверить, что удаленной доски нет в списке"):
        assert id_board not in id_after

    with (allure.step("Проверить, количество досок уменьшилось на единицу")):
        assert len(board_list_before['content']
                   ) - len(board_list_after['content']) == 1
