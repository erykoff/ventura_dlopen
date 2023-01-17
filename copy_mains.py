#!/usr/bin/env python

import os

base_file = "ventura_dlopen/main0.cpp"

nfiles = 500

counters = []

for counter in range(nfiles):
    out_file = f"ventura_dlopen/main{counter}.cpp"

    if os.path.isfile(out_file):
        continue

    with open(base_file, "r") as f_in:
        with open(out_file, "w") as f_out:
            line = f_in.readline()
            while line:
                if "PYBIND11_MODULE" in line:
                    f_out.write(f"PYBIND11_MODULE(_test{counter}, m)"" {\n")
                else:
                    f_out.write(line)
                line = f_in.readline()

init_file = "ventura_dlopen/__init__.py"

with open(init_file, "w") as f_init:
    for counter in range(nfiles):
        f_init.write(f"from ._test{counter} import add as add{counter}\n")
        f_init.write(f"from ._test{counter} import subtract as subtract{counter}\n")
