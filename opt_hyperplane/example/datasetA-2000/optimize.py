from opt_hyperplane.solver.hyperplane import HyperPlaneOptimizer

opt = HyperPlaneOptimizer("./datasetA-2000.json", "./solution.lp", "./solution.result")
opt.optimize()