from opt_hyperplane.solver.hyperplane import HyperPlaneOptimizer

opt = HyperPlaneOptimizer("./datasetA-5000.json", "./solution.lp", "./solution.result")
opt.optimize()