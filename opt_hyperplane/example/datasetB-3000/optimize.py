from opt_hyperplane.solver.hyperplane import HyperPlaneOptimizer

opt = HyperPlaneOptimizer("./datasetB-3000.json", "./solution.lp", "./solution.result")
opt.optimize()