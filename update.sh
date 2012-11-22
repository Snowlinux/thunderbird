#!/bin/bash

ARCHI=$1
CURDIR=$2
if [[ $ARCHI == *amd64* ]]; then
 ARCH_URL="x86_64"
else
 ARCH_URL="i686"
fi

echo "Downloading Thunderbird for $ARCHI"
cd $CURDIR/debian/thunderbird/opt
wget -nd -r -l1 --no-parent -A "*.bz2" http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-$ARCH_URL/en-US/
mv *bz2 thunderbird.tar.bz2
bzip2 -d thunderbird.tar.bz2
tar xvf thunderbird.tar
rm thunderbird.tar
rm thunderbird/omni.ja
rm -rf robots.txt
cd $CURDIR



