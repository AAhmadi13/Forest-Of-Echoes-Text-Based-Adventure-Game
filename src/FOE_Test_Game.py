import pytest
from FOE_Version_Final import (
    handle_movement,
    handle_take_item,
    handle_examine,
    handle_use_item,
    handle_maze_movement,
    GAME_CONFIG
)


def default_state():
    return {
        "location": "forest_entry",
        "inventory": [],
        "visited": [],
        "event_flags": {},
        "maze_mode": False,
        "maze_position": None,
        "collected_items": [],
        "just_entered": True
    }


@pytest.fixture
def mock_config():
    return {**GAME_CONFIG}


def test_valid_movement(mock_config):
    state = default_state()
    result = handle_movement(state, "right", mock_config)
    assert result["state"]["location"] == "shrouded_path"
    assert "config" in result


def test_take_item(mock_config):
    state = default_state()
    state["location"] = "shrouded_path"
    result = handle_take_item(state, "relic", mock_config)
    assert isinstance(result, dict)
    assert "relic" in result["state"]["inventory"]
    assert "you take" in result["output"].lower()


def test_examine_item_in_inventory(mock_config):
    state = default_state()
    state["inventory"].append("relic")
    result = handle_examine(state, "relic")
    assert isinstance(result, dict)
    assert "output" in result
    assert isinstance(result["output"], str)
    assert result["output"].strip() != ""



def test_examine_room_description(mock_config):
    state = default_state()
    result = handle_examine(state)
    assert "forest" in result["output"].lower() or "you" in result["output"].lower()


def test_use_invalid_item(mock_config):
    state = default_state()
    state["inventory"].append("key")
    result = handle_use_item(state, "key", mock_config)
    assert "no effect" in result["output"].lower() or "nothing here" in result["output"].lower()


def test_maze_invalid_wall(mock_config):
    state = default_state()
    state["location"] = "whispering_cave"
    state["maze_mode"] = True
    state["maze_position"] = [0, 0]
    maze = mock_config["rooms"]["whispering_cave"]["maze"]
    maze["layout"][0][1] = '#'
    result = handle_maze_movement(state, "right", mock_config)
    assert "blocks your path" in result["output"].lower()


def test_maze_trap(mock_config):
    state = default_state()
    state["location"] = "whispering_cave"
    state["maze_mode"] = True
    state["maze_position"] = [0, 0]
    maze = mock_config["rooms"]["whispering_cave"]["maze"]
    maze["layout"][1][0] = maze["trap_symbol"]
    result = handle_maze_movement(state, "forward", mock_config)
    assert "trap" in result["output"].lower()
    assert result["state"]["maze_position"] == maze["start"]


def test_maze_exit_reward(mock_config):
    state = default_state()
    state["location"] = "whispering_cave"
    state["maze_mode"] = True
    state["maze_position"] = [1, 1]
    maze = mock_config["rooms"]["whispering_cave"]["maze"]
    maze["layout"][1][2] = maze["exit_symbol"]
    maze["reward_item"] = "enchanted_sword"
    result = handle_maze_movement(state, "right", mock_config)
    assert "sword" in result["output"].lower()
    assert "enchanted_sword" in result["state"]["inventory"]
    assert result["state"]["maze_completed"] is True
