#!/usr/bin/env python3
import argparse
import os
import subprocess
import re
import pydot

# Default configuration for known drivers
DRIVERS = {
    "azoteq": {
        "files": ["drivers/sensors/azoteq_iqs5xx.c"],
        "output": "docs/azoteq_callgraph.svg",
        "defines": ["AZOTEQ_IQS5XX_TPS43"],
    },
    "pimoroni": {
        "files": ["drivers/sensors/pimoroni_trackball.c"],
        "output": "docs/pimoroni_callgraph.svg",
        "defines": [],
    },
    "cirque": {
        "files": ["drivers/sensors/cirque_pinnacle.c"],
        "output": "docs/cirque_callgraph.svg",
        "defines": [],
    },
    "trackpoint": {
        "files": ["drivers/ps2/ps2_mouse.c"],
        "output": "docs/trackpoint_callgraph.svg",
        "defines": [],
    },
}


def run_clang(files, defines=None, extra=None):
    """Invoke clang static analyzer and return raw output."""
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
        "quantum/logging",
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
    """Parse clang output into call graph edges."""
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


def gen_callgraph(files, output, defines=None, extra=None):
    """Generate a call graph SVG from source files."""
    clang_out = run_clang(files, defines=defines, extra=extra)
    edges = parse_graph(clang_out)
    graph = build_graph(edges)

    os.makedirs(os.path.dirname(output), exist_ok=True)
    graph.write_svg(output)
    if os.path.isfile(output) and os.path.getsize(output) > 0:
        print(f"Call graph written to {output}")
        return True
    print(f"Failed to write call graph to {output}")
    return False


def main():
    parser = argparse.ArgumentParser(description="Generate call graph using clang")
    parser.add_argument("files", nargs="*", help="C source files")
    parser.add_argument("-o", "--output", help="Output SVG path")
    parser.add_argument(
        "-D", "--define", dest="defines", action="append", metavar="MACRO", help="Macro definition for clang"
    )
    parser.add_argument(
        "--driver", choices=DRIVERS.keys(), default="azoteq", help="Use predefined settings for a driver"
    )
    args = parser.parse_args()

    cfg = DRIVERS.get(args.driver, {})
    files = args.files or cfg.get("files")
    output = args.output or cfg.get("output")
    defines = args.defines if args.defines is not None else cfg.get("defines")

    if not files or not output:
        parser.error("No source files or output specified")

    gen_callgraph(files, output, defines=defines)


if __name__ == "__main__":
    main()
