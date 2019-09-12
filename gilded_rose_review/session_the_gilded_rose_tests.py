# -*- coding: utf-8 -*-
import unittest

from session_the_gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]  # name, sell_in, quality
        gilded_rose = GildedRose(items) # instance of GildedRose class with items as arg
        gilded_rose.update_quality()  # i.e. progress 1 day, adjust Quality & Sell-in value accordingly
        self.assertEqual("foo", items[0].name)  # tests that name is correct, item was created properly

    def test_sulfuras_quality_stays_at_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]  # chose a random high sell-in
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)  # tests that quality remains at 80

    def test_sulfuras_past_date_stays_at_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)  # expect quality to remain at 80

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 20, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)  # expect sell-in to reduce
        # Note! two tests here. If first fails, we won't get error message from the second test
        self.assertEqual(31, items[0].quality)  # expect quality to increase

    def test_aged_brie_increases_by_2_after_date(self):
        items = [Item("Aged Brie", 0, 37)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, items[0].quality)  # expect quality to increase twice as fast after due date


    def test_aged_brie_hits_50_quality(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)  # expect quality to be capped at 50

    def test_normal_item(self):
        items = [Item("Rat Soup", 20, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    def test_normal_item_degrades_twice_as_fast(self):
        items = [Item("Rat Soup", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)  # expect to degrade twice as fast once past due date

    def test_normal_item_quality_stops_at_0(self):
        items = [Item("Rat Soup", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)  # no item shouold have negative quality

    def test_backstage_pass_increases_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(26, items[0].quality)

    def test_backstage_pass_cannot_exceed_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_pass_less_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(27, items[0].quality)  # expect quality to increase by 2 for sell-in below 10 days

    def test_backstage_pass_less_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)  # expect quality to increase by 3 for sell-in below 5 days

    def test_backstage_pass_less_than_0_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)  # expect quality to increase by 3 for sell-in below 5 days

    def test_conjured_item_degrading(self):
        items = [Item("Conjured Mana Potion", 15, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality) # degrade twice as fast as normal items, -2 before due date

    def test_conjured_item_at_0_quality(self):
        items = [Item("Conjured Mana Potion", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(36, items[0].quality) # degrade twice as fast as normal items, -4 after due date

if __name__ == '__main__':
    unittest.main()
