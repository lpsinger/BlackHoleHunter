#!/bin/bash
files=`ls -d m1*`
i=1
for file in $files; do
  mv -f $file sigbank$i
  let i="$i+1"
done
