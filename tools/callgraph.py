#!/usr/bin/env python3
import argparse
import os
import subprocess
import re
import pydot

def run_clang(files, defines=None, extra=None):
    cmd = [
        "clang",
        "-c",
        "-Wno-implicit-function-declaration",
        "-Xclang",
        "-analyze",
        "-Xclang",
        "-analyzer-checker=debug.DumpCallGraph",
    ]
    if defines:
        for d in defines:
            cmd.extend(["-D", d])
    if extra:
        cmd.extend(extra)
    includes = [
        ".",
        "quantum",
        "quantum/pointing_device",
        "drivers",
        "drivers/sensors",
        "tmk_core",
        "tmk_core/protocol",
        "platforms",
    ]
    for inc in includes:
        if os.path.isdir(inc):
            cmd.extend(["-I", inc])
    cmd.extend(files)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.stdout

def parse_graph(output):
    edges = []
    pattern = re.compile(r"Function:\s*(\S+)\s*calls:\s*(.*)")
    for line in output.splitlines():
        m = pattern.search(line)
        if m:
            func = m.group(1)
            callees = [c for c in m.group(2).split() if c]
            for callee in callees:
                edges.append((func, callee))
    return edges

def build_graph(edges):
    graph = pydot.Dot(graph_type="digraph", rankdir="LR")
    for src, dst in edges:
        graph.add_edge(pydot.Edge(src, dst))
    return graph

def main():
    parser = argparse.ArgumentParser(description="Generate call graph using clang")
    parser.add_argument("files", nargs="*", default=["drivers/sensors/azoteq_iqs5xx.c"], help="C source files")
    parser.add_argument("-o", "--output", default="docs/azoteq_callgraph.svg", help="Output SVG path")
    parser.add_argument("-D", "--define", dest="defines", action="append", default=["AZOTEQ_IQS5XX_TPS43"], metavar="MACRO", help="Macro definition for clang")
    args = parser.parse_args()

    clang_out = run_clang(args.files, defines=args.defines)
    edges = parse_graph(clang_out)
    graph = build_graph(edges)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    graph.write_svg(args.output)
    if os.path.isfile(args.output) and os.path.getsize(args.output) > 0:
        print(f"Call graph written to {args.output}")
    else:
        print("Failed to write call graph")

if __name__ == "__main__":
    main()
