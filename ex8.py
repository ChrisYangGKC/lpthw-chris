#!/usr/bin/env python
# -*- coding: utf-8 -*-

formatter = "%s %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("One", "Two", "Three", "Four")

print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) 