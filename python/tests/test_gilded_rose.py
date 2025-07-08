# -*- coding: utf-8 -*-
# import unittest
import pytest

from gilded_rose import (
    Item,
    GildedRose,
    NormalItem,
    AgedBrieItem,
    # SulfurasItem,
    BackstagePassesItem,
    ConjuredItem,
)


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_quality",
    [("item1", 0, 0, 0), ("item2", 1, 1, 0), ("item3", 1, 50, 49)],
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
        ("item3", 1, 49, 50),
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
def test__quality_never_neative(item_cls, name, sell_in, quality, expected_quality):
    item = Item(name, sell_in, quality)
    item_cls(item).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_quality",
    [
        ("item1", 2, 4, 7),
        ("item2", 12, 1, 2),
        ("item3", 10, 2, 4),
        ("item4", 1, 49, 50),
    ],
)
def test__BackstagePassesItem__quality_increase(
    name, sell_in, quality, expected_quality
):
    item = Item(name, sell_in, quality)
    BackstagePassesItem(item).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_quality",
    [
        ("item1", -1, 4, 0),
        ("item2", 1, 2, 0),
        ("item3", 1, 50, 48),
    ],
)
def test__ConjuredItem__quality_increase(name, sell_in, quality, expected_quality):
    item = Item(name, sell_in, quality)
    ConjuredItem(item).update_quality()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_quality",
    [
        ("+5 Dexterity Vest", 10, 20, 19),
        ("Aged Brie", 2, 0, 0),
        ("Elixir of the Mongoose", 5, 7, 6),
        ("Sulfuras, Hand of Ragnaros", 0, 80, 80),
        ("Sulfuras, Hand of Ragnaros", -1, 80, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20, 21),
        ("Backstage passes to a TAFKAL80ETC concert", 10, 14, 16),
        ("Backstage passes to a TAFKAL80ETC concert", 5, 19, 22),
        ("Backstage passes to a TAFKAL80ETC concert", -1, 50, 0),
        ("Conjured Mana Cake", 3, 6, 4),
    ],
)
def test__GildedRose__single_iteration(name, sell_in, quality, expected_quality):
    item = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(item)
    gilded_rose.update_quality()
    assert item[0].quality == expected_quality
