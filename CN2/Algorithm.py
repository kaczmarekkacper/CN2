from Rule import Rule


class Algorithm:
    def __init__(self, train_set):
        self.train_set = train_set
        self.whole_train_set_prob = {}
        self.selectors = None
        self.rule_list = []
        self.star = []
        self.max_star_size = None
        self.min_significance = None

        train_dict = self.__create_dict_by_classes(self.train_set)
        self.whole_train_set_prob = self.__calculate_prob_of_set(train_dict, len(self.train_set))

    @staticmethod
    def __create_dict_by_classes(train_set):
        train_dict = {}
        for example in train_set:
            if example.value in train_dict.keys():
                train_dict[example.value].append(example)
            else:
                train_dict[example.value] = [example]
        return train_dict

    @staticmethod
    def __calculate_prob_of_set(train_dict, set_size):
        set_prob = {}
        for value in train_dict:
            set_prob[value] = len(train_dict[value]) / set_size
        return set_prob

    def learn(self):
        self.rule_list = []
        best_cpx = "smth to start loop"
        while self.train_set and best_cpx:
            best_cpx = self.__find_best_complex(self.train_set)
            if best_cpx:
                self.__remove_examples(self.train_set, best_cpx.examples_covered)
                most_common_class = self.__find_most_common_class_in_set(best_cpx.examples_covered)
                best_cpx.prediction = most_common_class
                self.rule_list.append(best_cpx)
        self.__create_default_rule()

    def __find_best_complex(self, train_set):
        star = self.selectors
        best_cpx = None
        while star:
            new_star = self.__specialize_complexes(star)
            self.__order_complexes_by_scores(new_star, train_set)
            if len(new_star):
                new_star_best_complex = new_star[0]
                if self.__compare_complexes(new_star_best_complex, best_cpx):
                    best_cpx = new_star_best_complex
                if len(new_star) >= self.max_star_size:
                    new_star = new_star[0:self.max_star_size]
            star = new_star
        return best_cpx

    def __specialize_complexes(self, stars):
        new_star = []
        if stars is self.selectors:
            for selector in self.selectors:
                rule = Rule.Rule()
                rule.add_condition(selector[0], selector[1])
                new_star.append(rule)
            return new_star
        else:
            for selector in self.selectors:
                for star in stars:
                    star_copy = Rule.Rule()
                    star_copy.add_existing_conditions(star.conditions)
                    star_copy.add_condition(selector[0], selector[1])
                    if star_copy.check_if_conditions_unique():
                        new_star.append(star_copy)
        return new_star

    def __order_complexes_by_scores(self, new_star, train_set):
        new_star_copy = new_star.copy()
        for star in new_star_copy:
            star.fill_examples_covered(train_set)
            star.calculate_scores(self.whole_train_set_prob)
            if len(star.examples_covered) == 0 or star.significance < self.min_significance:
                new_star.remove(star)
        if len(new_star):
            new_star.sort(key=lambda e: (e.entropy, -len(e.examples_covered), -e.significance))

    @staticmethod
    def __remove_examples(train_set, examples_covered):
        for example in examples_covered:
            train_set.remove(example)

    @staticmethod
    def __find_most_common_class_in_set(examples):
        return max(set(examples), key=lambda e: e.value).value

    @staticmethod
    def __compare_complexes(new_complex, old_complex):
        if not old_complex:
            return True
        list_to_sort= [new_complex, old_complex]
        list_to_sort.sort(key=lambda e: (e.entropy, -len(e.examples_covered), -e.significance))
        if list_to_sort[0] == new_complex:
            return True
        else:
            return False

    def __create_default_rule(self):
        default_rule = Rule.Rule()
        most_common_class = None
        for prediction in self.whole_train_set_prob:
            if not most_common_class:
                most_common_class = prediction
                break
            if self.whole_train_set_prob[prediction] > self.whole_train_set_prob[most_common_class]:
                most_common_class = prediction
        default_rule.default_prediction = most_common_class
        self.rule_list.append(default_rule)

    def test(self, test_set):
        for example in test_set:
            for rule in self.rule_list:
                prediction = rule.eval(example)
                if prediction:
                    example.prediction = prediction
                    break
