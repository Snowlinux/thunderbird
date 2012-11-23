#!/usr/bin/python

import os, sys, commands

archi = sys.argv[1]
curdir = sys.argv[2]
release = sys.argv[3]
abort = False 

release = version
if "+" in version:
    if "lmde" not in version:
        abort = True
    release = version.split("+")[0]   
    
if "~" in version:
    release = version.split("~")[0]

if archi == "amd64":
    archi="linux-x86_64"
else:
    archi="linux-i686"

locales = {}
locales['ar'] = 'ar'
locales['bn-BD'] = 'bn'
locales['cs'] = 'cs'
locales['da'] = 'da'
locales['de'] = 'de'
locales['el'] = 'el'
locales['en-GB'] = 'en-gb'
locales['en-US'] = 'en-us'
locales['es-ES'] = 'es'
locales['fi'] = 'fi'
locales['fr'] = 'fr'
locales['he'] = 'he'
locales['hu'] = 'hu'
locales['id'] = 'id'
locales['it'] = 'it'
locales['ja'] = 'ja'
locales['ko'] = 'ko'
locales['nb-NO'] = 'nb'
locales['nl'] = 'nl'
locales['nn-NO'] = 'nn'
locales['pl'] = 'pl'
locales['pt-PT'] = 'pt'
locales['pt-BR'] = 'pt-br'
locales['ro'] = 'ro'
locales['ru'] = 'ru'
locales['sv-SE'] = 'sv'
locales['tr'] = 'tr'
locales['uk'] = 'uk'
locales['zh-CN'] = 'zh'

for locale in locales:
    if (locale == "en-US"):
        os.system("mkdir -p %s/debian/thunderbird/opt" % curdir)
        os.system("mkdir -p %s/debian/thunderbird-l10n-%s/opt/thunderbird" % (curdir, locales[locale]))
        os.chdir("%s/debian/thunderbird/opt" % curdir)
    else:
        os.system("mkdir -p %s/debian/thunderbird-l10n-%s/opt" % (curdir, locales[locale]))
        os.chdir("%s/debian/thunderbird-l10n-%s/opt" % (curdir,locales[locale]))

    if not abort:        
        os.system("wget http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/%s/%s/thunderbird-%s.tar.bz2" % (archi, locale, release))
        if (not os.path.exists("thunderbird-%s.tar.bz2" % release)):
            print "FAILED: Could not download http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/%s/%s/thunderbird-%s.tar.bz2" % (archi, locale, release)
            sys.exit(1)

        os.system("bzip2 -d thunderbird-%s.tar.bz2" % release)
        os.system("tar xvf thunderbird-%s.tar" % release)
        os.system("rm thunderbird-%s.tar" % release)
                
        if (locale == "en-US"):
            os.system("mv thunderbird/omni.ja %s/debian/thunderbird-l10n-%s/opt/thunderbird/omni.ja" % (curdir, locales[locale]))                    
        else:        
            os.system("mv thunderbird/omni.ja ./")
            os.system("rm -rf thunderbird/*")
            os.system("mv omni.ja thunderbird/")

os.chdir(curdir)
