import os
import argparse
import time
import shutil
import sys
sys.path.append('../src')
from clustering import Clustering

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--design", help="design_name: ariane, MegaBoom_x2 ", type = str, default = "ariane")
    parser.add_argument("--fixed_file", help="fixed file generated by grouping", type = str, default = "./fix_files_grouping/ariane.fix.old")
    parser.add_argument("--step_threshold", help = "threshold (x and y) to break clusters (in um)", type = float, default = 400.0)
    parser.add_argument("--distance", help="distance for merge clusters", type = float, default = 200.0)
    parser.add_argument("--grid_width", help="grid width, the width of soft macro", type = int, default = 100.0)
    parser.add_argument("--max_num_vertices", help="threshold for samller clusters", type = int, default = 100)
    parser.add_argument("--net_size_threshold",  help = "large net threshold", type = int, default = 300)
    parser.add_argument("--Nparts",  help = "number of clusters (only for hmetis, default  = 500)", type = int, default = 500)
    parser.add_argument("--setup_file", help = "setup file for openroad (default = setup.tcl)", type = str, default = "setup.tcl")
    parser.add_argument("--RePlace", help = "Run RePlace for blob placement (default = True)", type = bool, default = False)
    parser.add_argument("--placement_density", help = "Placement density for RePlace (default = 0.7)", type = float, default = 0.7)
    parser.add_argument("--GUI", help = "Run OpenROAD in GUI Mode (default = True)", type = bool, default = False)
    args = parser.parse_args()

    design = args.design

    # The fixed file should be generated by our grouping script in the repo.
    # Here we should use *.fix.old as the fix file.
    # *.fix.old includes the IOs and Macros in the corresponding group, thus
    # we don't need to change the hypergraph when we do partitioning.
    # Then we will remove all the IOs and Macros when we create soft blocks.
    fixed_file = args.fixed_file

    step_threshold = args.step_threshold
    distance = args.distance
    grid_width = args.grid_width
    max_num_vertices = args.max_num_vertices
    net_size_threshold = args.net_size_threshold
    Nparts = args.Nparts
    setup_file = args.setup_file
    RePlace  = args.RePlace
    placement_density = args.placement_density
    GUI = args.GUI


    # To use the grouping function, you need to specify the directory of src file
    src_dir = "../src"

    Clustering(design, src_dir, fixed_file, step_threshold, distance, grid_width,
            max_num_vertices, net_size_threshold, Nparts, setup_file,
            RePlace, placement_density, GUI)






