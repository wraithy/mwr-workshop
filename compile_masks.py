import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process a list of masks into rules')
parser.add_argument('mask_processor_path',  type=str, help='Where Mask Processor is located on your machine')
parser.add_argument('mask_path',  help='Where the masks are stored')
parser.add_argument('output',  help='Where to output the rule file')
args = parser.parse_args()

with open(args.mask_path) as mask_file, open(args.output, "w") as rules_file:
    outs = []
    for line in mask_file:
        line = line.strip()
        if line[0] == "#" or line[0] == "":
            continue
        mask = line
        out = subprocess.check_output([args.mask_processor_path, "'"+mask+"'"])
        outs.extend(out.split("\n"))
    for line in outs:
        rules_file.write(line + "\n")
