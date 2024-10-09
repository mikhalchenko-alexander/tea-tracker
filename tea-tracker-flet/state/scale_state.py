from mopyx import model

from scales.weights import empty_teapot_weight, cap_weight, water_min_weight, leaves_min_weight


@model
class ScalesModel:
    def __init__(self):
        self.cup_present = False
        self.cup_weight = 0

        self.tea_present = False
        self.tea_weight = 0

        self.water_present = False
        self.water_weight = 0

        self.lid_present = False
        self.lid_weight = 0

    def reset(self):
        self.cup_present = False
        self.cup_weight = 0

        self.tea_present = False
        self.tea_weight = 0

        self.water_present = False
        self.water_weight = 0

        self.lid_present = False
        self.lid_weight = 0

    def set_total_weight(self, total_weight):
        self.cup_weight = total_weight

    def set_objects(self, objects) -> bool:
        result = False
        teapot_in_objects = 'teapot' in objects
        if self.cup_present != teapot_in_objects:
            result = True
            self.cup_present = teapot_in_objects

        if not self.cup_present:
            self.tea_present = 0

        leaves_in_objects = 'leaves' in objects
        if self.tea_present != leaves_in_objects:
            result = True
            self.tea_present = leaves_in_objects

        if not self.tea_present:
            self.tea_weight = 0

        water_in_objects = 'water' in objects
        if self.water_present != water_in_objects:
            result = True
            self.water_present = water_in_objects

        if not self.water_present:
            self.water_weight = 0

        cap_in_objects = 'cap' in objects
        if self.lid_present != cap_in_objects:
            result = True
            self.lid_present = cap_in_objects

        if not self.lid_present:
            self.lid_weight = 0

        return result

    def set_weights(self, grams) -> bool:
        igrams = int(grams)
        result = False

        if self.cup_present:
            if self.cup_weight == 0:
                self.cup_weight = empty_teapot_weight
                result = True
        elif self.cup_weight > 0:
            self.cup_weight = 0
            result = True

        if self.cup_weight > 0 and self.tea_weight < leaves_min_weight:
            self.tea_weight = igrams - self.cup_weight
            result = True

        if self.cup_weight > 0 and self.tea_weight > 0 and self.water_weight < water_min_weight:
            self.water_weight = igrams - self.cup_weight - self.tea_weight
            if self.water_weight > 0:
                result = True
            if self.water_weight <= 0:
                self.water_weight = 0

        if self.lid_present and self.lid_weight == 0:
            self.lid_weight = cap_weight
            result = True

        return result


scales_model = ScalesModel()
