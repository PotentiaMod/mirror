import glob

for path in glob.glob('scratch-gui/build/**/*.js', recursive=True):
    print(f'Patching JS {path}')
    with open(path, 'r') as f:
        contents = f.read()
        contents = contents.replace(
            'https://trampoline.turbowarp.org',
            'https://trampoline.turbowarp.xyz'
        )
    with open(path, 'w') as f:
        f.write(contents)
