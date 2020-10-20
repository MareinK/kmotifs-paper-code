# implementation of Sequitur algorithm

import itertools
import math
import random


def escape(s):
    return (str(s).
            replace(' ', '·').
            replace('\t', '↹').
            replace('\n', '↵'))


class Symbol:
    _digrams = None

    def __init__(self, value):
        self.prev = self.next = None
        self.value = value
        if type(self.value) is Rule and self.value is not self:
            self.value.occurances.add(self)

    @property
    def digram(self):
        return (self.value, self.next.value)

    @property
    def rule(self):
        nxt = self.next
        while type(nxt) is not Rule:
            nxt = nxt.next
        return nxt

    def insert_after(self, symbol):
        symbol.join(self.next)
        self.join(symbol)

    def join(self, right):
        if self.next:
            self.delete_digram()
        self.next = right
        right.prev = self

    def delete_digram(self):
        if type(self) is Rule or type(self.next) is Rule:
            return
        if Symbol._digrams.get(self.digram) == self:
            del Symbol._digrams[self.digram]

    def check(self):
        if type(self) is Rule or type(self.next) is Rule:
            return False
        if self.digram not in Symbol._digrams:
            Symbol._digrams[self.digram] = self
            return False
        else:
            match = Symbol._digrams[self.digram]
            if match.next is not self:
                self.process_match(match)
            return True

    def process_match(self, match):
        if type(match.prev) is Rule and type(match.next.next) is Rule:
            rule = match.prev.value
            self.substitute(rule)
        else:
            rule = Rule()
            rule.last.insert_after(Symbol(self.value))
            rule.last.insert_after(Symbol(self.next.value))
            match.substitute(rule)
            self.substitute(rule)
            Symbol._digrams[rule.first.digram] = rule.first
        if type(rule.first.value) is Rule and rule.first.value.underused:
            rule.first.expand()

    def substitute(self, rule):
        prev = self.prev
        prev.next.delete()
        prev.next.delete()
        prev.insert_after(Symbol(rule))
        if not prev.check():
            prev.next.check()

    def delete(self):
        self.prev.join(self.next)
        if not type(self) is Rule:
            self.delete_digram()
            if type(self.value) is Rule:
                self.value.occurances.remove(self)

    def expand(self):
        assert type(self.value) is Rule
        if Symbol._digrams[self.digram] is self:
            del Symbol._digrams[self.digram]
        self.prev.join(self.value.first)
        self.value.last.join(self.next)
        Symbol._digrams[self.value.last.digram] = self.value.last
        Rule._rules.remove(self.value)


class Rule(Symbol):
    _identifier = itertools.count()
    _rules = None

    def __init__(self):
        super().__init__(self)
        self.identifier = next(Rule._identifier)
        self.occurances = set()
        self.join(self)
        Rule._rules.add(self)

    @property
    def first(self):
        return self.next

    @property
    def last(self):
        return self.prev

    @property
    def underused(self):
        return len(self.occurances) == 1

    def gather(self, func):
        nxt = self.next
        result = []
        while nxt is not self:
            result.append(func(nxt))
            nxt = nxt.next
        return result

    @property
    def values(self):
        return self.gather(lambda s: s.value)

    @property
    def expression(self):
        def expr(symbol):
            if type(symbol.value) is Rule:
                return symbol.value.expression
            else:
                return [symbol.value]
        return list(itertools.chain.from_iterable(self.gather(expr)))

    @property
    def score(self):
        return self.usage_count

    @property
    def usage_count(self):
        count = 0
        for occurance in self.occurances:
            if occurance is not None:
                count += occurance.rule.usage_count
            else:
                count += 1
        return count

    def __str__(self):
        return f'${self.identifier}'

    def __repr__(self):
        values = ' '.join(map(escape, self.values))
        score = round(self.score, 2)
        expression = ''.join(map(escape, self.expression))
        return f'{self.identifier} → {values} :{score}: {expression}'


class Grammar(dict):
    def top(self, n):
        candidates = [rule for rule in self.values() if rule.identifier != 0]
        return sorted(candidates, key=lambda r: -r.score)[:n]

    def __str__(self):
        rules = self.values()
        ids = [r.identifier for r in rules]
        vals = [' '.join(map(escape, r.values)) for r in rules]
        scores = [round(r.score, 2) for r in rules]
        exprs = [''.join(map(escape, r.expression)) for r in rules]
        maxid = max(map(len, map(str, ids)))
        maxval = min(30, max(map(len, vals[1:])))
        maxscore = max(map(len, map(str, scores)))
        f = '{0:>{4}} → {1:<{5}} :{2:>{6}}: {3}'
        zipped = zip(ids, vals, scores, exprs)
        lines = [f.format(*d, maxid, maxval, maxscore) for d in zipped]
        return '\n'.join(lines)


def grammar(values):
    Symbol._digrams, Rule._rules = dict(), set()
    root = Rule()
    root.occurances.add(None)

    for value in values:
        root.last.insert_after(Symbol(value))
        root.last.prev.check()
    rules = extract_rules(root)
    Symbol._digrams = Rule._rules = None
    return rules


def extract_rules(root):
    identifier = itertools.count()
    rules = Grammar()

    def process(s):
        if type(s.value) is Rule and s.value not in rules.values():
            s.value.identifier = next(identifier)
            rules[s.value.identifier] = s.value
            s.value.gather(process)

    process(root)
    return rules


if __name__ == '__main__':
    s = """One ring to rule them all
One ring to find them
One ring to bring them all
And in the darkness bind them"""
    g = grammar(list(s))
    print(g)
