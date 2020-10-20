# script that was used to rename the original .xlsx files to the form 'batch_trial.xlsx'

import shutil, os, re

TRIAL_PATTERN = re.compile(r'Trial\s+(\d+)')

for dirpath, dirname, filenames in os.walk('.'):
  if dirpath != '.':
    for filename in filenames:
      batch = os.path.basename(dirpath)
      trial = int(TRIAL_PATTERN.search(filename).groups()[0])
      _, ext = os.path.splitext(filename)
      oldfile = os.path.join(dirpath,filename)
      newfile = f'{batch}_{trial:03d}{ext}'
      shutil.copyfile(oldfile,newfile)
