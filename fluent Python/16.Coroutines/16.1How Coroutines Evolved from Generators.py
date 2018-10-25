# 生成器可以作为协程使用。协程是指一个过程，这个过程与调用方协作，产出由调用方提供的值


# 协程最近的演进来自 Python 3.3
# PEP 380 对生成器函数的句法做了两处改动，
# 1.现在，生成器可以返回一个值；以前，如果在生成器中给 return语句提供值，会抛出 SyntaxError 异常。
# 2.新引入了 yield from 句法，使用它可以把复杂的生成器重构成小型的嵌套生成器，省去了之前把生成器的工作委托给子生成器所需的大量样板代码。
