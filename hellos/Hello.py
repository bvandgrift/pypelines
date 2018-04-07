#!/usr/bin/env python3


class Hello:
    who = "World"

    def __init__(self):
        self.who = "World"

    def sayIt(self, whom=None):
        print(f'Hello {whom if whom else self.who}!')
