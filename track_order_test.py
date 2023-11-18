'''
Yandex Practicum        Дипломная работа
Бурмистрова Мария       Когорта 10
18 ноября 2023 г.
'''

import sending_requests


def get_track_number_of_order():
    track_number = sending_requests.post_new_order()
    return track_number.json()["track"]


def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = sending_requests.get_order_info(track_number)
    assert get_response.status_code == 200