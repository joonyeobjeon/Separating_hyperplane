from opt_hyperplane.solver.hyperplane import HyperPlaneOptimizer

opt = HyperPlaneOptimizer("./datasetC-xor.json")
opt.optimize()