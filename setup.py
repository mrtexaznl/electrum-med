#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-med.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-med.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-med")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-MED",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'medcoin_hybrid'],
    package_dir={
        'electrum_med': 'lib',
        'electrum_med_gui': 'gui',
        'electrum_med_plugins': 'plugins',
    },
    scripts=['electrum-med'],
    data_files=data_files,
    py_modules=[
        'electrum_med.account',
        'electrum_med.bitcoin',
        'electrum_med.blockchain',
        'electrum_med.bmp',
        'electrum_med.commands',
        'electrum_med.daemon',
        'electrum_med.i18n',
        'electrum_med.interface',
        'electrum_med.mnemonic',
        'electrum_med.msqr',
        'electrum_med.network',
        'electrum_med.plugins',
        'electrum_med.pyqrnative',
        #'electrum_med.scrypt',
        'electrum_med.simple_config',
        'electrum_med.socks',
        'electrum_med.synchronizer',
        'electrum_med.transaction',
        'electrum_med.util',
        'electrum_med.verifier',
        'electrum_med.version',
        'electrum_med.wallet',
        'electrum_med.wallet_bitkey',
        'electrum_med_gui.gtk',
        'electrum_med_gui.qt.__init__',
        'electrum_med_gui.qt.amountedit',
        'electrum_med_gui.qt.console',
        'electrum_med_gui.qt.history_widget',
        'electrum_med_gui.qt.icons_rc',
        'electrum_med_gui.qt.installwizard',
        'electrum_med_gui.qt.lite_window',
        'electrum_med_gui.qt.main_window',
        'electrum_med_gui.qt.network_dialog',
        'electrum_med_gui.qt.password_dialog',
        'electrum_med_gui.qt.qrcodewidget',
        'electrum_med_gui.qt.receiving_widget',
        'electrum_med_gui.qt.seed_dialog',
        'electrum_med_gui.qt.transaction_dialog',
        'electrum_med_gui.qt.util',
        'electrum_med_gui.qt.version_getter',
        'electrum_med_gui.stdio',
        'electrum_med_gui.text',
        'electrum_med_plugins.exchange_rate',
        'electrum_med_plugins.labels',
        'electrum_med_plugins.pointofsale',
        'electrum_med_plugins.qrscanner',
        'electrum_med_plugins.virtualkeyboard',
    ],
    description="Lightweight Litecoin Wallet",
    author="ecdsa",
    author_email="ecdsa@github",
    license="GNU GPLv3",
    url="http://electrum-med.org",
    long_description="""Lightweight Litecoin Wallet"""
)
