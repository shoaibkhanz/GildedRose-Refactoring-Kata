# -*- coding: utf-8 -*-
import unittest
import pytest

from gilded_rose import (
    Item,
    GildedRose,
    NormalItem,
    AgedBrieItem,
    SulfurasItem,
    BackstagePassesItem,
    ConjuredItem,
)


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_quality",
    [("item1", 0, 0, 0), ("item2", 1, 1, 0), ("item3", 1, 52, 50)],
)
def test__NormalItem__quality_decrease(name, sell_in, quality, expected_quality):
    item = Item(name, sell_in, quality)
    NormalItem(item).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_quality",
    [
        ("item1", 0, 0, 0),
        ("item2", 1, 1, 2),
        ("item3", 1, 52, 50),
    ],
)
def test__AgedBrieItem__quality_increase(name, sell_in, quality, expected_quality):
    item = Item(name, sell_in, quality)
    AgedBrieItem(item).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "item_cls, name, sell_in, quality, expected_quality",
    [
        (AgedBrieItem, "item1", 0, -1, 0),
        (AgedBrieItem, "item2", 1, -10, 0),
        (AgedBrieItem, "item3", 0, 0, 0),
        (NormalItem, "item1", 0, -1, 0),
        (NormalItem, "item2", 1, -10, 0),
        (NormalItem, "item3", 0, 0, 0),
        (BackstagePassesItem, "item1", 0, -1, 0),
        (BackstagePassesItem, "item2", 1, -10, 0),
        (BackstagePassesItem, "item3", 0, 0, 0),
        (ConjuredItem, "item1", 0, -1, 0),
        (ConjuredItem, "item2", 1, -10, 0),
        (ConjuredItem, "item3", 0, 0, 0),
    ],
)
def test__AgedBrieItem__quality_never_neative(
    item_cls, name, sell_in, quality, expected_quality
):
    item = Item(name, sell_in, quality)
    item_cls(item).update_quality()
    assert item.quality == expected_quality


# @pytest.mark.parametrize(
#     "name,sell_in,quality,expected_quality", [("foo", 0, 0, 0), ("foobar", 0, 52, 50)]
# )
# class GildedRoseTest(unittest.TestCase):
#     def test_foo(self, name, sell_in, quality, expected_quality):
#         items = [Item(name, sell_in, quality)]
#         gilded_rose = GildedRose(items)
#         gilded_rose.update_quality()
#         assert ""
