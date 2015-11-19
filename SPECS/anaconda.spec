%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Version: 21.48.22.56
Release: 1%{?dist}
License: GPLv2+ and MIT
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define gettextver 0.18.1
%define intltoolver 0.31.2-3
%define pykickstartver 1.99.66.5
%define yumver 3.4.3-91
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define nmver 1.0.0-6.git20150107
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.23-1
%define sckeyboardver 1.3.1
%define firewalldver 0.3.5-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 033-240
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.870-3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.31-3
%define libxklavierver 5.4
%define libtimezonemapver 0.4.1-2
%define helpver 7.1.8-1

BuildRequires: audit-libs-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gtk3-devel-docs
BuildRequires: glib2-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: pygobject3
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libgnomekbd-devel
BuildRequires: libxklavier-devel >= %{libxklavierver}
BuildRequires: pango-devel
BuildRequires: pykickstart >= %{pykickstartver}
%if ! 0%{?rhel}
BuildRequires: python-bugzilla
%endif
BuildRequires: python-devel
BuildRequires: python-urlgrabber >= %{pythonurlgrabberver}
BuildRequires: python-nose
BuildRequires: systemd
BuildRequires: yum >= %{yumver}
BuildRequires: NetworkManager-devel >= %{nmver}
BuildRequires: NetworkManager-glib-devel >= %{nmver}
BuildRequires: dbus-devel >= %{dbusver}
BuildRequires: dbus-python
BuildRequires: rpm-devel >= %{rpmver}
BuildRequires: libarchive-devel >= %{libarchivever}
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif
BuildRequires: libtimezonemap-devel >= %{libtimezonemapver}

Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-gui = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Requires: python-blivet >= 1:0.61.15.24
Requires: python-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libreport-rhel-anaconda-bugzilla >= 2.1.11-1
Requires: libselinux-python
Requires: rpm-python >= %{rpmver}
Requires: parted >= %{partedver}
Requires: pyparted >= %{pypartedver}
Requires: yum >= %{yumver}
Requires: python-urlgrabber >= %{pythonurlgrabberver}
Requires: pykickstart >= %{pykickstartver}
Requires: langtable-data >= %{langtablever}
Requires: langtable-python >= %{langtablever}
Requires: libuser-python
Requires: authconfig
Requires: firewalld >= %{firewalldver}
Requires: util-linux >= %{utillinuxver}
Requires: dbus-python
Requires: python-pwquality
Requires: python-IPy
Requires: python-nss
Requires: pytz
Requires: realmd
Requires: teamd
%ifarch %livearches
Requires: usermode
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum >= %{isomd5sum}
Requires: yum-utils >= %{yumutilsver}
Requires: createrepo
Requires: NetworkManager >= %{nmver}
Requires: NetworkManager-team
Requires: NetworkManager-glib >= %{nmver}
Requires: dhclient
Requires: kbd
Requires: chrony
Requires: python-ntplib
Requires: rsync
Requires: systemd
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64 ia64
Requires: dmidecode
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif
Requires: kexec-tools

Requires: python-coverage

# required because of the rescue mode and VNC question
Requires: anaconda-tui = %{version}-%{release}

Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty <= 0.107-1

%description core
The anaconda-core package contains the program which was used to install your
system.

%package gui
Summary: Graphical user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-widgets = %{version}-%{release}
Requires: python-meh-gui >= %{mehver}
Requires: adwaita-icon-theme
Requires: system-logos
Requires: tigervnc-server-minimal
Requires: libxklavier >= %{libxklavierver}
Requires: libgnomekbd
Requires: libtimezonemap >= %{libtimezonemapver}
Requires: nm-connection-editor
%ifarch %livearches
Requires: zenity
%endif
Requires: keybinder3
%ifnarch s390 s390x
Requires: NetworkManager-wifi
%endif
Requires: yelp
Requires: anaconda-user-help >= %{helpver}

%description gui
This package contains graphical user interface for the Anaconda installer.

%package tui
Summary: Textual user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}

%description tui
This package contains textual user interface for the Anaconda installer.

%package widgets
Summary: A set of custom GTK+ widgets for use with anaconda
Group: System Environment/Libraries
Requires: pygobject3
Requires: python

%description widgets
This package contains a set of custom GTK+ widgets used by the anaconda installer.

%package widgets-devel
Summary: Development files for anaconda-widgets
Group: Development/Libraries
Requires: glade
Requires: %{name}-widgets%{?_isa} = %{version}-%{release}

%description widgets-devel
This package contains libraries and header files needed for writing the anaconda
installer.  It also contains Python and Glade support files, as well as
documentation for working with this library.

%package dracut
Summary: The anaconda dracut module
Requires: dracut >= %{dracutver}
Requires: dracut-network
Requires: xz
Requires: pykickstart

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q

%build
%configure --disable-static \
           --enable-introspection \
           --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%ifarch %livearches
desktop-file-install ---dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop

# Add a sitecustomize.py to be loaded by liveinst
mkdir -p %{buildroot}%{_datadir}/anaconda/site-python
install -m 0644 pyanaconda/sitecustomize.py %{buildroot}%{_datadir}/anaconda/site-python/
%endif
# NOTE: If you see "error: Installed (but unpackaged) file(s) found" that include liveinst files,
#       check the IS_LIVEINST_ARCH in configure.ac to make sure your architecture is properly defined

%find_lang %{name}

%post widgets -p /sbin/ldconfig
%postun widgets -p /sbin/ldconfig


%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files
%doc COPYING

%files core -f %{name}.lang
%doc COPYING
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%{_datadir}/anaconda/help/*
%exclude %{_datadir}/anaconda/tzmapdata
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
%exclude %{_libdir}/python*/site-packages/pyanaconda/rescue.py*
%exclude %{_libdir}/python*/site-packages/pyanaconda/ui/gui/*
%exclude %{_libdir}/python*/site-packages/pyanaconda/ui/tui/*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%ifarch %livearches
%{_bindir}/liveinst
%{_sbindir}/liveinst
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_datadir}/applications/*.desktop
%endif

%files gui
%{_libdir}/python*/site-packages/pyanaconda/ui/gui/*

%files tui
%{_libdir}/python*/site-packages/pyanaconda/rescue.py
%{_libdir}/python*/site-packages/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{_libdir}/python*/site-packages/gi/overrides/*

%files widgets-devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Thu Oct 29 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.56-1
- Ignore interfaces with invalid VLAN IDs. (dshea)
  Resolves: rhbz#1274893

* Fri Oct 09 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.55-1
- network: create ifcfg files in tui if needed (rvykydal)
  Resolves: rhbz#1268155
- Do not limit ONBOOT default setting to url and nfs installation methods
  (rvykydal)
  Resolves: rhbz#1269264

* Wed Oct 07 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.54-1
- ibft: fix setting dracut boot args for static ibft nic configuration
  (rvykydal)
  Resolves: rhbz#1267526
- dracut: accept inst.dd=[file:]/dd.iso (wwoods)
  Resolves: rhbz#1268792
- Fix issues with the date&time not being updated on timezone changes
  (vpodzime)
  Resolves: rhbz#1267450

* Tue Sep 29 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.53-1
- Use otps.display_mode during early startup (mkolman)
  Resolves: rhbz#1267140

* Mon Sep 28 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.52-1
- Mount stage2 cdrom after running driver-updates (bcl)
  Resolves: rhbz#1266478

* Fri Sep 25 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.51-1
- Pull in new translations
  Related: rhbz#1047457

* Wed Sep 23 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.50-1
- Fix a pylint problem with the ostree patch. (clumens)
  Related: rhbz#1253527
- Update storage config after running dasdfmt. (sbueno+anaconda)
  Resolves: rhbz#1264411
- rpmostreepayload: Forcibly unmount everything in sysroot (walters)
  Resolves: rhbz#1253527

* Tue Sep 22 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.49-1
- Use correct installclass for RHEL Atomic Host (rvykydal)
  Resolves: rhbz#1265213
- Catch blkid failure in driver-updates (bcl)
  Resolves: rhbz#1262963
- Maximize anaconda instead of running fullscreen (dshea)
  Related: rhbz#1231856
- Do not display markup in showDetailedError. (dshea)
  Resolves: rhbz#1263963

* Fri Sep 18 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.48-1
- Skip setting up env and groups in software spoke for ks (bcl)
  Resolves: rhbz#1263493

* Tue Sep 15 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.47-1
- Show correct status for no %%packages with selected environment (mkolman)
  Related: rhbz#1261393
- Keep environment selection when reentering the software spoke (mkolman)
  Resolves: rhbz#1261393
- Remove an unused import. (clumens)
  Related: rhbz#1253672
- Only show the user spoke if no users are specified in kickstart (mkolman)
  Resolves: rhbz#1253672

* Fri Sep 11 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.46-1
- Handle driver rpms retrieved via network (bcl)
  Resolves: rhbz#1257916
- Use getDiskDescription for disk description strings (bcl)
  Resolves: rhbz#1247861
- Add getDiskDescription helper function (bcl)
  Related: rhbz#1247861
- Make sure anaconda reads in ks file from OEMDRV device. (sbueno+anaconda)
  Resolves: rhbz#1057271
- Try to deal with expected errors from devicetree.populate (vpodzime)
  Resolves: rhbz#1257648

* Thu Sep 10 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.45-1
- Fix 'cat: /tmp/dd_disk: No such file or directory' (jkonecny)
  Resolves: rhbz#1251394

* Wed Sep 09 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.44-1
- Fix another bash syntax problem in kickstart-genrules.sh (sbueno+anaconda)
  Resolves: rhbz#1057271
- Install all required packages. (dshea)
  Resolves: rhbz#1260624

* Tue Sep 08 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.43-1
- Quit in askvnc should not reboot image and dirinstall (bcl)
  Resolves: rhbz#1255069
- network: assume --device=link as default also for ks on hd (rvykydal)
  Related: rhbz#1085310
- Don't try to concatenate a list with a string (mkolman)
  Related: rhbz#1252444
- Always show the Network spoke in Initial Setup (mkolman)
  Resolves: rhbz#1259801
- Fix hiding curl 404 errors outside debug mode (vtrefny)
  Resolves: rhbz#1182776

* Thu Sep 03 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.42-1
- Remove a call to execute in storage thread to avoid a threading disaster.
  (sbueno+anaconda)
  Resolves: rhbz#1245268
- Remove a rogue reference to self.back_clicked. (clumens)
  Related: rhbz#1254548
- Fix a typo in service enablement in kickstart.py. (clumens)
  Related: rhbz#1252444
- Verify Initial Setup services are present before turning them ON/OFF
  (mkolman)
  Resolves: rhbz#1252444
- Set both .format's and .originalFormat's passphrase on unlock (vpodzime)
  Resolves: rhbz#1255679
- Make the Encrypt checkbox insensitive for encrypted non-BTRFS devices
  (vpodzime)
  Related: rhbz#1255679
- Make the default screen height yet one line shorter (vpodzime)
  Resolves: rhbz#1184378
- Don't crash if the Japanese PC-98 keyboard is selected (mkolman)
  Resolves: rhbz#1190589

* Wed Sep 02 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.41-1
- Enforce sane disk selections. (dlehman)
  Resolves: rhbz#1254548

* Tue Sep 01 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.40-1
- Skip OEMDRV if interactive DD is requested (bcl)
  Related: rhbz#1254270
- Copy updated driver ko to correct directory (bcl)
  Related: rhbz#1254270
- addRepo takes a repo object not a string (bcl)
  Related: rhbz#1254270
- Drivers are simply under /run/install/DD-x/ (bcl)
  Related: rhbz#1254270
- Fix a bash error in kickstart-genrules.sh (sbueno+anaconda)
  Resolves: rhbz#1057271
- Run nm-connection-editor with the --keep-above flag (mkolman)
  Resolves: rhbz#1231856

* Mon Aug 31 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.39-1
- Disallow /boot on lvm until grub2 fully supports it. (dlehman)
  Resolves: rhbz#1252466
- Force an encoding of utf-8 on liveinst installs (dshea)
  Resolves: rhbz#1257060
- Ignore zram block devices in the list-harddrives script output (mkolman)
  Resolves: rhbz#1247886
  Resolves: rhbz#1253184

* Fri Aug 28 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.38-1
- Run AnacondaExceptionHandler in cmdline mode (bcl)
  Resolves: rhbz#1256385
- anaconda.target: Wants systemd-logind.service (awilliam)
  Resolves: rhbz#1257311

* Wed Aug 26 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.37-1
- Process excludedGroupList after packages and groups. (clumens)
  Resolves: rhbz#1249036
- Fix the help button mnemonic display on spokes (dshea)
  Resolves: rhbz#1250918

* Mon Aug 24 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.36-1
- Don't write nfs repos to the target system (bcl)
  Resolves: rhbz#1246212
- Fix nfs mountpoint removal (bcl)
  Related: rhbz#1246212
- Fix the handling of nfs:// URLs. (dshea)
  Related: rhbz#1246212
- Start hubs with the buttons insensitive. (dshea)
  Resolves: rhbz#1255752
- Move locale environment logic into localization.py (dshea)
  Related: rhbz#1198642

* Mon Aug 17 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.35-1
- Skip source url checks when network is off (bcl)
  Resolves: rhbz#1251130
- Don't set net.device to link if there is no ksdevice (bcl)
  Resolves: rhbz#1085310
- Reading carrier while link is down raises IOError (bcl)
  Related: rhbz#1085310
- Make sure username entered in TUI if create a user chosen. (sbueno+anaconda)
  Resolves: rhbz#1249660

* Sun Aug 16 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.34-1
- Network protocols don't list Closest mirror first (vpodzime)
  Resolves: rhbz#1253196
- Make sure proper installclass selected for RHEL installs. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix traceback on tz spoke in text mode (sbueno+anaconda)
  Resolves: rhbz#1252025

* Thu Aug 13 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.33-1
- Re-enable addons as additional repositories. (clumens)
  Resolves: rhbz#1248323

* Wed Aug 12 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.32-1
- product.img buildstamp should override distribution buildstamp (bcl)
  Resolves: rhbz#1240238
- Tell libreport if it is a final release or not (vpodzime)
  Resolves: rhbz#1252036
- On incomplete ks, don't automatically proceed with install. (sbueno+anaconda)
  Resolves: rhbz#1251978
- Add the "make ci" target. (clumens)
  Related: rhbz#1196721
- Tweak tmux configuration file (jkonecny)
  Resolves: rhbz#1238799

* Fri Aug 07 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.31-1
- Only pass DASDs to is_ldl_dasd function. (sbueno+anaconda)
  Resolves: rhbz#1248666

* Wed Aug 05 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.30-1
- Add the anaconda-user-help package as dependency (mkolman)
  Resolves: rhbz#1247779

* Tue Aug 04 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.29-1
- Fix a line that still treated the fstype as a GtkComboBoxText (dshea)
  Resolves: rhbz#1248885
- Fix fastestmirror plugin check (bcl)
  Resolves: rhbz#1249569

* Fri Jul 31 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.28-1
- Display a EULA-related warning on progress hub at end of installation.
  (sbueno+anaconda)
  Resolves: rhbz#1249185
  Resolves: rhbz#1248432

* Thu Jul 30 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.27-1
- Fix error with OEMDRV ks auto-load check. (sbueno+anaconda)
  Related: rhbz#1057271

* Wed Jul 29 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.26-1
- Prevent incomplete translations from making the TUI unusable (mkolman)
  Resolves: rhbz#1235617
- Disable a Pylint false-positive (mkolman)
  Related: rhbz#1234896

* Tue Jul 28 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.25-1
- Add support for autostep and --autoscreenshot (mkolman)
  Resolves: rhbz#1234896
- Really fix unexpected exits in execReadlines (dshea)
  Related: rhbz#1188287
- iscsi: display portal (address:port) of node in node list (rvykydal)
  Related: rhbz#1195570

* Fri Jul 24 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.24-1
- Add parentheses around the IPV6 regex fragment. (dshea)
  Resolves: rhbz#1246133
- Add tests for IPv6 literals in URLs (dshea)
  Related: rhbz#1246133
- Do not set user home to / in advanced user dialog (bcl)
  Resolves: rhbz#1245837
- Fix Initial PPC PReP Boot Selector Name (rmarshall)
  Resolves: rhbz#1172755

* Thu Jul 23 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.23-1
- Handle missing environment without traceback (bcl)
  Resolves: rhbz#1245296
- Disable a Pylint false-positive (mkolman)
  Related: rhbz#1182562
- Make sure TUI is readable for non-latin languages (mkolman)
  Resolves: rhbz#1182562
- Auto-load ks.cfg if OEMDRV volume available. (sbueno+anaconda)
  Resolves: rhbz#1057271
- dracut: minor cleanup (wwoods)
  Related: rhbz#1168902
- dracut: fix missing messages for inst.ks=cdrom (wwoods)
  Related: rhbz#1168902
- Wait forever for kickstarts on CDROM (wwoods)
  Resolves: rhbz#1168902
- Allow cdrom-swapping when doing "inst.ks=cdrom[:...]" (wwoods)
  Resolves: rhbz#1168902
- anaconda-lib.sh: add tell_user() and dev_is_cdrom() (wwoods)
  Related: rhbz#1168902

* Wed Jul 22 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.22-1
- Fix various pylint problems caused by the new rescue mode. (clumens)
  Related: rhbz#965985
- network: use ibftx interface for iSCSI from iBFT in dracut (rvykydal)
  Resolves: rhbz#1077291
- Remove text.py from spec file (bcl)
  Related: rhbz#965985

* Mon Jul 20 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.21-1
- Remove the last usage of newt and get rid of it as a dependency
  (sbueno+anaconda)
  Related: rhbz#965985
- Enable anaconda to use the new rescue mode. (sbueno+anaconda)
  Resolves: rhbz#965985
- Get rid of unnecessary constants in constants_text. (sbueno+anaconda)
  Related: rhbz#965985
- Get rid of some unnecessary files. (sbueno+anaconda)
  Related: rhbz#965985

* Fri Jul 17 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.20-1
- Add support for architecture suffixes in help files (mkolman)
  Related: rhbz#1196721
  Related: rhbz#1072033
- network: add s390 options to default ifcfg files (rvykydal)
  Resolves: rhbz#1074570

* Wed Jul 15 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.19-1
- Don't ask to start vnc if user specifies text mode. (sbueno+anaconda)
  Resolves: rhbz#1241425
  Related: rhbz#1196721
- Fix pylint errors in the new driver disk code. (clumens)
  Related: rhbz#1084197
- Restore RHEL-specific stylesheet data. (dshea)
  Related: rhbz#1196721

* Fri Jul 10 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.18-1
- Start the network before the display (dshea)
  Resolves: rhbz#1240732
- Bump pykickstart version required. (sbueno+anaconda)
  Resolves: rhbz#1241413
- Set the no network error in refresh() (dshea)
  Resolves: rhbz#1238797
- Show the event box immediately when setting infobar messages. (dshea)
  Related: rhbz#1238797
- dracut: fix boot failure waiting for finished/dd.sh (wwoods)
  Related: rhbz#1084197
- driver_updates: fixes from patch review (wwoods)
  Related: rhbz#1084197
- dd-refactor: dracut + build bits (wwoods)
  Resolves: rhbz#1084197
  Resolves: rhbz#1164131
  Related: rhbz#1213546
- parse-kickstart: just emit 'inst.dd=XXX' for driverdisk (wwoods)
  Related: rhbz#1084197
- parse-kickstart: pylint fixes (wwoods)
  Related: rhbz#1084197
- dd-refactor: new driver_updates.py + tests (wwoods)
  Related: rhbz#1084197
- payload: fix driverdisk repos (wwoods)
  Related: rhbz#1084197
- Always write NTP servers to config files (wwoods)
  Resolves: rhbz#1197575
- dracut: fix boot with inst.ks and no inst.{repo,stage2} (wwoods)
  Resolves: rhbz#1238987

* Thu Jul 09 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.17-1
- Check for Gtk before importing escape_markup (bcl)
  Related: rhbz#1236995
- Add handling for unusable storage configurations. (dlehman)
  Resolves: rhbz#1236995
- Allow markup in the label/message of DetailedErrorDialog. (dlehman)
  Related: rhbz#1236995
- Allow passing an optional button list to showDetailedError. (dlehman)
  Related: rhbz#1236995
- Allow kwargs with gtk_action_wait, gtk_action_nowait decorators. (dlehman)
  Related: rhbz#1236995

* Tue Jul 07 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.16-1
- Ellipsize the file system type combo box (dshea)
  Resolves: rhbz#1212615
- Shorten the mount point entry to match the capacity entry (dshea)
  Resolves: rhbz#1212615
- Re-save custom.glade (dshea)
  Resolves: rhbz#1212615
- Ellipsize comboboxes (dshea)
  Resolves: rhbz#1212615
- Wrap device labels earlier (dshea)
  Resolves: rhbz#1212615
- Change text shown to users about the need to dasdfmt. (sbueno+anaconda)
  Related: rhbz#1170653
- Fix a typo in the dasdfmt dialog box. (sbueno+anaconda)
  Related: rhbz#1170653
- Enable anaconda to use the new cdl ks option, and detect ldl dasds.
  (sbueno+anaconda)
  Resolves: rhbz#1170656
  Resolves: rhbz#1170653
- Fix GRUB2 Password Update Scope (rmarshall)
  Related: rhbz#985962
- Enable Custom GRUB2 Password Utility (rmarshall)
  Related: rhbz#985962

* Tue Jul 07 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.15-1
- Explicitly try fetching netroot after network kickstart fetch (vpodzime)
  Resolves: rhbz#1238987
- Refresh advanced disks after disk summary dialog (bcl)
  Resolves: rhbz#1226354
- Show an alternative prompt if a hub contains only a single spoke (mkolman)
  Resolves: rhbz#1199234
- Don't crash if incorrect environment is set in kickstart (mkolman)
  Resolves: rhbz#1234890
- Allow /boot partition on iscsi with ibft (jkonecny)
  Related: rhbz#1164195
- Make sure we work with fresh data when trying to do netroot (vpodzime)
  Related: rhbz#1082500
- Make our manual triggering on network in dracut work (vpodzime)
  Resolves: rhbz#1082500
- Fix broken test by infiniband patch (jkonecny)
  Related: rhbz#1177032

* Thu Jul 02 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.14-1
- Add RAID swaps to /etc/fstab (bcl)
  Resolves: rhbz#1234469
- Fix kickstart install with infiniband (jkonecny)
  Resolves: rhbz#1177032
- Disable Label Entry for PPC PReP Boot (rmarshall)
  Resolves: rhbz#1172773
- Correctly propagate --ipv6gateway to ifcfg files(mkolman)
  Resolves: rhbz#1170845
- Ask for encryption passphrase when not specified in ks (vtrefny)
  Resolves: rhbz#1185466
- Connect scroll adjustments in the right class (dshea)
  Related: rhbz#1189899

* Wed Jul 01 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.13-1
- Cancel Container Edit Sensitizes Update (rmarshall)
  Resolves: rhbz#1168656
- Add support for specifying arbitrary mkfs options. (clumens)
  Resolves: rhbz#1217110
- Do not display curl 404 errors that can be safely ignored (vtrefny)
  Resolves: rhbz#1182776
- Fix the line counting when printing long widgets (vpodzime)
  Related: rhbz#1184378
- Improve how we set the default screen height in text mode (vpodzime)
  Resolves: rhbz#1184378

* Tue Jun 30 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.12-1
- dd: drop unnecessary archive_read_data_skip (Will Woods)
  Related: rhbz#1222056
- dd_extract: -l should not extract modules+firmware (Will Woods)
  Related: rhbz#1222056
- dd: fix permissions on extracted files (wwoods)
  Resolves: rhbz#1222056
- Create and use snapshot of on-disk storage with no modifications (vpodzime)
  Resolves: rhbz#1160862
  Resolves: rhbz#1187644
- Implement the class for storage snapshots (vpodzime)
  Related: rhbz#1187644
  Related: rhbz#1160862
- Prevent any changes in the StorageSpoke if just going back (vpodzime)
  Related: rhbz#1187644
  Related: rhbz#1160862
- fix inst.ks.sendmac for static ip=XXX (wwoods)
  Resolves: rhbz#1190115

* Fri Jun 26 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.11-1
- network: catch another race when calling dbus methods on invalid devices
  (rvykydal)
  Related: rhbz#1179276
- network: GUI, add connection even when virtual device activation failed
  (rvykydal)
  Resolves: rhbz#1179276
- Remove an extra '>' in the betanag warning (vpodzime)
  Related: rhbz#1196721
- Do not mix two lists of fields when applying changes in text mode (vpodzime)
  Resolves: rhbz#1231149

* Thu Jun 25 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.10-1
- Eliminate some false test results when running glade tests. (atodorov)
  Related: rhbz#1196721
- Fix adding 'boot=' option in FIPS mode (vtrefny)
  Resolves: rhbz#1190146
- Use the index in grubenv (bcl)
  Resolves: rhbz#1209678
- Make colon optional while adding iSCSI Initiator Name (sujithpshankar)
  Resolves: rhbz#1177573
- Add basic support for LVM cache creation in kickstart (vpodzime)
  Resolves: rhbz#1120421
- Change the betanag wording (back) to be better for RHEL (vpodzime)
  Related: rhbz#1196721
- Set sensitivity of the "Encrypt" checkbox together with its label (vpodzime)
  Resolves: rhbz#1181468
- Use Size, not int, for size (amulhern)
  Related: rhbz#1076055
  Related: rhbz#1196721
- Changes for scheduling size change on an existing device (amulhern)
  Related: rhbz#1076055
  Related: rhbz#1196721
- Remove too strict condition for changing size (amulhern)
  Related: rhbz#1076055
  Related: rhbz#1196721

* Mon Jun 22 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.9-1
- Enable Anaconda to configure NTP (jkonecny)
  Resolves: rhbz#1085013
- Retry package repository metadata downloads (mkolman)
  Resolves: rhbz#1177366
- Use UEFI VFAT ESP when kickstarting Intel Macs (jan.kundrat)
  Resolves: rhbz#1219196
- If using pre-existing, no size needs to be specified in ksdata (amulhern)
  Resolves: rhbz#1169783
  Related: rhbz#1196721
- Use the RHEL7 versions of certain partitioning commands. (clumens)
  Related: rhbz#1217110
- Fix set size to partition in custom spoke (jkonecny)
  Related: rhbz#1196721
- Expect addons to have categories for both GUI and TUI (vpodzime)
  Related: rhbz#1128616

* Thu Jun 18 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.8-1
- Fix nfs4 stage2 and repo handling (bcl)
  Resolves: rhbz#1230329
- Add support for reboot --kexec kickstart command (bcl)
  Related: rhbz#1207747
- Add inst.kexec and --kexec support to reboot with kexec (bcl)
  Resolves: rhbz#1207747
- Add setup_kexec method to prepare the system for a reboot with kexec (bcl)
  Related: rhbz#1207747
- Include NetworkManager-glib in anaconda-core (bcl)
  Related: rhbz#1196721
- Use simple_replace to edit langpacks.conf (bcl)
  Resolves: rhbz#1165980
- Add simple_replace config file function (bcl)
  Related: rhbz#1165980
- Keyboard Scroll Fails in Viewports (dshea)
  Resolves: rhbz#1189899
- Fix Issue with Spaces in Network IPs and Bad Input(jkonecny)
  Resolves: rhbz#1174451
- network: fix a typo in condition for installing teamd (rvykydal)
  Resolves: rhbz#1199185
- Fix IP / hostname mismatches when showing VNC server address (rvykydal)
  Resolves: rhbz#1186726
- Check also ipv6 default routes when looking for onboot=yes device (rvykydal)
  Resolves: rhbz#1185280

* Mon Jun 15 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.7-1
- Update upd-kernel so that it actually works (bcl)
  Resolves: rhbz#1166535
- Fix passing ,nfsvers=3 to dracut (bcl)
  Resolves: rhbz#1161820
- Extract xattrs from tar payload (bcl)
  Resolves: rhbz#1196021
- rpmostreepayload: write storage config after shared var is mounted (rvykydal)
  Resolves: rhbz#1203608
- Do not log Xorg output to tty5 (dshea)
  Related: rhbz#1188287
- Fix for "Kickstart installation fails..." (jkonecny)
  Resolves: rhbz#1197960

* Wed Jun 10 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.6-1
- Modify Proxy Label in Installation Source Spoke (rmarshall)
  Resolves: rhbz#1168554
- Add error checks to liveimg mount code (bcl)
  Related: rhbz#1178703
- If the network is disabled, also disable the network part of the source
  spoke. (clumens)
  Related: rhbz#1196721
- Grubby no longer needs to be explicitly included (dmarlin)
  Resolves: rhbz#1176705
- Don't allow /boot on iSCSI. (sbueno+anaconda)
  Resolves: rhbz#1164195
- Fix building docs when running under "make distcheck". (clumens)
  Related: rhbz#1196721
- Fix problems discovered by the glade tests. (clumens)
  Related: rhbz#1196721
- Include .glade.h files in the distribution. (clumens)
  Related: rhbz#1196721

* Mon Jun 08 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.5-1
- Actually distribute the clickable message test (dshea)
  Related: rhbz#1125145
- Get rid of the find button in the filter spoke. (dshea)
  Related: rhbz#1168950
- Rearrange filter.glade (dshea)
  Related: rhbz#1168950
- Fix errors in the vendor column renderers. (dshea)
  Related: rhbz#1168950
- Fix some minor inconsistencies in filter.glade (dshea)
  Related: rhbz#1168950
- Fix issues with advanced storage searching. (dshea)
  Resolves: rhbz#1168950
- Remove duplicate entries from search combo boxes (dshea)
  Resolves: rhbz#1168950
- Use named IDs for the filter type combo boxes. (dshea)
  Related: rhbz#1168950
- Rearrange filter.glade the way glade wants it now (dshea)
  Related: rhbz#1168950
- Pass the pylint test. (clumens)
  Related: rhbz#1196721

* Fri Jun 05 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.4-1
- network: on rhel don't assume autoconnections created by NM (rvykydal)
  Related: rhbz#1196721
- Start vncconfig for cut/paste (hamzy)
  Resolves: rhbz#1169991
- Don't unconditionally set ksdata.lang.seen to True (mkolman)
  Related: rhbz#1198642
- Make sure LANG is always set to something (dshea)
  Resolves: rhbz#1198642
- Add links to clickable warning and error messages. (dshea)
  Resolves: rhbz#1125145
- Add a test to look for clickable messages that aren't clickable enough.
  (dshea)
  Related: rhbz#1125145
- Allow markup and links in the info bar. (dshea)
  Related: rhbz#1125145
- Update the FCOE command to use the RHEL7 base class. (clumens)
  Related: rhbz#1196721
- Fix RHEL Atomic installclass test (bcl)
  Related: rhbz#1196721
- Use a rhel7.2 mock chroot for rc-release (bcl)
  Related: rhbz#1196721
- Build documentation during build instead of dist (dshea)
  Related: rhbz#1196721
- Clean out the mock chroot before attempting to run the rest of the test.
  (clumens)
  Related: rhbz#1196721
- Put all mock results into the top-level source dir. (clumens)
  Related: rhbz#1196721
- Change dracut requires to the RHEL7 version. (bcl)
  Related: rhbz#1196721
- dnf is not supported in RHEL7 (bcl)
  Related: rhbz#1196721
- Use createrepo, createrepo_c isn't available in RHEL7 (bcl)
  Related: rhbz#1196721
- Change F21 pykickstart commands to RHEL7 (jkonecny)
  Related: rhbz#1196721
- Add an option to startProgram to not reset the locale (dshea)
  Related: rhbz#1188287
- Set $LIBUSER_CONF early (dshea)
  Related: rhbz#1188287
- Assume UTC if setting the system time without a timezone (dshea)
  Related: rhbz#1188287
- Do not set $TZ (dshea)
  Related: rhbz#1188287
- Beware of 0 being the same bool value as None when setting time (vpodzime)
  Related: rhbz#1188287
- Fix the last member of the struct_time struct (vpodzime)
  Related: rhbz#1188287
- Remove timestamp-based version support. (dshea)
  Related: rhbz#1188287
- Avoid setting $LANG and $LANGUAGE, except where we can't (dshea)
  Resolves: rhbz#1188287
- Add a parameter to iutil.startProgram to extend the environment (dshea)
  Related: rhbz#1188287
- Add a method to set environment variables for child processes (dshea)
  Related: rhbz#1188287
- Set $DISPLAY before threads are started. (dshea)
  Related: rhbz#1188287
- Handle the simple cases of environment modification. (dshea)
  Related: rhbz#1188287
- Always use iutil to start processes. (dshea)
  Related: rhbz#1188287
- Move the X startup logic to iutil (dshea)
  Related: rhbz#1188287
- Move process watching to iutil. (dshea)
  Related: rhbz#1188287
- Close file descriptors while daemonizing auditd (dshea)
  Related: rhbz#1188287
- Add an option to only capture stdout with execWithCapture (dshea)
  Related: rhbz#1188287
- Simplify iutil.execReadlines. (dshea)
  Related: rhbz#1188287
- Add close_fds to the Popen call. (dshea)
  Related: rhbz#1188287
- Add an option to startProgram to reset signal handlers. (dshea)
  Related: rhbz#1188287
- Add a method startProgram to handle process starting (dshea)
  Related: rhbz#1188287
- Lock program_log_lock closer to where the log is written. (dshea)
  Related: rhbz#1188287
- Add missing files to po/POTFILES.in, after fixing the test for them.
  (clumens)
  Related: rhbz#1196721
- Backport iutil_test.py updates from master (atodorov). (clumens)
  Related: rhbz#1196721
- Backport pylint updates from master (atodorov). (clumens)
  Related: rhbz#1196721
- Fix strings with style problems. (clumens)
  Related: rhbz#1196721
- Backport gettext updates from master (atodorov). (clumens)
  Related: rhbz#1196721
- Remove the automated GUI tests. (clumens)
  Related: rhbz#1196721
- Fix Kickstart installation without default gateway errors out (jkonecny)
  Resolves: rhbz#1147181
- rescue: find root partition of ostree (atomic) installations (rvykydal)
  Resolves: rhbz#1152041
- Identify Atomic install class by correct product name (rvykydal)
  Resolves: rhbz#1193268
- rpmostreepayload: Avoid shutil.copytree in favor of cp -r to fix symlinks
  (walters)
  Resolves: rhbz#1199127
- atomic: set up atomic specific partitioning defaults (rvykydal)
  Resolves: rhbz#1155452
- A couple updates to installclasses. (clumens)
  Related: rhbz#1155452
- rpmostreepayload: Rework remote add handling (walters)
  Resolves: rhbz#1199127
- Use RHEL7 Bootloader command in parse-kickstart (rvykydal)
  Related: rhbz#1196721
- Use RHEL7 Network command in parse-kickstart (rvykydal)
  Related: rhbz#1196721

* Wed Jun 03 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.3-1
- Revert "Select http source if there is no mirror enabled." (bcl)
  Related: rhbz#1196721
- Make sure /boot is not LVM LV if we're on s390x (sbueno+anaconda)
  Resolves: rhbz#873135
  Related: rhbz#1196721
- Preserve kickstart url behavior for mirrorlist (bcl)
  Related: rhbz#1196721
  Related: rhbz#1109933
- Use a backslash to escape nfs spaces instead of x20 (bcl)
  Related: rhbz#1196721
  Related: rhbz#1109933
- Create missing parent directories for user's home directory (bcl)
  Resolves: rhbz#1163775
  Related: rhbz#1196721
- custom: Clearing errors should also clear Done clicked state (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1158609
- Clear errors when downloading new MD in text (bcl)
  Related: rhbz#1196721
  Related: rhbz#1125927
- Return result of default key handling in text summary hub (bcl)
  Related: rhbz#1196721
  Related: rhbz#997405
- Protect protected devices in custom spoke (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1052883
- Don't call storage.write for dirinstall (bcl)
  Related: rhbz#1196721
  Related: rhbz#1120206
- Don't call BusyCursor before Gdk is setup (bcl)
  Resolves: rhbz#1078868
  Related: rhbz#1196721
- Handle spaces in inst.repo, kickstart nfs, and url commands (bcl)
  Resolves: rhbz#1109933
  Related: rhbz#1196721
- Exclude hfsplus-tools from rhel (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1119305
- Skip nvram update on ppc64 image/dir installations (bcl)
  Resolves: rhbz#1136486
  Related: rhbz#1196721
- CmdlineError should exit with a 1 (bcl)
  Related: rhbz#1196721
  Related: rhbz#1102318
- Remove logging to tty3 and tty5 (bcl)
  Resolves: rhbz#1073336
  Related: rhbz#1196721
- Only install liveinst symlink on supported arches (bcl)
  Related: rhbz#1121678
  Related: rhbz#1196721
- Mountpoint encrypted checkbox reflects container state (bcl)
  Resolves: rhbz#1076171
  Related: rhbz#1196721
- Write sslverify=0 for url kickstart method (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1116858
- Add noverifyssl and proxy support to dracut ks handling (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1116858
- Install selected ks repos to target (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1119867
- Add check for the format of grub2 encrypted password (bcl)
  Related: rhbz#1196721
  Related: rhbz#1070327
- Use low level file i/o for rpm callback logging (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1035745
- Add platform specific group selection (bcl)
  Resolves: rhbz#884385
  Related: rhbz#1196721
- reiserfs is not supported (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1066635
- remove epdb SIGHUP debug handler (bcl)
  Related: rhbz#1196721
  Related: rhbz#1065557
- Clean up some rpmdiff errors (bcl)
  Related: rhbz#1196721
  Resolves: rhbz#1012624
- Remove Closest mirrors if no mirrors (bcl)
  Related: rhbz#876135
  Related: rhbz#1196721
- Select http source if there is no mirror enabled. (bcl)
  Related: rhbz#876135
  Related: rhbz#1196721
- Use RHEL7 kickstart commands (bcl)
  Related: rhbz#1196721
- Show error on invalid username attempts in TUI. (sbueno+anaconda)
  Resolves: rhbz#1171778
- Fix enlightbox call in ZFCPDialog. (sbueno+anaconda)
  Related: rhbz#1196721
- Get rid of unnecessary python disable-msg in zfcp spoke. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix some pylint errors in the zfcp panel. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix an accelerator collision found on the filter page. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix some issues pylint found. (sbueno+anaconda)
  Related: rhbz#1196721
- Show disk paths on Other page in advstorage. (sbueno+anaconda)
  Related: rhbz#1196721
- Add missing translation context for Add ECKD DASD button in advstorage.
  (sbueno+anaconda)
  Related: rhbz#1196721
- Add translation contexts for z and zfcp panel in advstorage.
  (sbueno+anaconda)
  Related: rhbz#1196721
- Convert devices size to str for GUI for zFCP devices (amulhern)
  Related: rhbz#1196721
- Fix string formatting of zFCP devices. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix the way zFCP devices are displayed in storage spoke. (sbueno+anaconda)
  Related: rhbz#1196721
- Show labels on Add zFCP dialog. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix failure to search by LUN in advanced storage spoke. (sbueno+anaconda)
  Related: rhbz#1196721
- Get rid of the clear button in advanced storage spoke. (sbueno+anaconda)
  Related: rhbz#1196721
- Fix up the z Panel in advanced storage. (sbueno+anaconda)
  Related: rhbz#1196721
- Add support for adding zFCP devices in the GUI (sbueno+anaconda)
  Related: rhbz#1196721
- Fix dracut reads ksdevice from missing os enviromnent (jkonecny)
  Related: rhbz#1085310
- Fix --device=link and --device not specified (rvykydal)
  Resolves: rhbz#1085310

* Mon Jun 01 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.2-1
- Remove an extlinux-related block from rpmostreepayload.py. (clumens)
  Related: rhbz#1196721
  Related: rhbz#1153409
- bootloader: Bridge efi_dir configuration earlier for rpmostreepayload
  (walters)
  Related: rhbz#1196721
  Related: rhbz#1153409
- rpmostreepayload: Handle grub2+EFI layout (walters)
  Related: rhbz#1196721
  Related: rhbz#1153409
- rpmostreepayload: Copy all subdirectories of /usr/lib/ostree-boot (walters)
  Related: rhbz#1196721
  Related: rhbz#1153409
- Handle the case of rpmostreepayload + GRUB2 (walters)
  Related: rhbz#1196721
  Related: rhbz#1153409
- Implement the new reqpart command. (clumens)
  Resolves: rhbz#1164660

* Fri May 29 2015 Brian C. Lane <bcl@redhat.com> - 21.48.22.1-1
- Update scripts/makebumpver to current version from master (bcl)
  Related: rhbz#1196721
- Add .0 to version number -- 21.48.22.0 (bcl)
  Related: rhbz#1196721
- Show empty VGs in the custom spoke. (dlehman)
  Related: rhbz#1196721
- Fix makeupdates handling of Release: (bcl)
  Related: rhbz#1196721
- network: add teamd package if team is used during installation (#1185670) (rvykydal)
  Related: rhbz#1196721
- network: pass team opts to dracut for netroot (#1075666) (rvykydal)
  Related: rhbz#1196721
- iscsi: when logging into nodes consider ip:port of node (#1114820) (rvykydal)
  Related: rhbz#1196721
- Don't traceback if connection does not have read-only setting (#1158919) (rvykydal)
  Related: rhbz#1196721
- network: display only actual fqdn of ip we offer for vnc connection (#1089429) (rvykydal)
  Related: rhbz#1196721
- network: fix a typo making creating virtual devices in %pre fail (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: support for bridge, require pykickstart with the support (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: Catch exception from NM failing to create a bridge device (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: add bridge support for kickstart %pre phase (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: generate kickstart commands for bridge devices (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: add bridge support to kickstart (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: support for adding bridge devices (#1075195) (rvykydal)
  Related: rhbz#1196721
- network: display bridge devices in status (#1075195) (rvykydal)
  Related: rhbz#1196721
- parent is unused, so mark it as such. (clumens)
  Related: rhbz#1196721
- network: enable NM ibft plugin only for ip=ibft boot option (#804511) (rvykydal)
  Related: rhbz#1196721
- network: add support for vlan tag in iBFT (#804511) (rvykydal)
  Related: rhbz#1196721
- network: GUI: reactivate connection automatically after configuration (#1033063) (rvykydal)
  Related: rhbz#1196721
- Fix position of Refresh List button in filter spoke (#1065716) (rvykydal)
  Related: rhbz#1196721
- Fix accelerator collision of Refresh button (#1065716) (rvykydal)
  Related: rhbz#1196721
- gui: add Refresh button to network storage UI (#1065716) (rvykydal)
  Related: rhbz#1196721
- Use absolute path for extlinux/menu.c32 (rvykydal)
  Related: rhbz#1196721
- iscsi: pass rd.* options of devices to be mouted in dracut (#1192398) (rvykydal)
  Related: rhbz#1196721
- network: adapt to NetworkManager package split-up (#1182633) (rvykydal)
  Related: rhbz#1196721
- Take "RHEL Atomic Host" as rhel installclass (#1150410) (rvykydal)
  Related: rhbz#1196721
- network: handle dbus UnknownMethod exception on invalid objects (#1061796) (rvykydal)
  Related: rhbz#1196721
- network: fix typo 'Private ksy pasword' (#1120374) (rvykydal)
  Related: rhbz#1196721
- Fix up a string style issue found in the last network commits. (clumens)
  Related: rhbz#1196721
- network: WPA Enterprise: don't ask twice for password (#1120374) (rvykydal)
  Related: rhbz#1196721
- network: add support for WPA Enterprise (#1120374) (rvykydal)
  Related: rhbz#1196721
- network: add s390 network ifcfg options also for bond slaves (#1090558) (rvykydal)
  Related: rhbz#1196721
- network: don't crash, just log for unrecognized bond options (#1039006) (rvykydal)
  Related: rhbz#1196721
- network: don't traceback on invalid team options (#1114282) (rvykydal)
  Related: rhbz#1196721
- network: copy resolv.conf to chroot before installing packages (#1048520) (rvykydal)
  Related: rhbz#1196721
- network: don't write HWADDR in ifcfgs generated by kickstart (#1130042) (rvykydal)
  Related: rhbz#1196721
- network: show ip of device with default route for vnc and ssh (#1083305) (rvykydal)
  Related: rhbz#1196721
- network: adapt to NM fixing virtual device disconnection (#1084953) (rvykydal)
  Related: rhbz#1196721
- Log installation successes and failures via ipmitool. (clumens)
  Related: rhbz#1196721
- In dracut, do not display a warning for network lines with just a hostname.  (clumens)
  Related: rhbz#1196721
- Preserve the order of boot args added by kickstart. (clumens)
  Related: rhbz#1196721
- Make the Selected Disks and Configure Mount Point dialogs wider. (clumens)
  Related: rhbz#1196721
- Sync up the Selected Disks and Configure Mount Points dialogs. (clumens)
  Related: rhbz#1196721
- Add rc-release target (bcl)
  Related: rhbz#1196721
- Change --skip-tx to --skip-zanata in scratch-bumpver (bcl)
  Related: rhbz#1196721
- Add --newrelease to makebumpver (bcl)
  Related: rhbz#1196721
- Update translation documentation for Zanata (bcl)
  Related: rhbz#1196721
- Switch translation support to fedora.zanata.org (bcl)
  Related: rhbz#1196721
- Revert "Use gettext to process glade files." (clumens)
  Related: rhbz#1196721
- Change of label in iscsi storage spoke (jkonecny)
  Related: rhbz#1196721
- Clear TUI source spoke errors that may have been leftover from a prior attempt. (#1196721) (sbueno+anaconda)
  Related: rhbz#1196721
- Fix completion setting in TUI language spoke. (#1196721) (sbueno+anaconda)
  Related: rhbz#1196721

* Mon Dec 08 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.22-1
- Really fix issue with starting in cmdline mode on s390x. (#1040933)
  (sbueno+anaconda)
- Fix EOF error that occurs if user input required in x3270. (#1171135)
  (jstodola)

* Tue Dec 02 2014 Vratislav Podzimek <vpodzime@redhat.com> - 21.48.21-1
- Revert "Make Python's default encoding detection work on Live installations
  (#1169019)" (awilliam)

* Mon Dec 01 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.20-1
- Revert "Search for a valid stage1 device on disks with stage1 mount points
  (#1168118)" (sbueno+anaconda)
- Make Python's default encoding detection work on Live installations
  (#1169019) (vpodzime)
- Force translation files download instead of skipping them (#1169023)
  (vpodzime)

* Fri Nov 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 21.48.19-1
- Search for a valid stage1 device on disks with stage1 mount points (#1168118)
  (awilliam)

* Thu Nov 27 2014 Vratislav Podzimek <vpodzime@redhat.com> - 21.48.18-1
- Tell curl it should follow redirects when fetching updates.img (#1168561)
  (vpodzime)
- Snapshot free space after clearpart for swap suggestion (#1167965) (vpodzime)

* Wed Nov 26 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.17-1
- Make sure storage info bar is displayed (#1166730) (bcl)
- Fix SELINUX_DEFAULT import (#1167047) (bcl)
- Fix noselinux cmdline default (#1167047) (bcl)

* Thu Nov 20 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.16-1
- Support high contrast mode in fedora-welcome (#1160499) (dshea)

* Tue Nov 18 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.15-1
- do not delete liveimg --url=file:/// file (gczarcinski)
- Provide useful hints on TTY1 during the installation (mkolman)
- Fix typo from commit 9b3259874. (#1120964) (dlehman)
- Remove the old custom partitioning help dialog (mkolman)
- Check if we read something when emptying stdin queue (vpodzime)
- Require min entropy for 'part --encrypted' devices (#1162695) (vpodzime)
- Don't rely on terminal attributes being configurable (#1162702) (vpodzime)
- Disable payloads that failed to setup (#1162732) (dshea)
- Don't change langpacks config of installer environment (#1066017) (rvykydal)

* Tue Nov 11 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.14-1
- Add support for doing a liveimg kickstart with local file (#1140358) (bcl)
- Add a placeholder for a product-specific logo (dshea)
- Load a stylesheet from product.img (dshea)
- Fix make distcheck (mkolman)
- Include help content in the Anaconda tarball (mkolman)
- Fix typo causing traceback when NTP is turned ON/OFF (vpodzime)
- Unpack the callback data given to us by blivet (vpodzime)
- Add timeout to callbacks waiting for enough entropy (#1073679) (vpodzime)
- Prevent tb on s390x when de-selecting a DASD and doing custom part.
  (sbueno+anaconda)
- Revert "Revert productName repo name change (#1128474)" (bcl)
- Update the background image paths used in Fedora. (dshea)
- dracut/save-initramfs.sh: don't save /tmp (wwoods)
- Add a pylint module to detect uses of interruptible system calls. (dshea)
- Wrap interruptible system calls in a loop (#1160041) (dshea)
- Warn users about liveinst usage of --updates (#1153550) (bcl)
- Catch EOFError in raw_input (#1158841) (bcl)
- Ensure we are specifying sensible target sizes for resize. (#1120964)
  (dlehman)
- Set the autopart fstype for boot too (#1112697) (bcl)
- Unconditionally clear the process handle when nm-c-e exits (#1132645) (dshea)
- Make anaconda more scrollable (#1135024) (dshea)
- Lightly rearrange the nav_area (dshea)
- Do not install interactive exception handler in cmdline mode (#1155979)
  (vpodzime)
- Wait until all spokes are setup before updating continue button (bcl)
- Allow adding prepboot to a blank disk in custom (#1155660) (bcl)
- Remove unused imports (vpodzime)

* Tue Oct 28 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.13-1
- Fix handling of md fwraid names in kickstart bootloader command. (#1156354)
  (dlehman)
- Fix switching environments when no environment is selected (#1155756) (dshea)
- Use an empty string for no root password instead of None (#1155576) (dshea)
- Just preserve the %%addon header args if an addon is missing (#1155026)
  (vpodzime)

* Thu Oct 23 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.12-1
- Fix a spelling error (#1153672) (dshea)
- Update checkSizes to work in terms of Size objects (#1129629). (clumens)

* Mon Oct 20 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.11-1
- Don't panic prematurely on a missing size (#1154190) (amulhern)
- Log when using updates from /tmp/updates/ (bcl)
- Fix # handling in SimpleConfigFile (#1045687) (bcl)

* Wed Oct 15 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.10-1
- Change our docs that are close to ReST to proper ReST (vpodzime)
- Run restorecon on /etc/hostname (#1133368) (bcl)
- Add authconfig and firewalld packages when used in ks (#1147687) (bcl)
- Allow kickstart with no method (#972265) (bcl)
- Fix a typo from 73d3a8e5. (sbueno+anaconda)
- Respect both ways how to disable bootloader installation (vpodzime)
- Don't care about crash args in bootloader (#1116323) (vpodzime)
- Add nombr to anaconda to suppress updating MBR (#886502) (gczarcinski)
- Use translated versions of the AM/PM strings consistently (vpodzime)
- Import GUI-specific stuff only when running GUI in entropy handling
  (vpodzime)
- Always store the information about display mode in ksdata (vpodzime)
- Make the date format locale-dependent in our GUI (#1044233) (vpodzime)
- A function for resolving date format and order (vpodzime)
- Reorganize the right side of the Custom spoke (#1094856) (vpodzime)
- Move _verifyLUKSDevicesHaveKey to Anaconda's codebase (vpodzime)
- Add support for thin pool profile specification in kickstart (vpodzime)
- Fix file name of the entropy dialog in POTFILES.in (vpodzime)
- Require minimum random data entropy when creating LUKS (#1073679) (vpodzime)
- Give blivet callbacks for reporting partitioning progress (vpodzime)
- Split localed's converted layouts and variants (#1073825) (vpodzime)
- Create free space snapshot before doing custom->autopart (vpodzime)
- Specify thin pool metadata/chunk size only if given by user (#1140635)
  (vpodzime)
- Distribute the right docs files (vpodzime)
- Don't automatically select environments for kickstart installs (#1018226)
  (dshea)
- Initialize the GUI lock in a way that doesn't break the API (dshea)
- Don't check enabledPlugins if plugins are not yet enabled (#1142544) (dshea)
- Really fix an enlightbox call. (dshea)
- Don't strip accents from the user-inputted keyboard string (dshea)
- Convert strings to unicode in have_word_match (#1146581) (dshea)
- Switch to using the new help content path (#1072033) (mkolman)
- Fix a race between checking for Gtk.main_level and running Gtk.main (dshea)
- Allow recursive lightbox calls (#1147337) (dshea)
- Disable the ntp service with --nontp (#1135768) (dshea)
- Ignore partition start if there is a biosboot partition (#1044849) (bcl)
- Require a larger /boot (#1129629). (clumens)
- Remove duplicates when adding new devices (#887526) (bcl)

* Wed Oct 08 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.9-1
- Bump blivet version requires for all the DASD changes in 0.61.4.
  (sbueno+anaconda)
- We now need to specify an epoch for the python-blivet version requires.
  (clumens)
- Fix autotools rules to properly include help placeholders (#1072033)
  (mkolman)
- Modify nm to return defaults when no dbus is available (bcl)
- Skip networkInitialize for image and dir installations (bcl)
- Ignore safe_dbus errors in keyboard setup (bcl)
- Skip syslog for dirinstall (bcl)
- s390x: show dialog if kernel cmdline in zipl.conf is too long.
  (sbueno+anaconda)
- Really exit when "Exit installer" in the error dialog is clicked (vpodzime)
- Don't allow /boot on lvm on s390x. (sbueno+anaconda)
- Add the new langsupport.py TUI spoke to POTFILES.in. (clumens)
- Remove the now-unused imports of storageInitialize. (clumens)
- Add support for language selection in text mode. (sbueno+anaconda)
- Don't force a user to return to the storage spoke after dasdfmt
  (sbueno+anaconda)
- Don't run storageInitialize after dasdfmt (sbueno+anaconda)
- s390x: Apply disk selection before dasdfmt to preserve data.
  (sbueno+anaconda)
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
- Preserve network args on s390x. (sbueno+anaconda)
- Deprecate RUNKS cmdline option. (sbueno+anaconda)
- Re-order the tz's in text mode to mirror the graphical order.
  (sbueno+anaconda)
- Fix an issue with bad NFS info specified in source spoke. (sbueno+anaconda)
- Warn if software selection size exceeds available space. (sbueno+anaconda)
- Fix q for quit issue in text mode (#997405) (sbueno+anaconda)
- Change the accelerator key for Add DASD label. (sbueno+anaconda)
- Add dialog box for adding DASDs. (sbueno+anaconda)
- Add a button for adding an ECKD DASD. (sbueno+anaconda)
- Change a confusing string in TUI NFS configuration screen. (#1057690)
  (sbueno+anaconda)
- NM-wifi is missing on s390(x) (dan)

* Wed Oct 01 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.8-1
- Show help also when alt+F1 is pressed (mkolman)
- Support display of the custom mnemonics on the help button (mkolman)
- Activate the built-in help when F1 is pressed (mkolman)
- Specify help file names for hubs and spokes (mkolman)
- Add a help button to every Anaconda screen (mkolman)
- Don't attempt terminal size detection on the s390 (#1145065) (mkolman)
- Fix Welcome spoke not showing up during kickstart installation (#1147943)
  (mkolman)
- Clear the list of watched PIDs before exiting. (#1146708) (dshea)
- Avoid the possibility of size variables being unset (#1146585) (dshea)
- Adapt to corrected interpetation of logvol --percent. (#1146156) (dlehman)
- Handle cancellation of new container creation. (dlehman)
- Reflect previous custom/autopart selection in the storage spoke. (#1144520)
  (dlehman)
- Clear out custom storage ksdata after first attempt to apply it. (#1144560)
  (dlehman)
- Pass size as Size when adjusting container after device removal. (#1141707)
  (dlehman)
- Handle 0's returned by Gdk (dshea)
- When running on HiDPI monitors, scale anaconda by a factor of 2 (dshea)
- Highlight languages in langsupport that contain selected locales (dshea)
- Add a wrapper function for GtkTreeViewColumn.set_cell_data_func (dshea)
- Clear the kickstart password if cleared by the user (#1133185) (dshea)
- Remove inactive languages from LINGUAS. (dshea)
- Use suggested-action on more buttons (#1131254) (dshea)
- Filter empty comps groups from both specific and generic lists (dshea)
- Use one thread for payload setup. (dshea)

* Wed Sep 17 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.7-1
- Set flags.rescue_mode not anaconda.rescue (#1101341) (amulhern)

* Thu Sep 11 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.6-1
- Update tx config (sbueno+anaconda)
- Use only the digits from productVersion (bcl)

* Tue Sep 09 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.5-1
- Revert productName repo name change (#1128474) (bcl)
- Do not try to disable no firstboot services (#1139621) (vpodzime)
- Let finding install classes be more flexible for Fedora (#1138820). (clumens)

* Thu Sep 04 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.4-1
- Use first part of Product for UEFI entry (#1128474) (bcl)
- Use first part of Product as repo name (#1128474) (bcl)
- makeupdates: Report git diff errors (bcl)

* Wed Aug 27 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.3-1
- Prevent crashes due to accessing X server from multiple threads (#1134507)
  (vpodzime)
- Remove anaconda_make_pixbuf (dshea)
- Require anaconda-widgets from anaconda-widgets-devel (dshea)
- Run /sbin/ldconfig when installing or uninstalling anaconda-widgets (dshea)
- Remove the shebang from anaconda.py (dshea)
- Exclude the compiled text and rescue files from anaconda-core (dshea)
- Update our copy of the GPL (dshea)
- Rearrange the entry, example and tip on Advanced User dialog (vpodzime)
- Write storage after liveimg install (#1080396) (bcl)
- Add some sanity checking to live payload (vpodzime)
- Use blivet's getFreeSpace for limitting automatic swap size (vpodzime)
- Ask users for enough space right at the first time (#876916) (vpodzime)
- Don't require user creation when root is locked (#1030626) (bcl)

* Fri Aug 01 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.2-1
- Mark zRAM devices as protected and ignore them (vpodzime)
- Make storage sanity check aware of base RAM requirements (#1123466)
  (vpodzime)
- Move sanityCheck code to anaconda's codebase (vpodzime)
- Do not multiply/divide RAM sizes by 1024 back and forth (vpodzime)
- Raise exception if reading lines from a killed process (vpodzime)
- Use zRAM swap up to 2 GB of RAM (vpodzime)
- RAM requirements depend on squashfs.img's origin (vpodzime)

* Wed Jul 23 2014 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 21.48.1-1

* Wed Jul 16 2014 Brian C. Lane <bcl@redhat.com> - 21.48-1
- Fix the custom accelerators in custom partitioning (#1118999) (dshea)
- Revert "Reset dnf package sack" (bcl)
- Ignore the home directory setting if no change was requested (#1119900)
  (dshea)
- Set an upper limit on uids and gids. (dshea)
- Remove the "Create a home directory" checkbox (dshea)
- Fix a typo: inital -> initial (mkolman)
- Don't create the configured.ini file (#1119166) (mkolman)
- zRAM swap for Anaconda (vpodzime)
- Split kickstart arg handling (bcl)
- Update icon names used within python code. (dshea)
- Add a check for whether icons used in glade files are valid (dshea)
- Load icons by name instead of stock-id. (dshea)
- Remove extra list() call with no effect (vpodzime)
- Add NetworkManager-wifi dependency for the GUI subpackage (#1111417)
  (mkolman)
- Python's octals changed; mount's didn't. (pjones)
- Add a basic test for ostree-based installs. (clumens)
- Print out exceptions at log level critical. (clumens)
- Rename environment variables in run_gui_tests.sh. (clumens)
- Rename gui/runtest.sh to fit in with the other test names. (clumens)
- Write the grub config even on errors (#1114774) (bcl)

* Fri Jul 11 2014 Brian C. Lane <bcl@redhat.com> - 21.47-1
- Fix references to requiredPackages (bcl)
- Drop anaconda. prefix from copied logs (bcl)
- dnf should put its logs in /tmp/ (bcl)
- Make sure the software listboxes are shown (bcl)
- dnf should report that it supports Closest Mirror (bcl)
- Do not prefer /tmp for dnf downloads (bcl)
- Reset dnf package sack (bcl)
- Fix dnf base repo setup to fall back to default gracefully (bcl)
- Move addDriverRepo into PackagePayload class (bcl)
- Rename some dnf items to match yum (bcl)
- rpmostreepayload: Drop selinux-ensure-labeled call (walters)
- Run anaconda in fullscreen whenever possible. (dshea)
- Correct the constant used with gtk_widget_set_state_flags (dshea)
- Restore some CSS rules from the pre-3.13 Adwaita theme. (dshea)
- Adapt to changes in blivet.udev interface. (amulhern)
- Bump blivet version to pick up blivet.udev interface changes. (amulhern)
- Use the enlightbox context manager for the add network device dialog
  (mkolman)
- DNFPayload: do not add group 'core' twice. (ales)
- Remove the window property from UIObject. (dshea)
- Unravel the Hub and Spoke classes. (dshea)
- Fix --kickstart option (bcl)
- Bump up the required pykickstart version (vpodzime)
- Use GtkRevealer for widget hiding in storage spoke (mkolman)
- rpmostreepayload: create /var/spool/mail required when adding user (rvykydal)
- rpmostreepayload: Don't recreateInitrds for this payload (walters)
- Don't use geolocation when installing with kickstart (mkolman)

* Wed Jul 02 2014 Brian C. Lane <bcl@redhat.com> - 21.46-1
- Ignore an error from pylint incorrectly analyzing types in dbus-python
  (dshea)
- Remove the Lightbox widget (dshea)
- Implement the lightbox in MainWindow (dshea)
- Added a method to create new GdkPixbufs from in-memory data (dshea)
- Add a delete-event handler for the main window (dshea)
- Add a window to manage Anaconda screen transitions. (dshea)
- Add a class BaseStandalone. (dshea)
- Increased the version of anaconda-widgets to 3.0 (dshea)
- Use globs for the anaconda widgets library paths (dshea)
- Remove the custom accelerators from custom storage. (dshea)
- Add a couple more deprecation warning ignores (dshea)
- Use a dict for string substitutions in a /boot/efi message. (clumens)
- Use the right index for selecting region (#1114234) (vpodzime)
- Add autopart --fstype support (#1112697) (bcl)
- Patches to allow /boot/efi to be RAID1 (#788313) (amulhern)
- Bump blivet version for succeeding commit. (amulhern)
- Map our log levels to syslog log levels (bcl)
- makeupdates: Put systemd files under /usr/lib/ (bcl)
- Make octal literals Python 3 compatible (mkolman)
- Use the built-in next() function for generators (mkolman)
- Make reduce function usage Python 3 compatible (mkolman)
- Use createrepo_c in place of createrepo (mkolman)

* Fri Jun 27 2014 Brian C. Lane <bcl@redhat.com> - 21.45-1
- Switch to tty1 if we get an exception before meh is setup (dshea)
- Remove surprises from X startup. (dshea)
- Import KS_MISSING_IGNORE from pykickstart.constants in DNF payload (mkolman)
- Import Pykickstart constants directly (mkolman)
- Switch error exit codes to 1 (bcl)
- Add help texts for the remaining Anaconda options (mkolman)

* Wed Jun 25 2014 Brian C. Lane <bcl@redhat.com> - 21.44-1
- Fix storage checker docstring (bcl)
- Modify --dirinstall to take a path (bcl)
- Drop ROOT_PATH, add a method to set it (bcl)
- Call setUpBootLoader in custom autopart (#1086811) (bcl)
- Remove the noipv6 Anaconda option (mkolman)
- Remove the -s/--script Anaconda option (mkolman)
- Make rescue_mode part of flags, hence more publicly available (#1090009)
  (amulhern)
- Check host filesystem space for dirinstall (bcl)
- Remove the viewport from the addon repo tree view (dshea)
- Add a check for GtkScrollables contained in GtkViewports (dshea)
- Enable rubber-banding in the disk tree views (dshea)
- Make the configure mount point dialog taller. (#924182) (dshea)
- Add the disk TreeViews directly to the scrolled windows (dshea)
- Opened up custom_storage_helpers.glade and hit Save (dshea)
- Add help texts for more Anaconda CLI options (mkolman)
- Remove the targetarch Anaconda option (mkolman)
- Add anaconda_options.txt to makeupdates (dshea)
- Allow the location of anaconda_options.txt to be overridden (dshea)
- Remove an unused import. (dshea)
- Remove the headless Anaconda option (mkolman)

* Thu Jun 19 2014 Brian C. Lane <bcl@redhat.com> - 21.43-1
- Allow NFS addon repos (#985080) (dshea)
- Add --disklabel support to clearpart (#1078537) (bcl)
- Replace redundant ifs with direct assignments to the anaconda variables
  (mkolman)
- Replace ifs when assigning option values to flags where possible (mkolman)
- Use True/False instead of 1/0 for flags (mkolman)
- Store auto gui results in the same directory as the test itself. (clumens)
- Use whatever network device was used to start installation. (clumens)
- Ignore more deprecation warnings. (dshea)
- Add help texts for the dmraid and nodmraid options (mkolman)
- Use True instead of 1 for the dmraid flag default value (mkolman)
- Add help texts for the ibft and noibft options (mkolman)
- Use True instead of 1 for the ibft flag default value (mkolman)
- Remove the iscsi and noiscsi options (mkolman)
- Add a new log level 'lock' for _yum_lock (bcl)
- Replace uses of gtk-missing-image (dshea)
- Improve the SpokeSelector icon error reporting. (dshea)

* Thu Jun 12 2014 Brian C. Lane <bcl@redhat.com> - 21.42-1
- Adjust the ui package paths to find hubs and spokes (bcl)
- Change emphasis from subvolumes to snapshots in removal warning. (dlehman)
- Reflect the fact that some block devices cannot be reformatted. (dlehman)
- Use StorageDevice.direct to detemine if a device is directly accessible.
  (dlehman)

* Wed Jun 11 2014 Brian C. Lane <bcl@redhat.com> - 21.41-1
- Use /usr/lib* in updates images. (dshea)
- Fix the paths we check for spokes. (sbueno+anaconda)
- Remove the kbdtype option (mkolman)
- Remove the noipv4 option (mkolman)
- Remove the autostep option (mkolman)
- Remove the disused nofb option (mkolman)
- Remove the module option (mkolman)

* Tue Jun 10 2014 Brian C. Lane <bcl@redhat.com> - 21.40-1
- fedora-welcome: Correct an icon name after the switch to Adwaita
  (kalevlember)
- Pass/check displaymode in collect_categories and collectCategoriesAndSpokes.
  (sbueno+anaconda)
- Add help texts to some Anaconda CLI options (mkolman)
- Don't install implicitly added but explicitly excluded packages (#1105013)
  (vpodzime)
- Update configure, make files, and PO files with new category changes.
  (sbueno+anaconda)
- Fix up collectCategoriesAndSpokes function. (sbueno+anaconda)
- Update all relevant UI files with new category path. (sbueno+anaconda)
- Move categories to pyanaconda.ui.categories. (sbueno+anaconda)
- Allow testing a regular install from the live environment. (clumens)
- Make sure /var/log/anaconda gets copied under the right root. (clumens)
- format.setup in blivet takes only kwargs. (clumens)
- Tweak spacing in the other storage options grid. (clumens)
- Remove the dlable option (mkolman)
- change default for grub2 save_entry to 0 (gczarcinski)
- Revert "Refresh after checkbox clicked (#1074188)" (dshea)
- Move assureLogoImage to GraphicalUserInterface (#1102238) (dshea)
- If we cannot activate keyboard, at least populate the missing items
  (#1104541) (vpodzime)
- network: generate dracut arguments also for IPADDRn ifcfg values (#1103571)
  (rvykydal)
- Memoize the results for *RaidLevelsSupported() functions (amulhern)
- RAID related changes for custom spoke. (amulhern)
- Bump required blivet version. (amulhern)
- Make parse-kickstart aware of the %%addon section (#1083002) (vpodzime)
- Revert "Work around a parsing bug in GtkBuilder" (dshea)
- Fix a typo in one of the bootloader installation warning messages (#1103410)
  (mkolman)
- Don't require network in standalone spoke for media installs (#1066807)
  (rvykydal)

* Mon Jun 02 2014 Brian C. Lane <bcl@redhat.com> - 21.39-1
- eu_ES has been dropped from the supported languages (bcl)
- Change 'elif encrypted' statement to 'else' statement. (amulhern)
- Work around a parsing bug in GtkBuilder (dshea)
- Don't uppercase the size values in the disk shopping cart. (clumens)
- Display the sentence about being able to reuse partitions even without roots.
  (clumens)
- Allow a couple more keyboard shortcuts on the custom part spoke. (clumens)
- Reword the close button on the software spoke's error dialog. (clumens)
- Fix up quoting around passing args to anaconda in the gui test. (clumens)
- Don't hide a serious issue (vpodzime)
- Move autopart choices to one place and use them in both GUI and TUI
  (vpodzime)
- Define default autopart type as a constant (vpodzime)
- Use enumerate() instead of getting indices of iterated items (vpodzime)
- Preserve net.ifnames cmdline arg (#1102401) (bcl)
- Revert the dialog sizing chunk from resize.glade. (clumens)
- Update GUI tests for changes in gtk/atk/anaconda/whatever. (clumens)
- Fix gui/runtest.sh to work under either "make check" or being run manually.
  (clumens)
- Add a -c argument to the ksflatten invocation. (clumens)
- Do basic logging setup when short circuiting the normal Anaconda init
  (mkolman)
- Fix boot option warning string formatting (mkolman)
- always rescan for vmlinuz if rescueKernelList (gczarcinski)
- move new-kernel-pkg rpmposttrans to end of install (gczarcinski)
- allow /boot on btrfs subvol or filesystem (gczarcinski)
- Allow /boot on LVMlv (gczarcinski)

* Wed May 28 2014 Brian C. Lane <bcl@redhat.com> - 21.38-1
- Parse boot options before parsing CLI options (#1101341) (mkolman)
- Check that bootloader devices are configured before validating (#1100928)
  (dshea)
- network: use IpInterface only for activated devices (#1101781) (rvykydal)
- Enable LVM Thin Provisioning in text mode (vpodzime)
- Remove the executable bit from anaconda.spec.in. (clumens)
- Fix the nm test for big-endian results (dshea)
- Fix issues with auto* and version.py (dshea)
- Allow file:// url handler in --repo arg (bcl)
- Ignore deprecation warnings for atk_role_register (dshea)
- Handle renames in makeupdates. (pjones)
- Move Anaconda version detection from isys to Python code (mkolman)
- network: use IpInterface instead of Interface (#1058906, #1029214) (rvykydal)
- network: don't modify network config for dirInstall and imageInstall
  (rvykydal)
- network: remove redundant image install guard (rvykydal)
- network: add first tests for nm.py (rvykydal)
- network: consolidate setNetworkOnbootDefault (rvykydal)
- Set ONBOOT=yes for the device used for installation (#1002544). (rvykydal)
- Use proper data for autopart type initialization (vpodzime)
- Line up the right side of the FCOE dialog. (clumens)
- Use default_width and _height on dialogs instead of _request. (clumens)
- Remove the border around the refresh storage dialog's button. (clumens)
- Short-circuit initialization when printing out Anaconda version (mkolman)
- Make print statements Python 3 compatible (mkolman)
- Fix the handling of set_const options pulled in from the boot cmdline (dshea)
- Fix the modify software tooltip on the installation options dialogs.
  (clumens)
- Better visually distinguish TUI spokes states (vpodzime)
- Reset the text direction as soon as the locale is changed (dshea)
- Show errors from the displayed mountpoint when exiting the custom spoke
  (dshea)
- Check that container names input by the user are valid (dshea)

* Tue May 20 2014 Brian C. Lane <bcl@redhat.com> - 21.37-1
- Chain up to parent size_allocate functions in our standalone widgets.
  (clumens)
- Format the help text to properly fit to the terminal window (mkolman)
- Call getPossiblePhysicalExtents() only once (vpodzime)
- Default PE size to blivet's default when requested from kickstart (#1098139)
  (vpodzime)
- A couple of anaconda whitespace fixes (mkolman)
- Replace the deprecated has_key() by in (mkolman)
- Disable pylint errors on NetworkData in the new network_test.py. (clumens)
- Tweak borders on the filter UI. (clumens)
- network: add tests (rvykydal)
- network: don't use ifcfg PREFIX when generating ipv6 dracut args (rvykydal)
- network: cleanup - remove ksdevice variable (rvykydal)
- Horizontally center the user creation spoke contents. (clumens)
- Un-indent the reclaim space checkbox. (clumens)
- Remove the RAID page from the filter UI. (clumens)
- install -> installation in a string on the source spoke. (clumens)
- Switch Anaconda to argparse (mkolman)
- rpmostreepayload: Use systemd-tmpfiles rather than handrolling mkdir
  (walters)
- Add some padding to the custom partitioning note. (dshea)
- Wrap the custom partitioning note (#1031850) (dshea)
- Make an ostree string easier for translators to deal with. (clumens)
- Fix the gettext warnings test for VPATH builds (dshea)
- network: fix crash on empty ksdevice boot option (#1096846) (rvykydal)
- Add RPMOSTreePayload (walters)
- bootloader: Allow extlinux loader configuration to handle RPMOSTreePayload
  case (walters)
- install: Handle distinct physical root/sysroot (walters)
- parse-kickstart: drop "mtu=" args (wwoods)
- Drop workaround for old dracut BOOTIF+ip problem (wwoods)
- Fix behavior (and docs) for ks=nfs:<path>/ (#1094645) (wwoods)
- Allow non-ASCII characters in passwords (#960837) (dshea)
- Use a separate label for passphrase warnings. (dshea)
- Move more of the passphrase dialog into the glade file. (dshea)
- Don't add redundant grub installs if stage1 is not a disk (dshea)
- Let the user continue on bootloader errors (#1006304) (bcl)
- Fix the parsing of NFS addon URLs (#966240) (dshea)
- Remove redundant import (mkolman)
- Don't overwrite function argument when parsing help texts (mkolman)
- Return CLI help text at once (mkolman)
- Fix typo in previous commit adjusting to blivet API change. (dlehman)
- Adjust for movement of functions from examples into blivet proper. (dlehman)

* Thu May 08 2014 Brian C. Lane <bcl@redhat.com> - 21.36-1
- Switch to adwaita-icon-theme (kalevlember)
- Hook up the TUI categories to autoconf/make. (#1095220) (dshea)
- Fix the object type specifying argument name for findActions (vpodzime)
- Remove keyword args 'ignoreErrors' from umountFilesystems() call. (amulhern)
- Updates for new blivet.size.Size.__new__ interface. (amulhern)
- Change uses of 'format' keyword param to 'fmt' keyword param (amulhern)
- Update devicetree.findActions invocations to match blivet interface change
  (amulhern)
- Bump blivet version to ensure next four patches get the right interface.
  (amulhern)

* Mon May 05 2014 Brian C. Lane <bcl@redhat.com> - 21.35-1
- Use format strings in the new kickstart error message translations. (clumens)
- Mark kickstart errors as translatable, and hopefully make them more useful
  too. (clumens)
- install: Move Payload postInstall() after bootloader (walters)
- iutil: Transparently redirect anyone who asks root=/mnt/sysimage to sysroot
  (walters)
- Fix the way categories are handled in text mode. (sbueno+anaconda)
- Move GUI-specific helper classes to a separate module (#1091542) (dshea)
- Fix license in parse-kickstart (mkolman)
- main: Set flags.extlinux if extlinux is used in interactive-defaults.ks
  (walters)
- anaconda.service: Set GIO_USE_VFS=local (walters)
- Use a gettext context where necessary when retranslating (#1091207) (dshea)
- Update makebumpver for python-bugzilla 1.0.0 (bcl)
- Skip source and software spoke in text live installations (#1092763) (bcl)
- Add correct kernel params if rootfs is btrfs on s390x. (#874622)
  (sbueno+anaconda)
- Don't crash on anaconda-yum output containing multiple colons (#1092441)
  (mkolman)
- Revert chrooting when setting user/root password (vpodzime)
- network: fix device configuration in text mode (#1058336) (rvykydal)
- Change order in which packages/groups are selected/excluded (#1091952)
  (vpodzime)
- Check the correct button when saving changes in the Custom spoke (#1090786)
  (vpodzime)
- Fix unloading modules in driver-updates (#1085099) (wwoods)
- Re-saved some of the glade files with a newer version of glade. (dshea)
- Add viewports for the ListBoxes in the software spoke. (dshea)
- Extend format string checks to translated format strings. (dshea)
- Fix typo in nm_is_connected method check. (rvykydal)
- iutil: Introduce getSysroot()/getTargetPhysicalRoot(), use instead of
  ROOT_PATH (walters)

* Thu Apr 24 2014 Brian C. Lane <bcl@redhat.com> - 21.34-1
- Improve the "adding yum repo" message structure (mkolman)
- Fix missing log message about adding a repository (#1089297) (mkolman)
- Ignore use of eval warnings. (dshea)
- Specify string format arguments as logging function parameters (dshea)
- New encrypted state is the dialog's encrypted attribute (vpodzime)
- Use human readable sizes with two decimal spaces in the GUI (vpodzime)
- Make the LUKS unlock callback a timed action (vpodzime)
- Hitting ENTER in the LUKS passwd entry should click the Unlock button
  (vpodzime)
- Block leaf device encryption if container is encrypted consistently
  (vpodzime)
- Do not remove the replacing item, remove the replaced one instead (vpodzime)
- Give include_btrfs variable a better name (vpodzime)
- Make the _resolve_btrfs_restrictions method's code nicer (vpodzime)
- Refactor the btrfs magic into a separate method (vpodzime)
- Switch the condition in long if-else statement (vpodzime)
- Give an opaque condition a better name explaining its real meaning (vpodzime)
- Refactor out the code for removing empty parents (vpodzime)
- Use the (vpodzime)
- Refactor out the code for adding device/mountpoint into a method (vpodzime)
- Relabel /home partition if using and existing one (#1087736) (vpodzime)
- Don't forget to call os._exit() in the child process (vpodzime)
- users: Add root= keyword argument to set{User,Root}Password (walters)
- users: Deduplicate code to fork()+chroot() (walters)
- gui/spokes/software: Enable iff payload is PackagePayload (walters)
- Use descriptive pylint messages instead of numbers. (clumens)
- Add input validation to the source spoke. (dshea)
- Remove the tests for duplicate and invalid repo names (dshea)
- Expand the proxy URL validation. (dshea)
- Convert the repository name test into a regex (dshea)
- Add a remove_check method for InputCheckHandler. (dshea)
- Use ID columns in the protocol combo boxes (dshea)
- Added a link to a bug about the user data in glade problem. (dshea)
- Remove the top and bottom padding from source spoke action area (dshea)
- Re-add a false-positive for the GLib module (dshea)

* Thu Apr 17 2014 Brian C. Lane <bcl@redhat.com> - 21.33-1
- Add an option to copy translation files to an updates.img (dshea)
- Set the selinux state from the command line (#784828) (dshea)
- Remove a whole bunch of pylint false positives (dshea)
- Ignore more informational messages printed by pylint pragmas (dshea)
- Use more wildcards in the tests dist_ variable (dshea)
- Make sure the idx variable is used instead of the old found variable
  (vpodzime)
- Disable a false positive from pylint (dshea)
- Only run dialogs in the enlightbox context (vpodzime)
- Separate code for finding item in containers combo and processing it
  (vpodzime)
- Check Update Settings button sensitivity when saving changes in one place
  (vpodzime)
- Only save changes if needed when adding mountpoint (vpodzime)
- No need to call bool() on a boolean expression result (vpodzime)
- Give names to some magic tuples, make them reusable and reuse them (vpodzime)
- Add DEVICE_TYPE_DISK's text description to the mapping (vpodzime)
- Move a few constants and mappings to the storage_utils module (vpodzime)
- Split long label's string into two lines (vpodzime)
- Don't rely on the ordering of autopart types in the combobox (vpodzime)
- Only save changes if there are any changes to be saved (vpodzime)
- Add device type constants to the device type combobox's store (vpodzime)
- Change some anaconda-yum DEBUGs to be more informative (bcl)
- Change Proxy Add Button to Ok (bcl)
- Display a message for missing required packages and groups (#1064565) (dshea)
- Fix issues with the errorHandler callback arguments (dshea)

* Thu Apr 10 2014 Brian C. Lane <bcl@redhat.com> - 21.32-1
- Refactor the code setting up the device type combobox a method (vpodzime)
- Rename 'swap' variable to 'is_swap' to better express its meaning (vpodzime)
- Refactor out the code setting up the fstype combobox into a method (vpodzime)
- Refactor the code updating info about device container into a method
  (vpodzime)
- Remove the default None value from the addPage's cb argument (vpodzime)
- Make on_updates_settings_clicked timed callback (vpodzime)
- Rename the callback for updating mountpoint settings (vpodzime)
- Hook up the GUI test so it's run as part of "make check". (clumens)
- Skip running pylint on files containing "skip-file". (clumens)
- Add comments to the kickstart tests. (clumens)
- Add the beginnings of an automated GUI test suite. (clumens)
- Add accessibility information to the user spoke. (clumens)
- Add accessibility information to the root password spoke. (clumens)
- Add accessibility information to the progress hub. (clumens)
- Add accessibility information to most of the widgets on the storage spoke.
  (clumens)
- Add enough accessibility information to the network spoke for livecds.
  (clumens)
- Add accessibility information to the keyboard spoke. (clumens)
- Add accessibility information to the date & time spoke. (clumens)
- Add a script and base kickstart file for making a dogtail-enabled livecd.
  (clumens)
- Add accessibility information to the welcome spoke and summary hub. (clumens)
- Add accessibility information to some of our widgets. (clumens)
- Don't use dhcp ntpservers for dir or image installation (bcl)
- Implement and use decorator for logging UI storage actions (vpodzime)
- Refactor out the code doing device reformat into a function (vpodzime)
- Refactor out the code handling encryption change into a function (vpodzime)
- Fix variable name when logging new fstype (vpodzime)
- Make it possible to override translation domain in GUIObjects (#1040240)
  (mkolman)
- Refactor out the code for handling device size change into a function
  (vpodzime)
- Refactor out the code for bounding size into a function (vpodzime)
- Refactor code for reverting device reformat into a function (vpodzime)
- Make the code changing an existing device more compact (vpodzime)
- Comment the part of the code changing an existing device (vpodzime)
- Do device change logging in one place where possible (vpodzime)
- Pass information about old and new device as a dictionary (vpodzime)
- Move code attempting to replace device into a separate function (vpodzime)
- Mountpoint validation should only care about the new fs type (vpodzime)
- Make size properties refreshing reused code (vpodzime)
- Use generator instead of list for auxiliary old_disk_names variable
  (vpodzime)
- Remove and unused variable in Custom spoke (vpodzime)
- Refactor mountpoint configuration validation out from _save_right_side
  (vpodzime)
- Don't overload selectorFromDevice function (vpodzime)
- Use dir_tree_map for the cleanPStore function (vpodzime)
- Check xconfig before setting the installed displaymode (dshea)
- DNFPayload: call close() when done with the Base. (ales)
- Do not try to get "" translated (vpodzime)
- Use for-cycle else: branch instead of extra variable (vpodzime)
- Have mountpoint descriptions defined in a dictionary (vpodzime)
- Uppercase global constants in the Custom spoke (vpodzime)
- Use cannonical RAID level names when populating RAID stores (vpodzime)
- No RAID level (RAID level None) is a valid choice for LVM(ThP) (vpodzime)
- LVM Thin Provisioning supports the same RAID levels as plain LVM (vpodzime)
- Only block the password/user spokes if data was given in kickstart (vpodzime)
- Disable a pylint error message for now. (clumens)
- Suppress selinux error log when using default (#1083239) (bcl)
- Use the AnacondaWidgets python gi-overrides for pylint (dshea)

* Wed Apr 02 2014 Brian C. Lane <bcl@redhat.com> - 21.31-1
- Only install consolehelper link on livearches (bcl)

* Wed Apr 02 2014 Brian C. Lane <bcl@redhat.com> - 21.30-1
- Add support ppc64le (hamzy)
- Validate proxy URLs (dshea)
- Provide feedback for invalid NTP hostnames. (dshea)
- Use GUIDialogInputCheckHandler in the advanced user dialog (dshea)
- Add a new InputCheck status for silent failures. (dshea)
- Add an InputCheckHandler subclass for dialogs. (dshea)
- Generalized and improved the proxy URL parsing regex (dshea)
- Update makebumpver for the newer python-bugzilla on rawhide. (clumens)
- network: don't crash on virtual devices turned off (#1080640) (rvykydal)
- network: don't pop HWADDR twice for vlan on s390 (#1061646) (rvykydal)
- Make safe_dbus module's functions less 'safe' (vpodzime)
- Add a list of cmdline args that append instead of replace (#1073130) (bcl)
- safe_dbus: Don't export DBus connection addresses as variables (walters)

* Wed Mar 26 2014 Brian C. Lane <bcl@redhat.com> - 21.29-1
- Add a Makefile target to create a set of empty .po files. (dshea)
- os.path.exists -> os.path.lexists when checking for authconfig. (clumens)
- Add support for tarfiles to liveimg kickstart command (bcl)
- mountExistingSystem raises an exception with dirty FS (#1080210) (vpodzime)
- Don't do yum lock logging when using updates.img (vpodzime)
- Pass Size(0) instead of 0 to the ContainerDialog if no size is given
  (vpodzime)
- Update the BaseWindow and HubWindow example UI fragments (dshea)
- Convert GtkHBox and GtkVBox to GtkBox. (dshea)
- Fix keyboard accelerator collisions from former stock buttons (dshea)
- Set the secret agent icon in the glade file (dshea)
- Remove stock labels and icons. (dshea)
- Run the pykickstart version test on the commands in parse-dracut (dshea)
- Don't reimport os - it's imported very early on. (clumens)
- Use an alternative image if logo is missing (mkolman)
- Update parse-kickstart for the new bootloader command. (clumens)
- Make sure the error info message starts on a new line (vpodzime)
- Define two env variables removing useless warnings (vpodzime)
- Check boot args for None (#1075918) (bcl)
- Revert "Enable make check in %%check and add the necessary BuildRequires"
  (dshea)
- Fix the argument list passed to the payloadInitialize thread (#1079628)
  (dshea)
- Fix filtering the _storage_playground out (vpodzime)
- Sync up step counts in install.py with reality. (clumens)
- Avoid the "unable to init server" message. (dshea)
- Do not attempt to run authconfig if it doesn't exist. (clumens)
- Allow skipping installation of the core group, if asked for in kickstart.
  (clumens)
- Drop the vconsole.font boot arg (#1074113) (vpodzime)

* Thu Mar 20 2014 Brian C. Lane <bcl@redhat.com> - 21.28-1
- Get the DBus session bus address in a method (dshea)
- Specify string format arguments as logging function parameters (dshea)
- Inhibit the screen saver on live installs (#928825) (dshea)
- Handle the dbus method call not returning anything. (dshea)
- Convert errors raised during dbus connection to DBusCallError (dshea)
- driverdisk: Show selection menu for network driver isos (#1075918) (bcl)
- Write a modprobe blacklist (#1073130) (bcl)
- Append cmdline arg values in BootArgs (#1073130) (bcl)
- Wait for other threads to finish before sending ready (#1075103) (bcl)
- set proxy related environmental variables (#854029) (bcl)
- Fix pylint error in yumpayload. (sbueno+anaconda)
- The custom spoke requires mountPointStore and mountPointCompletion, too.
  (clumens)
- Make the lists of files to check consistent across all checks. (dshea)
- Fix error handling in cmdline mode. (#1034773) (sbueno+anaconda)
- Don't create bootloader entries for kdump initrd and kernel. (#1036086)
  (sbueno+anaconda)
- Add a setting to network.py that got left out of the cherry-pick. (clumens)
- Enable make check in %%check and add the necessary BuildRequires (atodorov)
- Make it obvious user is going to begin installation. (#975793)
  (sbueno+anaconda)
- Move libtimezonemap requires to the anaconda-gui subpackage (vpodzime)
- network: apply ks configuration to devices activated in initramfs (#1037605)
  (rvykydal)
- Add support for kickstart --interfacename for vlans (#1061646) (rvykydal)
- network: handle race condition of disappearing active connection (#1073424)
  (rvykydal)
- Convert iter from filter model iter to backing store iter (#1074188)
  (amulhern)
- Provide ways in kickstart to skip kernel and bootloader (#1074522). (clumens)
- DNFPayload: apply the kickstart excludedList. (ales)
- Only pylint files that are in the git working copy (dshea)
- Move accordion population into a separate function (vpodzime)
- Short-circuit testing if root has any devices (vpodzime)
- Getting new devices is not enough cheap operation for being a property
  (vpodzime)
- Hide and unhide the same set of disks in the Custom spoke (vpodzime)
- Use GtkActionList when populating filesystem store (vpodzime)
- Fix XDG_RUNTIME_DIR not set messages by creating one (dshea)
- Make the ui_storage_logger reusable (vpodzime)
- Decide on supported RAID levels in a better way (vpodzime)
- Fix typo in the comment (vpodzime)
- Add and use MountpointSelector's attributes we need (vpodzime)
- Make code to get Size instance from user's input reusable (vpodzime)
- Make getting raid level less hacky (vpodzime)
- Implement a function to get container type name (vpodzime)
- Make custom partitioning helper constants look as constants (vpodzime)
- Simplify mountpoint validation and error reporting (vpodzime)
- Simplify label validation and error reporting (vpodzime)
- Move translated_new_install_name to the right place (vpodzime)
- Rename the __storage attribute to a more propriate name (vpodzime)
- Split out helper code from the Custom partitioning spoke (vpodzime)
- The reset button should only be sensitive if there's something to reset.
  (clumens)
- Confirm before resetting custom partitioning selections (#970093). (clumens)
- DNFPayload: Add languageGroups(). (ales)
- Use ROOT_PATH not /mnt/sysimage (bcl)
- Override ROOT_PATH with environmental variable (bcl)
- Import /etc/login.defs in libuser.conf (#979815) (dshea)
- Fix environment group changes based on ListBox row activation (dshea)
- DNFPayload: do not crash when an addon is unavailable. (ales)
- Payloads: make DEFAULT_REPOS a part of the interface. (ales)

* Tue Mar 11 2014 Brian C. Lane <bcl@redhat.com> - 21.27-1
- Don't disable anaconda repo on rawhide (bcl)
- Set log level to debug when using an updates image (bcl)
- driver-updates: accept burned driver discs (#1073719) (wwoods)
- Do nothing if previously selected selector gets focus again (#1029798)
  (vpodzime)
- Firstboot is deprecated and gone on Fedora 20 and anything newer (vpodzime)
- Reraise the exception properly (vpodzime)
- Set progress bar to 100 %% in a different way (#1058755) (vpodzime)
- Refresh after checkbox clicked (#1074188) (amulhern)
- Use instclass.efi_dir when constructing the EFI path (dshea)
- Add rescue kernels to the bootloader install list. (#1036349) (dshea)
- Cover both possible ways that GUI WWID may have been set (#1074184)
  (amulhern)
- Do not write out /etc/adjtime file on s390(x) (#1070748) (vpodzime)
- Ignore the data model and just return self.environment (mkolman)
- Software spoke can't be complete if the payload thread is running (mkolman)
- DNFPayload: blivet.size.Size() only knows 'spec' kwarg now. (ales)
- Specify string format arguments as logging function parameters (dshea)
- Add missing changelog entries (bcl)

* Fri Mar 07 2014 Brian C. Lane <bcl@redhat.com> - 21.26-1
- Don't traceback, just log a warning if connection is unavailable (#1070928)
  (mkolman)
- Remove unnecessary use_markup attributes. (dshea)
- Add a check for unnecessary markup. (dshea)
- Ignore the server keymap for spoke status if using VNC (#1045115) (dshea)
- Call % outside of the translation (dshea)
- Fix pylint errors about dangerous default values (dshea)
- Typo fix (dshea)
- driver-updates: skip iso selection with OEMDRV (#1066784) (bcl)
- driver-updates: allow interactive mode to load multiple devices (wwoods)
- driver-updates: add DoRefresh loop to select_iso() (#1066784) (wwoods)
- driver-updates: add 'refresh' to selection_menu() (wwoods)
- driver-updates: rework 'dd_finished' handling (wwoods)
- driver-updates: refactor dd_scan (wwoods)
- driver-updates: refactor menu to allow other options (wwoods)
- Bump blivet Requires for DASD changes. (#1064423) (sbueno+anaconda)
- Add GUI and TUI logic to handle unformatted DASDs. (#1064423)
  (sbueno+anaconda)
- Show unformatted DASDs in the local disk store. (#1064423) (sbueno+anaconda)
- Add dialog box to warn about formatting DASDs. (#1064423) (sbueno+anaconda)
- Update disk refs when recovering from a devicefactory failure. (#1032141)
  (dlehman)
- Add typelib and library paths to the test environment. (dshea)
- Run pylint with NO_AT_BRIDGE=1 set in the environment (dshea)
- pylint: Clean up accordion warnings (bcl)
- Let Gtk pick the size for the isoChooserDialog (#973376) (dshea)
- network kickstart: do not bind to MAC if SUBCHANNELS are present (#1070232)
  (rvykydal)

* Fri Feb 28 2014 Brian C. Lane <bcl@redhat.com> - 21.25-1
- pylint: Add a pile of new E1101 exceptions (bcl)
- pylint: change disable-msg to disable (bcl)
- Fix console for s390 and 'noshell' mode (#1070672) (wwoods)
- Check that the addon selection state exists before reading it (dshea)
- Set the name in the volume group store (dshea)
- Don't ignore the directory of the driver disk iso file (vpodzime)
- Set rpm macros in DNFPayload (dshea)
- Implement %%packages --instLangs (#156477) (dshea)
- Set rpm macro information in anaconda-yum. (dshea)
- Move the anaconda-yum exception handler (#1057120) (dshea)
- Only run gtk actions in the gtk thread. (dshea)
- Add createrepo Requires (#1016004) (bcl)
- Fix a traceback gathering free space info for a container. (#1069854)
  (dlehman)
- network: detect also fcoe vlan device names exceeding IFNAMESIZ (#1051268)
  (rvykydal)
- DNFPayload: display the download progress on the hub. (ales)
- driverdisk: Fix typo in error logging (#1016004) (bcl)
- driverdisk: Create a repo for network drivers (#1016004) (bcl)
- driverdisk: Catch blkid failure (#1036765) (bcl)
- driverdisk: Ignore extra blkid fields (#1036765) (bcl)
- We can't trust rhcrashkernel-param to give us newline-free text. (pjones)
- Remove redundant _setCurrentFreeSpace() call (#1043763) (amulhern)
- Enable python-coverage in anaconda (dshea)
- Move the sidebar to the right for RTL languages (dshea)
- Remove a bunch of unused includes and tests for headers (dshea)
- Add a note about when and how to remove isys.sync (dshea)
- Remove isys.isPseudoTTY (dshea)
- Convert isys.isIsoImage to python code (dshea)
- Focus the language search input by default (#973967) (dshea)
- Ensure media being verified is always unmounted (dshea)
- Write 'text'/'cmdline' in anaconda-ks.cfg in text/cmdline mode (wwoods)
- text install -> text system (#1021963) (wwoods)
- Support the 'skipx' kickstart command (wwoods)
- let systemd decide when to start anaconda-sshd (wwoods)
- Don't use tmux for inst.noshell (#1058607) (wwoods)
- Fix a nitpick from bcl. (pjones)
- Make rhcrashkernel-param get run on non-GRUB 2 platforms. (pjones)
- Cast the blame appropriately when the kernel refuses efivars changes.
  (pjones)
- Do not use shim.efi on ARMv8 aarch64 (#1067758) (dmarlin)
- Handle missing environments specified through kickstart (#1067492). (clumens)
- create_sparse_file in blivet now expects a Size object. (clumens)
- Don't traceback when no size is given in kickstart (#1067707). (clumens)

* Fri Feb 21 2014 Brian C. Lane <bcl@redhat.com> - 21.24-1
- setup default environment in initialize (bcl)
- Move environmentAddons into packaging (bcl)
- Skip running efibootmgr for image and dir installations (#1067749) (bcl)
- Move translatable format strings into python. (dshea)
- Added a check for translatable format strings in glade. (dshea)
- Use a single script to run the glade tests. (dshea)
- Check that s390x LVM configuration is valid. (#873135, 885011)
  (sbueno+anaconda)
- Re-apply disk selection on error in TUI storage. (#1056316) (sbueno+anaconda)
- Properly retry package downloads (#924860) (mkolman)
- Change the CSS class name of the sidebar (#1067049). (clumens)
- Preserve ipv6.disable=1 on target system (#1040751) (wwoods)
- Remove an unused import in driver-updates. (clumens)
- Fix heredoc usage in generated /etc/grub.d/01_users (#1044404). (dcantrell)

* Tue Feb 18 2014 Brian C. Lane <bcl@redhat.com> - 21.23-1
- driverdisk: Parse all blkid output (#857248) (bcl)
- Fix blkid output parsing and our output (vpodzime)
- Don't use positional arguments to initialize Gtk objects (dshea)
- Set mandatory property in network tui spoke. (#1064139) (sbueno+anaconda)
- Disallow /boot on RAID on s390x. (#1027670) (sbueno+anaconda)
- Remove a stray break statement (dshea)
- Use devicetree.resolveDevice instead of udev_resolve_devspec. (#1047338)
  (dlehman)
- Set ThreadManager.any_errors to be a property (dshea)
- Error on "bootloader --location=partition" when using grub2 (#969095).
  (clumens)
- Fix the handling of kernel parameters with no = (#1065704) (dshea)
- Deal with a couple more "except Exception" lines. (clumens)
- Fix pylint errors in the latest dnf-related commit. (clumens)
- DNFPayload: pick the right FS as package download target. (ales)
- DNFPayload: log import crashes. (ales)
- DNFPayload: use dnf.exceptions.MarkingError. (ales)
- Return the returned value in the fire_gtk_action (vpodzime)
- Allow AddonData classes to parse options in the %%addon line (dshea)
- Pass ints to Gtk resize functions (#1065021) (bcl)

* Fri Feb 14 2014 Brian C. Lane <bcl@redhat.com> - 21.22-1
- Remove app_paintable from a couple nav boxes (#1064708). (clumens)
- Give a more correct error for missing groups/packages on exclude (#1060194).
  (clumens)
- Fix some incorrect RPM macros in the spec file. (clumens)
- Allow using globs and alternative paths for specifying boot drive (#1057282).
  (clumens)
- Don't reset input check status when disabling a check (#1062273) (dshea)
- Fix how an input check is disabled (#1062275). (dshea)
- ListStore.remove expects an iter, not an int (#1062752). (clumens)

* Tue Feb 11 2014 Brian C. Lane <bcl@redhat.com> - 21.21-1
- Move save_netinfo into a hook (#1048231) (bcl)
- Cleanup log message for pylint (bcl)
- kickstart user accounts should be locked by default (#1063554) (bcl)
- pre-push hook checking bugzilla IDs on rhelX branches (vpodzime)
- Make sure LUKS devices can say they have a key (#1060255) (amulhern)
- Handle LUKS passphrase before doing sanity check (#1060255) (amulhern)
- Remove some unnecessary resets (#1060255) (amulhern)
- Do not consider no available LUKS passphrase an error in do_autopart
  (#1060255) (amulhern)
- Adapt to new blivet.sanityCheck() return type (#1060255) (amulhern)
- Adapt StorageChecker class for changed return type of sanityCheck (#1060255)
  (amulhern)
- Add sanityCheck functionality back into AutoPart.execute() (#1060255)
  (amulhern)
- Bump blivet version for changed sanityCheck() interface (amulhern)
- UnmanagedDeviceError and UnknownConnectionError are in the nm module.
  (clumens)
- blivet no longer has a protectedDevices property. (clumens)
- network: adapt to changed handling of devices without carrier in NM
  (#1062417) (rvykydal)
- driverdisk: Rename skip_dds to make pylint happy (bcl)
- driverdisk: Use a single systemd service to start DD UI (#1035663) (bcl)
- driverdisk: Add dd_args_ks handling to driver-updates (#1035663) (bcl)
- driverdisk: Process kickstart driverdisk commands (#1035663) (bcl)
- driverdisk: Handle kickstart driverdisk command (#1035663) (bcl)
- driverdisk: Use getargs instead of the env variable (#1035663) (bcl)
- Remove now-unused isys/devices.[ch]. (clumens)
- Call finalize functions in parent classes. (dshea)
- Fix crashes in the LayoutIndicator dispose function. (dshea)
- Require systemd (dshea)
- Remove the now-unused anaconda_spoke_header.png. (clumens)
- Minor aesthetic cleanups (#1045250). (duffy)
- Add a topbar design to SpokeWindows. (#1045250) (duffy)
- Update the Aarch64 packages to include efibootmgr. (dmarlin)
- Add a sidebar to the standalone and hub windows (#1045250) (duffy)
- Allow specifying an environment in the kickstart file (#1050994). (clumens)
- The autopart scheme combo should work for creating partitions manually, too.
  (clumens)

* Tue Feb 04 2014 Brian C. Lane <bcl@redhat.com> - 21.20-1
- makebumpver: Any failure should cancel the bump (bcl)
- Add option help text for --image and --dirinstall flags (#1056791) (amulhern)
- Update bumpver to allow Related bugs (bcl)
- Fix up some pylint errors. (clumens)
- If a user has been created, don't allow entering the user spoke (#1058564).
  (clumens)
- Tweak passphrase wording a bit. (clumens)
- Tweak the final progress messages to fit on the screen a little better
  (#1058463). (clumens)
- Fix iscsi target selection checkbox in GUI (#1058653) (rvykydal)
- network ks: allow setting only hostname with network command (#1051564)
  (rvykydal)
- fcoe: add fcoe=<NIC>:<EDB> to boot options for nics added manually (#1040215)
  (rvykydal)
- network GUI: ignore fcoe vlan devices (#1051268) (rvykydal)
- Use an unused variable. (dshea)
- Ignore an unused function warning on isys_init (dshea)
- Remove unused isys files. (dshea)
- Fix the handling of realloc failures. (dshea)
- Run cppcheck on the C source files. (dshea)
- Check RAID10 box for BTRFS (#1021856) (amulhern)
- Make sure directory for DD extraction exists (vpodzime)
- Handle --image arguments more thoroughly (#982164,#994488) (amulhern)
- Remove the border from the custom part notebook. (clumens)
- Style the Done button to make it more noticable (mizmo). (clumens)
- Change the string used to test for serial console (#1054951) (dmarlin)

* Tue Jan 28 2014 Brian C. Lane <bcl@redhat.com> - 21.19-1
- Change the reclaim space button rules (#980496) (bcl)
- Revert "Fix up username checking regex a bit." (dshea)
- Fix a pylint-caught problem from my previous cherry-pick. (clumens)
- Give priority to IPv4 addresses when showing VNC & SSH IP (#1056420)
  (mkolman)
- Display custom part warnings/errors on the spoke itself (#975840). (clumens)
- Fix listing threads that caused an error (vpodzime)
- Do not add errors item for thread in advance (vpodzime)
- Log exceptions before running exception handling (vpodzime)
- Fix kickstart 'updates' command (#1056727) (wwoods)
- Fix exitHandler loop deactivation (bcl)
- Show hidden disk images (#1034996) (bcl)
- Fix pylint errors (dshea)
- Provide a maximum width to the betanag dialog. (clumens)
- Don't include zero sized disks in the custom part UI either (#903131).
  (clumens)
- Move the Quit button to the right and make it consistently sized (#1038802).
  (clumens)
- "Delete All" on the reclaim dialog should not delete hdiso source (#980496).
  (clumens)
- Add a scrollbar to the error dialog (#1021506). (clumens)
- Change the product name we key off (#1055019). (clumens)
- Another dracut pylint change. (dshea)
- Fix page logic in driver selection (#1055333) (bcl)
- Give users way to select DD ISO interactively (#1036765) (vpodzime)
- Make network-fetched driver disk .iso files work (#1003595) (vpodzime)
- Disable pylint messages too annoying to deal with. (dshea)
- Fix unused variable warnings (dshea)
- Remove unused imports (dshea)
- Specify string format arguments as logging function parameters (dshea)
- Remove the raidstart and raidstop commands (dshea)
- Expand the reach of pylint (dshea)
- Put Xorg on tty6 in accordance with Ancient Anaconda Tradition (#980062)
  (wwoods)
- Fix the handling of kickstart NFS repos with options (#1045528) (dshea)
- Skip empty layout-variant specifications when setting layouts (#1057442)
  (vpodzime)

* Thu Jan 23 2014 Brian C. Lane <bcl@redhat.com> - 21.18-1
- Use validate_label to check whether label should be updated (#1038590)
  (amulhern)
- Always reject label if the format exists (#1038590) (amulhern)
- Make label field always sensitive (#1038590) (amulhern)
- Save module list after initial module load (#1050352) (bcl)
- Require gtk3 and glib2 documentation to build (dshea)
- Rename get_widgets_datadir to anaconda_get_widgets_datadir. (dshea)
- Include the annotation-glossary (dshea)
- Set device.format.label field close to where we read it (#1056139) (amulhern)
- Install the rpmrc file to the initrd.img (#1016004) (vpodzime)
- Give users hint about VNC password restrictions (#1053546) (vpodzime)
- Be more liberal in what is accepted as a size unit. (dshea)
- Remove en_spec parameters from blivet.size.Size. (dshea)

* Tue Jan 21 2014 Brian C. Lane <bcl@redhat.com> - 21.17-1
- Test for DataHolder Class (#1034427) (bcl)
- Use DataHolder for TUI nfs data (#1034427) (bcl)
- Add DataHolder class (#1034427) (bcl)
- Handle inst.{gpt,dnf,extlinux} using cmdline.getbool() (wwoods)
- Drop unreferenced 'useIPv[46]' flag (wwoods)
- Don't force shell on tty2 (#980062) (wwoods)
- add comment about boot-options.txt (wwoods)
- Add support for getting stage2 image from boot.iso (#1035514) (mkolman)
- Various changes to handling of filesystem label setting (#1038590) (amulhern)
- Fix translation context on the storage options dialogs. (clumens)
- Fix problems going into custom partitioning with the new work flow. (clumens)
- Don't show actions next to free space lines in the reclaim dialog (#1054208).
  (clumens)
- If there's a label in the ISO device combo, put it on a new line (#1031727).
  (clumens)
- Make the device name in a MountpointSelector less wide (#1048583). (clumens)
- If a root password is set, don't show the spoke (#910355, #1041405).
  (clumens)
- Check for certain disk attrs before trying to access them. (#1053055)
  (sbueno+anaconda)
- Use gtk_get_locale_direction. (dshea)
- Always run efibootmgr from ROOT_PATH (bcl)
- A class for scheduling Gtk actions and running them all at once (vpodzime)
- Remove some leftover float conversions. (dshea)
- Use uint64 for the resize target size. (dshea)
- Return program output as a string instead of a list (dshea)
- Implement and use a function for one-off running Gtk actions (vpodzime)
- Be more defensive when getting layouts and their variants (vpodzime)
- Implement and use functions for conversion between keymaps and layouts
  (vpodzime)
- Fix reset of existing device to its original size. (dlehman)
- Don't disable checks for global at the module level. (dshea)
- Clean up the pylint-false-positives. (dshea)
- Remove pylint comments that are no longer necessary (dshea)
- Allow pylint-false-positives to end with a newline (dshea)
- Change storage widget visibility based on disks selected. (clumens)
- Rename widgets in the two remaining options dialogs. (clumens)
- Allow going to the reclaim dialog even for autopart (#1014671). (clumens)
- Add the autopart type combo to custom storage (#1014671). (clumens)
- Tweak DiskOverview spacing a little bit (#1014671). (clumens)
- Add custom part and encryption buttons to the main storage spoke (#1014671).
  (clumens)
- Remove the existing install_options1 dialog, rename the others (#1014671).
  (clumens)
- Grow the spoke gradient image to fit the nav_area (#1035772). (clumens)
- Additional completion checks in network spoke. (#1044571) (sbueno+anaconda)
- Fix problems reported by pylint (dshea)
- Decode potentially 8-bit strings in TUI windows (dshea)

* Fri Jan 10 2014 Brian C. Lane <bcl@redhat.com> - 21.16-1
- Use blivet.size.Size for all size quantities. (dlehman)
- make anaconda-shell (wwoods)
- handle "ks=cdrom[:<path>]" on systems with multiple CDs (#1049237) (wwoods)
- dracut: add when_any_cdrom_appears for cdrom autoprobe (wwoods)
- dracut: minor shell cleanup (wwoods)
- fix inst.noshell (#807703) (wwoods)
- Error gracefully if we have a question in cmdline mode. (#869731)
  (sbueno+anaconda)
- Verify that designated label can be set (#1038590) (amulhern)
- Do not change sensitivity of label field (#1038590) (amulhern)
- Make the clear icon functional in language spoke. (sbueno+anaconda)
- Fix the translated pango markup check (dshea)
- Remove iutil.strip_markup. (dshea)
- Pass additional command-line arguments to pylint (dshea)
- Fix and ignore markup warnings where appropriate (dshea)
- Check that the Pango markup in glade files is valid (dshea)
- Added a pylint module to check pango markup. (dshea)
- Split the po-based translation code into a separate file. (dshea)
- Fix bool parsing of boot options with inst. prefix (#1044391) (mkolman)
- Use vc_keymap as X layout only if we get nothing from localed (#1048592)
  (vpodzime)
- Warn user if entering LUKS password with non-ASCII characters (#1039168)
  (vpodzime)
- Add back some erroneously removed set_use_underline calls (dshea)
- Only show the "DATA" heading if there are data mount points under it.
  (clumens)
- Don't allow the advanced user dialog to be saved with errors (dshea)
- Move the add_check stuff into helper classes. (dshea)
- Remove the UID and GID maximums. (#978846) (dshea)
- Fix an invalid mnemonic widget reference in passphrase entry (dshea)
- Added checks for some potential issues in glade files (dshea)
- Remove scrot dependency for global screenshot support (mkolman)
- Fix mnemonic widget reference id (vpodzime)

* Tue Jan 07 2014 Brian C. Lane <bcl@redhat.com> - 21.15-1
- Use the new Gtk.ListBox for displaying environments and addons (#1039683).
  (clumens)
- Display additional disk attributes in TUI storage spoke. (#1024760)
  (sbueno+anaconda)
- Fix 'select all disks' logic in TUI storage spoke. (sbueno+anaconda)
- Ignore the compile script (dshea)
- network GUI: don't crash when wifi is activated in standalone spoke
  (#1046138) (rvykydal)
- Use the right test for there being any storage actions. (clumens)
- Only display the actions summary dialog if there are any actions (#1030511).
  (clumens)
- Do not support kickstart+live installs (#1027160). (clumens)
- We no longer directly use libnl (#1034830). (clumens)
- Remove _transactionErrors from yumpayload.py. (clumens)
- Move xhost handling to the xinit script (#1045280) (dshea)
- Check for ready before baseRepo in completed (#1044985) (bcl)
- Treat the output of vncpasswd as binary data, since it is (#1045119) (dshea)
- Add iutil.exec* options for handling binary data (dshea)
- Print a message and exit if a user attempts to upgrade via kickstart. (dshea)

* Wed Dec 18 2013 Brian C. Lane <bcl@redhat.com> - 21.14-1
- Fix the release notes image cycler. (#1043393) (dshea)
- Do not schedule resize actions for non-resizing requests (#1039491)
  (vpodzime)
- Use ceil for minSize in resize dialog (#1040012) (bcl)
- Use integer numbers of megabytes in the Reclaim dialog (#1040012) (vpodzime)
- fcoe gui: repopulate device tree only if device was actually added (#1039223)
  (rvykydal)
- Exclude FCoE disks from local disks (#1039223) (rvykydal)
- fcoe: repopulate devicetree after adding FCoE SAN (#1039223) (rvykydal)
- Add initial 64-bit ARM aarch64 EFI support (#1034428) (dmarlin)
- Rename network spoke header (mkolman)
- Show the Shell spoke in debug mode (vpodzime)
- Accept only .iso files from the IsoChooser dialog (#1015169) (vpodzime)
- Just run the IsoChooser dialog lightbox (vpodzime)
- Use libxklavier's new methods instead of our nasty hack (vpodzime)
- Move atexit registration before running rescue mode (#1038855) (vpodzime)
- Only display the addon separator if there's a reason to. (clumens)
- Stop using deprecated gtk margin functions. (clumens)
- Fix the check_accelerators srcdir path. (dshea)
- Show msg in TUI if user attempts to create invalid username. (#965561)
  (sbueno+anaconda)
- Fix up username checking regex a bit. (sbueno+anaconda)
- Fix default device for ks=cdrom (#1042500) (bcl)
- createUser is already in a chroot (#1038241) (bcl)
- Skip checks on files that are not staged for commit. (dshea)
- Allow catching exceptions from threads (vpodzime)
- Enable warnings about abstract methods not overridden (dshea)
- Provide empty methods to override abstract parent methods. (dshea)
- Implement status in StandaloneSpoke. (dshea)
- Move a bunch of abstract methods from Payload to PackagePayload (dshea)
- Remove some methods from packaging.Payload. (dshea)
- Disable abstract method warnings in intermediate abstract classes. (dshea)
- Remove Personalization spoke (dshea)
- Remove some vestigal code from an earlier version of GUICheck (dshea)

* Thu Dec 12 2013 Brian C. Lane <bcl@redhat.com> - 21.13-1
- Refresh environment addons on source change (#1033749) (bcl)
- Fix selector device matching for unallocated partitions. (#1039292) (dlehman)
- Rename the network config spoke a little bit. (clumens)
- Don't encrypt device if container is encrypted (bcl)
- network: add s390 options in ifcfgs generated from kickstart (#1031376)
  (rvykydal)
- Remove enablement of whiteout/blackout plugins, and the requires on anaconda-
  yum-plugins. (notting)
- Fix checking if we are collecting our module (vpodzime)
- Remove an unnecessary continue statement in the potfiles check (vpodzime)
- Use sys.exit instead of os._exit in the potfiles test (vpodzime)
- List addons in exception report data (vpodzime)
- Make Hub.storage and Spoke.storage a property (dshea)
- Fix the botched helperization of StorageChecker (dshea)
- Disable tmpfs in the GUI (#1039511) (mkolman)
- Don't crash on NTP lookup without network (#1026079) (mkolman)
- Don't rely on Gtk being importable for exception handling (vpodzime)
- Support rnotes in SVG format (#1034407). (clumens)
- Fix a couple warnings from -Werror=format-security (#1036989). (clumens)
- Use abstract base classes for mixins. (dshea)
- Display free space remaining in containers (#1035832). (clumens)
- Make sure url and mirrorlist are not set at once (#1026834) (mkolman)
- if rootfs is btrfs, add rootflags=subvol to kernel parameters (gene)
- add ro to bootloader kernel parameters (gene)
- Added missing entries to POTFILES.in (dshea)
- Add a check that files with translatable strings are in POTFILES.in (dshea)
- Fix the handling of renames in the pylint git hook. (dshea)
- Remove startup-id from AnacondaBaseWindow. (dshea)

* Wed Dec 04 2013 Brian C. Lane <bcl@redhat.com> - 21.12-1
- Handle cancelation of device resize in the custom spoke. (#1027947) (dlehman)
- Disallow /boot on lvm until grub2 fully supports it. (#1036705) (dlehman)
- Disallow /boot on btrfs subvolume until grubby supports it. (#864198)
  (dlehman)
- Remove an empty initialize function. (clumens)
- Move PathDict into pyanaconda/ui/__init__.py. (clumens)
- Add one more directory for ignoring test log files (dshea)
- Defer translation of device_type_name (dshea)
- Disable pylint errors about gobject-introspection methods (dshea)
- Remove unused variables (dshea)
- Document the instl.multilib boot option (vpodzime)
- Minor tweak of our driver disk documentation (vpodzime)
- network: GUI, don't ask for wifi secrets upon Configure (#1033073) (rvykydal)
- network: GUI, add support for virtual devices removing (#1030870) (rvykydal)
- network: fix naming of slave ifcfg files from kickstart (#1036047) (rvykydal)
- network: GUI, handle virtual devices (bond, vlan, team) properly (#1036047)
  (rvykydal)
- Change how we test if the GUI is available in the anaconda script. (clumens)
- Update boot-options.txt. (amulhern)
- Omit /dev/sr* from list-harddrives (#1032500) (sbueno+anaconda)
- Fix EditTUISpoke to operate only on visible entries (vpodzime)
- Don't try to investigate empty string for unicode chars (#1035799) (vpodzime)
- Fix issues reported by the check_pw_visibility test (vpodzime)
- Add check testing visibility of password entries (vpodzime)
- Put tests of .glade files into a separate directory (vpodzime)
- Save a reference to the imported Xkl module for get_current_layout (dshea)
- Fix the Makefile.am subdirs for widget data. (dshea)
- Fix some pylint warnings. (clumens)
- Switch to libtimezonemap for the timezone map. (dshea)
- Set the _config_dialog property during __init__. (dshea)
- Fix handling of long release ids (mkolman)
- Store older valid packages in separate folder (mkolman)
- Fetch older valid releases (mkolman)
- Import Xkl only when really needed (vpodzime)
- Global screenshot support (#1025038) (mkolman)
- Require new version of python-blivet (vpodzime)
- Hide password characters in iSCSI login fields (#1034202) (vpodzime)
- Use format names instead of types in the resize dialog (vpodzime)
- Do not write out the vconsole.keymap boot option (#1035316) (vpodzime)

* Wed Nov 27 2013 Brian C. Lane <bcl@redhat.com> - 21.11-1
- Use raid RAID level constants instead of mdraid RAID level constants.
  (amulhern)
- Use level objects instead of level integer codes. (amulhern)
- clear software environment (#1029536) (bcl)
- Update source on errors (#1030997) (bcl)
- Fix errors in kickstart.py. (dshea)
- Update gettext.txt (dshea)
- Don't allow bootloader and /boot on iSCSI on s390 (#1034222) (vpodzime)
- Round float values coming from the Gtk stack (#1013586) (vpodzime)
- Generate missing machine-id (bcl)
- Fix problems reported by pylint. (dshea)
- Add HDD ISO support for TUI (#1000327) (mkolman)
- Use a directory in build tree for pylint data. (dshea)
- Remove MOSTLYCLEANDIRS from Makefile.am (dshea)
- fixup spec for fedup (bcl)

* Mon Nov 25 2013 Brian C. Lane <bcl@redhat.com> - 21.10-1
- Cleanup anaconda.spec.in (bcl)
- Handle non-leaf btrfs volumes with mountpoints. (#1016959) (dlehman)
- Use en_spec for blivet Size spec strings with constant components. (#1029616)
  (dshea)
- The gui and tui subpackages cannot be noarch (vpodzime)
- Cleanup unused and overly complicated stuff in isys (vpodzime)
- DNFPayload: tweak to the API changes in dnf-0.4.8 (ales)
- Don't use cached packages with different release id (mkolman)

* Fri Nov 22 2013 Brian C. Lane <bcl@redhat.com> - 21.9-1
- Add a test for accesses of yum.preconf outside of _resetYum. (clumens)
- Remove base_repo cache (#1011555) (bcl)
- Make _yum.preconf setup atomic (#1028245) (bcl)
- Remove threading from getBaseRepo handling (#1011555) (bcl)
- If there are incomplete spokes, let the user know which (#1032801). (clumens)
- tui: show Processing while source is busy (bcl)
- tui: wait for threads before entering source and software (#1032823) (bcl)
- clear errors when metadata is ok in tui source spoke (#1006570) (bcl)
- Fix parallel pylint in distcheck. (dshea)

* Wed Nov 20 2013 Brian C. Lane <bcl@redhat.com> - 21.8-1
- Fix geolocation on live installs (mkolman)
- Ignore the pylint warning on importing GraphicalUserInterface. (clumens)
- Fall back to text mode if GUI is not available (vpodzime)
- Get rid of unused isys.isCapsLockEnabled function (vpodzime)
- Don't rely on having zenity and require it only for GUI (vpodzime)
- No longer need the Gconf2 package (vpodzime)
- Split out anaconda's user interfaces into separate packages (vpodzime)
- Do not include tzmapdata into the main package (vpodzime)
- Create directories for stubs if they don't exist (vpodzime)
- Do not try to fetch our own packages that will be built (vpodzime)
- Remove the unused flags import from installclass.py. (clumens)
- Fix logging of pylint-one output (bcl)
- Do yum lock logging only with inst.debug or loglevel=debug (vpodzime)
- Don't panic on installclasses failing with inst.debug (vpodzime)

* Mon Nov 18 2013 Brian C. Lane <bcl@redhat.com> - 21.7-1
- Expand the use of ANACONDA_WIDGETS_DATADIR. (dshea)
- Make thread manager operations atomic (#1029898) (mkolman)
- Run pylint in multiple processes (vpodzime)
- Fix how "changed" signal is emitted on the TreeSelection (vpodzime)
- Pass biosdevname boot option to installed system (#1023609) (rvykydal)
- network: update required NetworkManager version (team support) (rvykydal)
- Use timing decorator for more actions (vpodzime)
- Add test for the have_word_match function (vpodzime)
- A nice decorator making Anaconda's GUI more responsive (vpodzime)
- Short-circuit layouts matching (vpodzime)
- Enforce upper bound for resize. (#1027947) (dlehman)
- Fix some pylint problems in network.py. (clumens)
- Add an updates location for the AnacondaWidgets overrides (dshea)
- Fix typo (#1003591) (rvykydal)
- network: call GDBus proxy methods like python (rvykydal)
- network: add team support for kickstart %%pre phase (#1003591) (rvykydal)
- network: generate kickstart commands for team devices (#1003591) (rvykydal)
- network: support for adding team devices (#1003591) (rvykydal)
- network: display team devices in status (#1003591) (rvykydal)
- network: add team support to kickstart (#1003591) (rvykydal)
- Initialize the AddLayouts dialog in advance in the KeyboardSpoke (vpodzime)
- Add function to map functions on items in the main thread (vpodzime)
- Allow having unique thread names with given prefix (vpodzime)
- Remove an unused and non-working leftover function resetResolve (vpodzime)
- Always center dialogs shown on top of lightbox (vpodzime)
- Set spokes' distribution and beta warning only once (vpodzime)
- use deepcopy on ksdata method (#1028243) (bcl)
- Change source spoke proxy handling to use local copy (#967805) (bcl)
- Apply a little tweak to the VNC password length message. (clumens)
- Match layouts with stripped accents in AddLayout dialog (vpodzime)
- Sort layout descriptions properly (#1026238) (vpodzime)
- Make AddLayout dialog persistent (vpodzime)
- Use Sphinx syntax in the iutil module (vpodzime)
- Warn if vnc passwd is longer than 8 chars (hamzy)
- Don't try to unicode unicode strings (#1029109) (vpodzime)
- Add tmpfs support (#918621) (mkolman)
- Added a few things that autoscan complained about (dshea)
- Actually use the config header we generate (dshea)
- Redirect pylint stderr to stdout (dshea)
- Fix the handling of files generated for xgettext (dshea)
- Use gettext to process glade files. (dshea)
- Always use $prefix in directory names. (dshea)
- Pass --enable-gtk-doc to configure in distcheck (dshea)
- Fix the liveinst install/uninstall hooks (dshea)
- Clean up after intltool (dshea)
- Add missing files to dist (dshea)
- DNFPayload: tweak to the API changes in dnf-0.4.7. (ales)
- Add tests for iutil (mkolman)

* Fri Nov 08 2013 Brian C. Lane <bcl@redhat.com> - 21.6-1
- Fix typos in translation functions (dshea)
- Put the cityCompletion back on the list of widgets (vpodzime)
- Do not translate strings defined at the module or class level. (clumens)
- Fix a couple places where we're doing %% inside of _(). (clumens)
- Add a custom pylint module to check i18n problems. (clumens)
- Remove an unused import. (clumens)
- Provide our own sorting functions for regions and timezones (#1025029)
  (vpodzime)
- Set locale for our process (vpodzime)
- Translate timezones in GUI (vpodzime)
- network gui: add apply tooltip to Configure button (#1018471) (rvykydal)
- Make dialog return code checking more robust (amulhern)
- Show last 4 bytes of wwid (#1024966) (jstodola)
- Handle focus changes of MountpointSelectors from outside (#975838) (vpodzime)
- network: do not crash when device for network --device is not found
  (#1023829) (rvykydal)
- Log continuing from hub if there are no spokes (vpodzime)
- Updates to boot-options.txt document (#1026449) (amulhern)
- No longer install anaconda user documentation (#1026449) (amulhern)

* Fri Nov 01 2013 Brian C. Lane <bcl@redhat.com> - 21.5-1
- Fix spoke sorting issues in text-mode. (#929177) (sbueno+anaconda)
- Send the continue click after the queue is empty (#1025347) (bcl)
- No longer use summary screen visit to decide whether bootloader has been
  configured (#1025811) (amulhern)
- Remove the bootloader line from the interactive kickstart file (#1025811)
  (amulhern)
- Set bootloader default location to mbr in constructor (#1025811) (amulhern)
- Remove column titles from the software spoke. (dshea)
- Fix the selection of default groups (#1023263) (dshea)
- Use the default yscale for the HubWindow alignment (dshea)
- Fix kickstart block device resolution. (#1022206) (dlehman)
- Specify query territory when getting language native name (vpodzime)
- Get rid of trailing whitespace (vpodzime)
- Export the right classes from the tui.spokes package (vpodzime)
- Define newLayoutStore before it is used by the filter (vpodzime)

* Wed Oct 30 2013 Brian C. Lane <bcl@redhat.com> - 21.4-1
- Fix up a couple more pylint errors. (clumens)
- Add check for Linux HFS+ ESP on Mac (#1010495) (bcl)
- Update bootDrive info when storage config updated in text-mode. (#861018)
  (sbueno+anaconda)
- Remove the special handling for en (dshea)
- Ignore SIGINT (#1024822) (amulhern)
- Don't show language twice for keyboard layouts (#1021907) (petersen)
- Make Software spoke ready even if there is no repo (#1010348) (vpodzime)
- Use decorator for methods that invalidate base repo cache (vpodzime)
- Use cache for base repo if possible (vpodzime)
- Make sure to actually set the autopart flag when needed. (#1023554) (dlehman)
- Fix Gtk errors about list store columns (dshea)
- Fix the layout up and down button sensitivies. (dshea)
- Fix the Gkbd spec string for layouts with no variant (dshea)
- pylint wants regexes with backslashes to be specified with 'r'. (clumens)
- Add ack flag checking to makebumpver (bcl)
- Correctly accept 'sshd' boot arg as alias for 'inst.sshd' (#924157) (wwoods)
- Only eject CDROM devices we're actually using (#949919) (wwoods)
- mem may not exist when it's printed out in these error messages. (clumens)

* Fri Oct 25 2013 Brian C. Lane <bcl@redhat.com> - 21.3-1
- Reset _proxyChange when a change is triggered (bcl)
- Setup No Update checkbox correctly (#1016801) (bcl)
- Fall back to closest mirror in source (#1016801) (bcl)
- anaconda-dracut: fix ks failure with hd:<dev>:some/path.ks (wwoods)
- Make sure lower bound for resize is applied. (#986575) (dlehman)
- Use devicetree to resolve device specs in kickstart. (#1022206) (dlehman)
- Disregard raid level combo when it isn't applicable. (#1022203) (dlehman)
- Mountpoint is an attr of the format, not the device. (#892747) (dlehman)
- Add bootloader execute before autopart (#1021258) (bcl)
- Do error checking of repository names on "Installation Source" screen.
  (amulhern)
- Avoid configure-event loops. (#1021511) (dshea)

* Wed Oct 23 2013 Brian C. Lane <bcl@redhat.com> - 21.2-1
- remove signal disconnect (#996899) (bcl)
- Re-saved every glade file with glade-3.16.0 (dshea)
- Fix pylint errors in network.py. (clumens)
- Always use decimal notation for Size specs (dshea)
- network kickstart: add support for devices configured in %%pre (#1019796)
  (rvykydal)
- network gui: make Configure button insensitive when no ap is selected
  (#1015212) (rvykydal)
- Encode possible unicode objects before calling str() on them (vpodzime)
- Fix a typo in function documentation (vpodzime)
- Use more general status for installations from media (#1017703) (vpodzime)

* Mon Oct 21 2013 Brian C. Lane <bcl@redhat.com> - 21.1-1
- Adds additional debug logging to yumpayload.py. (amulhern)
- Handle invalid JSON in geoloc (#1021410) (dshea)
- Revert "Only prompt for LUKS password if the user has chosen to configure
  automatically." (amulhern)
- Add context support to check_accelerators (dshea)
- Added translation contexts to the TUI. (dshea)
- Added translation contexts to the GUI. (dshea)
- Add support for context-based translations (dshea)
- Reset checks on both password fields. (#1020580) (dshea)
- Fix swaps added to fstab for noformat (gene)
- Don't update hub's continue button and label for every spoke (#1020373)
  (vpodzime)
- Add storage tests. (clumens)
- Add option to select all hard drives in text mode. (#965580)
  (sbueno+anaconda)
- BootLoaderError should not reset storage (#1019541) (bcl)
- Only prompt for LUKS password if the user has chosen to configure
  automatically. (amulhern)
- Remove an unused string (dshea)
- Translate AM and PM (dshea)
- Translate strings marked as translatable (dshea)
- network gui spoke: use GDBus to obtain list of settings (#1018467) (rvykydal)
- network: look for device settings also based on DEVICE value (#1017788)
  (rvykydal)
- Fix liveinst to work with livemedia-creator (#1009711) (bcl)
- Remove the button-label property on SpokeWindow. (clumens)
- Log entering/exiting spokes and hubs in the GUI. (clumens)
- Escape text inserted into markup strings (dshea)
- Move markup out of translatable strings (dshea)
- Move formating markup out of python where possible (dshea)
- Use explicit children to set label attributes (dshea)
- Turn on the image on the "Add a disk..." button. (dshea)

* Wed Oct 16 2013 Brian C. Lane <bcl@redhat.com> - 20.26-1
- Install bootloader to loop device in disk image installations. (#1019502)
  (dlehman)
- Don't try to configure a bootloader for s390 disk image installs. (#1019502)
  (dlehman)
- Fix initramfs generation for disk image installations. (#1019502) (dlehman)
- Save mountpoints specified for existing btrfs volumes. (#892747) (dlehman)
- Add a command line option for disabling friendly multipath names. (#977815)
  (dlehman)
- Remove en (dshea)
- "Fix" the zSeries device filter "label" (dshea)
- Replace placeholders with the strings from python (dshea)
- Add and fix keyboard accelerators (dshea)
- Check for labels with use_underline and no accelerator (dshea)
- Support checking the translation of plural strings (dshea)
- Specify a node id in check_accelerator exceptions (dshea)
- BTRFS cannot hold swap, no need to care about fstab swaps (vpodzime)
- Add ANACONDA_INSTALL_CLASSES to testenv.sh. (clumens)
- Put a version on the DNF requirement. (clumens)
- Revert "For now, ignore checking dnfpayload.py with pylint." (clumens)
- Fix the alignment of the Network Time switch (#1019301) (dshea)
- Tell blivet which swaps should appear in the fstab (#1011391) (vpodzime)
- Put only newly created or reformated swaps to the new root (vpodzime)
- Make code to get new devices reusable as property (vpodzime)
- Grab journal only from the last boot (vpodzime)
- DNFPayload: allow enable/disable calls for repos that do not exist. (ales)
- Add shell spoke to s390x installations (vpodzime)
- Put TUI spokes in common categories (vpodzime)
- MountpointSelector is a widget, set its property properly (#1013612)
  (vpodzime)
- Include the journal log on installed system (bcl)
- DNFPayload: error handling and logging cleanups. (ales)
- DNFPayload: reset the transaction goal on new package selection check. (ales)
- DNFPayload: implement environmentGroups() (ales)
- Some partition scheme is always selected (#1017435) (vpodzime)

* Fri Oct 11 2013 Brian C. Lane <bcl@redhat.com> - 20.25-1
- Don't use g_object_set on initialized objects. (dshea)
- Remove the "other" tab in the network spoke. (dshea)
- Fix duplicated id in custom.glade (dshea)
- Correctly generate rescue initrd (#1013087) (bcl)
- Refresh swap suggestion once we know which disks to use (vpodzime)
- Initialize the kickstart install method (#1017614) (dshea)
- Use correct format for raise in kickstart.py (bcl)
- Add install-requires target to the Anaconda makefile (mkolman)
- fix luksformat references (#1014493) (bcl)
- kickstart: check for correct format (#1014545) (bcl)
- Add checks for unexpanded macros. (dshea)
- UIScreen doesn't necessarily have the ready property (vpodzime)
- Print long widgets in a nice way (vpodzime)
- Consider errno 5 I/O errors hardware faults (vpodzime)
- Install kernel-lpae if supported (#1013015) (vpodzime)
- Bump firewalld version (mkolman)

* Wed Oct 09 2013 Brian C. Lane <bcl@redhat.com> - 20.24-1
- Clear bootDisk and bootloader stage info on errors (#1013482) (bcl)
- Catch BootLoaderError when setting up bootloader (#1013474) (bcl)
- Fix an incorrect formatting string in makeupdates. (clumens)
- network: remove function we don't need anymore (rvykydal)
- Don't translate constant strings. (dshea)
- Take into account disk space when calculating swap suggestion (#1016673)
  (vpodzime)
- DNFPayload: adapt to DNF change c3de85d6 of Base.install() error reporting.
  (ales)
- DNFPayload: the new libcomps makes env.option_ids a list of GroupID objects.
  (ales)
- Fix warning message when package version is not found in Koji (mkolman)

* Tue Oct 08 2013 Brian C. Lane <bcl@redhat.com> - 20.23-1
- Use Unicode in the TUI buffer strings (#1015620) (dshea)
- DNFPayload: install DNF itself. (ales)
- DNFPayload: direct conf.persistdir to the sysimage. (ales)
- Add a tooltip to the container combobox (#975801) (bcl)
- Use different colors for different message types. (dshea)
- Exit on exception in the askVNC spoke (#962804) (dshea)
- Don't skip the strength check if overriding a kickstart password (dshea)
- Allow password spoke to be exited without password (#1004931) (dshea)
- Re-check the password strength when the username changes (dshea)
- Only call pwquality once per password. (dshea)
- Use GUICheck checks for the root password strength (dshea)
- Use constants for password check failure messages (dshea)
- Use a constant to indicate GUICheck success (dshea)
- Remove a redundant error property from UserSpoke (dshea)
- Fix the usages of PWQError. (#1014405) (dshea)
- Fix usage of GtkLevelBar in glade. (dshea)
- Clean up callbacks in the user spoke. (dshea)
- Removed an untrue portion of a doc comment (dshea)
- Support for removing services from firewall needs newer PyKickstart (mkolman)
- Add support for removing services from the firewall (#957809) (mkolman)

* Fri Oct 04 2013 Brian C. Lane <bcl@redhat.com> - 20.22-1
- Only encrypt the TUI user password once (#1015220) (dshea)
- Don't try to collect removed modules (vpodzime)
- Moved the NFS nolock option into Payload._setupNFS (dshea)
- Grab journalctl logs if there is no /tmp/syslog (vpodzime)
- Pass layout and variant in specific format to Gkbd (#1011155) (vpodzime)
- Translate the "Quit" string at the end of liveinst. (dshea)

* Fri Sep 27 2013 Brian C. Lane <bcl@redhat.com> - 20.21-1
- Remove another reference to log_picker. (clumens)
- Turn spinner back on for configuration (bcl)
- Use assertIsInstance in the kickstart version test. (clumens)
- If the full device path is given in repo=hd:, still select it in the UI
  (#980479). (clumens)
- Display newly created partitions without a mountpoint, too (#886039).
  (clumens)
- Don't require pressing escape twice to kill the media check window (#965625).
  (clumens)
- Fix display of weak password warning (#1011850) (dshea)
- Fix the tui simpleline imports. (dshea)
- Don't confuse users by misleading tooltip (#1011112) (vpodzime)
- Assorted other pylint fixes for scripts and utils (dshea)
- Pass string format arguments as paramters to logging (dshea)
- Ignore the use of func_globals in a test case (dshea)
- Fix issues in the AnacondaWidgets python wrapper (dshea)
- Make exception handling more specific (dshea)
- Remove unused imports and variables (dshea)
- Remove unnecessary lambdas (dshea)
- Remove obsolete files. (dshea)
- Check whether the commit matches the tree (dshea)
- Run pylint on all python files (dshea)
- Don't use relative imports (dshea)
- Use g_signal_handler_disconnect instead of g_object_disconnect (#1010486)
  (vpodzime)
- Fixup Eula class (bcl)
- Allow searching for keyboard layouts in English (#1009806) (vpodzime)
- network: don't create ksdata for devices enslaved in GUI (#1011826)
  (rvykydal)
- Allow a proxy to be set before the method is saved (#1012096) (dshea)
- Export the pykickstart Eula command (vpodzime)

* Wed Sep 25 2013 Brian C. Lane <bcl@redhat.com> - 20.20-1
- Encrypt normal user passwords when doing text install. (#977732)
  (sbueno+anaconda)
- Escape the status before setting it as markup (vpodzime)
- network gui: do not crash on devices without settings (eg wireless)
  (#1010519) (rvykydal)
- Make the keyboard layout preview dialog bigger (#1011140) (vpodzime)
- Return switching options with the same order as shown (#1011130) (vpodzime)
- Use a temporary directory for verifying ISO media (dshea)
- Skip devices not controllable by blivet (#1009809) (dshea)
- Add translation support to check_accelerators (dshea)
- Make sure autopart type is handled deterministicaly in text mode (#1010453)
  (vpodzime)
- Don't rely on X server adding empty variant for its defaults (#1011658)
  (vpodzime)
- Make Keyboard spoke's status consistent with other statuses (#1011166)
  (vpodzime)
- LiveImageKSPayload skip the parent class setup method (#1010500) (bcl)
- Pass the actual format instead of Python built-in (#1009678) (vpodzime)
- Don't allow using updates with non-default network sources (#1008028)
  (vpodzime)
- Use Sphinx documentation format in nm.py. (rvykydal)
- Changed the keyboard accelerator for iscsi "Retry Log In" (dshea)
- Only fail on a missing firewalld command if the firewall is enabled
  (#1004976). (clumens)
- Cleanup some pylint failures in the network module (bcl)
- Add GtkNotebook support to the accelerators check. (dshea)

* Fri Sep 20 2013 Brian C. Lane <bcl@redhat.com> - 20.19-1
- tui ErrorDialog needs to be modal (#983316) (bcl)
- Keyboard variant names may contain dashes (#1008730) (vpodzime)
- Forbid "root" as a user or group name. (#968451) (dshea)
- Set the password strength color based on strength (#965596) (dshea)
- Fix the password confirmation match check (#1009907) (dshea)
- Replace removed python modules with stubs in makeupdates (vpodzime)
- Unlock encrypted partitions before finding installations (#901917) (vpodzime)
- Network TUI: remove unused import, import nm. (rvykydal)
- Network TUI: show the same status as in gui. (rvykydal)
- Network TUI: don't traceback when applying config to device without link.
  (rvykydal)
- Generate ifcfg VLAN_ID value for kickstart network --vlanid. (rvykydal)
- Network TUI: fix updating of ksdata in apply. (rvykydal)
- Network TUI: ignore slaves devices for configuration. (rvykydal)
- Clean up ifcfg file handling. (rvykydal)
- Check the validity of generated usernames in TUI (#965543) (dshea)
- Behave better when PYTHONPATH is already set (dshea)
- Decode keyboard layout descriptions as UTF-8 (#1009278) (dshea)
- Filter out devices with no media from custom (#960794) (bcl)

* Wed Sep 18 2013 Brian C. Lane <bcl@redhat.com> - 20.18-1
- ProgressHub no longer exists in pyanaconda/ui/tui/hubs. (clumens)
- Search all disk types for install media (#1004726) (dshea)
- git commit check for ack flag on rhel branches (bcl)
- Fix Lightbox for compositing window managers (#1008446) (dshea)
- Add metalink support to yumpayload (bcl)
- Make progress screen in text mode standalone spoke instead of hub (vpodzime)
- Render the right arrow based on the widget direction (#1008397) (vpodzime)
- Mirror the GUI if an RTL language is chosen (#1008397) (vpodzime)
- Removed unused GUI elements (dshea)
- Clean up what is and isn't translatable and how. (dshea)
- Removed the exceptionsText constant (dshea)
- Add comments for translators to TUI input strings (#854226) (dshea)
- Use python-format on all intltool-extract strings (dshea)

* Mon Sep 16 2013 Brian C. Lane <bcl@redhat.com> - 20.17-1
- Fix handling of blank size specs in the custom spoke. (#1004903) (dlehman)
- Block resize slider value changed handler when setting range. (#1007387)
  (dlehman)
- Remove an unused import. (clumens)
- Create the XklWrapper singleton in background (vpodzime)
- Translate layout and switching options descriptions on the fly (vpodzime)
- Improve XklWrapper's API (vpodzime)
- Move upcase_first_letter function to iutil (vpodzime)
- Remove the Layout class and things we don't need in XklWrapper (vpodzime)
- Ignore the whole m4 directory (vpodzime)
- Do not schedule hubs with no spokes available (#1006357) (vpodzime)
- Retranslate language filtering placeholder texts (#1007090) (vpodzime)
- Use pigz to create updates.img (vpodzime)
- The Desktop class doesn't need to inherit from SimpleConfigFile. (clumens)
- Fix yet another pylint error caught after the fact. (clumens)
- Move all languages found by geoip to the top in Welcome spoke (mkolman)
- Don't set ksdata.lang.seen to True if using default value (mkolman)
- DNFPayload: reset the sack and repos on updateBaseRepo() (ales)
- refactor: YumPayload: selectKernelPackage()->_select_kernel_package() (ales)
- DNFPayload: mirrorlist can not be an empty string. (ales)
- DNFPayload: display the download step in progressQ. (ales)
- DNFPayload: logging the missed packages/groups. (ales)
- DNFPayload: select kernel packages. (ales)
- DNFPayload: log when the transaction process unexpectedly terminates. (ales)
- DNFpayload: disable all NSS operations in RPM. (ales)
- DNFPayload: keyerror in isRepoEnabled() (ales)
- DNFPayload: implement selectEnvironment() (ales)

* Fri Sep 13 2013 Brian C. Lane <bcl@redhat.com> - 20.16-1
- add pre-commit hook to run pylint (bcl)
- Allow runpylint.sh to be passed files (bcl)
- handle case of no ifcfg and no hostname (#1002737) (bcl)
- Allow make targets to be run outside of $srcdir (dshea)
- Fix the wildcard usage in automake files. (dshea)
- Move the intltool Makefile rules into configure.ac (dshea)
- Fix a format parameter mapping (#1007472) (dshea)
- Check whether keyboard translations are stale (#972236) (dshea)
- Fix the handling of xklavier strings. (dshea)
- Center the Langsupport spoke's description (vpodzime)
- Set minimal width request for the locales box (vpodzime)
- Use constant for default keyboard layout (vpodzime)
- Try to use VConsole keymap name as X layout (#1007359) (vpodzime)
- Retranslate also layout indicator when retranslating BaseWindow (#1007087)
  (vpodzime)
- Check ready state before baseRepo (#1007448) (bcl)
- Fix po/Rules-extract so it doesn't remove itself (dshea)
- Include LayoutIndicator and TimezoneMap to the Micsellaneous Widgets
  (vpodzime)

* Wed Sep 11 2013 Brian C. Lane <bcl@redhat.com> - 20.15-1
- Don't set up the resize slider for non-resizable devices. (#997690) (dlehman)
- Remove 'completed' property from Autopart spoke in text UI. (sbueno+anaconda)
- Clean up code for input handling in TUI spokes. (sbueno+anaconda)
- set_hostname should proceed only on DVD and live installations (vpodzime)
- Don't use temporary file and move when writing out an ifcfg file (vpodzime)
- Set hostname when leaving network spokes (vpodzime)
- Keep file-naming convention with the Lightbox widget (vpodzime)
- Let users configure autopart options in interactive text ks. (#1001061)
  (sbueno+anaconda)
- Add parameters to format strings (dshea)
- Fix pre-processing of files for xgettext (#1005644) (dshea)
- Added a test to check for xgettext warnings (dshea)
- Make sure XklWrapper isn't dumped to the anaconda-tb file (vpodzime)
- Catch race of network device state vs reading its config properties (#980576)
  (rvykydal)

* Tue Sep 10 2013 Brian C. Lane <bcl@redhat.com> - 20.14-1
- Convert the lightbox into a GObject (#1000927) (dshea)
- Remove some more unused imports. (clumens)
- Move the Anaconda class to a proper module (vpodzime)
- Firstboot should be disabled by default after automated installations
  (vpodzime)
- Fix typo introduced in refactorization (#1005511) (vpodzime)
- Remove unused imports in the network spoke. (clumens)
- Get rid of the now-unused new_firmware variable. (clumens)
- Remove magic from the passphrase dialog (#921948) (vpodzime)
- Don't pass extra arguments to LangLocaleHandler.__init__() (vpodzime)
- Fix check for device state when reading its IPXConfig (#1001776, # 1005198)
  (rvykydal)

* Mon Sep 09 2013 Brian C. Lane <bcl@redhat.com> - 20.13-1
- Fix handling of flexible specs in onpart for member devices. (#1004885)
  (dlehman)
- Always regenerate initramfs (#994180) (bcl)
- Avoid the use of NamedTuple._make (dshea)
- Add superclass __init__()s and fix an indent (dshea)
- Pass logging string format variables as parameters (dshea)
- Remove unnecessary variables, imports, semicolons (dshea)
- Fix the user/group name regex (dshea)
- Fix problems with the test scripts (dshea)
- Handle kickstarts that don't specify timezone (#1001598) (mkolman)
- Don't set "date of last password change" /etc/shadow field (#985572)
  (hdegoede)

* Fri Sep 06 2013 Brian C. Lane <bcl@redhat.com> - 20.12-1
- Cleanup arch tests (dshea)
- Rearranged the automake tests. (dshea)
- Update po/ build files to the current gettext (dshea)
- Use libtool with gtkdoc-scanobj (dshea)
- Use autoconf to set the spec file Version. (dshea)
- Use the ustar format with make dist (dshea)
- Fix widgets autotools generation. (dshea)
- Require gtk-doc and GObject. (dshea)
- dracut no longer auto assembles everything (#960496) (bcl)
- Only ignore missing packages entries (#983316) (bcl)
- Fix a string that was modified before translation (#1004960) (dshea)
- Let users configure keyboard via anaconda in live installations (#1002533)
  (vpodzime)
- Use copy instead of move for NTP configuration (#985566) (hdegoede)
- Share code between the Welcome and Langsupport spokes (vpodzime)
- Do not try to set None as hostname (#1002737) (vpodzime)
- Fix crash on LiveCD if network is configured before installing (#1002373)
  (rvykydal)

* Thu Sep 05 2013 Brian C. Lane <bcl@redhat.com> - 20.11-1
- Add more details to iso device selector (#971290) (bcl)
- Warn user if they enter a weak password in TUI. (#1001039) (sbueno+anaconda)
- Don't mark spoke as completed if no repo is set. (#1001538) (sbueno+anaconda)
- Don't enable chronyd if disabled in kickstart (#1002583) (mkolman)
- Run firstboot-only spokes on first boot by default (vpodzime)
- Let hubs specify which environments they support (vpodzime)
- Don't mount cdroms that contain no mountable media. (#1000889) (dlehman)
- Don't try to parse langcode if none given (vpodzime)
- Get rid of the non-deterministic expand_langs and its usage (vpodzime)
- Rework the Langsupport spoke to work with all locales (vpodzime)
- Rework the Welcome spoke to allow users choose from all locales (vpodzime)
- Improve import in GUI utils a bit (vpodzime)
- Remove the cryptic "language-default keyboard" checkbutton (vpodzime)
- Allow seting up locale without modifying ksdata (vpodzime)
- Remove an unused argument of get_available_translations (vpodzime)
- Setup language early to a value we can figure out (vpodzime)

* Tue Sep 03 2013 Brian C. Lane <bcl@redhat.com> - 20.10-1
- Optionally hide the GUI option to install updates (dshea)
- Move the really_hide and really_show functions to utils (vpodzime)
- Search for all translations, not only one per langauge (#1001446) (vpodzime)
- Use the DEFAULT_LANG if GeoIP suggestion cannot be used (#1000715) (vpodzime)
- Network spoke: fix showing of ipv6 addresses (rvykydal)
- Use the sensitive-info log for sensitive location info (#986844) (mkolman)
- Add new logger for sensitive information (mkolman)
- Handle %%define changes for autofetch (mkolman)
- Update dumping of network info for new nmcli interface. (rvykydal)
- Text network spoke: more strict ipv6 address input checking (#909299)
  (rvykydal)
- Network spoke: show global ipv6 addresses (rvykydal)
- Text network spoke: add to translated files (po/POTFILES.in) (#902299)
  (rvykydal)
- Text network spoke: require netmask and gateway for static ipv4 (#902299)
  (rvykydal)
- Text network spoke: Condense device configuration information (#902299)
  (rvykydal)
- Text network spoke: fix ipv4 regex (#909299) (rvykydal)
- Resolved accelerator conflicts and marked excpetions. (dshea)
- Added tests for duplicated keyboard accelerators (dshea)
- Implement group creation with GID in GUI (#968085) (dshea)
- Remove unused imports. (dshea)
- Move dynamic labels out of custom.glade (#1000703) (dshea)

* Mon Aug 26 2013 Brian C. Lane <bcl@redhat.com> - 20.9-1
- Text network spoke: basic configuration support (#909299) (rvykydal)
- Add support for network configuration in TUI. (#909299) (sbueno+anaconda)
- Remove partial matches from Koji search results (mkolman)
- Handle >=,<=,= for package version, fix -a/--add (mkolman)
- Return only network devices supported in installer from nm_devices (#999514)
  (rvykydal)
- Obtain network device type specific dbus interface dynamically (#999514)
  (rvykydal)
- Catch no-hwaddr exception only for the respective call (#999514) (rvykydal)
- Don't catch hwaddr not found exception for ethernet devices (#999514)
  (rvykydal)
- Added a validation test for the GUI group list (dshea)
- Validate input fields on the user spoke. (#967245) (dshea)
- Added an input validation framework. (dshea)
- Pre-fetch widgets in advanced user dialog (dshea)
- Change validatePassword to be more flexible. (dshea)
- Moved regexes into regexes.py. (dshea)

* Fri Aug 23 2013 Brian C. Lane <bcl@redhat.com> - 20.8-1
- Fix a SIGSEGV when returning from storage spoke (#983319) (dshea)
- makebumpver: Fix problem with single line body (bcl)
- For now, ignore checking dnfpayload.py with pylint. (clumens)
- Don't do str() on an exception we're passing into a string substitution.
  (clumens)
- Check for hwaddress exceptions. (dshea)
- If LANG isn't set, set it to default value. (#997397) (sbueno+anaconda)
- Remove yet another unused import. (clumens)
- swap devices should be under the System portion (#962668). (clumens)
- Populate the repo store before changed can ever be called (#994940).
  (clumens)
- Make the ISO choosing widget wider (#973376). (clumens)
- Don't recommend /usr as a separate mount point anymore (#981465). (clumens)
- Do not run another instance of the TUI for errors (#997661) (vpodzime)
- Do not try to exit from the installation thread (vpodzime)
- Tell which thread failed to be added by the ThreadMgr (vpodzime)

* Wed Aug 21 2013 Brian C. Lane <bcl@redhat.com> - 20.7-1
- Modify the gtk_warning function in anaconda to use gtk3. (clumens)
- Fix some pylint warnings in the new DNF code. (clumens)
- Fix a couple more pykickstart handler version mismatches. (clumens)
- anaconda requires a later version of partitioning syntax now. (clumens)
- packaging: add dnf to the Anaconda's requires. (ales)
- Enable DNFPayload on specific triggers. (ales)
- DNFPayload: initial version. (ales)
- refactor: tear down the install device in PackagePayload.reset(). (ales)
- refactor: extract the device handling in YumPayload._configureBaseRepo up to
  PackagePayload. (ales)
- refactor: move YumPayload._setUpMedia() up to PackagePayload._setupMedia().
  (ales)
- Tweaks in the Payload interface. (ales)
- remove: configureAddOnRepo from the Payload interface. (ales)
- Payload: forgotten comment in spaceRequired() (ales)
- Payload: define txID to None. (ales)
- The NFS text dialog should never attempt to use method.url (#998446).
  (clumens)
- Remove the unittest target, since "make check" will do this for us. (clumens)
- Use the latest version of the RAID kickstart handler. (clumens)
- Update both the method and repo info. (dshea)
- remove the UBOOT class arm systems are now using EXTLINUX (dennis)
- ARM: switch to using extlinux by default (dennis)
- Update our pylint arguments. (clumens)
- Don't implicitly unpack exceptions.  That won't be supporetd in the future.
  (clumens)
- Modify how we call logging functions to take a list of parameters. (clumens)
- Use "raise Exception()" instead of "raise Exception, ..." (clumens)
- Hook up pylint and our nosetests to be run via "make check". (clumens)
- Drop unneeded required_space_text variable. (#997690) (dlehman)
- Specify also query script when getting locale's native name (vpodzime)
- Update runpylint.sh for pylint 1.0.0 (bcl)
- Clean up translation placeholders (#890157) (bcl)
- Don't override multilib setting unless the option was passed. (#987557)
  (dlehman)
- Set the encoding of custom.py to utf-8 (dshea)
- Report if a package was not found in Koji during autofetch (mkolman)
- Convert makeupdates from getopt to argparse (mkolman)
- Fixed the interpretation of RAID levels (dshea)
- Consolidate get_object() calls. (dshea)
- Add ASCII-only upper and lower string functions. (dshea)
- Fix the User/Group already exists log messages. (dshea)
- Normalize keyboard layout and variant strings from langtable (vpodzime)
- A few tests for the keyboard layout and variant strings processing (vpodzime)
- More robust parsing of the layout and variant string specification (vpodzime)
- Move DEFAULT_VC_FONT to constants (vpodzime)
- Match langs with stripped accents when filtering languages (vpodzime)
- Fix the User subclass using an old version of the pykickstart superclass.
  (clumens)
- Bring the kickstart version test back to life. (clumens)
- Don't read proxy for methods that have no proxy (dshea)

* Wed Aug 14 2013 Brian C. Lane <bcl@redhat.com> - 20.6-1
- Import DBusGMainLoop directly (bcl)
- Catch AttributeError when looking for InstallClass (bcl)
- dracut/parse-kickstart should use the updated method-related classes
  (#994978). (clumens)
- Ignore warnings about the global keyword and the DefaultInstall class.
  (clumens)
- Fix all the pylint warnings in the anaconda file. (clumens)
- Deal with the last of the catching Exception warnings. (clumens)
- Always define a continueButton and quitButton property. (clumens)
- Fix pylint warnings in the installclasses. (clumens)
- Remove a directory that does not exist from the PYTHONPATH for pylint.
  (clumens)
- Fix up some warnings about calling the superclass's __init__ method.
  (clumens)
- Remove the reference to "anaconda" in reIPL. (clumens)
- Fix up almost all of the redefining warning messages. (clumens)
- Add a bunch of gobject-introspection related ignore lines. (clumens)
- StorageChecker ought to have a self.storage attribute. (clumens)
- Ignore another error pylint can't quite figure out. (clumens)
- pylint doesn't understand what's in AnacondaKSHandler. (clumens)
- Remove the "Add custom add-on" button. (clumens)
- Fix up places where overridden methods don't take the same number of args.
  (clumens)
- Fix up all unused variable warnings. (clumens)
- Added files to MAINTAINERCLEANFILES (dshea)
- Reenabled the pylint test target (dshea)
- Cleanup the autogen scripts. (dshea)
- Remove m4 files from the widgets project. (dshea)
- Install gettext files at build time. (dshea)
- Use the python checks provided by automake. (dshea)
- Added a missing type check found by autoscan (dshea)
- Cleanup the widgets autoconf file (dshea)
- Add detail to logs when creating users and groups (dshea)
- Fix miscellaneous errors in installclass.py. (clumens)
- Fix a variety of errors in the packaging module. (clumens)
- Do not run pylint against executable files in pyanaconda/. (clumens)
- Clean up deprecated uses of the string module. (clumens)
- Call the right superclass's method. (clumens)
- Straighten out text UI methods so they have the same method signature.
  (clumens)
- Remove the lines to ignore E0611. (clumens)
- Bootloader.read is completely unused; cut it. (clumens)
- Fix all the "X is defined outside of __init__" warnings. (clumens)
- Display the correct string for the space required by packages. (clumens)
- Remove lines that clearly just don't do anything. (clumens)
- If we're not going to use the return value, don't grab it. (clumens)
- kernelVersionList in tarpayload.py should act the same as all other versions.
  (clumens)
- If we're not going to use the exception object, don't grab it. (clumens)
- Define stage2_device in the BootLoader class. (clumens)
- Don't call getPassAlgo before running createGroup. (clumens)
- Remove some unused values out of constants.py. (clumens)
- Finish taking care of pylint warnings in image.py. (clumens)
- Remove the unused network and write methods from the Anaconda object.
  (clumens)
- Remove the disable-msg lines for a couple C messages. (clumens)
- Remove some easy unused argument warnings. (clumens)
- Remove everything from InstallInterfaceBase except what Rescue needs.
  (clumens)
- Remove the duplicated imports. (clumens)
- Do not use a list or a dict as a default argument to a method. (clumens)
- Remove unneeded lambdas. (clumens)
- Fix up all the warnings where we used a reserved function name or keyword.
  (clumens)
- Fix up about half of the "except:" and "except Exception:" lines. (clumens)
- Fix a couple undefined variable errors that were real bugs. (clumens)
- Ignore statements that have no effect. (clumens)
- Fix up all the wildcard imports except two in packaging. (clumens)
- Remove all unused import lines. (clumens)
- Remove unnecessary pass statements. (clumens)
- Fix bad indentation and tab-instead-of-space warnings from pylint. (clumens)
- Put the pylint test back into service. (clumens)
- Run make with multiple jobs in makeupdates (vpodzime)
- Use gtk_image_new_from_icon_name (bcl)
- Remove caching of unused device list. (dlehman)
- Check MBR gap size even when /boot is on a plain partition. (#986431)
  (dlehman)

* Thu Aug 08 2013 Brian C. Lane <bcl@redhat.com> - 20.5-1
- Don't wait for systemctl shutdown command to exit (#974383) (bcl)
- Fix the logging of the spice-vdagent status (dshea)
- Update PYTHONPATH so unit tests work right out of the source tree. (clumens)
- Don't check for a firstboot service file before processing the command.
  (clumens)
- Strengthen the services command processing a bit. (clumens)
- Start spice-vdagent (#969405) (dshea)
- Skip password strength check for kickstart passwords (#986490) (dshea)
- Network spoke: fix refresh of device IP configuration (rvykydal)
- Add unsupported hardware dialog (#872728) (bcl)
- storage.py -> system.py in POTFILES.in (clumens)
- border_width=5 -> border_width=6 (clumens)
- No need to call threads_init anymore (bcl)
- Consolidate storage and networking under one category (#973013). (clumens)
- When doing a live install, set the ks method appropriately (#986069).
  (clumens)
- Check that we're doing an HD install before examining the attr (#989428).
  (clumens)

* Thu Aug 01 2013 Brian C. Lane <bcl@redhat.com> - 20.4-1
- POTFILES.in: rename time.py to time_spoke.py (bcl)
- Only move INSTALL_TREE when it is mounted (#888196) (bcl)
- Use ksdata.method.seen (#986069) (bcl)
- Threaded Koji RPM lookups and downloads (mkolman)
- Fix the langcode parsing regexp (vpodzime)
- Move tests to old_tests and add some new, working tests (vpodzime)
- Replace hostname with hostnamectl (#989584) (rvykydal)
- Require fcoe-utils only on ix86 and x86_64 architectures (#989913) (vpodzime)
- Fix searching for local RPMs with no version required (vpodzime)
- Expand the '~' in the RPM_FOLDER_NAME (vpodzime)
- Set system date and time with our own function (vpodzime)
- Remove the useless, confusing and lying PoolsNote (vpodzime)
- Use tiny, fast and thread-safe ntplib module instead of ntpdate (vpodzime)
- For vnc require network in intramfs (#989156) (rvykydal)
- Fix makeupdates' package fetching when no version is specified (vpodzime)
- Make it clear on the summary dialog that changes take effect later. (clumens)
- Don't mark the summary dialog's tree view as insensitive. (clumens)
- Work with files in a more pythonic way in makeupdates (vpodzime)
- Honor hostname set in kickstart (#988483) (rvykydal)
- Do not automatically set UTC mode on kickstart installs. (clumens)
- Add automatic fetching of RPMs for new Defines & Requires (mkolman)
- Don't prompt for ssh on s390x if doing an image install. (#983056) (sbueno)
- Rename tz spoke to avoid potential conflict with std 'time' module. (sbueno)

* Thu Jul 25 2013 Brian C. Lane <bcl@redhat.com> - 20.3-1
- Fix driver disk path for inst.dd= method (#987513) (bcl)
- Add support for NFS as install source in TUI. (#971298) (sbueno+anaconda)
- Allow logging into multiple iscsi nodes at once (#975831). (clumens)
- Fix crash while parsing ntp servers from DHCP6 (#969303) (dshea)
- Use ExceptionInfo namedtuple when dumping anaconda (#982299) (vpodzime)
- Wait for device connections for iface-bound iscsi in kickstart (#740105)
  (rvykydal)
- Refer to blivet instead of storage in iscsi kickstart (#740105) (rvykydal)
- Mark disk 'selected' if only one present in TUI. (#975790) (sbueno+anaconda)
- Update devicetree only if we logged in to some target in add iscsi dialog.
  (rvykydal)
- Don't show multipath members in specialized disks overview (#740105)
  (rvykydal)
- Do not populate devicetree after each single login in iscsi dialog (#740105)
  (rvykydal)
- Match also iface when logging into selected iface-bound iscsi target
  (#740105) (rvykydal)
- Fix handling of non-ASCII names (#969309) (dshea)
- Use inline completion for the region/city selection (vpodzime)
- Fix copyright of the main anaconda script (vpodzime)

* Mon Jul 15 2013 Brian C. Lane <bcl@redhat.com> - 20.2-1
- Use the new wait for connectivity function (mkolman)
- Improve waiting for network connectivity (mkolman)
- Use langtable to get default layout instead of our magic (#485137) (vpodzime)
- Adapt to the new localization module (vpodzime)
- Rewrite the localization module (vpodzime)
- Make the Welcome spoke wait for Geolocation lookup to finish (#975193)
  (mkolman)

* Tue Jul 09 2013 Brian C. Lane <bcl@redhat.com> - 20.1-1
- bump major version number
