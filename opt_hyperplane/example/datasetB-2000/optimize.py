from opt_hyperplane.solver.hyperplane import HyperPlaneOptimizer

opt = HyperPlaneOptimizer("./datasetB-2000.json", "./solution.lp", "./solution.result")
opt.optimize()