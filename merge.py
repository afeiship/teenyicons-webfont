import glob
import os
icons_solid = glob.glob('src/solid/*.svg')
icons_outline = glob.glob('src/outline/*.svg')

# prepare dist folder
os.system('rm -rf dist')
os.system('mkdir dist')

for icon in icons_solid:
    os.system('cp ' + icon + ' dist/' + icon.split('/')[-1].replace('.svg', '-solid.svg'))

for icon in icons_outline:
    os.system('cp ' + icon + ' dist/' + icon.split('/')[-1].replace('.svg', '-outline.svg'))
