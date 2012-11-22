#!/bin/bash

ARCHI=`getconf LONG_BIT`
if [[ $ARCHI == *64* ]]; then
 ARCHI="amd64"
 ARCH_URL="x86_64"
else
 ARCHI="i386"
 ARCH_URL="i686"
fi

mkdir -p opt
rm -rf opt/*
cd opt
wget --quiet -nd -r -l1 --no-parent -A "*.bz2" http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-$ARCH_URL/en-US/

RELEASE=`ls thunderbird* | cut -d "-" -f2 | sed "s/.tar.bz2//"`
bzip2 -d thunderbird-$RELEASE.tar.bz2
tar xf thunderbird-$RELEASE.tar
rm thunderbird-$RELEASE.tar
rm thunderbird/omni.ja
cd ..

echo "Downloaded thunderbird $RELEASE for $ARCHI"

rm -rf opt/robots.txt

export DEBFULLNAME='Clement Lefebvre'
export DEBEMAIL='root@linuxmint.com'
dch -v "$RELEASE" -b

dpkg-buildpackage -us -uc -rfakeroot


