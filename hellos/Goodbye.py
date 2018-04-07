#!/usr/bin/env python3


class Goodbye:
    who = "World"

    def sayIt(self, whom=None):
        print(f"Goodbye {whom if whom else self.who}!")
