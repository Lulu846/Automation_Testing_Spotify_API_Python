import random
import unittest

from requests_folder.requests_file import put_play_list, get_play_list, post_play_list


class TestPutPlayList(unittest.TestCase):

    def test_put_play_list(self):
        random_number = random.randint(1,9999999999999999)
        playlist_id = post_play_list("31blt7yquqmibecnjbknv5uk5rba", f"playlist_test_put{random_number}", False, True, "test_description").json()["id"]
        response = put_play_list(playlist_id, "playlist_test_api", False, True, "updated_playlist")
        assert response.status_code == 200, f'Error got {response.json()}'
        global test_valid
        for i in range(0, 30):
            test_valid = False
            while True:
                try:
                    assert get_play_list(playlist_id).json()["name"] == "playlist_test_api"
                    assert get_play_list(playlist_id).json()["collaborative"] == False
                    assert get_play_list(playlist_id).json()["public"] == True
                    assert get_play_list(playlist_id).json()["description"] == "updated_playlist"
                    test_valid = True
                except Exception:
                    continue
                break
        assert test_valid == True
