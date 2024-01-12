import glob
import os
icons_solid = glob.glob('dist/solid/*.svg')
icons_outline = glob.glob('dist/outline/*.svg')

# prepare dist folder
os.system('mkdir -p dist/all')

for icon in icons_solid:
    os.system('cp ' + icon + ' dist/all/' + icon.split('/')[-1].replace('.svg', '-solid.svg'))

for icon in icons_outline:
    os.system('cp ' + icon + ' dist/all/' + icon.split('/')[-1].replace('.svg', '-outline.svg'))
