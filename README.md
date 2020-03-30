# pomegranate-mathematica

A small package to parse Wolfram Mathematica distributions and get pomegranate objects instead, so it is operable from python. For the reference on how to use distributions from pomegranate consult [their documentation](https://pomegranate.readthedocs.io/en/latest/index.html)

## Install with pip
```
pip install pomegranate-mathematica
```

## Requirements

* pomegranate (only tested for 0.11)
* lark-parser

## Usage

```
import pomegranate_mathematica as pmmath

pmmath.to_pomegranate("NormalDistribution[1.0, 2.5]")
```

## Why?

I just had plenty of output from Wolfram Mathematica, and converting it manually to pomegranate was too tedious. So here we go.

## What's available?

The list of Wolfram Mathematica distributions that are supported, and their pomegranate counterpart: (If the parser sees something that it can't recognize it throws an exception. GIGO.)

* MixtureDistribution (GeneralMixtureModel in pomegranate)
* NormalDistribution
* LogNormalDistribution
* UniformDistribution
* BernoulliDistribution
* ExponentialDistribution
* PoissonDistribution
* BetaDistribution
* GammaDistribution
