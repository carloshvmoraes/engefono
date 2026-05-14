import os

posts_dir = 'posts'
output_file = 'merged_posts.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(posts_dir):
        filepath = os.path.join(posts_dir, filename)
        print(f'Merging {filepath}...')
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')