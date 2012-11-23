#!/bin/bash

ARCHI=$1
CURDIR=$2
RELEASE=$3
if [[ $ARCHI == *amd64* ]]; then
 ARCH_URL="x86_64"
else
 ARCH_URL="i686"
fi

echo "Downloading Thunderbird for $ARCHI"
cd $CURDIR/debian/thunderbird/opt
wget http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-$ARCH_URL/en-US/thunderbird-$RELEASE.tar.bz2
bzip2 -d thunderbird-$RELEASE.tar.bz2 || exit 1
tar xvf thunderbird-$RELEASE.tar
rm thunderbird-$RELEASE.tar
rm thunderbird/omni.ja
cd $CURDIR



