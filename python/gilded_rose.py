# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class FactoryItems(ABC):
    def __init__(self, item: Item):
        self.items = item

    @abstractmethod
    def update_quality(self) -> None:
        pass


class NormalItem(FactoryItems):
    def update_quality(self) -> None:
        """
        Represents a normal item that degrades in quality over time.

        - `sell_in` decreases by 1 each day.
        - `quality` decreases by 1 per day.
        - Once the `sell_in` date has passed (`sell_in < 0`), `quality` decreases twice as fast (2 per day).
        - `quality` is never negative.
        - If initialized with `quality > 50`, it will be capped at 50 during the next update to enforce the quality ceiling.

        """
        self.items.sell_in -= 1
        degrade_item = 2 if self.items.sell_in < 0 else 1
        self.items.quality = max(0, self.items.quality - degrade_item)
        if self.items.quality > 50:
            self.items.quality = 50


class AgedBrieItem(FactoryItems):
    def update_quality(self) -> None:
        """
        Aged Brie is a special item that increases in quality the older it gets.

        - Each day, its `sell_in` decreases by 1.
        - Its `quality` increases by 1 per day.
        - If `quality` is below 1, it gets an additional increase (though this may not be necessary based on rules).
        - Quality is capped at 50, and the logic ensures it never exceeds this limit.
        """
        self.items.sell_in -= 1
        self.items.quality += 1
        if self.items.quality < 1:
            self.items.quality += 1
        elif self.items.quality > 50:
            # NOTE: I could decrement the value by 1, however, this is to
            # avoid a situation where we manually assigned the value greater
            # than 51, for e.g. 52 then a decrementing would make it by 1
            # would make it 51 and not 50.
            self.items.quality = 50


class Sulfuras(FactoryItems):
    def update_quality(self) -> None:
        """Sulfuras is legendary: no changes to sell_in or quality."""
        pass


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
