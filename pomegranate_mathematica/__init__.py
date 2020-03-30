from lark import Lark, Transformer
from pomegranate import GeneralMixtureModel
from pomegranate.distributions import *

class MathematicaTransformer(Transformer):
    """
    Transformes parsed tree of Wolfram Mathematica distribution expression 
    into a pomegranate object
    """
    def posfloat(self, args):
        return float(args[0].value)
    
    def negfloat(self, args):
        return -float(args[0].value)
    
    def listelement(self, args):
        return args[0]
    
    def _list(self, args):
        return args
    
    def distribution(self, args):
        return args[0]
    
    def mixture(self, args):
        weights = args[0]
        distributions = args[1]
        return GeneralMixtureModel(distributions, weights=weights)
    
    def normal(self, args):
        return NormalDistribution(mean=args[0], std=args[1])
    
    def lognormal(self, args):
        return LogNormalDistribution(mu=args[0], sigma=args[1])
    
    def uniform(self, args):
        return UniformDistribution(start=args[0][0], end=args[0][1])
    
    def bernoulli(self, args):
        return BernoulliDistribution(p=args[0])
    
    def exponential(self, args):
        return ExponentialDistribution(rate=args[0])
    
    def poisson(self, args):
        return PoissonDistribution(l=args[0])
    
    def beta(self, args):
        return BetaDistribution(alpha=args[0], beta=args[1])
    
    def gamma(self, args):
        return GammaDistribution(alpha=args[0], beta=args[1])
    
parser = Lark('''distribution: mixture
                | lognormal
                | normal
                | uniform
                | bernoulli
                | exponential
                | poisson
                | beta
                | gamma
                
            mixture: "MixtureDistribution[" list "," list "]"
            
            normal: "NormalDistribution[" float "," float "]"
            lognormal: "LogNormalDistribution[" float "," float "]"
            uniform: "UniformDistribution[" list "]"
            bernoulli: "BernoulliDistribution[" float "]"
            exponential: "ExponentialDistribution[" float "]"
            poisson: "PoissonDistribution[" float "]"
            beta: "BetaDistribution[" float "," float "]"
            gamma: "GammaDistribution[" float "," float "]"
            
            list: "{" (listelement ",")* listelement "}" -> _list
            listelement: float | distribution
            float: "-" NUMBER -> negfloat
                | NUMBER -> posfloat
            
            %import common.NUMBER
            %ignore " "           // Disregard spaces in text
         ''', start="distribution")

def to_pomegranate(mathematica):
    """
    Returns a pomegranate distribution object. Note: it throws an exception if a Mathematica expression cannot be parsed
    
    arguments:
        mathematica -- a string containing Wolfram Mathematica expression for a distribution
    """
    return MathematicaTransformer().transform(parser.parse(mathematica))