def get_building(quadrangle, room_number):
    """Finds and returns the building that a room is in for a specific quadrangle, or None"""

    quadrangle = quadrangle.lower()

    def in_ranges(ranges):
        """Determines if a room is in a list of ranges (each specified by tuples)"""
        for first, last in ranges:
            if first <= room_number <= last:
                return True
        return False

    if quadrangle == "fargo":
        if in_ranges([(201, 208), (301, 311), (401, 417)]):
            return 1
        elif in_ranges([(209, 218), (312, 324), (418, 434)]):
            return 2
        elif in_ranges([(219, 226), (325, 334), (435, 450)]):
            return 3
        elif in_ranges([(551, 554), (651, 656), (751, 754), (851, 856), (951, 957), (1051, 1058)]):
            return 4
        elif in_ranges([(361, 364), (461, 464), (561, 566)]):
            return 5
        elif in_ranges([(365, 372), (465, 475), (567, 584)]):
            return 6
        elif in_ranges([(148, 149), (386, 388), (486, 491), (586, 589), (686, 691), (786, 793)]):
            return 7
    elif quadrangle == "porter":
        if in_ranges([(203, 208), (303, 311), (405, 417)]):
            return 1
        elif in_ranges([(209, 215), (312, 321), (418, 431)]):
            return 2
        elif in_ranges([(216, 219), (322, 326), (432, 440)]):
            return 3
        elif in_ranges([(551, 554), (641, 646), (741, 744), (841, 846), (941, 947), (1041, 1048)]):
            return 4
        elif in_ranges([(341, 346), (441, 447), (540, 550)]):
            return 5
        elif in_ranges([(361, 370), (461, 473), (561, 581)]):
            return 6
        elif in_ranges([(301, 302), (401, 404), (501, 506), (601, 604), (701, 706), (801, 807)]):
            return 7
    elif quadrangle == "red_jacket":
        if in_ranges([(201, 210), (301, 313), (401, 421)]):
            return 1
        elif in_ranges([(211, 219), (314, 325), (422, 439)]):
            return 2
        elif in_ranges([(326, 333), (440, 450), (540, 559)]):
            return 3
        elif in_ranges([(585, 588), (676, 681), (776, 779), (876, 881), (976, 982), (1076, 1083)]):
            return 4
        elif in_ranges([(361, 372), (461, 475), (561, 584)]):
            return 5
        elif in_ranges([(191, 192), (391, 394), (491, 496), (591, 594), (691, 696), (791, 797)]):
            return 6
    elif quadrangle == "richmond":
        if in_ranges([(201, 210), (301, 313), (401, 420)]):
            return 1
        elif in_ranges([(211, 219), (314, 325), (421, 439)]):
            return 2
        elif in_ranges([(341, 348), (441, 451), (541, 560)]):
            return 3
        elif in_ranges([(561, 564), (661, 667), (761, 764), (861, 866), (961, 967), (1061, 1068)]):
            return 4
        elif in_ranges([(371, 382), (471, 485), (571, 594)]):
            return 5
        elif in_ranges([(191, 192), (391, 394), (491, 496), (595, 598), (691, 696), (791, 797)]):
            return 6
    elif quadrangle == "spaulding":
        if in_ranges([(215, 220), (318, 323), (426, 434)]):
            return 1
        elif in_ranges([(207, 214), (307, 317), (409, 425)]):
            return 2
        elif in_ranges([(201, 206), (301, 306), (401, 408)]):
            return 3
        elif in_ranges([(576, 579), (676, 681), (776, 779), (876, 881), (976, 983), (1076, 1083)]):
            return 4
        elif in_ranges([(379, 384), (485, 491), (580, 590)]):
            return 5
        elif in_ranges([(351, 360), (451, 463), (551, 572)]):
            return 6
        elif in_ranges([(341, 342), (441, 444), (540, 545), (641, 644), (741, 746), (841, 848)]):
            return 7
    elif quadrangle == "wilkeson":
        if in_ranges([(224, 230), (328, 334), (443, 452)]):
            return 1
        elif in_ranges([(213, 223), (314, 327), (425, 442)]):
            return 2
        elif in_ranges([(203, 212), (304, 313), (409, 424)]):
            return 3
        elif in_ranges([(501, 504), (601, 606), (701, 704), (801, 806), (901, 908), (1001, 1008)]):
            return 4
        elif in_ranges([(377, 380), (477, 480), (588, 595)]):
            return 5
        elif in_ranges([(367, 376), (467, 476), (574, 587)]):
            return 6
        elif in_ranges([(256, 257), (356, 366), (456, 466), (556, 573)]):
            return 8
    return None
