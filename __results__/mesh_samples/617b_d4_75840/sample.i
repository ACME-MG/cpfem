
BEGIN SCULPT
    
    # Dimensions
    nelx = 5
    nely = 82
    nelz = 106

    # Mesh Improvement
    smooth = 2
    defeature = 1
    remove_bad = 0.0

    # Remove cuts
    void_mat = 1
    
    # Solver
    laplacian_iters = 10
    max_opt_iters = 100
    # adapt_type = 5
    # adapt_levels = 2
    
    # Output
    input_spn = ./results/221215234846/sample.spn
    exodus_file = ./results/221215234846/sample

END SCULPT