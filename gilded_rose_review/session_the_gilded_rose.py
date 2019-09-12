# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.sell_in -= 1

            # guard clauses to handle special items
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            elif item.name == "Aged Brie":
                self.process_aged_brie(item)
                continue

            elif "Conjured" in item.name:
                item.quality -= 2
                if item.sell_in < 0:
                    item.quality -= 2
                item.quality = max(item.quality, 0)
                continue

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.process_backstage_pass(item)
                continue

            else:  #  default items
                self.process_normal(item)

    def process_aged_brie(self, item):
        item.quality += 1
        if item.sell_in < 0:
            item.quality += 1
        item.quality = min(item.quality, 50)  # guard clause

    def process_normal(self, item):
        item.quality -= 1
        if item.sell_in < 0:  # past due date, quality degrades twice as fast
            item.quality -= 1
        item.quality = max(item.quality, 0)

    def process_backstage_pass(self, item):
        if item.sell_in < 0:  # guard clause
            item.quality = 0
        elif item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(item.quality, 50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
