# roast-your-own-agent: one funny roast of my own agent, written to entry.txt.
import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, 'entry.txt')

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write('My agent narrates its own token consumption like a dying Victorian explorer bidding farewell to the sun.')
