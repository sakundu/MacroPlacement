#!/usr/bin/env bash
##########################################################################
# Update HMETIS_DIR PLC_WRAPPER_MAIN and CT_PATH
##########################################################################
if [ $PHY_SYNTH -eq 1 ]; then
    export PROJ_DIR=`pwd | grep -o '\S*/MacroPlacement'`
    export NETLIST_FILE=`readlink -f *.pb.txt`
    export BLOCK_NAME=`basename ${NETLIST_FILE} | sed 's@.pb.txt@@'`
    export TECH=`echo $PWD | awk -F'/' '{print $(NF-3)}'`
    export OUTPUT_DIR="./output_${BLOCK_NAME}_${TECH}"
    export HMETIS_DIR="${PROJ_DIR}/../../../GB/CT/hmetis-1.5-linux"
    export PLC_WRAPPER_MAIN="${PROJ_DIR}/../../../GB/CT/plc_wrapper_main"
    export CT_PATH="${PROJ_DIR}/../../../GB/CT/circuit_training"
    bash -i ../../../../util/run_grp.sh 2>&1 | tee log/grouping.log
fi
