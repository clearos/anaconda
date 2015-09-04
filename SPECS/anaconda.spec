%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Patch1: anaconda-clearos-add-clearos-install-class.patch
Patch2: anaconda-clearos-set-right-eula-location.patch
Patch3: anaconda-clearos-efidir-clearos.patch
Patch4: anaconda-clearos-disable-mirrors.patch
Patch5: anaconda-clearos-bootfs-default-to-xfs.patch
Patch6: anaconda-clearos-remove-user-add.patch
Version: 19.31.123
Release: 1%{?dist}.3
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

%define anacondabuild %{name}-19.31.123
%define helpver 7.1.4
# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2
Source1: anaconda-user-help-%{helpver}.tar.gz

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define gettextver 0.11
%define intltoolver 0.31.2-3
%define libnlver 1.0
%define pykickstartver  1.99.43.17
%define yumver 3.4.3-91
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define nmver 1.0.0-6.git20150107
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.25.2-1
%define sckeyboardver 1.3.1
%define firewalldver 0.3.5-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 033-26
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.870-3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.13-4

BuildRequires: audit-libs-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: pygobject3
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libgnomekbd-devel
BuildRequires: libnl-devel >= %{libnlver}
BuildRequires: libxklavier-devel
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
# required for help content generation
BuildRequires: python-lxml
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif


Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-gui = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Requires: python-blivet >= 0.61.0.17-1
Requires: python-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libreport-rhel-anaconda-bugzilla >= 2.1.11-1
Requires: libselinux-python
Requires: rpm-python
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
Requires: keybinder3
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
Requires: dhclient
Requires: kbd
Requires: chrony
Requires: ntpdate
Requires: rsync
Requires: hostname
Requires: systemd
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64 ia64 aarch64
Requires: dmidecode
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif

# required because of the rescue mode and VNC question
Requires: anaconda-tui = %{version}-%{release}

Requires: python-coverage

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
Requires: anaconda-user-help = %{version}-%{release}
Requires: python-meh-gui >= %{mehver}
Requires: gnome-icon-theme-symbolic
Requires: system-logos
Requires: tigervnc-server-minimal
Requires: libxklavier
Requires: libgnomekbd
Requires: nm-connection-editor
%ifarch %livearches
Requires: zenity
%endif
Requires: yelp
%ifnarch s390 s390x
Requires: NetworkManager-wifi
%endif

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
Requires: anaconda-widgets = %{version}-%{release}

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

%package user-help
Summary: Content for the Anaconda built-in help system

%description user-help
This package hold the content for the Anaconda built-in help system.

%prep
%setup -q
%setup -a 1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%configure --disable-static \
           --enable-introspection \
           --enable-gtk-doc
%{__make} %{?_smp_mflags}

# generate content for the help system
( cd anaconda-user-help-%{helpver} && python prepare_anaconda_help_content.py %{helpver})

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

# install the help content
mkdir -p %{buildroot}%{_datadir}/anaconda/help
cp -r %{_builddir}/%{anacondabuild}/anaconda-user-help-%{helpver}/anaconda_help_content/* %{buildroot}%{_datadir}/anaconda/help

%ifarch %livearches
desktop-file-install ---dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%endif
# NOTE: If you see "error: Installed (but unpackaged) file(s) found" that include liveinst files,
#       check the IS_LIVEINST_ARCH in configure.ac to make sure your architecture is properly defined

%find_lang %{name}


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
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%exclude %{_datadir}/anaconda/help/*
%exclude %{_datadir}/anaconda/tzmapdata
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
%exclude %{_libdir}/python*/site-packages/pyanaconda/rescue.py
%exclude %{_libdir}/python*/site-packages/pyanaconda/text.py
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
%{_datadir}/icons/hicolor/*
%endif

%files gui
%{_libdir}/python*/site-packages/pyanaconda/ui/gui/*

%files tui
%{_libdir}/python*/site-packages/pyanaconda/rescue.py
%{_libdir}/python*/site-packages/pyanaconda/text.py
%{_libdir}/python*/site-packages/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{_libdir}/python*/site-packages/gi/overrides/*
%{_datadir}/anaconda/tzmapdata/*

%files widgets-devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%files user-help
%{_datadir}/anaconda/help/*

%changelog
* Fri Apr 03 2015 Shad L. Lords <slords@clearfoundation.com> - 19.31.123-1.v7.3
- Remove user options screen

* Fri Apr 03 2015 Shad L. Lords <slords@clearfoundation.com> - 19.31.123-1.v7.2
- Add patch to inject ClearOS install class, and make it default

* Thu Mar 26 2015 Karanbir Singh <kbsingh@centos.org> - 19.31.123-1.el7.centos.2
- Bump for rebuild

* Fri Mar 20 2015 Karanbir Singh <kbsingh@centos.org> - 19.31.123-1.el7.centos.1
- Add path to restore installclass, set EULA path, ensure xfs as default

* Thu Mar 05 2015 CentOS Sources <bugs@centos.org> - 19.31.123-1.el7.centos
- Add CentOS install class as default
- use the right path for the EULA string (issue 7165,  bstinson)

* Mon Feb 16 2015 Brian C. Lane <bcl@redhat.com> - 19.31.123-1
- iscsi: pass rd.* options of devices to be mouted in dracut (rvykydal)
  Resolves: rhbz#1192398

* Mon Jan 26 2015 Brian C. Lane <bcl@redhat.com> - 19.31.122-1
- Show empty VGs in the custom spoke. (dlehman)
  Resolves: rhbz#1185832
- network: add teamd package if team is used during installation (rvykydal)
  Resolves: rhbz#1185670

* Tue Jan 20 2015 Brian C. Lane <bcl@redhat.com> - 19.31.121-1
- network: adapt to NetworkManager package split-up (rvykydal)
  Resolves: rhbz#1182633
- network: pass team opts to dracut for netroot (rvykydal)
  Resolves: rhbz#1075666

* Fri Jan 16 2015 Brian C. Lane <bcl@redhat.com> - 19.31.120-1
- Add support for architecture suffixes in help files (mkolman)
  Related: rhbz#1072033

* Wed Jan 14 2015 Brian C. Lane <bcl@redhat.com> - 19.31.119-1
- Update error handler classes (bcl)
  Resolves: rhbz#1181146
- Pass a Size instance to blivet instead of number of bytes (vpodzime)
  Related: rhbz#1171116
- If using pre-existing, no size needs to be specified in ksdata (amulhern)
  Resolves: rhbz#1169783

* Wed Jan 07 2015 Brian C. Lane <bcl@redhat.com> - 19.31.118-1
- Fix handling of md fwraid names in kickstart bootloader command. (dlehman)
  Resolves: rhbz#1167375
- Do not bypass name setters in the custom spoke. (dlehman)
  Related: rhbz#1138370
- Don't try to use math.ceil on blivet.size.Size instances. (dlehman)
  Resolves: rhbz#1164191
- Preserve kickstart url behavior for mirrorlist (bcl)
  Related: rhbz#1109933
- Use a backslash to escape nfs spaces instead of x20 (bcl)
  Related: rhbz#1109933
- Allow adding prepboot to a blank disk in custom (bcl)
  Resolves: rhbz#1176829

* Thu Dec 18 2014 Brian C. Lane <bcl@redhat.com> - 19.31.117-1
- Don't install langpacks.conf if nowhere to install to (dshea)
  Resolves: rhbz#1172004

* Mon Dec 15 2014 Brian C. Lane <bcl@redhat.com> - 19.31.116-1
- Fix the way we create the list of DASDs needing dasdfmt. (sbueno+anaconda)
  Related: rhbz#1073982
- Fix threading issues for dasdfmt in gui storage. (sbueno+anaconda)
  Resolves: rhbz#1073982
- Make sure /boot is not LVM LV if we're on s390x (sbueno+anaconda)
  Resolves: rhbz#873135

* Tue Dec 09 2014 Brian C. Lane <bcl@redhat.com> - 19.31.115-1
- Fix EOF error that occurs if user input required in x3270. (jstodola)
  Resolves: rhbz#1171135
- Remove magic from the passphrase dialog (vpodzime)
  Resolves: rhbz#1168645
- Close file descriptors when forking child processes (vpodzime)
  Related: rhbz#1083978
- Close file descriptors when running ntpdate (vpodzime)
  Resolves: rhbz#1083978

* Fri Dec 05 2014 Brian C. Lane <bcl@redhat.com> - 19.31.114-1
- Pass the help content version to the script that generates it (mkolman)
  Related: rhbz#1072033
- Use Anaconda version for the help subpackage (mkolman)
  Related: rhbz#1072033

* Thu Dec 04 2014 Brian C. Lane <bcl@redhat.com> - 19.31.113-1
- Make sure help content files are not part of the core sub-package (mkolman)
  Related: rhbz#1072033
- iscsi: when logging into nodes consider ip:port of node (rvykydal)
  Resolves: rhbz#1114820

* Mon Dec 01 2014 Brian C. Lane <bcl@redhat.com> - 19.31.112-1
- Update the nav_box internal child for datetime_spoke. (dshea)
  Resolves: rhbz#1155548
- Remove the spacing properties from GtkLevelBar (dshea)
  Resolves: rhbz#1155548
- Put the cityCompletion back on the list of widgets (vpodzime)
  Resolves: rhbz#1155548
- Remove the "other" tab in the network spoke. (dshea)
  Resolves: rhbz#1155548
- Add help content subpackage (mkolman)
  Related: rhbz#1072033

* Tue Nov 25 2014 Brian C. Lane <bcl@redhat.com> - 19.31.111-1
- Fix pylint errors in the last addons.py commit. (clumens)
  Related: rhbz#1155955
- Provide useful hints on TTY1 during the installation
  Resolves: rhbz#1166834

* Mon Nov 24 2014 Brian C. Lane <bcl@redhat.com> - 19.31.110-1
- Fix PWQError issues. (sbueno+anaconda)
  Resolves: rhbz#1066988
- Just preserve the %%addon header args if an addon is missing (vpodzime)
  Resolves: rhbz#1155955

* Fri Nov 21 2014 Brian C. Lane <bcl@redhat.com> - 19.31.109-1
- Skip tui askvnc reboot for dirinstall (bcl)
  Resolves: rhbz#1164254
- Fix the ISO chooser dialog (dshea)
  Resolves: rhbz#1163026

* Wed Nov 19 2014 Brian C. Lane <bcl@redhat.com> - 19.31.108-1
- Fix a bad cherry-pick in an error handler (dshea)
  Related: rhbz#1057032
- Add support for custom gid to advanced user setup (bcl)
  Resolves: rhbz#1163803
- Create missing parent directories for user's home directory (bcl)
  Resolves: rhbz#1163775

* Thu Nov 13 2014 Brian C. Lane <bcl@redhat.com> - 19.31.107-1
- Convert LVM_PE_SIZE to KiB (vpodzime)
  Resolves: rhbz#1163081
- Check if we read something when emptying stdin queue (vpodzime)
  Related: rhbz#1162702
- Require min entropy for 'part --encrypted' devices (vpodzime)
  Resolves: rhbz#1162695
- Don't rely on terminal attributes being configurable (vpodzime)
  Resolves: rhbz#1162702
- network: fix a typo making creating virtual devices in %%pre fail (rvykydal)
  Related: rhbz#1075195
- Don't traceback if connection does not have read-only setting (rvykydal)
  Resolves: rhbz#1158919
- Get rid of unused _dasd variable in custom spoke. (sbueno+anaconda)
  Related: rhbz#1158590

* Thu Nov 06 2014 Brian C. Lane <bcl@redhat.com> - 19.31.106-1
- Prevent tb on s390x when de-selecting a DASD and doing custom part.
  (sbueno+anaconda)
  Resolves: rhbz#1158590
- Add the entropy dialog to POTFILES.in. (clumens)
  Related: rhbz#1073679
- Unpack the callback data given to us by blivet (vpodzime)
  Related: rhbz#1073679
- Add timeout to callbacks waiting for enough entropy (vpodzime)
  Resolves: rhbz#1073679

* Fri Oct 31 2014 Brian C. Lane <bcl@redhat.com> - 19.31.105-1
- custom: Clearing errors should also clear Done clicked state (bcl)
  Resolves: rhbz#1158609
- Set the autopart fstype for boot too (bcl)
  Resolves: rhbz#1112697
- Lightly rearrange the nav_area (dshea)
  Resolves: rhbz#1158969

* Wed Oct 22 2014 Brian C. Lane <bcl@redhat.com> - 19.31.104-1
- Remove an extlinux-related block from rpmostreepayload.py. (clumens)
  Related: rhbz#1153409
- bootloader: Bridge efi_dir configuration earlier for rpmostreepayload
  (walters)
  Related: rhbz#1153409
- rpmostreepayload: Handle grub2+EFI layout (walters)
  Related: rhbz#1153409
- rpmostreepayload: Copy all subdirectories of /usr/lib/ostree-boot (walters)
  Related: rhbz#1153409
- Handle the case of rpmostreepayload + GRUB2 (walters)
  Related: rhbz#1153409
- Enable dmidecode on aarch64 (jdisnard). (clumens)
  Resolves: rhbz#1134651

* Mon Oct 20 2014 Brian C. Lane <bcl@redhat.com> - 19.31.103-1
- Really fix issue with starting in cmdline mode on s390x. (sbueno+anaconda)
  Resolves: rhbz#1040933
- Add authconfig and firewalld packages when used in ks (bcl)
  Resolves: rhbz#1147687
- Fix the rest of the new pylint error messages. (clumens)
  Related: rhbz#1121678
- Change disable-msg to disable for the new pylint. (clumens)
  Related: rhbz#1121678
- Don't panic prematurely on a missing size (amulhern)
  Resolves: rhbz#1154068
- Get rid of some unnecessary text from dasdfmt dialog. (sbueno+anaconda)
  Resolves: rhbz#1153050
- rpmostreepayload: Drop selinux-ensure-labeled call (walters)
  Related: rhbz#1113535

* Thu Oct 16 2014 Brian C. Lane <bcl@redhat.com> - 19.31.102-1
- Fix a spelling error (dshea)
  Related: rhbz#1072619

* Tue Oct 14 2014 Brian C. Lane <bcl@redhat.com> - 19.31.101-1
- Update pykickstart ver to bring in fix for bug (amulhern)
  Related: rhbz#1149718
- Fix a typo from 73d3a8e5. (sbueno+anaconda)
  Resolves: rhbz#1040933
- Fix a bug unmounting /boot on efi+atomic installs. (clumens)
  Resolves: rhbz#1150588
- Fix issues with the date&time not being updated on timezone changes
  (vpodzime)
  Resolves: rhbz#1151479

* Fri Oct 10 2014 Brian C. Lane <bcl@redhat.com> - 19.31.100-1
- Get rid of an unused variable in the localization test. (clumens)
  Related: rhbz#1044233
- Import GUI-specific stuff only when running GUI in entropy handling
  (vpodzime)
  Related: rhbz#1073679
- Always store the information about display mode in ksdata (vpodzime)
  Related: rhbz#1073679
- Make the date format locale-dependent in our GUI (vpodzime)
  Resolves: rhbz#1044233
- A function for resolving date format and order (vpodzime)
  Related: rhbz#1044233
- Switch to using the new help content path (mkolman)
  Related: rhbz#1072033
- Clear out custom storage ksdata after first attempt to apply it. (dlehman)
  Resolves: rhbz#1144604
- Take "RHEL Atomic Host" as rhel installclass (rvykydal)
  Resolves: rhbz#1150410

* Tue Oct 07 2014 Brian C. Lane <bcl@redhat.com> - 19.31.99-1
- Use the /usr/share/anaconda/help for help content (mkolman)
  Related: rhbz#1072033
- Fix the value written to /etc/sysconfig/desktop (dshea)
  Related: rhbz#1121678
- s390x: show dialog if kernel cmdline in zipl.conf is too long.
  (sbueno+anaconda)
  Resolves: rhbz#885011
- Ignore the "No value passed for parameter self" warning. (clumens)
  Related: rhbz#1131382
- Move help docs outside of livearch block in spec file (bcl)
  Related: rhbz#1072033

* Fri Oct 03 2014 Brian C. Lane <bcl@redhat.com> - 19.31.98-1
- Really exit when "Exit installer" in the error dialog is clicked (vpodzime)
  Related: rhbz#1131382
- Graphically handle errors arising from ostree repo pull problems. (clumens)
  Resolves: rhbz#1131382
- Fix log message formating introduced by autostep support (mkolman)
  Related: rhbz#1059295
- Fix autotools rules to properly include help placeholders (mkolman)
  Related: rhbz#1072033

* Thu Oct 02 2014 Brian C. Lane <bcl@redhat.com> - 19.31.97-1
- Remove a reference to the depreciated copy-screenshots script (mkolman)
  Related: rhbz#1059295
- Clear errors when downloading new MD in text (bcl)
  Related: rhbz#1125927
- Return result of default key handling in text summary hub (bcl)
  Related: rhbz#997405
- Bump up the required version of pykickstart (vpodzime)
  Related: rhbz#869456
- Add support for thin pool profile specification in kickstart (vpodzime)
  Resolves: rhbz#869456
- Add support for autostep and --autoscreenshot (mkolman)
  Resolves: rhbz#1059295
- Don't crash if escrow certificate is requested without network access
  (mkolman)
  Resolves: rhbz#1085265

* Tue Sep 30 2014 Brian C. Lane <bcl@redhat.com> - 19.31.96-1
- network: support for bridge, require pykickstart with the support (rvykydal)
  Related: rhbz#1075195
- Specify help file names for hubs and spokes (mkolman)
  Related: rhbz#1072033
- Add a help button to every Anaconda screen (mkolman)
  Resolves: rhbz#1072033
- Show environment specified in kickstart as selected in the GUI (mkolman)
  Resolves: rhbz#1087831
- Fix Welcome spoke not showing up during kickstart installation (mkolman)
  Resolves: rhbz#1147943
- network: display only actual fqdn of ip we offer for vnc connection
  (rvykydal)
  Resolves: rhbz#1089429

* Mon Sep 29 2014 Brian C. Lane <bcl@redhat.com> - 19.31.95-1
- Bump blivet version Requires so default s390x boot change is picked up
  (sbueno+anaconda)
  Related: rhbz#1035201
- Don't allow /boot on lvm on s390x. (sbueno+anaconda)
  Resolves: rhbz#1035201
- Handle failures to instantiate storage devices when parsing kickstart.
  (dlehman)
  Related: rhbz#1072285
- Fix pylint problem for #1066988. (sbueno+anaconda)
  Related: rhbz#1066988
- Protect protected devices in custom spoke (bcl)
  Resolves: rhbz#1052883
- network: Catch exception from NM failing to create a bridge device (rvykydal)
  Related: rhbz#1075195
- network: add bridge support for kickstart %%pre phase (rvykydal)
  Resolves: rhbz#1075195
- network: generate kickstart commands for bridge devices (rvykydal)
  Resolves: rhbz#1075195
- network: add bridge support to kickstart (rvykydal)
  Resolves: rhbz#1075195
- network: support for adding bridge devices (rvykydal)
  Resolves: rhbz#1075195
- network: display bridge devices in status (rvykydal)
  Resolves: rhbz#1075195
- Fix PWQError issue when checking TUI passwords. (sbueno+anaconda)
  Related: rhbz#1066988
- parent is unused, so mark it as such. (clumens)
  Related: rhbz#804511
- Add the new langsupport.py TUI spoke to POTFILES.in. (clumens)
  Related: rhbz#1000326
- network: GUI: reactivate connection automatically after configuration
  (rvykydal)
  Resolves: rhbz#1033063
- Remove the now-unused imports of storageInitialize. (clumens)
  Related: rhbz#1074010
- Ignore two accelerator collisions on the filter screen. (clumens)
  Related: rhbz#1065716
- network: enable NM ibft plugin only for ip=ibft boot option (rvykydal)
  Resolves: rhbz#804511
- network: add support for vlan tag in iBFT (rvykydal)
  Resolves: rhbz#804511
- Add support for language selection in text mode. (sbueno+anaconda)
  Resolves: rhbz#1000326

* Fri Sep 26 2014 Brian C. Lane <bcl@redhat.com> - 19.31.94-1
- yumpayload: handle new NFS install source with inst.stage2=nfs:... (wwoods)
  Resolves: rhbz#1001638
- Allow cdrom-swapping when doing "inst.ks=cdrom[:...]" (wwoods)
  Resolves: rhbz#1122104
- anaconda-lib.sh: add tell_user() and dev_is_cdrom() (wwoods)
  Related: rhbz#1122104
- anaconda-lib.sh: add tell_user() and dev_is_cdrom() (wwoods)
- Use shim on uefi now. (pjones)
  Related: rhbz#1100048
- Enable MAKEDEBUG in /etc/sysconfig/kernel . (pjones)
  Related: rhbz#957681
- Don't force a user to return to the storage spoke after dasdfmt
  (sbueno+anaconda)
  Related: rhbz#1074010
- Don't run storageInitialize after dasdfmt (sbueno+anaconda)
  Resolves: rhbz#1074010
- If the network is disabled, also disable the network part of the source
  spoke. (clumens)
  Resolves: rhbz#1072453
- Fix position of Refresh List button in filter spoke (rvykydal)
  Related: rhbz#1065716
- network: handle dbus UnknownMethod exception on invalid objects (rvykydal)
  Resolves: rhbz#1061796
- Avoid the possibility of size variables being unset (dshea)
  Related: rhbz#1116435

* Thu Sep 25 2014 Brian C. Lane <bcl@redhat.com> - 19.31.93-1
- s390x: Apply disk selection before dasdfmt to preserve data.
  (sbueno+anaconda)
  Resolves: rhbz#1078892
- Fix an error in recent commit 4518009. (dlehman)
  Related: rhbz#1027224
- Adapt to corrected interpetation of logvol --percent. (dlehman)
  Resolves: rhbz#1116435
- Fix accelerator collision of Refresh button (rvykydal)
  Related: rhbz#1065716
- Handle cancellation of new container creation. (dlehman)
  Resolves: rhbz#1027224
- Don't attempt terminal size detection on the s390 (mkolman)
  Resolves: rhbz#1145065
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
  Related: rhbz#1070115
- Don't show the Add DASD button unless on s390x. (sbueno+anaconda)
  Related: rhbz#1070115
- Preserve network args on s390x. (sbueno+anaconda)
  Resolves: rhbz#1087502
- Don't set GRUB_DISTRIBUTOR here. (pjones)
  Related: rhbz#996794

* Fri Sep 19 2014 Brian C. Lane <bcl@redhat.com> - 19.31.92-1
- Ignore one accelerator conflict on the new custom part RHS. (clumens)
  Related: rhbz#1094856
- The new Device(s) label has no mnemonic, so remove use_underline. (clumens)
  Related: rhbz#1094856
- Really fix string formatting of zFCP devices (sbueno+anaconda)
  Related: rhbz#1024902
- Don't call storage.write for dirinstall (bcl)
  Related: rhbz#1120206
- Convert devices size to str for GUI for zFCP devices (amulhern)
  Resolves: rhbz#1144464
- Fix string formatting of zFCP devices (sbueno+anaconda)
  Related: rhbz#1024902
- Fix the POTFILES.in list (vpodzime)
  Related: rhbz#1073679
- Make the Find button not jump out of the visible area (vpodzime)
  Resolves: rhbz#1074183
- Require minimum random data entropy when creating LUKS (vpodzime)
  Resolves: rhbz#1073679
- Give blivet callbacks for reporting partitioning progress (vpodzime)
  Related: rhbz#1073679
- Change how we test if the GUI is available in the anaconda script. (clumens)
  Related: rhbz#1078868
- Revert "Don't call BusyCursor before Gdk is setup (vpodzime)"
  Related: rhbz#1078868
- Reorganize the right side of the Custom spoke (vpodzime)
  Resolves: rhbz#1094856
- Fix the way zFCP devices are displayed in storage spoke. (sbueno+anaconda)
  Resolves: rhbz#1024902
- Set flags.rescue_mode not anaconda.rescue (amulhern)
  Related: rhbz#1090009
  Resolves: rhbz#1143056
- Split localed's converted layouts and variants (vpodzime)
  Resolves: rhbz#1073825
- Create free space snapshot before doing custom->autopart (vpodzime)
  Related: rhbz#1132436
- Deprecate RUNKS cmdline option. (sbueno+anaconda)
  Resolves: rhbz#1040933

* Wed Sep 17 2014 Brian C. Lane <bcl@redhat.com> - 19.31.91-1
- Don't call BusyCursor before Gdk is setup (bcl)
  Resolves: rhbz#1078868
- Fix SELINUX_DEFAULT import (bcl)
  Resolves: rhbz#1137049
- Actually show an error message for bad passwords in TUI. (sbueno+anaconda)
  Resolves: rhbz#1066988
- Catch and rethrow BTRFSValueError as KickstartException (amulhern)
  Related: rhbz#1019685
- Bump version so BTRFSValueError is found (amulhern)
  Related: rhbz#1019685
- Re-order the tz's in text mode to mirror the graphical order.
  (sbueno+anaconda)
  Resolves: rhbz#1032560
- Apply a better check for whether to fail if authconfig is missing. (clumens)
  Resolves: rhbz#1140640
- driver-updates: fix backspace/delete in dd menus (wwoods)
  Resolves: rhbz#1080380
- Fix an issue with bad NFS info specified in source spoke. (sbueno+anaconda)
  Resolves: rhbz#1097432
- gui: add Refresh button to network storage UI (rvykydal)
  Resolves: rhbz#1065716
- Use timing decorator for more actions (vpodzime)
  Related: rhbz#1065716
- Make the LUKS unlock callback a timed action (vpodzime)
  Related: rhbz#1065716
- A nice decorator making Anaconda's GUI more responsive (vpodzime)
  Related: rhbz#1065716
- network: fix typo 'Private ksy pasword' (rvykydal)
  Related: rhbz#1120374
- Anaconda requires new python-meh split into multiple packages (vpodzime)
  Related: rhbz#1012509

* Mon Sep 15 2014 Brian C. Lane <bcl@redhat.com> - 19.31.90-1
- Fix TUI error message regarding user name creation (sbueno+anaconda)
  Resolves: rhbz#1058637
- Warn if software selection size exceeds available space (sbueno+anaconda)
  Resolves: rhbz#1010070
- Fix up a string style issue found in the last network commits. (clumens)
  Related: rhbz#1120374
- network: WPA Enterprise: don't ask twice for password (rvykydal)
  Related: rhbz#1120374
- network: add support for WPA Enterprise (rvykydal)
  Resolves: rhbz#1120374
- Handle spaces in inst.repo, kickstart nfs, and url commands (bcl)
  Resolves: rhbz#1109933
- Fix q for quit issue in text mode (sbueno+anaconda)
  Resolves: rhbz#997405
- Additional message if kickstart was used but did not finish (amulhern)
  Related: rhbz#1117908
- Move some statically detectable kickstart errors out of anaconda (amulhern)
  Related: rhbz#1117908
- Exclude hfsplus-tools from rhel (bcl)
  Resolves: rhbz#1119305
- Allow to search specialized and network devices after pressing Enter
  (mkolman)
  Resolves: rhbz#1058364
- Fix hang at reboot with VNC installs (wwoods)
  Resolves: rhbz#1036572
- Define the gettext method earlier (dshea)
  Resolves: rhbz#1140605
- mountExistingSystem raises an exception with dirty FS (vpodzime)
  Resolves: rhbz#1080210
- Don't care about crash args in bootloader (vpodzime)
  Resolves: rhbz#1116338
- Split out anaconda's user interfaces into separate packages (vpodzime)
  Resolves: rhbz#1012509
  Related: rhbz#999464

* Wed Sep 10 2014 Brian C. Lane <bcl@redhat.com> - 19.31.89-1
- Fix noselinux cmdline default (bcl)
  Resolves: rhbz#1137049
- Snapshot free space after clearpart for swap suggestion (vpodzime)
  Resolves: rhbz#1132436
- tui: show software and source spoke iff payload is PackagePayload (rvykydal)
  Resolves: rhbz#1139142
- filesystem -> file system in a few more places. (clumens)
  Related: rhbz#1121678
- filesystem -> file system (clumens)
  Related: rhbz#1121678
- Change the accelerator key for Add DASD label. (sbueno+anaconda)
  Related: rhbz#1070115
- Add dialog box for adding DASDs. (sbueno+anaconda)
  Resolves: rhbz#1070115
- Add a button for adding an ECKD DASD. (sbueno+anaconda)
  Resolves: rhbz#1070115
- network: add s390 network ifcfg options also for bond slaves (rvykydal)
  Resolves: rhbz#1090558

* Fri Sep 05 2014 David Lehman <dlehman@redhat.com> - 19.31.88-1
- Adjust to python-blivet-0.61.0.1
  Related: rhbz#1075561
- Make rescue_mode part of flags, hence more publicly available (amulhern)
  Related: rhbz#1090009
  Related: rhbz#1075561
- Use human readable sizes with two decimal spaces in the GUI (vpodzime)
  Resolves: rhbz#1067080
  Related: rhbz#1075561
- fix inst.virtiolog (wwoods)
  Resolves: rhbz#1074499
- network: don't crash, just log for unrecognized bond options (rvykydal)
  Resolves: rhbz#1039006
- network: don't traceback on invalid team options (rvykydal)
  Resolves: rhbz#1114282
- Add a Licensing category (mkolman)
  Related: rhbz#1039677

* Wed Sep 03 2014 Brian C. Lane <bcl@redhat.com> - 19.31.87-1
- Filter out devices with no media from custom (bcl)
  Resolves: rhbz#1049446
- Skip nvram update on ppc64 image/dir installations (bcl)
  Resolves: rhbz#1136486
- For yum-based installs, move the progress bar while packages are installing.
  (clumens)
  Related: rhbz#1024403
- Sync up step counts in install.py with reality. (clumens)
  Related: rhbz#1024403
- Change a confusing string in TUI NFS configuration screen. (sbueno+anaconda)
  Resolves: rhbz#1057690
- Split kickstart arg handling (bcl)
  Related: rhbz#1088459
- Fix --kickstart option (bcl)
  Related: rhbz#1088459
- Add anaconda_options.txt to makeupdates (dshea)
  Related: rhbz#1088459
- Allow the location of anaconda_options.txt to be overridden (dshea)
  Related: rhbz#1088459
- Add help texts to Anaconda CLI options (mkolman)
  Related: rhbz#1088459
- Use booleans and direct assignments for flags (mkolman)
  Related: rhbz#1088459
- Remove obsolete and disused Anaconda options (mkolman)
  Related: rhbz#1088459
- Move Anaconda version detection from isys to Python code (mkolman)
  Related: rhbz#1088459
- Parse boot options before parsing CLI options (mkolman)
  Related: rhbz#1088459
- Format the help text to properly fit to the terminal window (mkolman)
  Related: rhbz#1088459
- Switch Anaconda to argparse (mkolman)
  Related: rhbz#1088459
- Don't overwrite function argument when parsing help texts (mkolman)
  Related: rhbz#1088459
- Return CLI help text and version without delay (mkolman)
  Related: rhbz#1088459
- network: copy resolv.conf to chroot before installing packages (rvykydal)
  Resolves: rhbz#1048520
- network: fix crash on empty ksdevice boot option (rvykydal)
  Resolves: rhbz#1096846

* Thu Aug 28 2014 Brian C. Lane <bcl@redhat.com> - 19.31.86-1
- CmdlineError should exit with a 1 (bcl)
  Related: rhbz#1102318
- Do not attempt to run authconfig if it doesn't exist. (clumens)
  Related: rhbz#1123479
- Provide ways in kickstart to skip kernel and bootloader. (clumens)
  Related: rhbz#1123479
- Implement %%packages --instLangs. (dshea)
  Related: rhbz#1123479
- Allow skipping installation of the core group, if asked for in kickstart.
  (clumens)
  Related: rhbz#1123479
- Default PE size to blivet's default when requested from kickstart (vpodzime)
  Resolves: rhbz#1098139
- Re-enable addons as additional repositories. (clumens)
  Resolves: rhbz#1061174
- Fix installing from a second iso (bcl)
  Resolves: rhbz#1040722
- Don't change langpacks config of installer environment (rvykydal)
  Resolves: rhbz#1066017
- network: don't write HWADDR in ifcfgs generated by kickstart (rvykydal)
  Resolves: rhbz#1130042
- Use one thread for payload setup. (dshea)
  Resolves: rhbz#1125927
- Move the Anaconda class to a proper module (vpodzime)
  Related: rhbz#1125927
- Remove logging to tty3 and tty5 (bcl)
  Resolves: rhbz#1073336

* Fri Aug 22 2014 Brian C. Lane <bcl@redhat.com> - 19.31.85-1
- Check host filesystem space for dirinstall (bcl)
  Resolves: rhbz#1078876
- Fix bad indentation in my last commit. (clumens)
  Related: rhbz#980483
- Fix problems with the hdiso method. (clumens)
  Resolves: rhbz#980483
- Write the grub config even on errors
  Related: rhbz#1129435

* Mon Aug 18 2014 Brian C. Lane <bcl@redhat.com> - 19.31.84-1
- Only install liveinst symlink on supported arches (bcl)
  Related: rhbz#1121678

* Fri Aug 15 2014 Brian C. Lane <bcl@redhat.com> - 19.31.83-1
- Write storage after liveimg install (bcl)
  Related: rhbz#1080396
- Add some sanity checking to live payload (vpodzime)
  Related: rhbz#1080396
- Add support for tarfiles to liveimg kickstart command (bcl)
  Resolves: rhbz#1080396
- Mountpoint encrypted checkbox reflects container state (bcl)
  Resolves: rhbz#1076171
- Block leaf device encryption if container is encrypted consistently
  (vpodzime)
  Related: rhbz#1076171
- Fix gettext_potfiles.py for rhel7-branch (dshea). (clumens)
  Related: rhbz#1121678
- Add an option to makebumpver to skip all checks. (clumens)
  Related: rhbz#1121678
- Include .glade.h in the source distribution (dshea). (clumens)
  Related: rhbz#1121678
- Pass --enable-gtk-doc to configure in distcheck (dshea)
  Related: rhbz#1121678
- Fix the handling of files generated for xgettext (dshea)
  Related: rhbz#1121678
- Fix the liveinst install/uninstall hooks (dshea)
  Related: rhbz#1121678
- Always use $prefix in directory names. (dshea)
  Related: rhbz#1121678
- Use libtool with gtkdoc-scanobj (dshea)
  Related: rhbz#1121678
- Move the intltool Makefile rules into configure.ac (dshea)
  Related: rhbz#1121678
- Fix the wildcard usage in automake files. (dshea)
  Related: rhbz#1121678
- Write sslverify=0 for url kickstart method (bcl)
  Resolves: rhbz#1116858
- Add noverifyssl and proxy support to dracut ks handling (bcl)
  Resolves: rhbz#1116858
- Log installation successes and failures via ipmitool. (clumens)
  Resolves: rhbz#782019
- Suppress selinux error log when using default (bcl)
  Resolves: rhbz#1083239
- Skip source and software spoke in text live installations (bcl)
  Resolves: rhbz#1092763
- Default the OK button on the iscsi dialog to insensitive. (clumens)
  Resolves: rhbz#975823
- Change strings per stylistic advice from ECS (dshea)
  Resolves: rhbz#1035898
- Untranslate the type column of the network device type combobox (dshea)
  Related: rhbz#1035898
- Always define a continueButton and quitButton property. (clumens)
  Related: rhbz#1121678
- Resolve problems detected by our glade tests. (clumens)
  Related: rhbz#1121678
- Remove log_picker. (clumens)
  Related: rhbz#1121678
- Add missing files to dist (dshea)
  Related: rhbz#1121678
- Fix pre-processing of files for xgettext. (dshea)
  Related: rhbz#1121678
- Take care of strings with multiple substitutions. (clumens)
  Related: rhbz#1121678
- Remove lots of unused code from isys. (clumens)
  Related: rhbz#1121678
- Ignore a couple places where pylint warns us about accessing yum. (clumens)
  Related: rhbz#1121678
- Deal with all the methods where argument numbers differ. (clumens)
  Related: rhbz#1121678
- The Desktop class doesn't need to inherit from SimpleConfigFile. (clumens)
  Related: rhbz#1121678
- Fix up most of the "has no member" errors. (clumens)
  Related: rhbz#1121678
- Fix up all the redefined attribute errors. (clumens)
  Related: rhbz#1121678
- Make sure variables are defined in a __init__ method. (clumens)
  Related: rhbz#1121678
- Take care of some one-off pylint errors. (clumens)
  Related: rhbz#1121678
- Avoid the use of NamedTuple._make (dshea)
  Related: rhbz#1121678
- Modify the gtk_warning function in anaconda to use gtk3. (clumens)
  Related: rhbz#1121678
- Fix translation errors caught by our custom pylint tests. (clumens)
  Related: rhbz#1121678
- Take care of some one-off pylint errors. (clumens)
  Related: rhbz#1121678
- Get rid of too-general exception handling. (clumens)
  Related: rhbz#1121678
- Fix warnings about abstract methods not being overridden. (clumens)
  Related: rhbz#1121678
- Remove the lines to ignore E0611. (clumens)
  Related: rhbz#1121678
- Do not use sets or lists as default arguments to functions. (clumens)
  Related: rhbz#1121678
- Get rid of unnecessary lambdas. (clumens)
  Related: rhbz#1121678
- Get rid of unused variables. (clumens)
  Related: rhbz#1121678
- Use r"" for certain regular expressions. (clumens)
  Related: rhbz#1121678
- Use "raise Exception()" instead of "raise Exception, ..." (clumens)
  Related: rhbz#1121678
- Don't redefine built-in python keywords and methods. (clumens)
  Related: rhbz#1121678
- Get rid of all unused imports. (clumens)
  Related: rhbz#1121678
- Fix all indentation errors. (clumens)
  Related: rhbz#1121678
- Convert logging calls to not do string substitution. (clumens)
  Related: rhbz#1121678
- Add missing source files to po/POTFILES.in. (clumens)
  Related: rhbz#1121678
- Use the RHEL7 versions of kickstart command objects. (clumens)
  Related: rhbz#1121678
- Hook up the new test cases to automake/autoconf. (clumens)
  Related: rhbz#1121678
- Copy the tests/ directory from master over, less the gui tests. (clumens)
  Related: rhbz#1121678
- Remove the existing tests/ directory. (clumens)
  Related: rhbz#1121678
- Return int instead of Decimal when getting available free space (vpodzime)
  Related: rhbz#1053462
- Set rpm macro information in anaconda-yum. (dshea)
  Resolves: rhbz#1114586
- Keep selection when switching environments (mkolman)
  Related: rhbz#1043655
- Populate the repo store before changed can ever be called (clumens).
  Related: rhbz#1119867
- Install selected ks repos to target (bcl)
  Resolves: rhbz#1119867
- Add check for the format of grub2 encrypted password (bcl)
  Related: rhbz#1070327
- Don't use geolocation when installing with kickstart (mkolman)
  Resolves: rhbz#1111717
- Check xconfig before setting the installed displaymode (dshea)
  Resolves: rhbz#1081768
- Allow a wider variety of mountpoints (dshea)
  Resolves: rhbz#1109140
- Fix the handling of kickstart NFS repos with options (dshea)
  Resolves: rhbz#1121008
- Wrap the custom partitioning note (dshea)
  Resolves: rhbz#1098320
- Add support ppc64le (hamzy)
  Resolves: rhbz#1125474
- Cleanup arch tests (dshea)
  Related: rhbz#1125474
- Do not write out the vconsole.* boot options (vpodzime)
  Resolves: rhbz#1111405
- Use blivet's getFreeSpace for limitting automatic swap size (vpodzime)
  Resolves: rhbz#1053462

* Fri Aug 08 2014 Brian C. Lane <bcl@redhat.com> - 19.31.82-1
- Use low level file i/o for rpm callback logging (bcl)
  Resolves: rhbz#1035745
- Allow AddonData classes to parse options in the %%addon line (dshea)
  Resolves: rhbz#1065674
- Display a fatal error if unable to encrypt a password. (dshea)
  Resolves: rhbz#1057032
- Filter empty comps groups from both specific and generic lists (dshea)
  Resolves: rhbz#1071359
- Let Gtk pick the size for the isoChooserDialog (clumens)
  Resolves: rhbz#1063840
- Give a more correct error for missing groups/packages on exclude (clumens).
  Resolves: rhbz#1060194
- Clear out errors at the beginning of _save_right_side. (clumens)
  Resolves: rhbz#1070504
- Add more information to the custom part summary dialog. (clumens)
  Resolves: rhbz#975804
- Check that bootloader devices are configured before validating (dshea)
  Related: rhbz#1070283
- Fix the User subclass using an old version of the pykickstart superclass.
  (clumens)
  Resolves: rhbz#1083928
- Don't require user creation when root is locked (bcl)
  Resolves: rhbz#1030626
- Add platform specific group selection (bcl)
  Resolves: rhbz#884385
- Make parse-kickstart aware of the %%addon section (vpodzime)
  Resolves: rhbz#1083002
- Don't install implicitly added but explicitly excluded packages (vpodzime)
  Resolves: rhbz#1105013

* Fri Aug 01 2014 Brian C. Lane <bcl@redhat.com> - 19.31.81-1
- Highlight languages in langsupport that contain selected locales (dshea)
  Resolves: rhbz#1072355
- Add a wrapper function for GtkTreeViewColumn.set_cell_data_func (dshea)
  Related: rhbz#1072355
- Don't add redundant grub installs if stage1 is not a disk (dshea)
  Resolves: rhbz#1070283
- Don't use dhcp ntpservers for dir or image installation (bcl)
  Resolves: rhbz#1088506
- Preserve net.ifnames cmdline arg (bcl)
  Resolves: rhbz#1102410
- Add autopart --fstype support (bcl)
  Resolves: rhbz#1112697
- Don't skip cpfmtxa formatted dasds if zerombr specified in ks.
  (sbueno+anaconda)
  Resolves: rhbz#1073982
- rpmostreepayload: create /var/spool/mail required when adding user (rvykydal)
  Resolves: rhbz#1113535
- rpmostreepayload: Don't recreateInitrds for this payload (walters)
  Resolves: rhbz#1113535
- Use absolute path for extlinux/menu.c32 (rvykydal)
  Resolves: rhbz#1113535
- Only fail on a missing firewalld command if the firewall is enabled.
  (clumens)
  Resolves: rhbz#1113535
- Make sure /var/log/anaconda gets copied under the right root. (clumens)
  Resolves: rhbz#1113535
- format.setup in blivet takes only kwargs. (clumens)
  Resolves: rhbz#1113535
- rpmostreepayload: Use systemd-tmpfiles rather than handrolling mkdir
  (walters)
  Resolves: rhbz#1113535
- Make an ostree string easier for translators to deal with. (clumens)
  Resolves: rhbz#1113535
- Add RPMOSTreePayload (walters)
  Resolves: rhbz#1113535
- bootloader: Allow extlinux loader configuration to handle RPMOSTreePayload
  case (walters)
  Resolves: rhbz#1113535
- install: Handle distinct physical root/sysroot (walters)
  Resolves: rhbz#1113535
- install: Move Payload postInstall() after bootloader (walters)
  Resolves: rhbz#1113535
- iutil: Transparently redirect anyone who asks root=/mnt/sysimage to sysroot
  (walters)
  Resolves: rhbz#1113535
- main: Set flags.extlinux if extlinux is used in interactive-defaults.ks
  (walters)
  Resolves: rhbz#1113535
- iutil: Introduce getSysroot()/getTargetPhysicalRoot(), use instead of
  ROOT_PATH (walters)
  Resolves: rhbz#1113535
- Use ROOT_PATH not /mnt/sysimage (bcl)
  Resolves: rhbz#1113535
- Override ROOT_PATH with environmental variable (bcl)
  Resolves: rhbz#1113535
- gui/spokes/software: Enable iff payload is PackagePayload (walters)
  Resolves: rhbz#1113535

* Fri Jul 25 2014 Brian C. Lane <bcl@redhat.com> - 19.31.80-1
- Retranslate language filtering placeholder texts (vpodzime)
  Resolves: rhbz#1091885
- Set the selinux state from the command line (dshea)
  Resolves: rhbz#1084524
- Don't create the configured.ini file (mkolman)
  Resolves: rhbz#1119166
- Don't crash on anaconda-yum output containing multiple colons (mkolman)
  Resolves: rhbz#1092473

* Tue Apr 29 2014 Brian C. Lane <bcl@redhat.com> - 19.31.79-1
- network: fix device configuration in text mode (rvykydal)
  Resolves: rhbz#1091434

* Mon Apr 28 2014 Brian C. Lane <bcl@redhat.com> - 19.31.78-1
- Fix unloading modules in driver-updates (wwoods)
  Resolves: rhbz#1085099

* Wed Apr 09 2014 Brian C. Lane <bcl@redhat.com> - 19.31.77-1
- network: show ip of device with default route for vnc and ssh (rvykydal)
  Resolves: rhbz#1083305

* Mon Apr 07 2014 Brian C. Lane <bcl@redhat.com> - 19.31.76-1
- network: adapt to NM fixing virtual device disconnection (rvykydal)
  Resolves: rhbz#1084953

* Tue Apr 01 2014 Brian C. Lane <bcl@redhat.com> - 19.31.75-1
- Display WWIDs in the filter UI for FCoE devices (clumens).
  Resolves: rhbz#1080316
- Make it possible to override translation domain in GUIObjects (mkolman).
  Related: rhbz#1040240

* Fri Mar 28 2014 Brian C. Lane <bcl@redhat.com> - 19.31.74-1
- network: don't crash on virtual devices turned off (rvykydal)
  Resolves: rhbz#1080640
- Do not try to set keyboard preview dialog's size (vpodzime)
  Resolves: rhbz#1011140

* Thu Mar 27 2014 Brian C. Lane <bcl@redhat.com> - 19.31.73-1
- Add a list of cmdline args that append instead of replace (bcl)
  Related: rhbz#1073130

* Mon Mar 24 2014 Brian C. Lane <bcl@redhat.com> - 19.31.72-1
- Check boot args for None (bcl)
  Related: rhbz#1073130
  Resolves: rhbz#1075918
- network: don't pop HWADDR twice for vlan on s390 (rvykydal)
  Related: rhbz#1061646

* Fri Mar 21 2014 Brian C. Lane <bcl@redhat.com> - 19.31.71-1
- driverdisk: Show selection menu for network driver isos (bcl)
  Resolves: rhbz#1075918

* Wed Mar 19 2014 Brian C. Lane <bcl@redhat.com> - 19.31.70-1
- Write a modprobe blacklist (bcl)
  Resolves: rhbz#1073130
- Append cmdline arg values in BootArgs (bcl)
  Related: rhbz#1073130
- Only the Summary TUI hub wants to accept 'b' to continue (vpodzime)
  Resolves: rhbz#1077546

* Tue Mar 18 2014 Brian C. Lane <bcl@redhat.com> - 19.31.69-1
- Convert iter from filter model iter to backing store iter (amulhern)
  Resolves: rhbz#1074188

* Fri Mar 14 2014 Brian C. Lane <bcl@redhat.com> - 19.31.68-1
- Revert "Refresh after checkbox clicked (amulhern)"
  Related: rhbz#1074188
- Wait for other threads to finish before sending ready (bcl)
  Resolves: rhbz#1075103

* Tue Mar 11 2014 Brian C. Lane <bcl@redhat.com> - 19.31.67-1
- driver-updates: accept burned driver discs (wwoods)
  Resolves: rhbz#1073719
- Refresh after checkbox clicked (amulhern)
  Resolves: rhbz#1074188
- Don't create bootloader entries for kdump initrd and kernel.
  (sbueno+anaconda)
  Resolves: rhbz#1036086
- Cover both possible ways that GUI WWID may have been set (amulhern)
  Resolves: rhbz#1074184
- network: apply ks configuration to devices activated in initramfs (rvykydal)
  Resolves: rhbz#1037605
- Make it obvious user is going to begin installation. (sbueno+anaconda)
  Resolves: rhbz#975793
- Fix error handling in cmdline mode. (sbueno+anaconda)
  Resolves: rhbz#1034773
- Do nothing if previously selected selector gets focus again (vpodzime)
  Resolves: rhbz#1029798

* Fri Mar 07 2014 Brian C. Lane <bcl@redhat.com> - 19.31.66-1
- set proxy related environmental variables (bcl)
  Resolves: rhbz#854029
- network: handle race condition of disappearing active connection (rvykydal)
  Resolves: rhbz#1073424
- Do not write out /etc/adjtime file on s390(x) (vpodzime)
  Resolves: rhbz#1070748
- Don't traceback, just log a warning if connection is unavailable (mkolman)
  Resolves: rhbz#1070928

* Tue Mar 04 2014 Brian C. Lane <bcl@redhat.com> - 19.31.65-1
- driver-updates: skip iso selection with OEMDRV (bcl)
  Related: rhbz#1066784
- driver-updates: allow interactive mode to load multiple devices (wwoods)
  Related: rhbz#1066784
- driver-updates: add DoRefresh loop to select_iso() (wwoods)
  Resolves: rhbz#1066784
- driver-updates: add 'refresh' to selection_menu() (wwoods)
  Related: rhbz#1066784
- driver-updates: rework 'dd_finished' handling (wwoods)
  Related: rhbz#1066784
- driver-updates: refactor dd_scan (wwoods)
  Related: rhbz#1066784
- driver-updates: refactor menu to allow other options (wwoods)
  Related: rhbz#1066784
- Bump blivet Requires for DASD changes. (sbueno+anaconda)
  Related: rhbz#1064423
- Add GUI and TUI logic to handle unformatted DASDs. (sbueno+anaconda)
  Resolves: rhbz#1064423
- Show unformatted DASDs in the local disk store. (sbueno+anaconda)
  Resolves: rhbz#1064423
- Add dialog box to warn about formatting DASDs. (sbueno+anaconda)
  Resolves: rhbz#1064423
- Update disk refs when recovering from a devicefactory failure. (dlehman)
  Resolves: rhbz#1032141
- network kickstart: do not bind to MAC if SUBCHANNELS are present (rvykydal)
  Resolves: rhbz#1070232

* Fri Feb 28 2014 Brian C. Lane <bcl@redhat.com> - 19.31.64-1
- Fix console for s390 and 'noshell' mode (wwoods)
  Resolves: rhbz#1070672
- Set the name in the volume group store (dshea)
  Resolves: rhbz#1070854
- Always run efibootmgr from ROOT_PATH (bcl)
  Resolves: rhbz#1054968
- Only run gtk actions in the gtk thread. (dshea)
  Resolves: rhbz#1067405
- Don't ignore the directory of the driver disk iso file (vpodzime)
  Related: rhbz#1036765

* Wed Feb 26 2014 Brian C. Lane <bcl@redhat.com> - 19.31.63-1
- Revert "Force reboot the system on cmdline error. (sbueno+anaconda)"
  Related: rhbz#1034773
- Revert "Make it obvious user is going to begin installation.
  (sbueno+anaconda)"
  Related: rhbz#975793
- Add createrepo Requires (bcl)
  Related: rhbz#1016004
- ListStore.remove expects an iter, not an int (clumens).
  Resolves: rhbz#1062752
- Don't require network in standalone spoke for media installs (rvykydal)
  Resolves: rhbz#1066807
- Add support for kickstart --interfacename for vlans (rvykydal)
  Resolves: rhbz#1061646
- network: detect also fcoe vlan device names exceeding IFNAMESIZ (rvykydal)
  Related: rhbz#1051268

* Tue Feb 25 2014 Brian C. Lane <bcl@redhat.com> - 19.31.62-1
- driverdisk: Create a repo for network drivers (bcl)
  Resolves: rhbz#1016004
- fix inst.noshell (wwoods)
  Resolves: rhbz#1058607
- Don't use tmux for inst.noshell (wwoods)
  Resolves: rhbz#1058607
- driverdisk: Catch blkid failure (bcl)
  Related: rhbz#1036765
- driverdisk: Ignore extra blkid fields (bcl)
  Resolves: rhbz#1036765
- We can't trust rhcrashkernel-param to give us newline-free text. (pjones)
  Related: rhbz#814813
- Enable python-coverage in anaconda (dshea)
  Resolves: rhbz#1066339
- Remove redundant _setCurrentFreeSpace() call (amulhern)
  Related: rhbz#1043763
- Ensure media being verified is always unmounted (dshea)
  Resolves: rhbz#1050943
- Write 'text'/'cmdline' in anaconda-ks.cfg in text/cmdline mode (wwoods)
  Related: rhbz#1021963
- text install -> text system (wwoods)
  Resolves: rhbz#1021963
- Support the 'skipx' kickstart command (wwoods)
  Related: rhbz#1021963
- setup default environment in initialize instead of refresh (bcl)
  Resolves: rhbz#1066972
- Fix a nitpick from bcl. (pjones)
  Related: rhbz#814813
- Force reboot the system on cmdline error. (sbueno+anaconda)
  Resolves: rhbz#1034773
- Make rhcrashkernel-param get run on non-GRUB 2 platforms. (pjones)
  Resolves: rhbz#814813
- fix typo, extra bracket (bcl)
  Resolves: rhbz#1067758
- Do not use shim.efi on ARMv8 aarch64 (dmarlin)
  Resolves: rhbz#1067758
- Handle missing environments specified through kickstart (clumens).
  Resolves: rhbz#1067492
- Add 'c' to continue to timezone TUI spoke. (sbueno+anaconda)
  Resolves: rhbz#979335
- Make it obvious user is going to begin installation. (sbueno+anaconda)
  Resolves: rhbz#975793

* Fri Feb 21 2014 Brian C. Lane <bcl@redhat.com> - 19.31.61-1
- Skip running efibootmgr for image and dir installations (bcl)
  Resolves: rhbz#1067749
- reiserfs is not supported (bcl)
  Resolves: rhbz#1066635
- Show hidden disk images (bcl)
  Resolves: rhbz#1034996
- remove epdb SIGHUP debug handler (bcl)
  Related: rhbz#1065557
- Preserve ipv6.disable=1 on target system (wwoods)
  Resolves: rhbz#1040751
- Check that s390x LVM configuration is valid. (sbueno+anaconda)
  Resolves: rhbz#873135
  Resolves: rhbz#885011
- Re-apply disk selection on error in TUI storage. (sbueno+anaconda)
  Resolves: rhbz#1056316
- Disable tmpfs in the GUI (mkolman)
  Resolves: rhbz#1061666
- Change the CSS class name of the sidebar (clumens).
  Resolves: rhbz#1067049
- Error on "bootloader --location=partition" when using grub2 (clumens).
  Resolves: rhbz#969095
- Fix heredoc usage in generated /etc/grub.d/01_users (dcantrell).
  Resolves: rhbz#1044404

* Tue Feb 18 2014 Brian C. Lane <bcl@redhat.com> - 19.31.60-1
- Set mandatory property in network tui spoke. (sbueno+anaconda)
  Resolves: rhbz#1064139
- Disallow /boot on RAID on s390x. (sbueno+anaconda)
  Resolves: rhbz#1027670
- Use devicetree.resolveDevice instead of udev_resolve_devspec. (dlehman)
  Resolves: rhbz#1047338
- Set ThreadManager.any_errors to be a property (dshea)
  Resolves: rhbz#1066467
- driverdisk: Parse all blkid output (bcl)
  Resolves: rhbz#857248
  Related: rhbz#1036765
- Use vc_keymap as X layout only if we get nothing from localed (vpodzime)
  Resolves: rhbz#1066018
- Tell libreport if it is a final release or not (vpodzime)
  Resolves: rhbz#1063690
- Fix blkid output parsing and our output (vpodzime)
  Related: rhbz#1036765

* Fri Feb 14 2014 Brian C. Lane <bcl@redhat.com> - 19.31.59-1
- Allow using globs and alternative paths for specifying boot drive (clumens).
  Resolves: rhbz#1057282
- Remove app_paintable from a couple nav boxes (clumens).
  Resolves: rhbz#1064708
- Allow catching exceptions from threads (vpodzime)
  Resolves: rhbz#1063705

* Tue Feb 11 2014 Brian C. Lane <bcl@redhat.com> - 19.31.58-1
- adding support for new rhel7 branding graphics (duffy)
  Related: rhbz#1045250
- Properly retry package downloads (mkolman)
  Resolves: rhbz#924860
- Mark language search string in welcome spoke translatable. (sbueno+anaconda)
  Resolves: rhbz#955229
- Automatically reboot after successful cmdline installation. (sbueno+anaconda)
  Resolves: rhbz#1056507
- dracut: add when_any_cdrom_appears for cdrom autoprobe (wwoods)
  Resolves: rhbz#1049237
- Update the Aarch64 packages to include efibootmgr (dmarlin)
  Resolves: rhbz#1061927
- kickstart user accounts should be locked by default (bcl)
  Resolves: rhbz#1063554
- Move save_netinfo into a hook (bcl)
  Resolves: rhbz#1048231
- Fix kickstart 'updates' command (wwoods)
  Resolves: rhbz#999898
- Make sure LUKS devices can say they have a key (amulhern)
  Resolves: rhbz#1060255
- Handle LUKS passphrase before doing sanity check (amulhern)
  Resolves: rhbz#1060255
- Remove some unnecessary resets (amulhern)
  Related: rhbz#1060255
- Do not consider no available LUKS passphrase an error in do_autopart
  (amulhern)
  Resolves: rhbz#1060255
- Adapt to new blivet.sanityCheck() return type (amulhern)
  Related: rhbz#1060255
- Adapt StorageChecker class for changed return type of sanityCheck (amulhern)
  Related: rhbz#1060255
- Add sanityCheck functionality back into AutoPart.execute() (amulhern)
  Related: rhbz#1060255
- Bump blivet version for changed sanityCheck() interface (amulhern)
  Related: rhbz#1060255
- Removed unused ErrorRecoveryFailure import (amulhern)
  Related: rhbz#1060255
- network: adapt to changed handling of devices without carrier in NM
  (rvykydal)
  Resolves: rhbz#1062417
- Once again fix cmdline error handling. (sbueno+anaconda)
  Resolves: rhbz#1034773
- On incomplete ks, don't automatically proceed with install. (sbueno+anaconda)
  Resolves: rhbz#1034282
- Add correct kernel params if rootfs is btrfs on s390x. (sbueno+anaconda)
  Resolves: rhbz#874622

* Fri Feb 07 2014 Brian C. Lane <bcl@redhat.com> - 19.31.57-1
- driverdisk: Use a single systemd service to start DD UI (bcl)
  Related: rhbz#1035663
- driverdisk: Add dd_args_ks handling to driver-updates (bcl)
  Resolves: rhbz#1035663
- driverdisk: Process kickstart driverdisk commands (bcl)
  Related: rhbz#1035663
- driverdisk: Handle kickstart driverdisk command (bcl)
  Related: rhbz#1035663
- driverdisk: Use getargs instead of the env variable (bcl)
  Related: rhbz#1035663
- If a user has been created, don't allow entering the user spoke (clumens).
  Resolves: rhbz#1058564
- Fix crashes in the LayoutIndicator dispose function. (dshea)
  Resolves: rhbz#1061206
- Add support for fcoe --autovlan option (rvykydal)
  Resolves: rhbz#1055779
- Require systemd (dshea)
  Resolves: rhbz#1060823
- Remove the now-unused anaconda_spoke_header.png. (clumens)
  Related: rhbz#1045250
- Minor aesthetic cleanups (duffy).
  Resolves: rhbz#1045250
- Add a topbar design to SpokeWindows. (duffy)
  Resolves: rhbz#1045250
- Prevent kickstart parsing errors from ending up in boot options (mkolman)
  Resolves: rhbz#1060184
- Add a sidebar to the standalone and hub windows (duffy)
  Resolves: rhbz#1045250
- Allow specifying an environment in the kickstart file (clumens).
  Resolves: rhbz#1050994
- The autopart scheme combo should work for creating partitions manually, too.
  (clumens)
  Related: rhbz#1014671
- Global screenshot support (mkolman)
  Related: rhbz#1025038

* Tue Feb 04 2014 Brian C. Lane <bcl@redhat.com> - 19.31.56-1
- Add option help text for --image and --dirinstall flags (amulhern)
  Resolves: rhbz#1056791
- Search for service files of all first boot utilities (vpodzime)
  Resolves: rhbz#1060698
- Check RAID10 box for BTRFS (amulhern)
  Resolves: rhbz#1021856
- Remove unused import (amulhern)
  Related: rhbz#1022497
- Change the string used to test for serial console (dmarlin)
  Resolves: rhbz#1054951

* Fri Jan 31 2014 Brian C. Lane <bcl@redhat.com> - 19.31.55-1
- Fix iscsi target selection checkbox in GUI (rvykydal)
  Resolves: rhbz#1058653
- Don't Require NetworkManager-config-server (rvykydal)
  Resolves: rhbz#1012511
  Related: rhbz#1012511
- Set progress bar to 100 %% in a different way (vpodzime)
  Resolves: rhbz#1058755
- Do not add step for realmd if we are not gonna run it (vpodzime)
  Related: rhbz#1058755
- Make sure directory for DD extraction exists (vpodzime)
  Related: rhbz#1016004
- Removed unused variable (amulhern)
  Resolves: rhbz#982164
  Related: rhbz#982164
- Handle --image arguments more thoroughly (amulhern)
  Resolves: rhbz#982164
- Style the Done button to make it more noticable (mizmo). (clumens)
  Related: rhbz#1045250
- Display free space remaining in containers (clumens).
  Resolves: rhbz#1035832
- If a root password is set, don't show the spoke (clumens).
  Resolves: rhbz#1041405

* Tue Jan 28 2014 Brian C. Lane <bcl@redhat.com> - 19.31.54-1
- Set an upper limit on uids and gids. (dshea)
  Resolves: rhbz#1053103
- Change the reclaim space button rules (bcl)
  Resolves: rhbz#980496
  Related: rhbz#980496
- Check the validity of generated usernames in TUI (dshea)
  Resolves: rhbz#1058634
- Allow capital letters in usernames (dshea)
  Resolves: rhbz#1058638
- Display custom part warnings/errors on the spoke itself (clumens).
  Resolves: rhbz#975840
- Use integer numbers of megabytes in the Reclaim dialog (vpodzime)
  Resolves: rhbz#1034232
- Fix pylint errors (dshea)
  Related: rhbz#1021506
- Move the Quit button to the right and make it consistently sized (clumens).
  Resolves: rhbz#1038802
- Change the product name we key off (clumens).
  Resolves: rhbz#1055019
- Don't include zero sized disks in the custom part UI either (clumens).
  Resolves: rhbz#903131
- "Delete All" on the reclaim dialog should not delete hdiso source (clumens).
  Resolves: rhbz#980496
- Add a scrollbar to the error dialog (clumens).
  Resolves: rhbz#1021506
- Don't show the language twice for keyboard layouts. (dshea)
  Resolves: rhbz#1021849

* Fri Jan 24 2014 Brian C. Lane <bcl@redhat.com> - 19.31.53-1
- Put Xorg on tty6 in accordance with Ancient Anaconda Tradition (wwoods)
  Resolves: rhbz#980062
- handle "ks=cdrom[:<path>]" on systems with multiple CDs (wwoods)
  Resolves: rhbz#1049237
- Fix page logic in driver selection (bcl)
  Resolves: rhbz#1055333
- Fix problems going into custom partitioning with the new work flow. (clumens)
  Related: rhbz#1014671
- Allow going to the reclaim dialog even for autopart (clumens).
  Resolves: rhbz#1014671
- Add the autopart type combo to custom storage (clumens).
  Resolves: rhbz#1014671
- Tweak DiskOverview spacing a little bit (clumens).
  Resolves: rhbz#1014671
- Add custom part and encryption buttons to the main storage spoke (clumens).
  Resolves: rhbz#1014671
- Remove the existing install_options1 dialog, rename the others (clumens).
  Resolves: rhbz#1014671
- Extend the timeout period to 180s in the case of cmdline error.
  (sbueno+anaconda)
  Resolves: rhbz#1034773

* Thu Jan 23 2014 Brian C. Lane <bcl@redhat.com> - 19.31.52-1
- Only eject CDROM devices we're actually using (wwoods)
  Resolves: rhbz#966495
- Use validate_label to check whether label should be updated (mulhern)
  Related: rhbz#1038590
- Always reject label if the format exists (mulhern)
  Related: rhbz#1038590
- Make label field always sensitive (mulhern)
  Related: rhbz#1038590
- Give users way to select DD ISO interactively (vpodzime)
  Resolves: rhbz#1036765
- Save module list after initial module load (bcl)
  Resolves: rhbz#1050352

* Wed Jan 22 2014 Brian C. Lane <bcl@redhat.com> - 19.31.51-1
- fcoe: add fcoe=<NIC>:<EDB> to boot options for nics added manually (rvykydal)
  Resolves: rhbz#1040215
- Be more liberal in what is accepted as a size unit. (dshea)
  Resolves: rhbz#1039485
- Set device.format.label field close to where we read it (amulhern)
  Resolves: rhbz#1056139
- network: set ONBOOT=yes for iface used during DVD (hd:) installation
  (rvykydal)
  Resolves: rhbz#1052898
- Fix tb due to non-existant disk attr. (sbueno+anaconda)
  Resolves: rhbz#1056019
  Resolves: rhbz#1054746
- Install the rpmrc file to the initrd.img (vpodzime)
  Resolves: rhbz#1016004
- Give users hint about VNC password restrictions (vpodzime)
  Resolves: rhbz#1053546
- Unlock encrypted partitions before finding installations (vpodzime)
  Resolves: rhbz#1043783

* Mon Jan 20 2014 Brian C. Lane <bcl@redhat.com> - 19.31.50-1
- Use DataHolder for TUI nfs data (bcl)
  Resolves: rhbz#1034427
- Add DataHolder class (bcl)
  Related: rhbz#1034427
  Resolves: rhbz#1034427
- Various changes to handling of filesystem label setting (mulhern)
  Related: rhbz#1038590
- Don't show actions next to free space lines in the reclaim dialog (clumens).
  Resolves: rhbz#1054208
- If there's a label in the ISO device combo, put it on a new line (clumens).
  Resolves: rhbz#1031727
- network: don't activate default auto connections after switchroot (rvykydal)
  Resolves: rhbz#1012511
- network ks: allow setting only hostname with network command (rvykydal)
  Resolves: rhbz#1051564

* Fri Jan 17 2014 Brian C. Lane <bcl@redhat.com> - 19.31.49-1
- Show labels on Add zFCP dialog. (sbueno+anaconda)
  Resolves: rhbz#1054675
- Check for certain disk attrs before trying to access them. (sbueno+anaconda)
  Resolves: rhbz#1053055
- Change the name of the system z devices panel. (sbueno+anaconda)
  Related: rhbz#1024949
  Resolves: rhbz#1024949
- Fix selector device matching for unallocated partitions. (dlehman)
  Resolves: rhbz#1044523
- Grow the spoke gradient image to fit the nav_area (clumens).
  Resolves: rhbz#1035772
- Remove the UID and GID maximums. (dshea)
  Resolves: rhbz#1053103

* Thu Jan 16 2014 Brian C. Lane <bcl@redhat.com> - 19.31.48-1
- Return program output as a string instead of a list (dshea)
  Resolves: rhbz#1054142

* Thu Jan 16 2014 Vratislav Podzimek <vpodzime@redhat.com> - 19.31.47-1
- Fix closest mirror showing up when it shouldn't (mkolman)
  Resolves: rhbz#1031663
- There is no raid module on rhel7-branch (vpodzime)
  Related: rhbz#1052446
- Skip empty layout-variant specifications when setting layouts (vpodzime)
  Resolves: rhbz#1054083
- Add left and right margins to the Progress hub (vpodzime)
  Resolves: rhbz#1039556
- Disallow /boot on btrfs subvolume until grubby supports it. (dlehman)
  Resolves: rhbz#1052446
- Decode potentially 8-bit strings in TUI windows (dshea)
  Resolves: rhbz#1046836
- Do not translate strings defined at the module or class level. (clumens)
  Related: rhbz#1046836
- Require package for proper reporting to RHEL bugzilla (vpodzime)
  Related: rhbz#1015093

* Tue Jan 14 2014 Brian C. Lane <bcl@redhat.com> - 19.31.46-1
- Fix typo (bcl)
  Resolves: rhbz#1032066

* Tue Jan 14 2014 Brian C. Lane <bcl@redhat.com> - 19.31.45-1
- Get rid of the clear button in advanced storage spoke. (sbueno+anaconda)
  Related: rhbz#1024949
  Resolves: rhbz#1024949
- Fix failure to search by LUN in advanced storage spoke. (sbueno+anaconda)
  Resolves: rhbz#1026822
- Fix up the z Panel in advanced storage. (sbueno+anaconda)
  Resolves: rhbz#1024949
- Add support for adding zFCP devices in the GUI (sbueno+anaconda)
  Resolves: rhbz#994423
- Clean up rebase artifacts from previous commit. (dlehman)
  Related: rhbz#1029630
- Fix minimal install selection with incomplete kickstart (mkolman)
  Resolves: rhbz#1032066
- Disallow /boot on lvm until grub2 fully supports it. (dlehman)
  Resolves: rhbz#967880
- Handle cancelation of device resize in the custom spoke. (dlehman)
  Resolves: rhbz#1029630
- Handle non-leaf btrfs volumes with mountpoints. (dlehman)
  Resolves: rhbz#1026210
- Make sure to actually set the autopart flag when needed. (dlehman)
  Resolves: rhbz#1023584
- Make sure upper and lower bounds for resize are applied. (dlehman)
  Resolves: rhbz#1023190
- Disregard raid level combo when it isn't applicable. (dlehman)
  Resolves: rhbz#1020370
- Make the clear icon functional in language spoke. (sbueno+anaconda)
  Resolves: rhbz#1051609
- Remove the reference to "anaconda" in reIPL. (sbueno+anaconda)
  Resolves: rhbz#1052167
- Fix traceback on s390x bootloader install. (sbueno+anaconda)
  Resolves: rhbz#1052167
- Additional completion checks in network spoke. (sbueno+anaconda)
  Resolves: rhbz#1044571
- Fix interactive partitioning with incomplete kickstart (mkolman)
  Resolves: rhbz#1032124

* Mon Jan 13 2014 Brian C. Lane <bcl@redhat.com> - 19.31.44-1
- Be more defensive when getting layouts and their variants (vpodzime)
  Related: rhbz#1024774
- Implement and use functions for conversion between keymaps and layouts
  (vpodzime)
  Related: rhbz#1024774
- Provide our own sorting functions for regions and timezones (vpodzime)
  Resolves: rhbz#1025029
- Translate timezones in GUI (vpodzime)
  Resolves: rhbz#1015209
- Make layout and switching options description translated (vpodzime)
  Resolves: rhbz#1015209
- Update dumping of network info for new nmcli interface (rvykydal)
  Resolves: rhbz#1048166
- network: do not crash when device for network --device is not found
  (rvykydal)
  Resolves: rhbz#1023829
- network GUI: don't crash when wifi is activated in standalone spoke
  (rvykydal)
  Resolves: rhbz#1046138
- network GUI: ignore fcoe vlan devices (rvykydal)
  Resolves: rhbz#1051268

* Fri Jan 10 2014 Brian C. Lane <bcl@redhat.com> - 19.31.43-1
- Fix the release notes image cycler. (dshea)
  Resolves: rhbz#1049967
- Error gracefully if we have a question in cmdline mode. (sbueno+anaconda)
  Resolves: rhbz#869731
- Verify that designated label can be set (#1038590) (amulhern)
  Related: rhbz#1038590
- Do not change sensitivity of label field (#1038590) (amulhern)
  Related: rhbz#1038590
- Also update POTFILES.in for the new category name (clumens).
  Resolves: rhbz#1050053
- Rename network spoke header (mkolman).
  Resolves: rhbz#1050053
- Rename the network config spoke a little bit (clumens).
  Resolves: rhbz#1050053
- Consolidate storage and networking under one category (clumens).
  Resolves: rhbz#1050053
- Fix bool parsing of boot options with inst. prefix (mkolman)
  Resolves: rhbz#1044391
- Treat the output of vncpasswd as binary data, since it is (dshea)
  Resolves: rhbz#1045162
- Add iutil.exec* options for handling binary data (dshea)
  Related: rhbz#1045162
- Do not allow 'root' as a user name (vpodzime)
  Resolves: rhbz#1032671
- Add Shell spoke to s390x installations (vpodzime)
  Resolves: rhbz#1019248
- Put TUI spokes in common categories (vpodzime)
  Related: rhbz#1019248

* Tue Jan 07 2014 Brian C. Lane <bcl@redhat.com> - 19.31.42-1
- Display additional disk attributes in TUI storage spoke. (sbueno+anaconda)
  Resolves: rhbz#1024760
- network GUI: fix typo making device adding fail silently (rvykydal)
  Resolves: rhbz#1047799
- network GUI: fix porting thinko in log msg causing traceback on Configure
  (rvykydal)
  Resolves: rhbz#1047941
- Only display the actions summary dialog if there are any actions (clumens).
  Resolves: rhbz#1030511

* Fri Dec 20 2013 Brian C. Lane <bcl@redhat.com> - 19.31.41-1
- Check for ready before baseRepo in completed (bcl)
  Resolves: rhbz#1044985
- Print a message and exit if a user attempts to upgrade via kickstart. (dshea)
  Resolves: rhbz#1036756
- Don't show the language twice for keyboard layouts (dshea)
  Resolves: rhbz#1021849
- If there are incomplete spokes, let the user know which (clumens).
  Resolves: rhbz#1032801
- network: GUI, don't ask for wifi secrets upon Configure (rvykydal)
  Resolves: rhbz#1033073
- network: GUI, add support for virtual devices removing (rvykydal)
  Resolves: rhbz#1030870
- network: fix naming of slave ifcfg files from kickstart (rvykydal)
  Related: rhbz#1036047
  Resolves: rhbz#1036047
- network: GUI, handle virtual devices (bond, vlan, team) properly (rvykydal)
  Resolves: rhbz#1036047
- network: call GDBus proxy methods like python (rvykydal)
  Related: rhbz#1036047
  Resolves: rhbz#1036047
- network: add team support for kickstart %%pre phase (rvykydal)
  Resolves: rhbz#1003591
- network: generate kickstart commands for team devices (rvykydal)
  Resolves: rhbz#1003591
- network: support for adding team devices (rvykydal)
  Resolves: rhbz#1003591
- network: display team devices in status (rvykydal)
  Resolves: rhbz#1003591
- network: add team support to kickstart (rvykydal)
  Resolves: rhbz#1003591
- Accept only .iso files from the IsoChooser dialog (vpodzime)
  Resolves: rhbz#1015169
- Fix a typo (rvykydal)
  Related: rhbz#1039223
  Resolves: rhbz#1039223

* Tue Dec 17 2013 Brian C. Lane <bcl@redhat.com> - 19.31.40-1
- Add initial 64-bit ARM aarch64 EFI support (dmarlin)
  Resolves: rhbz#1034428
- Don't wait for systemctl shutdown command to exit (bcl)
  Resolves: rhbz#994188
- Fix default device for ks=cdrom (bcl)
  Resolves: rhbz#1042500
- Fix geolocation on live installs (mkolman)
  Resolves: rhbz#1032735
- Use ExceptionInfo namedtuple when dumping anaconda (vpodzime)
  Resolves: rhbz#983787
- Catch OSError if there are problems running authconfig. (sbueno+anaconda)
  Resolves: rhbz#994674
- Move atexit registration before running rescue mode (vpodzime)
  Resolves: rhbz#1042722
- Set environment variables in anaconda systemd shell file (amulhern)
  Resolves: rhbz#1023913
- Don't allow bootloader and /boot on iSCSI on s390 (vpodzime)
  Resolves: rhbz#1034222
- Remove enablement of whiteout/blackout plugins and adapt requires (notting)
  Resolves: rhbz#1040530

* Mon Dec 16 2013 Brian C. Lane <bcl@redhat.com> - 19.31.39-1
- use deepcopy on ksdata method (bcl)
  Resolves: rhbz#1024509
- Update source on errors (bcl)
  Resolves: rhbz#1030997
- clear errors when metadata is ok in tui source spoke (bcl)
  Resolves: rhbz#1034420
- Generate missing machine-id (bcl)
  Resolves: rhbz#1034916
- fcoe gui: repopulate device tree only if device was actually added (rvykydal)
  Related: rhbz#1039223
  Resolves: rhbz#1039223
- Exclude FCoE disks from local disks (rvykydal)
  Related: rhbz#1039223
  Resolves: rhbz#1039223
- fcoe: repopulate devicetree after adding FCoE SAN (rvykydal)
  Resolves: rhbz#1039223
- createUser is already in a chroot (bcl)
  Resolves: rhbz#1038241
- Hide password characters in iSCSI login fields (vpodzime)
  Resolves: rhbz#1034202
- Do not try to setup None NFS repository (vpodzime)
  Resolves: rhbz#1028699

* Wed Dec 11 2013 Brian C. Lane <bcl@redhat.com> - 19.31.38-1
- Make _yum.preconf setup atomic (bcl)
  Resolves: rhbz#882279
- refactor into _setupInstallDevice (bcl)
  Related: rhbz#882279
  Resolves: rhbz#882279
- Pass biosdevname boot option to installed system (rvykydal)
  Resolves: rhbz#1030943
- network: add s390 options in ifcfgs generated from kickstart (rvykydal)
  Resolves: rhbz#1031376
- Don't require pressing escape twice to kill the media check window (clumens)
  Resolves: rhbz#1015173
- Change source spoke proxy handling to use local copy (bcl)
  Resolves: rhbz#1029245
- clear software environment (bcl)
  Resolves: rhbz#1029536
- Make thread manager operations atomic (mkolman)
  Resolves: rhbz#1029898

* Thu Dec 05 2013 Brian C. Lane <bcl@redhat.com> - 19.31.37-1
- Omit /dev/sr* from list-harddrives (sbueno+anaconda)
  Resolves: rhbz#1032500

* Thu Nov 21 2013 Brian C. Lane <bcl@redhat.com> - 19.31.36-1
- Network protocols don't list Closest mirror first (vpodzime)
  Resolves: rhbz#1028697

* Mon Nov 18 2013 Brian C. Lane <bcl@redhat.com> - 19.31.35-1
- Set spokes' distribution and beta warning only once (vpodzime)
  Related: rhbz#1028370

* Mon Nov 11 2013 Brian C. Lane <bcl@redhat.com> - 19.31.34-1
- Don't try to unicode unicode strings (vpodzime)
  Resolves: rhbz#1029109
- Add tmpfs support (mkolman)
  Resolves: rhbz#918621

* Wed Nov 06 2013 Brian C. Lane <bcl@redhat.com> - 19.31.33-1
- Avoid raising an exception if epdb module unavailable (amulhern)
  Resolves: rhbz#1026779
- Display a EULA-related warning on progress hub at end of installation.
  (sbueno+anaconda)
  Resolves: rhbz#909309
  Related: rhbz#909309
- Show last 4 bytes of wwid (jstodola)
  Resolves: rhbz#1024966
- Display a EULA-related warning on the progress hub at the end of installation. (clumens)
  Related: rhbz#909309
- Handle focus changes of MountpointSelectors from outside (vpodzime)
  Resolves: rhbz#975838
- Make network-fetched driver disk .iso files work (vpodzime)
  Resolves: rhbz#1003595
- Updates to boot-options.txt document (amulhern)
  Related: rhbz#1026385
  Resolves: rhbz#1026385
- No longer install anaconda user documentation (amulhern)
  Resolves: rhbz#1026385

* Fri Nov 01 2013 Brian C. Lane <bcl@redhat.com> - 19.31.32-1
- Send the continue click after the queue is empty (bcl)
  Resolves: rhbz#1025346
- Fix kickstart block device resolution. (dlehman)
  Resolves: rhbz#1025508
- No longer use summary screen visit to decide whether bootloader has been
  configured (amulhern)
  Resolves: rhbz#916529
- Remove the bootloader line from the interactive kickstart file (amulhern)
  Resolves: rhbz#916529
  Related: rhbz#916529
- Set bootloader default location to mbr in constructor (amulhern)
  Resolves: rhbz#916529
- Add HDD ISO support for TUI (mkolman)
  Resolves: rhbz#1000327

* Wed Oct 30 2013 Brian C. Lane <bcl@redhat.com> - 19.31.31-1
- Update bootDrive info when storage config updated in text-mode.
  (sbueno+anaconda)
  Resolves: rhbz#861018
- Ignore SIGINT (amulhern)
  Resolves: rhbz#971323
- Make Software spoke ready even if there is no repo (vpodzime)
  Resolves: rhbz#1001054
- Correctly accept 'sshd' boot arg as alias for 'inst.sshd' (wwoods)
  Resolves: rhbz#924157
- Fix the Gkbd spec string for layouts with no variant (dshea)
  Resolves: rhbz#1011155
- mem may not exist when it's printed out in these error messages. (clumens)
  Related: rhbz#1019322
- Use devicetree to resolve device specs in kickstart. (dlehman)
  Resolves: rhbz#1019322
- Add bootloader execute before autopart (bcl)
  Resolves: rhbz#1022418
- BootLoaderError should not reset storage (bcl)
  Resolves: rhbz#1022418
  Related: rhbz#1022418
- Mountpoint is an attr of the format, not the device. (dlehman)
  Resolves: rhbz#1019510
- Do error checking of repository names on "Installation Source" screen.
  (amulhern)
  Resolves: rhbz#1020991

* Wed Oct 23 2013 Brian C. Lane <bcl@redhat.com> - 19.31.30-1
- Turn spinner back on for configuration (bcl)
  Related: rhbz#1019970
  Resolves: rhbz#1019970
- Correctly generate rescue initrd (bcl)
  Related: rhbz#1019970
  Resolves: rhbz#1019970
- Always regenerate initramfs (bcl)
  Resolves: rhbz#1019970
- remove signal disconnect (bcl)
  Resolves: rhbz#996899
- Always use decimal notation for Size specs (dshea)
  Resolves: rhbz#999440
- network kickstart: add support for devices configured in %%pre (rvykydal)
  Resolves: rhbz#1019796
- network gui spoke: use GDBus to obtain list of settings (rvykydal)
  Resolves: rhbz#1019775
- network: remove function we don't need anymore (rvykydal)
  Resolves: rhbz#1019775
  Related: rhbz#1019775
- network gui: make Configure button insensitive when no ap is selected
  (rvykydal)
  Resolves: rhbz#1015212
- Use a temporary directory for verifying ISO media (dshea)
  Related: rhbz#1017648
- Skip devices not controllable by blivet (dshea)
  Resolves: rhbz#1017648
- Use more general status for installations from media (vpodzime)
  Resolves: rhbz#1017703

* Mon Oct 21 2013 Brian C. Lane <bcl@redhat.com> - 19.31.29-1
- Use Unicode in the TUI buffer strings (dshea)
  Resolves: rhbz#1002462
- Don't ask to start vnc if user specifies text mode. (sbueno+anaconda)
  Resolves: rhbz#959119
- Do not accept changes if the user presses Esc on summary screen.
  Resolves: rhbz#998384

* Thu Oct 17 2013 Brian C. Lane <bcl@redhat.com> - 19.31.28-1
- Fix liveinst to work with livemedia-creator (bcl)
  Resolves: rhbz#1009711
- Fix initramfs generation for disk image installations. (dlehman)
  Resolves: rhbz#1018925
- Save mountpoints specified for existing btrfs volumes. (dlehman)
  Resolves: rhbz#1019510
- Add a command line option for disabling friendly multipath names. (dlehman)
  Resolves: rhbz#977815
- Keyboard variant names may contain dashes (vpodzime)
  Resolves: rhbz#1017556
- swap devices should be under the System portion (clumens).
  Resolves: rhbz#1017838
- Don't try to configure a bootloader for s390 disk image installs. (dlehman)
  Resolves: rhbz#994521
- Install bootloader to loop device in disk image installations. (dlehman)
  Resolves: rhbz#955202
- network: look for device settings also based on DEVICE value (rvykydal)
  Resolves: rhbz#1017788

* Fri Oct 11 2013 Brian C. Lane <bcl@redhat.com> - 19.31.27-1
- Refresh swap suggestion once we know which disks to use (vpodzime)
  Related: rhbz#1016673
- fix luksformat references (bcl)
  Resolves: rhbz#1014493
- kickstart: check for correct format (bcl)
  Resolves: rhbz#1014545
- UIScreen doesn't necessarily have the ready property (vpodzime)
  Related: rhbz#1000409
- Print long widgets in a nice way (vpodzime)
  Related: rhbz#1000409
- Take into account disk space when calculating swap suggestion (vpodzime)
  Resolves: rhbz#1016673

* Wed Oct 09 2013 Brian C. Lane <bcl@redhat.com> - 19.31.26-1
- Clear bootDisk and bootloader stage info on errors (bcl)
  Resolves: rhbz#1013482
- Catch BootLoaderError when setting up bootloader (bcl)
  Resolves: rhbz#1013474

* Wed Oct 09 2013 Vratislav Podzimek <vpodzime@redhat.com> - 19.31.25-1
- Clean up some rpmdiff errors (bcl)
  Resolves: rhbz#1012624
* Tue Oct 08 2013 Brian C. Lane <bcl@redhat.com> - 19.31.24-1
- Pass layout and variant in specific format to Gkbd (vpodzime)
  Resolves: rhbz#1011155
- Return switching options with the same order as shown (vpodzime)
  Resolves: rhbz#1011130
- Make the keyboard layout preview dialog bigger (vpodzime)
  Resolves: rhbz#1011140
- Make Keyboard spoke's status consistent with other statuses (vpodzime)
  Resolves: rhbz#1011166
- Generate ifcfg VLAN_ID value for kickstart network --vlanid (rvykydal)
  Resolves: rhbz#1011860
- Set ONBOOT=yes for the device used for installation (rvykydal).
  Resolves: rhbz#1002544
- Add a tooltip to the container combobox (bcl)
  Resolves: rhbz#975801
- Support for removing services from the firewall needs newer PyKickstart
  (mkolman)
  Related: rhbz#1016008
- Add support for removing services from the firewall (mkolman)
  Related: rhbz#1016008
- Don't set ksdata.lang.seen to True if using default value (mkolman)
  Resolves: rhbz#997397
- network gui: do not crash on devices without settings (eg wireless)
  (rvykydal)
  Related: rhbz#1011928
  Resolves: rhbz#1011928
- Network TUI: show the same status as in gui (rvykydal)
  Resolves: rhbz#1011928
- Network TUI: don't traceback when applying config to device without link
  (rvykydal)
  Resolves: rhbz#1011866
- Network TUI: fix updating of ksdata in apply (rvykydal)
  Resolves: rhbz#1011855
- Network TUI: ignore slaves devices for configuration (rvykydal)
  Resolves: rhbz#1011841
- network: don't create ksdata for devices enslaved in GUI (rvykydal)
  Resolves: rhbz#1011826
- Clean up ifcfg file handling (rvykydal)
  Resolves: rhbz#1011826
- Don't use temporary file and move when writing out an ifcfg file (vpodzime)
  Related: rhbz#1011826
  Resolves: rhbz#1011826

* Fri Oct 04 2013 Brian C. Lane <bcl@redhat.com> - 19.31.23-1
- Only encrypt the TUI user password once. (dshea)
  Related: rhbz#1012028

* Tue Oct 01 2013 Brian C. Lane <bcl@redhat.com> - 19.31.22-1
- Moved the NFS nolock option into Payload._setupNFS (dshea)
  Resolves: rhbz#1001593
- Don't try to parse langcode if none given (vpodzime)
  Resolves: rhbz#1013955

* Mon Sep 30 2013 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 19.31.21-1
- Move DEFAULT_VC_FONT to constants (vpodzime)
  Resolves: rhbz#1012811
- Fix issue where spoke returns to hub early in text mode. (sbueno+anaconda)
  Resolves: rhbz#979375
- Don't confuse users by misleading tooltip (vpodzime)
  Resolves: rhbz#1011112
- Display newly created partitions without a mountpoint, too (clumens).
  Resolves: rhbz#886039
- If the full device path is given in repo=hd:, still select it in the UI
  (clumens).
  Resolves: rhbz#980479
- tui ErrorDialog needs to be modal (bcl)
  Resolves: rhbz#983316

* Thu Sep 26 2013 Brian C. Lane <bcl@redhat.com> - 19.31.20-1
- Encrypt normal user passwords when doing text install. (sbueno+anaconda)
  Resolves: rhbz#1012028
- Fixup Eula class (bcl)
  Related: rhbz#1000409
- Center the Langsupport spoke's description (vpodzime)
  Related: rhbz#1006458
- Normalize keyboard layout and variant strings from langtable (vpodzime)
  Related: rhbz#1006458
- More robust parsing of the layout and variant string specification (vpodzime)
  Related: rhbz#1006458
- Share code between the Welcome and Langsupport spokes (vpodzime)
  Related: rhbz#1006458
- Rework the Langsupport spoke to work with all locales (vpodzime)
  Related: rhbz#1006458
- Match langs with stripped accents when filtering languages (vpodzime)
  Related: rhbz#1006458
- Get rid of the non-deterministic expand_langs and its usage (vpodzime)
  Related: rhbz#1006458
- Rework the Welcome spoke to allow users choose from all locales (vpodzime)
  Resolves: rhbz#1006458
- Allow seting up locale without modifying ksdata (vpodzime)
  Related: rhbz#1006458
- Remove an unused argument of get_available_translations (vpodzime)
  Related: rhbz#1006458
- Specify also query script when getting locale's native name (vpodzime)
  Related: rhbz#1006458
- Fix the langcode parsing regexp (vpodzime)
  Related: rhbz#1006458
- Adapt to the new localization module (vpodzime)
  Related: rhbz#1006458
- Rewrite the localization module (vpodzime)
  Related: rhbz#1006458

* Wed Sep 25 2013 Brian C. Lane <bcl@redhat.com> - 19.31.19-1
- Export the pykickstart Eula command (vpodzime)
  Related: rhbz#1000409
- LiveImageKSPayload skip the parent class setup method (bcl)
  Resolves: rhbz#1010500

* Fri Sep 20 2013 Brian C. Lane <bcl@redhat.com> - 19.31.18-1
- Search all disk types for install media (dshea)
  Resolves: rhbz#1004726

* Fri Sep 13 2013 Brian C. Lane <bcl@redhat.com> - 19.31.17-1
- Don't set up the resize slider for non-resizable devices. (dlehman)
  Resolves: rhbz#1008049
- Fix handling of flexible specs in onpart for member devices. (dlehman)
  Resolves: rhbz#1008048
- Don't mount cdroms that contain no mountable media. (dlehman)
  Resolves: rhbz#1008050
- Check MBR gap size even when /boot is on a plain partition. (dlehman)
  Resolves: rhbz#1008051
- Try to use VConsole keymap name as X layout (vpodzime)
  Resolves: rhbz#1007359
- Check ready state before baseRepo (bcl)
  Resolves: rhbz#1001538
  Related: rhbz#1001538

* Wed Sep 11 2013 Brian C. Lane <bcl@redhat.com> - 19.31.16-1
- Let users configure autopart options in interactive text ks.
  (sbueno+anaconda)
  Resolves: rhbz#1001061
- Catch race of network device state vs reading its config properties
  (rvykydal)
  Resolves: rhbz#919478
- Fix check for device state when reading its IPXConfig (rvykydal)
  Resolves: rhbz#1005681
- Network spoke: fix showing of ipv6 addresses (rvykydal)
  Resolves: rhbz#1005681
- Network spoke: show global ipv6 addresses (rvykydal)
  Resolves: rhbz#1005681
- Network spoke: fix refresh of device IP configuration (rvykydal)
  Resolves: rhbz#1005681
- Firstboot should be disabled by default after automated installations
  (vpodzime)
  Resolves: rhbz#985277

* Mon Sep 09 2013 Brian C. Lane <bcl@redhat.com> - 19.31.15-1
- Handle kickstarts that don't specify timezone (mkolman)
  Resolves: rhbz#1001598
- Only ignore missing packages entries (bcl)
  Resolves: rhbz#983316

* Thu Sep 05 2013 Brian C. Lane <bcl@redhat.com> - 19.31.14-1
- Add more details to iso device selector (bcl)
  Resolves: rhbz#971290
- Warn user if they enter a weak password in TUI. (sbueno+anaconda)
  Resolves: rhbz#1001039
- Don't mark spoke as completed if no repo is set. (sbueno+anaconda)
  Resolves: rhbz#1001538
- Run firstboot-only spokes on first boot by default (vpodzime)
  Related: rhbz#1000409
- Let hubs specify which environments they support (vpodzime)
  Related: rhbz#1000409
- Don't enable chronyd if disabled in kickstart (mkolman)
  Resolves: rhbz#1002583

* Wed Sep 04 2013 Brian C. Lane <bcl@redhat.com> - 19.31.13-1
- Remove Closest mirrors if no mirrors (bcl)
  Related: rhbz#876135
- Fix fastestmirror plugin check (bcl)
  Related: rhbz#876135
- Optionally hide the GUI option to install updates (dshea)
  Resolves: rhbz#999442
- Move the really_hide and really_show functions to utils (vpodzime)

* Wed Aug 28 2013 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 19.31.12-1
- Text network spoke: more strict ipv6 address input checking (rvykydal)
  Resolves: rhbz#909299
- Text network spoke: add to translated files (po/POTFILES.in) (rvykydal)
  Resolves: rhbz#909299
- Text network spoke: require netmask and gateway for static ipv4 (rvykydal)
  Resolves: rhbz#909299
- Text network spoke: Condense device configuration information (rvykydal)
  Resolves: rhbz#909299
- Text network spoke: fix ipv4 regex (rvykydal)
  Resolves: rhbz#909299
- Text network spoke: basic configuration support (rvykydal)
  Resolves: rhbz#909299
- Add support for network configuration in TUI. (sbueno+anaconda)
  Resolves: rhbz#909299

* Mon Aug 26 2013 Brian C. Lane <bcl@redhat.com> - 19.31.11-1
- Return only network devices supported in installer from nm_devices (rvykydal)
  Resolves: rhbz#999514
- Obtain network device type specific dbus interface dynamically (rvykydal)
  Resolves: rhbz#999514
- Catch no-hwaddr exception only for the respective call (rvykydal)
  Resolves: rhbz#999514
- Don't catch hwaddr not found exception for ethernet devices (rvykydal)
  Resolves: rhbz#999514

* Thu Aug 22 2013 Brian C. Lane <bcl@redhat.com> - 19.31.10-1
- Check for hwaddress exceptions. (dshea)
  Resolves: rhbz#999514
- If LANG isn't set, set it to default value. (sbueno+anaconda)
  Resolves: rhbz#997397
- Do not run another instance of the TUI for errors (vpodzime)
  Resolves: rhbz#997661
- Do not try to exit from the installation thread (vpodzime)
  Related: rhbz#997661
- Tell which thread failed to be added by the ThreadMgr (vpodzime)
  Related: rhbz#997661

* Wed Aug 21 2013 Brian C. Lane <bcl@redhat.com> - 19.31.9-1
- The NFS text dialog should never attempt to use method.url (clumens).
  Resolves: rhbz#998446
- Update both the method and repo info. (dshea)
  Resolves: rhbz#999185

* Mon Aug 19 2013 Brian C. Lane <bcl@redhat.com> - 19.31.8-1
- dracut no longer auto assembles everything (bcl)
  Resolves: rhbz#960496
- Don't override multilib setting unless the option was passed. (dlehman)
  Resolves: rhbz#987557
- Don't read proxy for methods that have no proxy (dshea)
  Resolves: rhbz#997410

* Wed Aug 14 2013 Brian C. Lane <bcl@redhat.com> - 19.31.7-1
- dracut/parse-kickstart should use the updated method-related classes
  (clumens).
  Resolves: rhbz#994978

* Tue Aug 13 2013 Brian C. Lane <bcl@redhat.com> - 19.31.6-1
- Change the betanag wording to be better for RHEL (clumens).
  Resolves: rhbz#917820

* Wed Aug 07 2013 Brian C. Lane <bcl@redhat.com> - 19.31.5-1
- Need to import the version constant we are using, too (clumens).
  Resolves: rhbz#994366

* Tue Aug 06 2013 Brian C. Lane <bcl@redhat.com> - 19.31.4-1
- Use ksdata.method.seen (bcl)
  Resolves: rhbz#989461
- Check that we're doing an HD install before examining the attr (clumens).
  Resolves: rhbz#989428

* Mon Aug 05 2013 Brian C. Lane <bcl@redhat.com> - 19.31.3-1
- Skip password strength check for kickstart passwords (dshea)
  Resolves: rhbz#993040
- Add unsupported hardware dialog (bcl)
  Resolves: rhbz#872728
- Only move INSTALL_TREE when it is mounted (bcl)
  Resolves: rhbz#888196
- Require fcoe-utils only on ix86 and x86_64 architectures (vpodzime)
  Resolves: rhbz#989913
- For vnc require network in intramfs (rvykydal)
  Resolves: rhbz#990071
- Honor hostname set in kickstart (rvykydal)
  Resolves: rhbz#988483
- Don't prompt for ssh on s390x if doing an image install. (sbueno)
  Resolves: rhbz#983056

* Thu Jul 25 2013 Brian C. Lane <bcl@redhat.com> - 19.31.2-1
- Fix driver disk path for inst.dd= method (bcl)
  Resolves: rhbz#987513
- Allow logging into multiple iscsi nodes at once (clumens).
  Resolves: rhbz#975831
- Add support for NFS as install source in TUI. (sbueno+anaconda)
  Resolves: rhbz#971298
- Fix crash while parsing ntp servers from DHCP6 (dshea)
  Resolves: rhbz#987978
- Wait for device connections for iface-bound iscsi in kickstart (rvykydal)
  Resolves: rhbz#740105
- Refer to blivet instead of storage in iscsi kickstart (rvykydal)
  Resolves: rhbz#740105
- Mark disk 'selected' if only one present in TUI. (sbueno+anaconda)
  Resolves: rhbz#975790
- Update devicetree only if we logged in to some target in add iscsi dialog.
  (rvykydal)
  Related: rhbz#740105
- Don't show multipath members in specialized disks overview (rvykydal)
  Resolves: rhbz#740105
- Do not populate devicetree after each single login in iscsi dialog (rvykydal)
  Resolves: rhbz#740105
- Match also iface when logging into selected iface-bound iscsi target
  (rvykydal)
  Resolves: rhbz#740105
- Make sure proper installclass selected for RHEL installs. (sbueno+anaconda)
  Resolves: rhbz#975720

* Tue Jul 09 2013 Brian C. Lane <bcl@redhat.com> - 19.31.1-1

* Thu May 23 2013 Brian C. Lane <bcl@redhat.com> - 19.30-1
- Fix software selection in text UI. (#965974) (sbueno+anaconda)
- Don't call _update_summary from within _add_disk_overview. (clumens)
- getDisks should not return a list that has duplicates in it. (clumens)
- Fix the rescan button (#929299). (clumens)
- Let checkbox disable updates-testing (#962522) (bcl)
- disable updates when method is set in ks (#952791) (bcl)
- Fix string formatting on text UI storage spoke. (#965460) (sbueno+anaconda)

* Tue May 21 2013 Brian C. Lane <bcl@redhat.com> - 19.29-1
- Handle empty text in simpleline (bcl)
- Fixup TUI source to work with kickstart (bcl)
- Add missing disk_selection XML (#962012,#962631) (bcl)
- Add ability for users to specify an installation source repo in text UI.
  (sbueno+anaconda)
- Add the ability to select software in text UI. (sbueno+anaconda)
- Add 'refresh' option in TUI; lock users out of threads that aren't ready
  (sbueno+anaconda)
- Add 'software' category to TUI summary hub (sbueno+anaconda)
- Only try to activate layouts if runtime system can be changed (vpodzime)
- Be more defensive in handling layouts from kickstart (#963103) (vpodzime)
- Return all layouts the XklWrapper knows about (#883555) (vpodzime)
- Fix issue where FS selection not applied in text UI. (#964069)
  (sbueno+anaconda)

* Thu May 16 2013 Brian C. Lane <bcl@redhat.com> - 19.28-1
- Remove testing leftover (#963503) (rvykydal)

* Wed May 15 2013 Brian C. Lane <bcl@redhat.com> - 19.27-1
- Partial fix for screen resize problems (#869364) (clumens)
- Remove an extra call to page clicked handler from refresh. (#959722)
  (dlehman)
- Always run through the full storage spoke. (#960732) (dlehman)
- Update apply button as appropriate after invoking dialogs. (#960254)
  (dlehman)
- Don't allow setting btrfs subvolumes' size. (#959723) (dlehman)
- Drop btrfs-specific raid level "single" for non-btrfs. (#959688) (dlehman)
- Update btrfs volume label when changing volume name. (#959727) (dlehman)
- Don't allow setting labels for btrfs subvolumes. (#960601) (dlehman)

* Wed May 15 2013 Brian C. Lane <bcl@redhat.com> - 19.26-1
- Pressing Delete on custom part should remove the selected mountpoint.
  (clumens)
- Use the same text formatting on the langsupport spoke as on the welcome
  spoke. (clumens)
- Remove the now-unused LanguageMixIn. (clumens)
- Do not BuildRequire python-bugzilla on RHEL (#953182) (dcantrell)
- Don't require network configuration in Live DVD (#962485) (rvykydal)
- Set default FS choice to LVM in text mode (#962600) (sbueno+anaconda)
- Move udev rules generation to pre-trigger (#958924) (bcl)
- Suggest names for btrfs mountpoints (bcl)
- Use a method to reset current_selector (#959707) (bcl)
- Fix non-default language being hidden in welcome spoke (mkolman)
- Mark placeholder text in add addtnl keyboard screen as translatable.
  (sbueno+anaconda)
- Mark language search string translatable. (#955229) (sbueno+anaconda)
- Remove the get_current_layout_name function (#895766) (vpodzime)
- Add support for the realm command (mkolman)
- Revert "Add support for the realm command" (mkolman)
- Add support for the realm command (mkolman)
- Support for getting NTP servers from DHCP (#862755) (mkolman)

* Thu May 09 2013 Brian C. Lane <bcl@redhat.com> - 19.25-1
- Change the buttons on the quit dialog. (clumens)
- Add FONT=latarcyrheb-sun16 to /etc/vconsole.conf (vpodzime)
- Use ntpdate instead of rdate (#950267) (vpodzime)
- Add layouts with a country if not added with a language (#960569) (vpodzime)
- Fixup xconf keymap code for text/dirinstall (bcl)
- Bump pykickstart to 1.99.30 for liveimg support (bcl)
- Add kickstart liveimg install command (bcl)
- Make sure all threads are done before install (bcl)
- Make sure stage1_disk isn't empty (#950487) (bcl)
- Add /boot/efi to suggested mountpoints (#960677) (bcl)
- Add extlinux command-line option. (mattdm)
- Add extlinux as a bootloader type. (mattdm)
- Bump the pykickstart requirement for the extlinux patches. (clumens)
- Revert "Busy cursor when applying changes in the custom spoke" (mkolman)
- Revert "Context manager for doing things with busied cursor" (mkolman)
- Use the F19 bootloader class from pykickstart, for --extlinux (mattdm)
- Transform bootloader --extlinux to extlinux command-line option (mattdm)
- Rework the layout of the storage spoke for low resolution setups. (clumens)
- Fix lower resolution display problems on the filter spoke. (clumens)
- Don't show iscsi passwords when focused, either.  Enjoy typing blind.
  (clumens)
- Add a couple more things to .gitignore. (clumens)
- Remove the bootloader class's obsoletes attribute. (clumens)
- Disable sort indicators on the filter UI. (clumens)
- Remove the Viewport from the disk shopping cart. (clumens)
- Cleaning up some of the TUI storage code (sbueno+anaconda)
- Add ability in TUI for users to select partitioning scheme. (sbueno+anaconda)
- Use the firmware-provided language if it's something we support. (pjones)
- Use systemd-localed for writing out xorg conf file (#958714) (vpodzime)
- Busy cursor when applying changes in the custom spoke (vpodzime)
- Make sure the "unbusy cursor" is used for the exception window (vpodzime)
- Context manager for doing things with busied cursor (vpodzime)
- Revert "Add signal handlers for controlling password entry visibility."
  (#958608). (clumens)
- Force a password to be set if option checked in TUI. (#927956)
  (sbueno+anaconda)
- Fix a minor display issue in TUI. (sbueno+anaconda)
- hostname has dropped -v option (bcl)
- Only override proxy and noverifyssl if specified (#880482) (bcl)

* Fri May 03 2013 Brian C. Lane <bcl@redhat.com> - 19.24-1
- Fix check for early exit from on_container_changed. (dlehman)
- Add ability to manipulate container sizes directly. (dlehman)
- Don't lock users who chose custom storage out. (dlehman)
- Don't allow unhiding of hidden disks during disk image installs. (#956020)
  (dlehman)
- Add layout indicator to the LUKS passphrase dialog (vpodzime)
- Add layout indicator to the BaseWindow (vpodzime)
- LayoutIndicator widget (vpodzime)
- self._password is set to None not "" initially (#958723) (vpodzime)
- Use constants for protocol's order instead of magic numbers (vpodzime)
- Support setting the name of a btrfs subvol (#892363). (clumens)
- If there are errors processing the kickstart file early on, just print them.
  (clumens)
- Stop defining _, N_, and P_ all over the place. (clumens)
- Fix a probably rare traceback in resizing from the custom part UI. (clumens)
- Add methods to do some hiding/showing that we do several different places.
  (clumens)
- Make it more obvious which fields on custom part are editable (#958251).
  (clumens)
- Clean up some of the get_object usage in custom.py. (clumens)
- Streamline DatetimeSpoke's timezone updating (#953311) (vpodzime)
- Allow setting timezone on the map without signal (vpodzime)
- Sensitivity of the date&time settings doesn't depend on timezone (vpodzime)
- Give the RAID level label on custom a mnemonic widget. (clumens)
- Give the hostname entry a keyboard shortcut. (clumens)

* Mon Apr 29 2013 Brian C. Lane <bcl@redhat.com> - 19.23-1
- Only check mandatory spokes in automated install (#956960,#895258) (bcl)
- Add scratch-bumpver target (bcl)
- Add Driver Update Disk repo handling to Anaconda (bcl)
- Add Driver Update Disk support to anaconda-dracut (bcl)
- Port driver update utilities from loader (bcl)
- Fix a typo. (clumens)
- Do not translate a blank window name. (clumens)
- Add a separator under the default language on the welcome screen. (clumens)
- Move the selected language to the top of the list on the welcome screen.
  (clumens)
- Remove the unused LanguageSpoke. (clumens)
- Add the "Add FCoE" dialog (#903122). (clumens)
- Allow enabling /etc/anaconda.repos.d repos like the docs say (#955724).
  (clumens)
- Move where the password quality checker is created (#956049). (clumens)
- Allow multiple disk selection with Shift-click (#864707) (vpodzime)
- Select all disks in the box with advanced storage as well (vpodzime)
- Don't change DiskOverview's background on 'chosen' changed (vpodzime)
- Fix number of arguments for languageGroups (liveDVD class) (#957038)
  (rvykydal)
- Apply some minor padding fixes on the container editing dialog. (clumens)
- If no root password was given, lock root's account (#927922). (clumens)
- Remove some unneeded boxes and alignments in the NTP config dialog. (clumens)
- Default to using the iscsi discovery credentials for login, if provided.
  (clumens)
- langsupport spoke: keep data.lang.lang first in status of spoke (rvykydal)
- Unpack property value returned by GDBus before using it (#956614) (rvykydal)
- Don't traceback when no activated devices were found for ks network default
  (#956614) (rvykydal)
- Ask about VNC also in connecting state, not only connected (#952801)
  (rvykydal)

* Wed Apr 24 2013 Brian C. Lane <bcl@redhat.com> - 19.22-1
- Container management improvements. (dlehman)
- Include swap-related disk space needs in storage options dialogs. (#951269)
  (dlehman)
- Show the summary screen before the luks passphrase dialog. (dlehman)
- Add language support spoke (#912364) (rvykydal)
- Add kickstart lang --addsupport option (#912364) (rvykydal)
- Add network --ipv6gateway kickstart option (#905226) (rvykydal)
- Remove pre-18.0 history from anaconda.spec. (clumens)
- Add free space information to DiskOverviews (#949746). (clumens)
- Raise exception if our module fails to be imported (vpodzime)
- Fix exception handling in rescue mode (vpodzime)
- Select all disks when Ctrl+A is pressed (#864707) (vpodzime)
- DiskOverview needs to grab focus if clicked (vpodzime)

* Mon Apr 22 2013 Brian C. Lane <bcl@redhat.com> - 19.21-1
- Set seen for lang from option & use constant for default (mkolman)
- Hook the Geolocation module to Anaconda (mkolman)
- Add geolocation module (mkolman)
- Add logging to exception handling (vpodzime)
- Run exception handling in the main thread also in TUI (vpodzime)
- Update network ksdata with cmdline options (#893784) (rvykydal)
- Return network devices actually activated (instead of just active) (#949002)
  (rvykydal)
- Don't traceback if we can't find PermHwAddr when looking for slaves (#949341)
  (rvykydal)
- Add support for iSCSI iface binding. (rvykydal)
- Fix a traceback when handling node login authentication. (clumens)
- Add a requirement on python-IPy now. (clumens)
- Display individual buttons on the filter UI instead of a combo. (clumens)
- Hook up authentication for iSCSI discovery and node login. (clumens)
- When the clear button is clicked on the filter spoke, clear out the fields.
  (clumens)
- Remove the extra "Target LUN" search option. (clumens)
- If all iSCSI nodes have been logged into, leave the dialog. (clumens)
- Populate the port combo on the filter spoke's search page. (clumens)
- Hook up filtering for iSCSI devices. (clumens)
- Add initial iSCSI support to the advanced storage UI. (clumens)
- Add a generic function to FilterPage for setting up a GtkComboBoxText.
  (clumens)
- self.disks -> self.pages in filter UI refresh method. (clumens)
- Add a button to bring up the Add Additional dialogs. (clumens)
- Remove pixmaps no longer needed by newui. (clumens)
- Add a checkmark on a DiskOverview when it is selected. (clumens)
- Make a couple UI modifications to the resize slider. (clumens)
- Make several changes to how addons are displayed (#873498). (clumens)
- Allow clicking on environment and addon text to toggle them (#928010).
  (clumens)
- Fix scrolling problems on the environment side of software selection
  (#928008). (clumens)
- Handle quit messages on the text progress UI hub (#895756). (clumens)
- If there's an error while in text mode, display it. (clumens)
- Force sizes on the network toolbar buttons (#951580). (clumens)
- Disable the "Closest mirror" option if there's no fastestmirror plugin
  (#876135). (clumens)
- Move text UI summary hub setup into the setup method (#927315, #950956).
  (clumens)
- Bring the text storage spoke a little more in line with the graphical one.
  (clumens)
- Make a home directory for the user by default (#950792). (clumens)
- Add some padding under the ransom notes on the progress hub. (clumens)
- Remove a lot of ancient crud from the installclasses. (clumens)
- Set the default fs type on RHEL (#951088). (clumens)
- Add a Spoke.changed attribute. (clumens)
- Display device names on MountpointSelectors (#888872). (clumens)
- Add signal handlers for controlling password entry visibility. (clumens)
- Ransom notes can be either PNGs or JPGs. (clumens)
- dracut/parse-kickstart: handle network --mtu (wwoods)
- Exclude a couple more password variables from dumps (bcl)
- Enlightbox dialogs in the custom spoke (vpodzime)
- Create and use GtkWindowGroup for our windows (vpodzime)
- We can import Gtk globally now (vpodzime)
- Handle both types of data we can get from libxklavier (#950921) (vpodzime)

* Tue Apr 16 2013 Brian C. Lane <bcl@redhat.com> - 19.20-1
- Fix two more syntax errors in the custom spoke. (#952662) (dlehman)

* Mon Apr 15 2013 Brian C. Lane <bcl@redhat.com> - 19.19-1
- Show device size with full precision to avoid spurious resize. (#951276)
  (dlehman)
- Fix another typo (old_fstype->old_fs_type). (#951593) (dlehman)
- Fix typo encryption_changed->changed_encryption. (#950700) (dlehman)
- Remove some remnants of old multipath code. (#951259) (dlehman)
- Protect the block device containing the stage2 image. (dlehman)
- Clarify code for iutil.get_active_console() etc. (wwoods)

* Thu Apr 11 2013 Brian C. Lane <bcl@redhat.com> - 19.18-1
- Revert "Revert "Don't emit "gfxterm" in grub2 configs (#821355)"" (pjones)
- Make "s" a hotkey for "Save Changes" on Advanced User Configuration. (pjones)
- Clean up tracebacks saved in pstore space (#950709) (pjones)
- Move anaconda-yum to /usr/libexec/anaconda/ (bcl)
- Cleanup: remove dead upgrade code (wwoods)
- Fix console= persistence, remove serial (#928269) (wwoods)
- Revert "Don't emit "gfxterm" in grub2 configs (#821355)" (pjones)
- Disable grub2-mkconfig's submenus by default. (pjones)
- Don't emit "gfxterm" in grub2 configs (#821355) (pjones)
- updates to boot-options.txt (wwoods)
- flags.py: remove unused flags (wwoods)
- remove flags.virtpconsole (wwoods)
- Call os.chdir("/") after calling os.chroot (vpodzime)

* Tue Apr 09 2013 Brian C. Lane <bcl@redhat.com> - 19.17-1
- Pass open file to execWithRedirect for vncpasswd (#948638) (bcl)
- Fix ip= saving in parse-kickstart (hamzy)
- Fix initial raid level when switching to a raid-capable device type.
  (dlehman)
- The raid level combo cannot be not sensitive for preexisting devices.
  (dlehman)
- Make sure fstype combo is not sensitive for btrfs devices. (dlehman)
- Add an entry to the raid level combo for btrfs' single. (dlehman)
- Clean up _save_right_side and adapt to changes in blivet.devicefactory.
  (dlehman)
- Remove anaconda's udev rules. (dlehman)
- Add requires for some things that aren't strictly required by blivet.
  (dlehman)
- Parent's finalize method needs self (vpodzime)
- Use Sphinx syntax for docstrings (vpodzime)
- Use None for unbounded size requests. (dlehman)
- Disable yum lock debugging for the final release. (clumens)
- The source spoke should display something nicer than "Not ready" (#948112).
  (clumens)
- Don't run storage execution in an endless loop (#948331, #948285). (clumens)
- If an incorrect source is given for a ks install, don't fallback (#948212).
  (clumens)
- Fix a bug when creating a new mountpoint with no given size (#948228).
  (clumens)
- memInstalled has moved (#947261). (clumens)
- Correctly report an error if OSError is hit when setting up the source
  (#947634). (clumens)
- Add anaconda-yum to %%files (bcl)

* Thu Apr 04 2013 Brian C. Lane <bcl@redhat.com> - 19.16-1
- Modify LocaledWrapper to use our safe_dbus module (#928287) (vpodzime)
- Add module providing safe DBus operations (vpodzime)
- Define a DEFAULT_DBUS_TIMEOUT constant and use it (vpodzime)
- Execute the yum transaction in another process (bcl)
- Add anaconda-yum (bcl)
- Add execReadlines utility (bcl)
- Use namedtuple instead of our magic tuples (vpodzime)
- Tell python-meh architecture of the anaconda package (vpodzime)
- Add release number to the result of getAnacondaVersion (vpodzime)
- Fix _isys.so location in the updates.img (vpodzime)
- Network spoke: Fix reading of device type from combobox (#947120) (rvykydal)

* Tue Apr 02 2013 Brian C. Lane <bcl@redhat.com> - 19.15-1
- Fix two small problems with the UID/GID spin buttons (#929173, #929138).
  (clumens)
- The Update Settings button should only be sensitive if you change something.
  (clumens)
- Move datetime spoke initialization into its own thread, too. (clumens)
- Make it more clear nothing will happen immediately on custom storage
  (#883195). (clumens)
- Replace the custom part size spinner with an entry. (clumens)
- Add a factory class for our various communications queues. (clumens)
- Make exception handling in the rescue mode work (#926913) (vpodzime)

* Thu Mar 28 2013 Brian C. Lane <bcl@redhat.com> - 19.14-1
- Handle the end of the %%addon section (vpodzime)
- Don't allow setting a mountpoint for an fstype we cannot mount. (dlehman)
- Fix a bug I introduced with 3c78c1a5c. (clumens)
- Get rid of the customization expanders on custom partitioning. (clumens)
- Translate the "Create a new volume group..." text (#892782). (clumens)
- Move the Desired Capacity label and spinner into its own row (#907883,
  #904999). (clumens)
- move Xorg test up so we might start vnc instead (hamzy)
- Set word wrapping on the label telling you how to switch layouts (#924885).
  (clumens)
- gtk_thread_wait -> gtk_action_wait in custom.py (#926926). (clumens)
- Support multiple values for kicstart network --namserver= in dracut (#917481)
  (rvykydal)
- get_widget -> get_object (#927898). (clumens)
- THREAD_* constants are in pyanaconda, not pykickstart. (clumens)
- Network spoke: fix model access thinko in Add device dialog (rvykydal)
- Use constants for thread names (mkolman)
- Move network connection timeout from network to constants (mkolman)
- udev-settle.service is now systemd-udev-settle.service (wwoods)
- Add boot-options.txt (wwoods)

* Fri Mar 22 2013 Brian C. Lane <bcl@redhat.com> - 19.13-1
- Set Tip text on the create user spoke. (dcantrell)
- Use space instead of underscore when user uses the timezone name (#924352)
  (msivak)
- Use only self.data in TUI timezone spoke's status (msivak)
- Use the named tuple in root password dialog (#924138) (msivak)
- Add message instructing users they can type to search for language.
  (sbueno+anaconda)
- Don't unbusy the cursor until the first action is ready to display. (clumens)
- Move custom storage setup into its own thread. (clumens)
- When you turn off NTP, clear the warning along the bottom of the screen.
  (clumens)
- If the disk has no serial number, don't give the DiskOverview a popup.
  (clumens)
- Reorder the columns on the shopping cart so name is next to description.
  (clumens)
- Add device node names to the resize dialog as a new column. (clumens)
- Use an emblem for indicating spokes have not been completed. (clumens)
- If you remove all the disks in the shopping cart, disable the buttons.
  (clumens)
- Apply a style to the network spoke's toolbar. (clumens)
- Add a little more space between the updates checkbox and the add repo stuff.
  (clumens)
- Remove the partition scheme expanders. (clumens)
- Don't error out if a ks %%include is missing when looking for sshpw
  (#923627). (clumens)
- Do not guess username immediately when user clears it (#924184) (msivak)
- Do not require password when no user is requested (#924150) (msivak)
- Refresh the checkboxes on AdvancedUser dialog properly (#924257) (msivak)
- Allow setting the default GID of the new user. (msivak)
- Add call to new-kernel-pkg --rpmposttrans (#922988) (bcl)
- Make our gtk_* decorators safer and more intelligent (vpodzime)
- Add method for checking if in main thread to the ThreadManager (vpodzime)
- Port the mandatory logic for User and Password spokes from GUI to TUI
  (msivak)
- Use only self.data to determine completeness in User spoke (msivak)
- Make firstboot kickstart command aware of initial-setup (msivak)
- Add command and data updates to AnacondaKSHandler's __init__ (msivak)

* Tue Mar 19 2013 Brian C. Lane <bcl@redhat.com> - 19.12-1
- _model -> model in filter.py. (clumens)
- Add some documentation to FilterPage. (clumens)
- Add the advanced storage UI and hook it up. (clumens)
- Don't wrap the DO creation in gtk_thread_wait. (clumens)
- Add a button to the specialized window to bring up the add dialog. (clumens)
- Filter out multipath devices from the getDisks results. (clumens)
- Reduce duplicated code between the GUI and TUI. (clumens)
- Set the horizontal and vertical scales to what we want. (clumens)
- Move DiskOverview creation out into its own method. (clumens)
- Add a slot on the storage spoke for display of advanced storage. (clumens)
- Log the actual exception for getPackage (bcl)
- Add the addon repos from a repo's treeinfo file (bcl)
- Disable failed repos, not remove them (bcl)
- Add repo addon to source spoke (bcl)
- Remove the previous addon repo code and UI (bcl)
- Addon repo glade changes (bcl)
- Enable updates repo by default (bcl)
- Adjust _getTreeInfo so that proxy_url can be passed (bcl)
- Add enable flag to RepoData object (bcl)
- Modify repo interface in packaging (bcl)
- Change the source DiskOverview to a label (bcl)
- Display the reason for payloadInstallHandler error (bcl)

* Mon Mar 18 2013 Brian C. Lane <bcl@redhat.com> - 19.11-1
- Don't create temporary lists if not needed (vpodzime)
- Fix reclaiming disk space for non-us installations. (rvykydal)
- Allow for raising thread exceptions when threadMgr.get is called (bcl,
  clumens). (clumens)
- Hook up the new refresh dialog. (clumens)
- Add a dialog prompting the user to refresh anaconda's view of storage.
  (clumens)
- Add a refresh button to the custom partitioning toolbar. (clumens)
- Add a reset button to the bottom right of the custom spoke. (clumens)
- Hook up the new action summary dialog. (clumens)
- Add a summary screen of actions to be performed on all disks. (clumens)
- Catch error when incorrect nfs address entered (sbueno+anaconda)
- Use GDBus also for connection settings update. (rvykydal)
- Network spoke: improve message format parametrization for translators
  (rvykydal)
- Don't set ibft device renaming for dracut, let it just do its job (#828505)
  (rvykydal)
- Mark Timezone selection as firstboot spoke (msivak)
- Add user creation spoke to TUI (msivak)
- Refactor TUI password spoke to use the declarative EditTUISpoke (msivak)
- Use guess_username from pyanaconda.users in gui.spokes.UserSpoke (msivak)
- Add declarative EditTUISpoke (msivak)
- Allow modyfying exit question in TUI (msivak)
- Return False from TUI.run() if it was exited prematurely (msivak)
- Add guess_username function to users.py (msivak)
- Mark incomplete mandatory spokes in text mode (msivak)
- Network spoke: move formatting parameters out of translation function
  (rvykydal)
- Network spoke: add keyboard accelerator to add device combobox (#906263)
  (rvykydal)
- Network spoke: don't decorate add_device_dialog (#906263) (rvykydal)
- Don't pass undefined stdout from execWithCapture. (rvykydal)
- Network spoke: import network module instead of list of too many functions
  (rvykydal)
- Vlan support: kickstart (#906272) (rvykydal)
- Vlan support: generate kickstart (#906272) (rvykydal)
- Vlan support: GUI - hub status information (#906272) (rvykydal)
- Network spoke: check whether added network device is already in list
  (#906272) (rvykydal)
- Vlan support: GUI - add "Vlan ID" and "Parent" to vlan tab (#906272)
  (rvykydal)
- Return correct nm_device_setting_value for bonds and vlans (#906272)
  (rvykydal)
- Vlan support: GUI - show vlan devices (#906272) (rvykydal)
- Vlan support: GUI - add "Parent" and "Vlan ID" info (glade) (#906272)
  (rvykydal)
- Vlan support: GUI - add vlan device (glade) (#906272) (rvykydal)
- Show that password was set by kickstart in TUI (msivak)
- Add settable quit message to TUI (msivak)
- Check _current_action for not being None before using it (vpodzime)

* Mon Mar 11 2013 Brian C. Lane <bcl@redhat.com> - 19.10-1
- Bonding support: GUI - hub status information (#906263) (rvykydal)
- Bonding support: GUI - generate kickstart network command for bonds (#906263)
  (rvykydal)
- Bonding support: GUI - add device dialog (#906263) (rvykydal)
- Bonding support: GUI - add device dialog (glade) (#906263) (rvykydal)
- Bonding support: GUI - device list, configuration and adding bond (#906263)
  (rvykydal)
- Bonding support: GUI - Slaves line in Wired tab (glade) (#906263) (rvykydal)
- Crypt the root we get from the user (#918991). (jkeating)
- Adapt to the new libxklavier's behaviour (vpodzime)
- We use python-meh's interfaces instead of Anaconda's (vpodzime)
- Redraw screen in case of valid input and nothing new scheduled (vpodzime)
- Fix two places where we are locking up the main thread (#886680). (clumens)
- Log when we acquire and release the _yum_lock (dlehman, clumens). (clumens)
- Do not fail when the logging stream cannot be opened (in initial-setup..)
  (msivak)
- Mark DateTime spoke as usable for Firstboot (msivak)
- Fix a missing import and move the addon KS output template (msivak)
- Make the TUI mainloop more resistant to screen implementation errors (msivak)
- Teach TUI how to react on async events (msivak)
- Could not load UI file advanced_user.glade (hamzy)
- Don't try to remove the timer when it's None (DatetimeSpoke) (vpodzime)
- Log failed imports in the collect functions (vpodzime)
- remove the remnants of sparc support (dennis)
- Remove installmethod.py (dead code) (wwoods)
- Make default media eject behavior match old behavior (wwoods)
- Silence "cp: cannot stat '/etc/cmdline'..." error message (wwoods)

* Fri Mar 01 2013 Brian C. Lane <bcl@redhat.com> - 19.9-1
- Behave nice when root password is set by kickstart (msivak)
- Password spoke is mandatory if the created user is not an admin (msivak)
- Use the user data provided by kickstart (msivak)
- Add the User creation spoke including the Advanced dialog (msivak)
- Bonding support: kickstart (rvykydal)
- Condense some duplicated and overly wordy code in custom.py. (clumens)
- Add a new allMembers property that returns a list of pages and members.
  (clumens)
- All Pages have a title, so get rid of the getattr games. (clumens)
- Allow more than one Page to be expanded at a time. (clumens)
- Get rid of the currentPage method. (clumens)
- Promote page._members to page.members. (clumens)
- Require passing the title to a Page's constructor. (clumens)
- Pressing F12 should do the same thing as clicking "Done" (#840998). (clumens)
- A bunch more "install" -> "installation" changes. (clumens)
- When the user clicks "Reclaim Space", go back to the hub (#911792). (clumens)
- Modify the logic that makes the reclaim button sensitive (#911793). (clumens)
- Add a free space line under every disk in the reclaim dialog. (clumens)
- Remove the initial sentence from the top of the reclaim dialog (#911793).
  (clumens)
- Fix a traceback in verifying optical media on the source spoke. (clumens)
- Revert "Hook up the "Remove Packages" button on the dep solving error
  screen." (#905899). (clumens)
- Don't display "(null)" as a MountpointSelector's mountpoint. (clumens)
- dracut: add anaconda-pre-shutdown.sh to fix eject (#809920) (wwoods)
- Continue booting when checkisomd5 is aborted (#891551) (bcl)
- Fix ksdevice=<MAC> - instead of renaming the device to ksdev0 just use it
  (rvykydal)
- Add pigz to initrd.img (wwoods)
- Use %%_prefix macro value when calling configure in makeupdates (vpodzime)
- Try to import modules the standard way first in collect (msivak)

* Thu Feb 21 2013 Brian C. Lane <bcl@redhat.com> - 19.8-1
- Add more stuff to the exception reporting skip list. (clumens)
- Compare Sizes to Sizes in the reclaim dialog (#913484). (clumens)
- The disk cart summary does not need a mnemonic. (clumens)

* Wed Feb 20 2013 Brian C. Lane <bcl@redhat.com> - 19.7-1
- Fix RAID level test (bcl)
- unpack product.img to /updates (#911873) (bcl)
- If you attempt to search on the network device pane, don't crash. (clumens)
- Don't treat the _ in x86_64 as a mnemonic. (clumens)
- If you set_markup, the label forgets set_use_underline from glade. (clumens)
- Don't try to update spokes that are indirect. (clumens)
- If you cannot reclaim more space, don't show the reclaim radio (#911791).
  (clumens)
- Swap the order of the part scheme combo and encryption checkbox. (clumens)
- Fix for the addons kickstart support (vpodzime)
- kickstart.py needs udev that now lives in blivet (vpodzime)
- Refactor pieces of the Datetime spoke and move some parts to kickstart.py
  (vpodzime)
- Set ONBOOT=no for default autoconnections (#905918, #886090) (rvykydal)
- Don't use "type" to name a variable. (rvykydal)
- Update all spokes on a Hub when spoke is exited (msivak)
- Wait for continueButton in KS mode if the user changed anything (msivak)
- Fix up word wrap on the DetailedErrorDialog. (clumens)
- Display storage warnings, similar to how errors are displayed (#909410).
  (clumens)
- Fix reprompting and screen redrawing on invalid input (vpodzime)
- Refresh addons_paths once we know if gui or tui takes place (vpodzime)
- Fixup anaconda.spec (bcl)

* Thu Feb 14 2013 Brian C. Lane <bcl@redhat.com> - 19.6-1
- fix uuid reference in parse-kickstart (bcl)
- Fixup kickstart script logging (bcl)
- Tell libreport the crash happened in Anaconda (#885690) (vpodzime)
- Restore older behavior regarding ks argument without a file name (#910550).
  (clumens)
- Move the encryption checkbox to the dialog (bcl)
- re-fetch metadata when proxy settings change (bcl)
- Apply some fixes to the spec file (#909592, metherid (clumens)
- install -> installation in a couple user-visible strings. (clumens)
- Restore support for partial kickstart files (#887254). (clumens)
- Get rid of packagesSeen. (clumens)
- Remove debugging print (DatetimeSpoke) (vpodzime)
- Honor modules' __all__ when doing collect (msivak)
- Use ksdata.addons instead of ksdata.addon and add ADDON_PATHS to sys.path
  (vpodzime)
- Remove unused modules (dbus) and stuff from network.py (rvykydal)
- Replace get_NM_connection() using new nm module. (rvykydal)
- Replace get_NM_settings_value() using new nm module (rvykydal)
- Replace nmIsConnected() using new nm module (rvykydal)
- Replace hasActiveNetDev() using new nm module (rvykydal)
- Replace getDevicesProperies() using new nm module (rvykydal)
- Replace getIPAddresses() using new nm module (rvykydal)
- Replace getMacAddress() using new nm module (rvykydal)
- Replace isWirelessDevice() using new nm module (rvykydal)
- Replace getLinkStatus() using new nm module (rvykydal)
- Replace getActiveNetDevs() using new nm module (rvykydal)
- Replace getDevices() using new nm module (rvykydal)
- Move NM dbus calls to separate module. (rvykydal)
- Move networking functions from isys to network module. (rvykydal)
- Remove unused stuff from network.py (rvykydal)
- Remove unused networking stuff from isys (rvykydal)
- Network spoke: remove unused NM path and interface constants (rvykydal)
- Add 'eject' to the anaconda initramfs (wwoods)
- Ensure hookdir exists before creating eject script (wwoods)
- remove anaconda-cleanup-initramfs.service (wwoods)
- Add dracut/save-initramfs.sh (wwoods)
- Bring back the askmethod parameter (#889887). (clumens)
- Add a new selectorFromDevice method to the accordion. (clumens)
- The storage logger is now the blivet logger. (dlehman)
- DeviceFactory has moved from blivet to blivet.devicefactory. (dlehman)

* Fri Feb 08 2013 Brian C. Lane <bcl@redhat.com> - 19.5-1
- Add --dirinstall command (bcl)
- Convert the mount point entry to one containing a drop down. (clumens)
- Move the Modify SW button into a link in the text. (clumens)
- Rework all the dialogs after you click Done on the storage spoke (#903501).
  (clumens)
- Overrides for the Gdk have _2BUTTON_PRESS defined (vpodzime)
- Add entries with completions to the comboboxes (DatetimeSpoke) (vpodzime)
- Make the custom partitioning bullet points take up less horizontal space.
  (clumens)
- Don't say you can reuse existing mountpoints unless there are some. (clumens)
- Point gobject-introspection at our updates directory for overrides. (clumens)

* Mon Feb 04 2013 Brian C. Lane <bcl@redhat.com> - 19.4-1
- Remove libcurl requirement from configure.ac. (dlehman)
- DMI_CHASSIS_VENDOR has moved into blivet. (dlehman)

* Fri Feb 01 2013 Brian C. Lane <bcl@redhat.com> - 19.3-1
- unpack product.img to correct location (#869098) (bcl)
- Fix including _isys.so and isys/__init__.py in updates.img (vpodzime)
- Fix typo "DHCPV6" (rvykydal)
- Don't crash on wireless connections created in Live CD desktop (#895736)
  (rvykydal)
- Adapt ifcfg -> ksdata mapping to NM change from IPADDR to IPADDR0. (rvykydal)
- Fix static and dhcp of network --ipv6 command (set IPV6_AUTOCONF=no)
  (rvykydal)
- NM defaults to IPV6_AUTOCONF=yes (rvykydal)
- Fix up spacing on installation options dialog buttons a little bit. (clumens)
- Ignore double clicks on the DiskOverviews (#902467). (clumens)
- When the user creates a new mountpoint, display it by default (#886039).
  (clumens)
- Add device node name information to the storage spoke and disk cart
  (#902617). (clumens)
- Do not include disks that have 0 size (#903131, #904977). (clumens)
- Preserve the state of the Customize... expanders on custom storage (#883134).
  (clumens)
- Make it a little more clear what's happening on the disk selection spoke
  (#903498). (clumens)
- Move Xorg to vt7 (bcl)
- Network: read ipv6 configuration type from NM settings instead of ifcfg file
  (rvykydal)
- Don't fail on missing ifcfg file when setting default ONBOOT (#904817)
  (rvykydal)
- Don't fail on invalid network --device kickstart specification. (rvykydal)
- Ignore ipv6 for a device (IPV6INIT=no) only for noipv6 option. (rvykydal)
- Network: fix disabling of ipv6 (noipv6 option) (rvykydal)
- Stop writing /etc/sysconfig/network (#895900) (rvykydal)
- We dont create missing ifcfg files on our own in anaconda anymore. (rvykydal)
- Use NM dbus interface to modify ifcfg configuration (#893892) (rvykydal)
- Document FileSystemSpaceChecker. (clumens)
- Add the customization category to POTFILES.in. (clumens)
- Add a license and overview to the g-i overrides file. (clumens)
- Create/clarify some documentation in the custom widgets. (clumens)
- Condense string formatting in a couple custom widgets. (clumens)
- Remove the widget-specific TODO list. (clumens)
- Add selinux to the list of parameters we pass on (#895860). (clumens)
- Display error status messages in a darker red color. (clumens)
- Add newline at the end of xorg.conf generated from ksdata (vpodzime)
- Move pyanaconda.packaging.get_mount_* into blivet.util. (dlehman)
- Remove obsolete references to simpleFilter. (dlehman)
- Remove the storage module and replace it with blivet. (dlehman)
- Move tsort, platform, and baseudev into storage. (dlehman)
- Start laying groundwork for splitting storage out of pyanaconda. (dlehman)
- Remove anaconda flag checking from OpticalDevice.eject. (dlehman)
- Remove unused functions and move storage-specific utils to storage. (dlehman)
- Remove installclass arch filtering. (dlehman)
- Handle sending program output to tty5 through the logging setup. (dlehman)
- Use dumpe2fs output to determine dirty fs. (dlehman)
- Remove filesystem migration code. (dlehman)
- Use threadMgr.wait to check threads (bcl)
- Add error reporting to threadMgr (bcl)

* Fri Jan 25 2013 Brian C. Lane <bcl@redhat.com> - 19.2-1
- Use only one large grid for the hubs. (clumens)
- Indicate nothing will happen until "Begin Installation" is clicked (#883195).
  (clumens)
- Exit anaconda correctly on SIGTERM (vpodzime)
- Move communication module to pyanaconda/ui (vpodzime)
- Function getDefaultHostname was renamed some time ago. (rvykydal)
- Use constant for default hostname ("localhost.localdomain" currently)
  (rvykydal)
- Make update_hostname function do just one thing - update ksdata. (rvykydal)
- Rename wait_for_dhcp pieces to say what they actually do (rvykydal)
- Initialize network synchronously (#902090) (rvykydal)
- xgettext wants "utf-8", not "utf8".  Python doesn't seem to care. (clumens)
- On the storage spoke, only show the summary button if a disk is selected.
  (clumens)
- Add text letting people know they can use existing filesystems (#883150).
  (clumens)
- Default to mirrored RAID instead of striped (#888867). (clumens)
- Replace the RAID level checkboxes with a single combo box. (clumens)
- Don't allow mountpoints to start with /proc or /sys either. (clumens)
- Add 'nmcli dev list' output to data gathered after crash (vpodzime)
- Add lsblk output to data gathered after crash (#879940) (vpodzime)
- Cleanup some trailing whitespace on otherwise empty lines (vpodzime)
- Refactor and cleanup exception handling pieces (vpodzime)
- Exception handling for text mode (#865325) (vpodzime)
- python-meh's saveExceptionWindow no longer uses the accountManager (vpodzime)
- Enable line wrapping in a couple more places (#901551). (clumens)
- Support /boot on RAID metadata version 1.2 (#896163). (clumens)
- Don't check memory for rescue mode (#895948). (clumens)
- Split __init__ and setup in TUI screens so we can set the environment and
  search paths (msivak)
- Add a requirement on device-mapper-multipath (#895973) (msivak)
- Update default fs type code (#855401). (clumens)
- Display the background gradient image from a map signal handler. (clumens)
- Remove the old cmdline and script interfaces. (clumens)
- anaconda-cleanup doesn't use an interface at all. (clumens)
- Remove the old text mode UI. (clumens)
- Move constants_text out of the textw directory. (clumens)
- Remove more references to system-config-*. (clumens)
- Add device NM_DEVICE_TYPE_ETHERNET to isys (#893892) (rvykydal)
- Dump missing ifcfg ifles only for ethernet devices (#893892) (rvykydal)
- Take over dhcp connection by NM for network root (eg nfs) (#883451, #893656)
  (rvykydal)
- Use DEFAULT_LANG instead of magic value "en_US.UTF-8" (vpodzime)
- fixup spec with 19.1 commits (bcl)

* Mon Jan 14 2013 Brian C. Lane <bcl@redhat.com> - 19.1-1
- Rework the reclaim dialog to have a resize slider. (clumens)
- g_type_init call is no longer needed (bcl)

* Fri Jan 11 2013 Brian C. Lane <bcl@redhat.com> - 18.40-1
- Prepare structures to save spoke completenes for firstboot and GIE (msivak)
- Do not call exit at the end of GUI interface, just quit the main loop
  (msivak)
- Improve handling of .py and .pyc equivalence while collecting classes
  (msivak)
- Set default language to en_US.UTF-8 (#891379) (msivak)
- Set the local hostname during installation (vpodzime)
- Refactor and cleanup our localization module (vpodzime)
- Network spoke: use correct state value to display device status. (rvykydal)
- drop fcoe-utils dependency for s390x (rhbz#894025) (sbueno+anaconda)
- More TODO list wrangling. (clumens)
- On storage, remove the "Continue" button and make "Done" do it all (#882737).
  (clumens)
- getLUKSPassphrase is no longer used, so kill it. (clumens)
- "Hub" shouldn't be in the title for any text mode hub. (clumens)
- Do not lightbox any dialogs on the custom storage spoke (#875291). (clumens)
- Revert "Do not lightbox the Add Mountpoint dialog (#875291)." (clumens)
- Don't allow changing a VG name to empty in the VG editor (#892395). (clumens)
- Check country_layouts is not None when using it (#893026) (vpodzime)
- Don't redownload payload from closest mirror only if we actually have some
  (#892665) (rvykydal)
- Remove some modules obsoleted by the packaging module. (dlehman)
- Prefer country over language when returning default layout (#867110)
  (vpodzime)
- Fix Quit button in standalone network spoke (#892120) (rvykydal)
- Network spoke: add sanity check for hostname setting (#856456) (rvykydal)
- Network spoke: add hostname setting (#856456) (rvykydal)
- Fix completeness check for md fwraid arrays. (#892621) (dlehman)
- Fix handling of failure to create a new container. (#892046) (dlehman)
- Force disk selection for interactive installs. (#888293) (dlehman)
- Mark another string for translation (#892760). (clumens)
- Do not lightbox the Add Mountpoint dialog (#875291). (clumens)
- Strip out pango markup before attempting to match languages (#892463).
  (clumens)
- Mark the live progress hub message for translation (#892069). (clumens)
- Allow deleting whole disks using the reclaim dialog (#880686). (clumens)
- Don't allow mountpoints to start with /dev (#891447). (clumens)
- Disable the configure button for pre-existing devices (#888296). (clumens)
- Add keyboard mnemonics to the spoke selectors, too. (clumens)
- Add keyboard accelerators to a whole lot of widgets (#864964). (clumens)
- Try fallback if none exactly matching language is found (#891487) (vpodzime)
- Only skip welcome screen for ks installs (#891755) (bcl)
- protect getDirSize from vanishing files (#891759) (bcl)
- start vnc without ip address (#832510) (bcl)
- Update physical device's sysfs path for btrfs (sub)volumes. (#891443)
  (dlehman)
- Wrap text on the updates checkbox to fix screen placement (#888880).
  (clumens)
- The return value from execWithRedirect is an int (#891313). (clumens)
- Add placeholder names to a couple strings (#890157). (clumens)
- Fix multiple copies of spokes appearing from update image (msivak)
- Import pyanaconda.addons in the anaconda script (vpodzime)
- Update the API which controls where should spokes be displayed (msivak)
- Update the way we look for glade files, spokes, hubs and categories (msivak)
- Make screenshot routines reusable in Firstboot (msivak)
- Do not fail when missing directories are present in addon paths (msivak)
- Pass addons paths to user interfaces (msivak)
- hook up help window close button (#889570) (bcl)
- add setKeyboardCheckButton to list of things to translate (#889352) (bcl)
- Mark for translation and show translated some more GUI elements (#877658)
  (vpodzime)
- Translate storage errors (#877658) (vpodzime)
- Don't allow changing the boot disk from inside the custom spoke. (#889585)
  (dlehman)
- Add help text and a help button to the custom storage spoke. (#889570)
  (dlehman)
- Allow /boot on btrfs subvol if using grub2. (#888603,868465) (dlehman)
- Don't keep old device name when switching to btrfs in custom. (dlehman)
- Fix container member set management for md arrays. (#889101) (dlehman)
- Include incomplete devices when listing dependant devices. (#889330)
  (dlehman)
- Use systemd to run checkisomd5 (#874486) (harald)
- fixup direct nfs iso url handling (#879187) (bcl)
- fixup nfs repo install code (#879187) (bcl)

* Wed Dec 19 2012 Brian C. Lane <bcl@redhat.com> - 18.39-1
- Add more yum locking to yumpayload (#860022) (bcl)
- The percent bar can go in the same column as the space label. (clumens)
- Don't resize NTFS partitions to smaller than the filesystem on them
  (#885912). (clumens)
- Remove some unused error handling code from old UI. (clumens)
- Don't generate ifcfg files for non-existing devices in parse-kickstart
  (#886647) (rvykydal)
- Encode unicode strings returned by pytz.country_timezones() (#887236)
  (vpodzime)
- Always set passphrase for newly encrypted devices. (#888560) (dlehman)
- Handle edit of preexisting encrypted lv. (#885378) (dlehman)
- Raise DeviceError instead of ValueError from device ctor. (#888089) (dlehman)
- Set line wrap on the info bar (#888112). (clumens)
- Don't crash when vg edit triggers spurious change event. (#883699) (dlehman)
- Add handling for incomplete lvm/md devices. (#876441) (dlehman)
- Fallback to mdN if no name was found for incomplete md array. (#873224)
  (dlehman)
- Add product.py to POTFILES (#858628). (clumens)
- Sort categories in GUI alphabetically (msivak)
- Fix typo in variable name (msivak)
- Collect addon paths properly (msivak)
- Move the import constants line below setupPythonUpdates (msivak)
- Only close AddLayout dialog on double-click if something is selected
  (#887371) (vpodzime)
- Add warning to keyboard spoke on live installations (#886463) (vpodzime)
- Split ksdata execute and setup methods for addons (msivak)
- Add support for KS %%addon section and the API+code to use it (msivak)
- Import collected modules only once (msivak)
- Update run-spoke to use paths (msivak)
- Export QuitDialog and it's message string (msivak)
- Update the hack we use to preload AnacondaWidgets - we need to load the
  typelib not just the .so file (msivak)
- Add FirstbootMixIn (msivak)
- Move the path definitions to Interface and pass it to the Hubs from there
  (msivak)
- Make TUI ready for getting spokes from multiple directories (msivak)
- Make GUI more reusable and support multiple directories for spokes and
  categories (msivak)
- Modify collect so it works with directories with missing __init__.py (msivak)
- Split completed and mandatory attributes (msivak)
- Move info about possible actions below the free space info (vpodzime)
- Fix a couple pylint errors (#867125). (clumens)
- Fix an undefined variable error (#867129). (clumens)
- The fs type combo should be sensitive when reformat is checked (#887201).
  (clumens)
- Remove idiomatic, hard to translate text (#865598). (clumens)
- Activate default layout when it is changed (#882440) (vpodzime)
- Validate and correct vg names as needed. (dlehman)
- Don't allow resize of devices with no/unrecognized formatting. (#869841)
  (dlehman)
- Add keyboard dracut setup args (#875567) (vpodzime)
- recheck software when source changes (#875599) (bcl)
- Include the new lib directory in the package (#886319, #886470). (clumens)
- Add a gradient background to spoke headers (mizmo, clumens). (clumens)
- Only allow changing filesystem type if the reformat combo is checked
  (#885906). (clumens)
- It's possible for mountpoint to be None (#885279). (clumens)
- Explicitly set True/False in the bootloader setting (#885381). (clumens)

* Tue Dec 11 2012 Brian C. Lane <bcl@redhat.com> - 18.38-1
- In interactive installs, default to bootloader in the MBR (#885284).
  (clumens)
- Make sure software selection is checked against filesystem space. (#853636)
  (dlehman)
- Update default install size and disk space estimate. (dlehman)
- Add checkbox for setting language default layout (#866887) (vpodzime)
- Change testing area label to something more appropriate (KeyboardSpoke)
  (vpodzime)
- Fix getting country layout variants (vpodzime)
- Wait for slower dhcp before running vnc server (#868777) (rvykydal)
- Network spoke: fix NMClient signal callback arguments (#885488) (rvykydal)
- Add logging for networking and improve logging of ifcfg files (rvykydal)
- Honor user request via UI to not install a bootloader. (#885240) (dlehman)
- Handle partition removals regardless of deepcopy. (#884896) (dlehman)
- Default to partitions for /boot* instead of just /boot/efi. (#884606)
  (dlehman)
- Fix a logic error in ActionDestroyFormat.obsoletes. (#885004) (dlehman)
- Take device type into account when making the config button sensitive
  (#885051). (clumens)
- Hide VG-related widgets when displaying a non-LV mountpoint first (#885131).
  (clumens)
- Install default system for %%packages --default (#869978) (bcl)
- Fix a typo in the live cd completion text (#884373). (clumens)
- Do not allow deleting or editing a protected device in custom part (#884599).
  (clumens)
- If path doesn't exist, don't traceback.  Return None. (clumens)
- Add/remove the HDISO source from protectedDevSpecs (#882147). (clumens)
- Put the bad VG name into the error message (#884359). (clumens)
- Use updated connection settings object for default auto config files
  (#883383) (rvykydal)

* Wed Dec 05 2012 Brian C. Lane <bcl@redhat.com> - 18.36-1
- Call udev_settle from inside udev_trigger. (dlehman)
- Prevent enabling the encryption checkbutton erroneously. (dlehman)
- Make sure Storage is initialized before refreshing the custom spoke.
  (dlehman)
- Fix initialization of Storage.roots to use a list. (#884270) (dlehman)
- Don't allow reformat without setting a mountpoint. (#883076) (dlehman)
- Fix check for toggled encryption checkbutton. (#882722) (dlehman)
- Make sure FS minSize is never greater than its currentSize. (#876547)
  (dlehman)
- When considering whether anything can be shrunk, throw out protected devs.
  (clumens)
- In the UI, mark the HDISO source device as protected (#879610). (clumens)
- update mdraid superBlock space calculation (#883483) (bcl)
- Remove resetResolver function, we don't need it anymore (#868695) (rvykydal)
- Network spoke: improve logging. (rvykydal)
- Unify writeNetworkConf with other modules (rename, put in ks.execute)
  (rvykydal)
- Fix network command --onboot and --activate options. (rvykydal)
- Fix two calls of self.window.set_info (#883632) (vpodzime)
- Use BaseWindow.set_warning and set_error in GUIObject's methods (vpodzime)

* Tue Dec 04 2012 Brian C. Lane <bcl@redhat.com> - 18.35-1
- Fix a bug when switching back to an HDISO install source (#879612). (clumens)
- Lower case the DONE button on media check. (clumens)
- Change mirrorlist checkbox text (#883191). (clumens)
- Change the bootloader button to indicate you can also not install one.
  (clumens)
- Stop writing /etc/sysconfig/keyboard (#871543) (mschmidt)
- Stop writing /etc/sysconfig/i18n (#871543) (mschmidt)
- Write /etc/hostname (#871543) (mschmidt)
- Correct doing string substitution for encryption. (clumens)
- Add install.py to POTFILES.in so a lot more strings can be translated.
  (clumens)
- Only instantiate main line action objects when they are needed. (clumens)
- Add a category to POTFILES.in so "USER SETTINGS" gets translated. (clumens)
- Make sure product info and spoke titles are translated throughout. (clumens)
- Substitute on new_install_name when it's needed, not at the top of custom.py.
  (clumens)
- Compare the protocol combox box on position, not text. (clumens)
- When we retranslate the welcome window, inform glibc. (clumens)
- Add gettext checks to widgets/configure.ac. (clumens)
- The initial welcome screen is the only one that needs to do retranslation.
  (clumens)
- Remove the generic retranslate method from the python portion of the UI.
  (clumens)
- Do not allow manipulating protected devices in the reclaim dialog (#882147).
  (clumens)
- ISOImage needs to look at /run/install/source for the mounted image
  (#879142). (clumens)
- Minor TODO list update. (clumens)
- Get rid of the unneeded action1. (clumens)
- Do not list some layouts twice (#882526) (vpodzime)
- Check if the given NTP server is a valid hostname (#865869) (vpodzime)
- Improve and document network.sanityCheckHostname (vpodzime)
- don't write network settings on image install (bcl)

* Sat Dec 01 2012 Brian C. Lane <bcl@redhat.com> - 18.34-1
- remove extra space in custom.py (bcl)

* Fri Nov 30 2012 Brian C. Lane <bcl@redhat.com> - 18.33-1
- Escape single percent signs in RPM changelog entries. (dcantrell)
- Fixes for PkgWrangler review. (dcantrell)
- Don't let defaults override user-specified container settings. (#879702)
  (dlehman)
- Fix partition allocation when enabling container encryption. (#879702)
  (dlehman)
- Remove partitions from all appropriate DiskLabel instances. (#870586)
  (dlehman)
- Add a way for users to set the names of lvm and md devices. (dlehman)
- Update the RAID-specific UI after changing the device's disk set. (dlehman)
- Correctly handle the default vg not having been instantiated yet. (dlehman)
- Drop requested container disks that don't have enough space. (#873293)
  (dlehman)
- Don't allow LVM disk set selection via configure button. (dlehman)
- Try to add new device to an existing container if disks are full. (dlehman)
- Fix code to lock encryption checkbutton for LV in existing VG (#877871)
  (dlehman)
- Add support for changing a new LV's VG. (dlehman)
- Fix check for in-use LV name to include VG name. (#875477) (dlehman)
- Remove the automatic show_all from those info_bar related functions.
  (clumens)
- Add set_info, set_error, set_warning functions to the BaseWindow object.
  (clumens)
- set_info functions may not be called from outside the main thread (#873600).
  (clumens)
- Test if path is valid before using it (NTPConfigDialog) (vpodzime)

* Wed Nov 28 2012 Brian C. Lane <bcl@redhat.com> - 18.32-1
- Bootloader checking should work in terms of self.stage1/2_ attrs (#880277).
  (clumens)
- Catch OverflowError in manual partitioning. (sbueno+anaconda)
- Do not accept tabs in the keyboard layout test box (#897312). (clumens)
- Wait for slower dhcp for payload setup and hostname setting (#873468)
  (rvykydal)

* Mon Nov 26 2012 Brian C. Lane <bcl@redhat.com> - 18.31-1
- Rename icons for liveinst (conflict with redhat-logos) (#878037) (rvykydal)
- Rework actions in the resize dialog to avoid shortcomings (#866209, #867770).
  (clumens)
- Check that everything's a GDK window before attempting to manipulate it.
  (clumens)
- On live installs, the progress hub should have a Quit button (#854904).
  (clumens)
- If no bootloader is to be installed, pop up a warning. (clumens)
- Escape ampersands in spoke status text. (clumens)
- Allow not setting any boot device via the UI (#867469). (clumens)
- Allow specifying whether the URL you've given is a mirrorlist or not
  (#868558). (clumens)
- Prevent false positives when checking for encryption change. (dlehman)
- Don't add incomplete VGs to the LVM reject filter. (#878225) (dlehman)
- Show device names for devices in the Unknown page/subsection. (#855646)
  (dlehman)
- Add a page to the custom RHS notebook for uneditable devices. (#875942)
  (dlehman)
- Fix error in iutil.execCapture when fatal and non-zero exit (stefw)
- Allow iutil.execWithCapture to work without a chroot (stefw)
- Handle hd iso leavings by dracut (#876897) (jkeating)
- show error when rsync fails (#868755) (bcl)

* Mon Nov 19 2012 Brian C. Lane <bcl@redhat.com> - 18.30-1
- only raise rsync error on error 12 (#868755) (bcl)
- Dump default auto connection's ifcfg file instead of writing a new one
  (#870922) (rvykydal)
- Number timezones starting with 1 (#859342) (msivak)
- only call bootloader.check() if bootloader is setup (#875278) (bcl)
- Fix operator precedence when checking for the presence of transifex-client.
  (clumens)
- Make the custom and keyboard toolbar buttons larger (mizmo). (clumens)
- More changes to leave the spoke via a glib idle call, not calling directly.
  (clumens)
- Hide the custom addon button. (clumens)
- Enable verbose yum logging once more (jkeating)
- rm transifex-client buildreq; check and install only if needed (sbueno)
- Handle nfsiso leavings by dracut (#876223) (jkeating)
- Prevent some raid-related tracebacks. (#874034) (dlehman)
- Don't try to save changes to a locked luks device. (#876180) (dlehman)
- Keyboard test layout padding fix (mizmo). (clumens)
- Correct colors for selected items in mountpoint selector widget (mizmo).
  (clumens)
- Include hidden disks in the storage spoke's list of devices (#875475).
  (clumens)
- Make the DetailedErrorDialog taller by default (#874620). (clumens)
- If there's only a Quit button, don't make it secondary. (clumens)
- Handle package dependency errors on kickstart installs too (#865073).
  (clumens)
- Remove iso-codes dependency, libxklavier has it fixed now (vpodzime)
- Rework custom partitioning alignment too (mizmo). (clumens)
- Attempt to fix the shrunken storage UI (mizmo). (clumens)
- Do not allow TreeView search in AddLayout dialog (#876131) (vpodzime)
- DiskOverview widget selection color correction (mizmo). (clumens)
- Use the main loop to control displaying the resize dialog. (clumens)
- Use ksdata to set default runlevel (jkeating)
- Execute xconfig data (#874868) (jkeating)
- Write out xconfig data when executed (jkeating)
- Code cleanups (jkeating)
- Link to the correct default target (jkeating)
- Add a mapping of old run level to new systemd target (jkeating)

* Mon Nov 12 2012 Brian C. Lane <bcl@redhat.com> - 18.29-1
- Quit after handling transaction errors. (clumens)
- Add a function to display relevant transaction errors (#873106). (clumens)
- Don't decorate error dialogs. (clumens)
- Fix error handling when new device ends up with size 0. (dlehman)
- Explicitly request all free space when no size given in custom. (#872833)
  (dlehman)
- Disable the language spoke off the first hub, for now (#874263). (clumens)
- Wrap text on install options dialogs (#874265). (clumens)
- Encode unicode strings from XklWrapper (#873762) (vpodzime)
- New version (out of order) (bcl)
- Network spoke: fix traceback (number of callback parameters) (#875393)
  (rvykydal)
- Adjust right margin for MountpointSelector (mizmo). (clumens)
- Fix introspection warnings for widgets (stefw)

* Fri Nov 09 2012 Brian C. Lane <bcl@redhat.com> - 18.28-1
- Show NFS as the source if dracut left it for us (#875235) (jkeating)
- Convert the accordion Button to a LinkButton (mizmo). (clumens)
- Buttons shouldn't scream at people (#868536, mizmo). (clumens)
- Don't attempt to handle exceptions when NFS mounts fail. (clumens)
- If there's an error setting up the source, display it as the status.
  (clumens)
- Add logging around the messages that can be processed by the hub. (clumens)
- You can't reformat a btrfs volume/subvolume. (dlehman)
- Always account for device removals in their containers. (dlehman)
- Fix container member management for md devices. (dlehman)
- Use a more robust method for removing previous autopart. (#868589) (dlehman)
- Post-custom sanity check determines storage spoke completeness. (#868925)
  (dlehman)
- Fix detection of inactive md arrays. (#873031) (dlehman)
- Vastly simplify the process for applying changes from custom spoke. (dlehman)
- Clean up container disk set and encryption change handling. (#874714)
  (dlehman)
- Honor kickstart bootloader --location=none. (#871143) (dlehman)
- Use original raid level and disk set when reverting a device. (dlehman)
- Set raid level based on defined volume for not-yet-btrfs mounts. (dlehman)
- Network spoke: improve status info (shorten) (rvykydal)
- Network spoke: update list of connected devices in hub status (rvykydal)
- Network spoke: Add "Connecting..." state to status (#868704) (rvykydal)
- Network spoke: Update status of networking in hub (#868704) (rvykydal)
- check for small grub2 embed space (#737508) (bcl)
- Set SpokeSelector's tooltip to spoke's status (vpodzime)
- Don't let mount/umount block python threads (#873600). (clumens)
- Fix makeupdates to correctly detect and include changes in isys. (clumens)
- Update pot file with proper lower cased buttons (#868536, mizmo). (clumens)
- Default to LVM on text installs too (#874586). (clumens)
- Remove network enablement in anaconda from rescue mode (#873854) (rvykydal)
- Add very basic U-Boot support for ARM platforms (dmarlin)
- Fix test for changed disk set for partitions. (#873994) (dlehman)
- Add support for preexisting whole-disk formatting. (#870476) (dlehman)
- There is no Storage.destroyFormat method. (dlehman)
- Move DEVICE_TYPE constants into storage and use them everywhere. (dlehman)
- A device scheduled for reformat is not unused. (dlehman)
- Catch the right exception when settin up raid options ui. (#873486) (dlehman)
- Network spoke: Use connection state that triggered a callback (bug #871429)
  (rvykydal)
- Use sr_Latn_RS instead of sr_RS (vpodzime)

* Wed Nov 07 2012 Brian C. Lane <bcl@redhat.com> - 18.27-1
- Mark more UI strings with N_ (#874276). (clumens)
- Pressing Enter on the passphrase dialog should continue (#788556). (clumens)
- Pressing Enter should activate the rightmost button on the detailed dialog.
  (clumens)
- Pressing enter on a MountpointSelector should display it on the RHS
  (#873352). (clumens)
- Make language groups work again (#873865) (jkeating)
- Update payload if slower dhcp succeeds in network pre-hub spoke (#873468)
  (rvykydal)
- Fix group access after parsing btrfs subvol list output. (#868468) (dlehman)
- Account for autopart swap size when checking free space. (dlehman)
- ignoredisk.onlyuse contains names, not StorageDevice instances. (#873463)
  (dlehman)
- Correctly handle toggle of encryption state for devices. (#873445) (dlehman)
- Handle changes to encryption state of container members. (#873445) (dlehman)
- Change custom spoke to apply encryption to PVs, not LVs. (dlehman)
- Widen the sidebar on custom partitioning (mizmo). (clumens)
- Fix spacing and padding on SpokeSelectors (mizmo). (clumens)
- Set the font globally (mizmo). (clumens)
- Handle if we get something other than a .treeinfo file (#872012). (clumens)
- If repo metadata fetching fails, set an info error message (#873605).
  (clumens)
- Enable yum langpacks plugin to get conditional packages (#868869) (jkeating)
- Base whether an add-on is selected on the selectedGroups, not ksdata
  (#873092). (clumens)
- Add UTC and GMT-X timezones (#863199) (vpodzime)
- TimezoneMap should handle "" timezone (vpodzime)
- raise error on rsync failure (#868755) (bcl)
- exclude bind mounts from rsync (#871637) (bcl)
- Fix up the InstallOptions3Dialog.refresh arguments (#873392). (clumens)
- Mark strings at the top of spokes with N_; translate later with _ (#872791).
  (clumens)
- Do not decorate the dialog that appears when you click on storage info bar.
  (clumens)
- You have to give "raise" an exception if you're outside a handler (#872874).
  (clumens)
- Prompt for encryption passphrase in reclaim path. (#869391) (dlehman)
- Prevent user from hitting save without entering a passphrase. (#869391)
  (dlehman)
- Font and padding updates for the network spoke (mizmo). (clumens)
- Fix alignment on the Add and Configure Mount Point dialogs. (clumens)
- Network spoke: activate wifi connection after setting secrets (#871132)
  (rvykydal)
- Fix nfsiso as stage2 (#871554) (jkeating)
- Fix traceback when saving changes to an existing partition. (#872446)
  (dlehman)
- Some more stuff for the mangleMap (#866730) (vpodzime)
- Handle locale's encoding and script in a better way (vpodzime)
- Use both language and country to guess layout (#861061) (vpodzime)
- Fix remaining issues with md fwraid. (#872739) (dlehman)
- Do not return None from Size.__str__ (#869405) (vpodzime)
- Add a platform weight for ARM images (dmarlin)
- Remove a bunch of stuff from the TODO list. (clumens)
- Don't decorate the main exception window. (clumens)
- Move the custom partitioning's Apply Changes button. (clumens)
- Indent partition type options under the expander further. (clumens)
- Left align the Label label, and indent the custom options further. (clumens)
- Lots of custom partitioning UI changes (mizmo). (clumens)
- Update fonts on the welcome language spoke (rlerch). (clumens)
- Lots of storage spoke font and spacing changes (mizmo). (clumens)
- Set the background of the custom partitioning accordion back to white
  (mizmo). (clumens)
- Set the Local Standard Disks background back to white (mizmo). (clumens)
- Reorder Device Type options in custom part to match the Partition Type combo.
  (clumens)
- Use the same terminology for partitions as is in use on the custom spoke.
  (clumens)
- livecd specific code has moved (bcl)
- Add progress percentage info to liveinst (bcl)

* Thu Nov 01 2012 Brian C. Lane <bcl@redhat.com> - 18.23-1
- Update parsing of 'btrfs subvol list' to match its new output. (#868468)
  (dlehman)
- Add a way to select the default device type. (dlehman)
- Enable specification of disk(s) for individual mountpoints. (#870569)
  (dlehman)
- Improve management of complex devices in custom spoke. (#865199) (dlehman)
- Save btrfs subvols' requested size. (dlehman)
- Reclaim extra set member growth evenly across members. (dlehman)
- Give lvmpv a slightly more realistic minimum size. (dlehman)
- Fix required space calculation for lvm. (dlehman)
- Don't filter disks when scanning storage after autopart fails. (#866717)
  (dlehman)
- Fix detection of partitioned md devices. (#866519) (dlehman)
- Correct handling of disks with hidden formats. (#866519) (dlehman)
- Revert "Fall back to lvm autopart if the default fails." (dlehman)
- Revert the default autopart type to lvm. (#870207) (dlehman)
- Apparently necessary kpartx changes (#867593) (dlehman)
- Mark a few more important strings for translation. (clumens)
- If lang= was provided on the command line, set the installation language.
  (clumens)
- Make the decision to skip the welcome screen more complicated. (clumens)
- Set a translation domain before loading a glade file. (clumens)
- Don't decorate the NTP config dialog. (clumens)
- Mark properties in existing glade files as translatable. (clumens)
- Widget properties exposed via glade need to be marked as translatable.
  (clumens)
- Network spoke: don't try to call replace on None (traceback) (#869106)
  (rvykydal)
- Fix nfsiso repo selection (#871648) (jkeating)

* Wed Oct 31 2012 Brian C. Lane <bcl@redhat.com> - 18.22-1
- Revert "Update parsing of 'btrfs subvol list' to match its new output.
  (#868468)" (dlehman)
- Pass RAID level to btrfs volume constructor. (#866101) (dlehman)
- Fix a traceback when removing non-existing partitions in custom. (#869839)
  (dlehman)
- Update parsing of 'btrfs subvol list' to match its new output. (#868468)
  (dlehman)
- Remove the word "review" from the label on the custom checkbutton. (#871109)
  (dlehman)
- Require that the root filesystem be created by anaconda. (#871104) (dlehman)
- On error, reset the RHS to what it used to be (#869422). (clumens)
- Don't prompt when in cmdline mode (#869685) (jkeating)
- Force a root password to be set (#869675) (jkeating)
- Network spoke: fix hostname handling in standalone spoke (#868535) (rvykydal)
- Network spoke: fix config info update after switching device OFF and ON
  (#871429) (rvykydal)
- Network spoke: connected requires activated (not active) connection (#871129)
  (rvykydal)
- Blank out passphrases from /root/anaconda-ks.cfg (#868519). (clumens)
- Setup package repo in the background (#870552) (jkeating)
- check disklabels when calculating free space (#863892) (bcl)
- updateBaseRepo does not need a storage argument. (clumens)
- Fix up calling superclass setup methods in packaging (#870556). (clumens)
- Fix a race condition with kickstarts (#868834) (jkeating)
- run checkisomd5 from anaconda-diskroot (#848764) (bcl)
- skip luks passphrase in exception dump (#868509) (bcl)
- Replace ' ' with '_' when looking for ifcfg files (#869106) (rvykydal)
- Remove storageComplete, which was only called from dispatch.py. (clumens)
- Remove dispatch.py and its associated test case. (clumens)
- Use a slightly different method to get supported languages (#858801, tagoh).
  (clumens)
- Fix problems when changing things in the software spoke (#868742, #869424).
  (clumens)
- Network spoke: fix callback arguments for device add/remove. (rvykydal)
- display storage errors in text mode storage spoke (bcl)
- only clear errors if re-running the check (#868707) (bcl)
- set boot flag and name for EFI partition (#866106) (bcl)
- clear pmbr_boot on EFI systems (#844551) (bcl)
- Lots of UI layout tweaks (mizmo). (clumens)
- /etc/sysconfig/keyboard doesn't support vconsole.xyz options. (notting)

* Thu Oct 25 2012 Brian C. Lane <bcl@redhat.com> - 18.21-1
- Add PowerNV as a recognized PPC platform (nacc)
- anaconda should print unknown platform information (hamzy)
- Toggle chosen property on focus change (MountpointSelector) (vpodzime)
- Lock source spoke while depsolving (#867591) (jkeating)
- In custom part, don't display mountpoints without associated disks (#865942).
  (clumens)
- Tie "Reclaim Space" button sensitivity to how much space the user freed
  (#869375). (clumens)

* Tue Oct 23 2012 Brian C. Lane <bcl@redhat.com> - 18.20-1
- Add dialog for configuring layout switching options (vpodzime)
- Initialize layout switching if needed (vpodzime)
- Save layout switching configuration (vpodzime)
- Add support for layout switching options to XklWrapper (vpodzime)
- We need to set _root in two places for a MountpointSelector. (clumens)
- Correctly destroy the deletion confirmation dialog. (clumens)
- Don't set self.data.method.url until after checking for a protocol (#869102).
  (clumens)
- Fix an undetected bug when setting up an HTTPS method. (clumens)
- YabootSILOBase objects don't have an encrypted_password parameter (#869016).
  (clumens)
- rprivate -> make-rprivate (#869246). (clumens)
- If NFS is selected in the source spoke, the URL must contain a colon
  (#869103). (clumens)
- Modify behavior when leaving the reclaim storage dialog (#864128, #867770,
  #868903). (clumens)
- Set the status text in the SpokeSelector widget differently now. (clumens)
- Use the correct font for each language on the welcome screen (#868836,
  tagoh). (clumens)
- Everywhere we make a MountpointSelector, give it a _root attr (#868702).
  (clumens)
- payloadInstallHandler should only optionally take a package argument
  (#868542). (clumens)
- Add a reformat checkbutton to indicate a desire to reformat the device.
  (dlehman)

* Fri Oct 19 2012 Brian C. Lane <bcl@redhat.com> - 18.19-1
- Reset the comps to empty along with everything else in yum. (clumens)
- Hook up the "Remove Packages" button on the dep solving error screen.
  (clumens)
- If nothing's changed in the software spoke, don't redo dep solving. (clumens)
- skip vnc prompt with text mode and kickstart (bcl)
- Use correct name for MD RAID device description text. (dlehman)
- Fix selector management after a reformat action is scheduled. (dlehman)
- Aqcuire yum lock before doing the work of _yumCacheDirHack. (#858993)
  (dlehman)
- Reset error list on success of doKickstartStorage. (dlehman)
- Tighten up management of passphrases across Storage resets. (#865364)
  (dlehman)
- Do not count not-yet-created filesystems as free space. (#866895) (dlehman)
- Remove any preexisting autopart layout before space check. (#866895)
  (dlehman)
- Apply disk selections to the devicetree before the space check. (#866895)
  (dlehman)
- Update free space totals before refresh after removing a device. (dlehman)
- Log exceptions raised from PartitionDevice constructor. (dlehman)
- Fix size specs for PartitionFactory. (dlehman)
- Reinitialize disks after removing the last partition from custom spoke.
  (dlehman)
- Refactor shouldClear slightly. (dlehman)
- Use correct means for getting device type in the custom spoke. (dlehman)
- Repopulate the RHS after editing a device. (dlehman)
- Don't bother resizing a container that has just been emptied. (dlehman)
- Don't allow implicit fstype change via mountpoint. (#866953) (dlehman)
- Set up devices before trying to decrypt them. (#865247, #867533) (dlehman)
- Don't short-circuit devicetree populate based on clearpart setting. (dlehman)
- Keep hostname when updating ksdata after GUI network configuration (#866516)
  (rvykydal)
- don't save system time on s390 (#867856) (dan)
- Network spoke: make Configure button insensitive when running nmce (#865931)
  (rvykydal)

* Wed Oct 17 2012 Brian C. Lane <bcl@redhat.com> - 18.18-1
- remove firewall.py from POTFILES.in (bcl)
- Add missing pieces for kickstart's encryption cipher option. (dlehman)
- update to use firewalld (#815540) (bcl)
- Fix a typo in method name (#863765) (msivak)
- Add missing import (#867296) (msivak)
- There is no anaconda object available in writeSysconfigKernel (vpodzime)

* Tue Oct 16 2012 Brian C. Lane <bcl@redhat.com> - 18.17-1
- Add an error handler for fatal package installation errors (#865291).
  (clumens)
- Modify the status test for the software selection spoke. (clumens)
- Various layout and font improvements to the keyboard spoke (mizmo, rlerch).
  (clumens)
- Just return the size string uppercased (#867074). (clumens)
- Revert "Use a capital "B" in the size module (#859932)." (clumens)
- Revert "Fix one more reference to bits (#859932)." (clumens)
- Fix padding around the addons view in the software spoke. (clumens)
- The Unknown page selectors/devices have no root. (dlehman)
- Avoid using mount --move on shared paths (#853508) (jkeating)
- Revert "Release Gdk lock in exception handling" (msivak)
- Make all Gtk calls from inside of it's main loop (and thread) (msivak)
- Remove Gdk thread initialization, introduce new helper functions and make
  exception handler be called by Gtk only once (msivak)
- Fix threading initialization (msivak)
- Do not remove the layout if it was added back (#865830) (vpodzime)
- Release Gdk lock in exception handling (vpodzime)
- Configure new-kernel-pkg to keep tboot configuration on updates (#742885)
  (pjones)
- Honor the nompath option. (dlehman)
- Validate lv names. (dlehman)
- Add support for specifying encryption cipher mode via kickstart. (dlehman)
- Acquire the yum lock before accessing YumBase.repos. (#858993) (dlehman)
- Remove the entry on the resize dialog's combo boxes. (clumens)
- disks_free -> disks_size (#863647). (clumens)
- Fix one more reference to bits (#859932). (clumens)
- Fix a traceback in media check (#865897). (clumens)
- Add support for deleting an entire root via the existing ConfirmDeleteDialog.
  (clumens)
- Don't traceback when removing a mountpoint with no expanded selector
  (#862746). (clumens)
- Remove the code for removing an entire Root all at once. (clumens)
- Yet more TODO list updates. (clumens)
- Don't display "None" in the name of a root. (clumens)
- Fix configuration of protected wireless connections (#855526) (rvykydal)
- Fix graphical kickstart with %%packages data (jkeating)
- Add password validation to text password spoke (jkeating)
- Make use of the validatePassword routine from users.py (jkeating)
- Add a password verification method to users.py (jkeating)
- Always honor the 'nokill' flag (vpodzime)
- Fall back to lvm autopart if the default fails. (#864708) (dlehman)
- Special boot devices are handled the same whether they exist or not.
  (dlehman)
- Fix a bug allocating fixed-size partitions. (dlehman)
- Clean up size sets immediately after allocation run. (#864771) (dlehman)
- Make sure partition base sizes are adequate for their formatting. (dlehman)
- Don't fail to account for all set members' growth. (dlehman)
- Remove some extra calls to show_first_mountpoint. (dlehman)
- Show the correct raid options for btrfs. (dlehman)
- Support change of raid level in custom spoke. (dlehman)
- Use devicetree as partition list source instead of parted. (#864718)
  (dlehman)
- Use Storage convenience methods to schedule reclaim actions. (dlehman)
- Pass disk list when trying to recover from device type change failure.
  (dlehman)
- Fill in missing parts of the disabled raid features dict. (dlehman)
- Clear errors when entering or leaving the custom spoke. (dlehman)
- Hook up signal handler for raid feature checkbuttons. (dlehman)
- Raise MDRaidError instead of ValueError from devicelibs.mdraid. (dlehman)
- Minimum we have to do with HW clock (vpodzime)
- Check X layouts specified in kickstart for validity (vpodzime)
- Work with VConsole keymap and X layouts separately (vpodzime)
- Add class wrapping systemd-localed functionality (vpodzime)
- Don't write XkbVariants if none are specified (vpodzime)
- Add comment to the begining of generated xorg.conf file (vpodzime)
- Don't display "None" for NIC vendors and products NM can't identify (#859540)
  (rvykydal)

* Thu Oct 11 2012 Brian C. Lane <bcl@redhat.com> - 18.16-1
- Don't try to load ifcfg files for wifi devices (#865355) (vpodzime)
- Rewrite isWirelessDevice to Python and DBus calls (#862801) (vpodzime)
- Use a capital "B" in the size module (#859932). (clumens)
- The environment window needs a vertical scroll bar (#865066). (clumens)
- liveinst should recognize inst.updates too (#865398). (clumens)
- Improve validation of device edit requests. (dlehman)
- Fix listing of subvolumes for existing btrfs volumes. (dlehman)
- Remove overzealous correction of device type for /boot*. (#863574) (dlehman)
- Pad filesystem minimum sizes to ensure other OS can still run. (dlehman)
- Handle encrypted partitions in size set classes. (dlehman)
- Don't set mountpoints of "(null)" in mountpoint selectors. (dlehman)
- Prevent crash trying to populate raid options on a one-disk system. (dlehman)
- Rework type combos and don't offer RAID on one-disk systems. (dlehman)
- Bundle more of data/ in updates.img (jkeating)
- Revive reipl (#860244) (jkeating)

* Wed Oct 10 2012 Brian C. Lane <bcl@redhat.com> - 18.15-1
- add noverifyssl to anaconda-dracut (#852229) (bcl)
- Don't crash when running anaconda a second time (jkeating)
- Handle ssh prompt in new tmux world (jkeating)
- Add a service to run anaconda directly on the tty (jkeating)
- Add a script to attach to anaconda's tmux (jkeating)
- Add ARM-OMAP class to create a uboot partition to support the boot-loader.
  (dmarlin)
- Avoid a loop of storage spoke executions during kickstart (#865048).
  (clumens)
- Correct lookup of raid.XX "mountpoints" for kickstart installs (#864764).
  (clumens)
- Change language matching on the welcome screen back around. (clumens)
- Another attempt at fixing the squished screen bug (#849211). (clumens)
- Fix a stupid typo in the disk shopping cart (#864842). (clumens)
- Reorder the buttons and labels on the bottom left of the storage spoke.
  (clumens)
- Modify the DetailedErrorDialog buttons. (clumens)
- Sync up hidden/unhidden disks between the UI and storage module (#864180).
  (clumens)
- When handling a storage error, reload self.disks (#862972). (clumens)
- Fix sshd bringup when also using a kickstart file (#863441) (jkeating)
- Require root password spoke be visited (#859069) (jkeating)
- add some thread logging (bcl)
- Reword the description on the resize dialog (#863577). (clumens)
- Present an error message if no disks are detected (#864093). (clumens)
- When changing environments, don't explicitly exclude groups (#863886).
  (clumens)
- Fix marking the "Modify Software Selection" button as sensitive in one case.
  (clumens)

* Mon Oct 08 2012 Brian C. Lane <bcl@redhat.com> - 18.14-1
- Add UI support for encrypted automatic partitioning. (dlehman)
- Add support to the custom spoke for encrypted block devices. (dlehman)
- Add a page for decrypting existing LUKS devices. (dlehman)
- Add a dialog for collecting a passphrase for newly encrypted devices.
  (dlehman)
- Add a property that provides a list of all selectors in the accordion.
  (dlehman)
- Handle luks formats during populate if they have a passphrase set. (dlehman)
- Add encryption support to the device factory classes. (dlehman)
- s/dev/disk in the disk shopping cart. (clumens)
- Set a default payload in InstallOptions1Dialog (#863582). (clumens)
- Pass disks into the SelectedDisksDialog (#863588). (clumens)

* Fri Oct 05 2012 Chris Lumens <clumens@redhat.com> - 18.13-1
- Make sure packages anaconda requires are installed. (clumens)
- Add method returning current activated X layout (vpodzime)
- Fix a deadlock when trying to add a keyboard layout (#862612). (clumens)
- ntfsresize uses SI (MB) while the rest of us use IEC (MiB). (#862109)
  (dlehman)
- Remove empty extended partitions after removing a logical partition.
  (dlehman)
- Handle all logical/extended partitions in unusedDevices. (dlehman)
- Update autopart/custom setting before moving to reclaim dialog. (#863225)
  (dlehman)
- Raise an exception early in newDevice if no disks were specified. (#858139)
  (dlehman)
- Fix a regression in BTRFSVolumeDevice.listSubVolumes. (#862742) (dlehman)
- Fix behavior of resolveDevice when devspec is a device name. (dlehman)
- Prevent BTRFS volumes from ever having the name None. (dlehman)
- Prevent negative free value for filesystems. (#861812) (dlehman)
- Don't show extended partitions that contain logical partitions. (#862971)
  (dlehman)
- Delete ts data instead of trying to undo dep installs. (#851114) (dlehman)
- Change the manglings for a couple locales (petersen). (clumens)
- Hook up the "Modify Software Selection" button on install opts dialogs.
  (clumens)
- More TODO list updates. (clumens)
- Add a label to the resize dialog for how much space is required. (clumens)
- Add a column to the disk shopping cart for setting the boot device (#860430).
  (clumens)
- Rework the disk shopping cart link a little bit. (clumens)
- Do not use constant value in SoftwareSpoke's completed property (vpodzime)
- Pull in existing swaps and bootloader devices whenever there are mounts.
  (dlehman)
- Revert broken logic for newly formatted devices in unusedDevices. (dlehman)
- Add an apply button to the device/mountpoint configuration options. (dlehman)
- Don't base StorageSpoke.ready on storage execute thread presence. (#861574)
  (dlehman)
- Prevent systemd timeout waiting for encryption passphrase. (#861123)
  (dlehman)
- Fix traceback when switching device type to lvm. (#860990) (dlehman)
- Fix error handling in the add mountpoint dialog. (#860992) (dlehman)
- Allow xfs /boot. (dlehman)
- Fix makeupdates to work for glade files in subdirs of spokes/ or hubs/.
  (dlehman)
- Fix parsing of NFS method strings (#860966) (jkeating)
- Make the URL entry sensitive for NFS installs, too (#863014). (clumens)
- Add in a locale mapping to avoid incorrect system settings (#858591).
  (clumens)

* Wed Oct 03 2012 Brian C. Lane <bcl@redhat.com> - 18.12-1
- copy-logs changed names (bcl)
- Reference correct UI button name (#862409) (jkeating)
- Don't echo vnc password to the screen (#862593) (jkeating)
- Make the log copy script the last one to run (jkeating)
- Copy ks script logs into the install root as well (jkeating)
- Create ks script logs outside of chroot (jkeating)
- Don't look for ifcfgs of wireless devices (#860791) (rvykydal)
- doAutoPartition should raise errors instead of handle them. (clumens)
- In the install options dialogs, call out how much space is on selected disks.
  (clumens)
- In order to display the resize prompt dialog, we need to compare Sizes to
  Sizes. (clumens)
- Use a better starting value for required space than 0. (clumens)
- Default to CLEARPART_TYPE_NONE (#855976). (clumens)
- Remove some unused clearpart-related settings. (clumens)
- Hook up the new resize dialog. (clumens)
- Add a resize dialog. (clumens)
- Require the hostname package (#862419) (jkeating)

* Tue Oct 02 2012 Chris Lumens <clumens@redhat.com> - 18.11-1
- Use gdk_threaded() when running AddLayout dialog (vpodzime)
- Work the anaconda object into the VNC test (jkeating)
- Use askvnc spoke to change vnc password (jkeating)
- Fix logic error in vnc password length check (jkeating)
- Allow vncpassword spoke text to be configurable (jkeating)
- Don't ask for VNC if we can't do it (jkeating)
- Skip VNC prompt if text is requested in kickstart (jkeating)
- KEYTABLE is now vconsole.keymap (#859298) (bcl)
- The partitionErrorHandler text needs a 's' in the format string (#861376).
  (clumens)
- Fix a problem with storage error handling (#861376). (clumens)
- Fix bootloader setup on s390. (#857940) (dlehman)
- Make Keboard and Welcome spokes runtime-system friendly (vpodzime)
- Make DateTime spoke runtime-system friendly (vpodzime)
- Add a guard for testing if we can modify runtime system (vpodzime)
- Bring back prompt for VNC (jkeating)
- Add standalone spoke to prompt for VNC (jkeating)
- Fail on incomplete ksdata when in cmdline mode (jkeating)
- Add a flag attribute to handle cmdline mode (jkeating)
- fix libuser setup (#855481) (bcl)
- Remove obsolete requirement on comps-extras. (notting)

* Wed Sep 26 2012 Chris Lumens <clumens@redhat.com> - 18.10-1
- isys.mount needs to be told when something should be mounted NFS (#860273).
  (clumens)
- Disks with new disklabels don't count as new devices in custom. (dlehman)
- Fix thread synchronization issue going from storage to custom. (#860495)
  (dlehman)
- Treat disks with unrecognized or no formatting as empty. (#858862) (dlehman)
- Improve management of mountpoint selectors in the custom spoke. (dlehman)
- Improve handling of existing devices when refreshing the custom spoke.
  (dlehman)
- Apply custom changes not involving actions to the main devicetree. (dlehman)
- Add a mountpoint entry to the device options area. (dlehman)
- Move mountpoint validation out of the add mountpoint dialog. (dlehman)
- Only run the storage sanity check if we've run autopart. (dlehman)
- Add a method to reset a device to its original state. (dlehman)
- Make a copy of the original format instead of just storing another ref.
  (dlehman)
- Reformatting effectively removes a device from an existing Root. (dlehman)
- Fix test for whether to create biosboot during autopart. (#853628) (dlehman)
- Close AddLayout dialog on double-click (vpodzime)
- Remove useless handler of Cancel button (AddLayout dialog) (vpodzime)
- Don't rely on having some month and year selected (#859185) (vpodzime)
- Add debug option to bumpver (bcl)
- Raise an error if bootDrive is invalid (jkeating)
- Handle automated installs (jkeating)
- Handle errors from text storage execute (jkeating)
- Fix ready and completed properties for text storage (jkeating)
- Use ksdata to determine text password completeness (jkeating)

* Tue Sep 25 2012 Chris Lumens <clumens@redhat.com> - 18.9-1
- And remove compssort.py from POTFILES.in, too. (clumens)
- Select a default environment (#858180). (clumens)
- Remove compssort.py. (clumens)
- Don't attempt to catch and re-raise a SystemError from AnacondaThread.run.
  (clumens)
- Add a progress message for quitting the installer. (clumens)
- GUI error handling dialogs need to be protected from threading deadlocks.
  (clumens)
- Initialize gdk threading as well. (clumens)
- Handle --ignoremissing in _applyYumSelections (#859021). (clumens)
- Fix the destination path for anaconda.xlog (#860041). (clumens)
- Hide the ISO install source if you've nuked all possible drives (#858088).
  (clumens)
- Don't write out /etc/sysconfig/clock anymore (#859217). (clumens)
- Index the exn mapping by string, not by object. (clumens)
- Don't write HOSTNAME=HOSTNAME=myhostnamehere (#859141). (clumens)
- Close temp file before moving it (#858681) (vpodzime)
- Update widget-specific TODO list. (clumens)
- Don't use grey for the status text of a SpokeSelector (#855638). (clumens)
- Fix a typo in makeupdates. (clumens)
- UEFI paths must include a leading backslash on some machines. (#856938)
  (pjones)
- Read cmdline files from /run/install (jkeating)
- Copy command line files prior to pivot (jkeating)
- Grab the proxy username from the correct text entry (#858536). (clumens)
- Remove our use of scsi_wait_scan (#858393). (clumens)
- Don't overwrite the opts attribute on NFS installs (#858700). (clumens)
- Change the keyboard shortcut for the updates checkbox. (clumens)
- Add the storage category to POTFILES.in. (clumens)
- Don't explicitly start the progress spinner in python code. (clumens)
- Move the progress bar back down to the bottom of the progress hub. (clumens)
- Remove a bunch of stuff from the TODO list for a change. (clumens)
- Move check of new partition size against format limits. (dlehman)
- Improve growth check when deciding where to allocate new partitions.
  (dlehman)
- Keep btrfs selectors' sizes in sync as volume size changes. (dlehman)
- Allow specification of a label for new swap space via custom ui. (dlehman)
- Don't allow stage2 as stage1 unless specified via location. (dlehman)
- Remove reference to PartitioningWarning, which was removed last week
  (#875931). (clumens)
- Add a way to test exception handling (vpodzime)
- Fix dumpState to work with the new python-meh (#856235) (vpodzime)

* Fri Sep 14 2012 Chris Lumens <clumens@redhat.com> - 18.8-1
- Make sure the InstallOptionsNDialogs get the correct space labels. (clumens)
- Get rid of the big pause going from the storage spoke back to the hub.
  (clumens)
- Don't fail when making updates if the symlink already exists. (clumens)
- Make sure to set the default TZ in ksdata so the completed method works.
  (clumens)
- Allow creation of biosboot and prepboot partitions in the custom spoke.
  (dlehman)
- Hide removable disks containing install media from the custom spoke.
  (dlehman)
- Make the minimum size for custom spoke partitions 1MB. (dlehman)
- The return value of execWithRedirect is an integer. (dlehman)
- Only include following free space in partitions' max size. (dlehman)
- Handle btrfs volumes with a dataLevel of None. (dlehman)
- Handle newDevice partitions smaller than the default of 500MB. (#853125)
  (dlehman)
- Add underlines to the expander and encryption checkbox in custom
  partitioning. (clumens)
- Remember to mark an environment as selected in the store. (clumens)
- Rename the addon/environment store columns to make sense. (clumens)
- Use slightly less confusing labels for the various back buttons. (clumens)
- Add a property to SpokeWindow for setting the single button's label.
  (clumens)
- Rename the SpokeWindow's back button to just button. (clumens)
- Use the blocking read to avoid busy wait in TUI progress (msivak)
- Make progress hub spokes possible and move the root password there (msivak)
- Don't let user hit Add button if no new layouts are selected (vpodzime)
- Gtk.ListStore.iter_previous now returns new iterator (#849060) (vpodzime)
- Write storage configs after payload install for live installs. (#856836)
  (dlehman)
- Update the pot file for various important string changes. (clumens)
- Attempt to fix word wrapping issues with the betanag dialog (#853913).
  (clumens)
- CONTINUE -> BEGIN INSTALLATION (#856614). (clumens)
- Language selection should work the same as keyboard selection (#854570).
  (clumens)
- Fix ransom notes cycling. (clumens)
- Improve the clarity of the custom checkbutton label. (dlehman)
- Add error handling around significant ui-initiated storage operations.
  (dlehman)
- Improve error granularity slightly in automatic partitioning. (dlehman)
- Fix detection of preexisting md arrays again. (dlehman)
- Handle changes to sizes of predefined devices in custom spoke. (dlehman)
- Fix traceback when switching device type to BTRFS. (dlehman)
- Validate mountpoints in the add-a-mountpoint dialog. (dlehman)
- Tell 'lvm' that yes, we really, really want to remove PV (vpodzime)
- Use 250ms interval for installation progress updating (vpodzime)
- network spoke: hide for live CD and image installs (#854586) (rvykydal)
- Fixed luks_add_key() (jsafrane)
- Display a radio button next to the environment choices. (clumens)
- Update TODO list. (clumens)
- Set the busy spinning cursor while the UI is loading. (clumens)
- network spoke: add "No network devices available" status (rvykydal)
- network spoke: clear device info if no network devices are found (#853903)
  (rvykydal)
- fix root password setup (#855481) (bcl)
- Rewrite expand_langs to return more items (vpodzime)
- Don't try to setup X layouts in text installation (#852447) (vpodzime)
- Add UTF-8 enconding suffix to our language strings (#854688) (vpodzime)
- Require rsync (vpodzime)
- Don't rely on chrony.conf file being available (#854899) (vpodzime)
- Require chrony and rdate, because Anaconda needs them (#854899) (vpodzime)
- Use the real path to dracut-lib.sh (#851362) (jkeating)
- fixup live install (#853988, #854962) (bcl)
- Only check media if we really want it (#853404) (jkeating)
- Fix thinko in anaconda arg handling portion of multilib patch. (dlehman)
- Honor kickstart and command line switches to enable multilib. (dlehman)
- Quitting the live installer shouldn't reboot the system (#854904). (clumens)
- The kickstart language-related command is "lang", not "language". (clumens)
- Fix btrfs/lvm/raid kickstart installs (#853649). (clumens)
- Store "en" as the default, not "en_US". (clumens)
- Mark ksdata.*.execute invocations as another step (vpodzime)
- Reorder and comment options passed to rsync (vpodzime)
- Fix bug in writing keyboard configuration files (vpodzime)
- network spoke: require connection only for url and nfs methods (#853899)
  (rvykydal)
- Drop the addBase handling in anaconda - if you want a group, list a group.
  (notting)
- Don't depend on storage or instClass in EFIGRUB (pjones)
- Use self.stage1_device where appropriate in EFIGRUB. (pjones)
- Explicitly disable the rootpw lock (#853788) (jkeating)
- require nm-connection-editor (#854586) (bcl)
- Include packaging log in exception reports. (dlehman)
- Add Kazakh as a valid translation. (clumens)
- Deselect any existing environment when selecting a new one (#851510).
  (clumens)
- Use chvt command for tty switching (vpodzime)
- Use the disk's serial number instead of index as an ID. (clumens)
- Use the disk's ID for deleting from the shopping cart, not an index
  (#853798). (clumens)
- Use the F18_Partition class (#853593). (clumens)
- Remove anaconda.instLanguage object and language module (vpodzime)
- Remove lang-table and localeinfo.py (vpodzime)
- parse-kickstart: handle 'network --ipv6=auto ...' (wwoods)
- parse-kickstart: set IPV6INIT=yes when using ipv6 (#830434) (wwoods)
- Make TUI password spoke behave the same as it's GUI counterpart (msivak)
- Remove ROOT_PATH/etc/localtime before symlinking timezone (vpodzime)
- Continue post-installation steps even if writing NTP configuration fails
  (vpodzime)
- update transifex.txt for newui (bcl)
- Handle invalid spoke input (#853253) (jkeating)
- Remove unnecessary (and broken) import (#853576) (jkeating)
- Destroy the Add Mountpoint dialog when escape is pressed (#853058). (clumens)
- Keep the current spoke on top of the hub. (clumens)
- And then fix an assortment of non-packaging pylint errors, too. (clumens)
- Fix problems in the packaging module that pylint detected. (clumens)
- Update runpylint to find newui modules correctly. (clumens)
- Prevent duplicate mountpoint creation. (dlehman)
- If there's only one disk, select it by default. (dlehman)
- Evaulate growth potential for all reqs, even when allocating a fixed req.
  (dlehman)
- Do not honor partitions' disk attr when reallocating them. (dlehman)
- Set size is a safe max size for partitions. (dlehman)
- Set the ANACONDA udev property in the post-switchroot udevdb. (dlehman)
- Calculate size func kwargs at call time to pick up changes. (dlehman)
- Add support md devices and btrfs raid features in the custom spoke. (dlehman)
- Move the BTRFS options to last and remove unsupported options. (dlehman)
- Remove "Technology" ComboBoxes from device options for now. (dlehman)
- Tweak setContainerMembers to work with a defined md array. (dlehman)
- Add support for named md devices. (dlehman)
- Make sure a disk is partitioned before treating it as such. (#849707)
  (dlehman)
- Setup python path /after/ we've done updates (jkeating)
- Fix a string substitution think-o (jkeating)
- We now BuildRequires python-babel as well. (clumens)
- Update TODO list. (clumens)
- Only show groups in the UI if they have members that install by default
  (default or manadtory packages). (notting)
- Symlink /run/initramfs/inst.{updates,product} to /tmp (jkeating)
- Use shutil.move for replacing old config with the new one (vpodzime)
- Honor user's choice on NTP (ON/OFF) (vpodzime)
- Don't crash if someone gives us bad timezone (vpodzime)
- Use expand_langs to find matching language (LanguageSpoke) (vpodzime)
- Move expandLangs to localization module (vpodzime)
- Use Gtk.main_level() to check if main loop is already running (vpodzime)
- Move setup from ImagePayload to LiveImagePayload. (clumens)
- Avoid duplicates in the packages property. (clumens)
- Set a progress message when liveinst starts installing software. (clumens)
- Fix default definitions of some payload class methods. (clumens)
- Add a spaceRequired property for LiveImagePayload. (clumens)
- getDirSize should stay on a single filesystem, not look at submounts.
  (clumens)
- Don't look for existing installations on live devices. (clumens)
- We don't need image_file in the live payload. (clumens)
- Now that we're using rsync, the livecd and rootfs do not have to match.
  (clumens)
- Disable software selection and source spokes on live installs. (clumens)
- Fix args to LiveImagePayload.setup (#852272). (clumens)
- require anaconda-widgets (bcl)
- Handle already mounted optical devices (#851274) (jkeating)
- Return full device object of selected optical drive (jkeating)
- Add a method to determine if device is mounted (jkeating)
- anaconda-cleanup: fix DeviceTree args (bcl)
- Unset install_device if repo setup fails (jkeating)
- _peopleRepositoriesFilter -> _peopleRepositoriesFilterEntry (#852182).
  (clumens)
- on_*_changed callbacks take one argument, not two. (clumens)
- Use the correct icon size constant. (clumens)
- remove dead code (setMethodstr, expandFTPMethod) (wwoods)
- parse-kickstart: update some TODO comments (wwoods)
- parse-kickstart: simplify logging (wwoods)
- enable fastestmirror yum plugin (#849797) (bcl)
- networking: remove Network() object (rvykydal)
- networking: use ksdata.network.hostname instead of actual installer hostname
  (rvykydal)
- networking: consolidate writing/copying of configuration files (rvykydal)
- networking: 70-persistent-net.rules doesn't exist anymore. (rvykydal)
- networking: disable ipv6 directly in installed system config file (rvykydal)
- networking: mirror end-of-installation network config tweaks in ksdata.
  (rvykydal)
- networking: write configuration in doInstall (rvykydal)
- Add mounts before swaps so the default selection is a mount. (dlehman)
- Use MB if a new mountpoint size does not include a unit spec. (#850839)
  (dlehman)
- Correctly handle partitions with sizes smaller than 500MB. (#850839)
  (dlehman)
- Don't include removed devices in Storage.unusedDevices. (dlehman)
- Handle SameSizeSet growth trimming when all members are too large. (dlehman)
- Add several missing yum lock aqcuisitions. (#851212) (dlehman)
- Offer completions for new mountpoints. (dlehman)
- Add old_source checking for closest mirror and url methods too (#851336).
  (clumens)
- Revert "Only use mounted media that has repodata" (jkeating)
- Only use mounted media that has repodata (jkeating)
- _bootloaderClass -> bootloaderClass for some platforms (#848173). (clumens)
- Make the storage info bar clickable to reveal error messages. (clumens)
- Move the software-specific error message out of the DetailedErrorDialog
  class. (clumens)
- Add a gui password spoke (jkeating)
- Put traceback reports on a diet. (clumens)

* Wed Aug 22 2012 Chris Lumens <clumens@redhat.com> - 18.7-1
- Do another _main_window -> main_window change. (clumens)
- Mark the storage category title for translation. (clumens)
- _actions should be set up in the __init__ method. (clumens)
- Don't require hfs-tools on RHEL (#849987). (clumens)
- dracut: remove workarounds for broken splitsep() (wwoods)
- dracut: update Requires: in spec (wwoods)
- Use ksdata.timezone and timezone module instead of anaconda.timezone
  (vpodzime)
- Remove the last usage of the system-config-date in Anaconda (vpodzime)
- Add support for swap --hibernation on LVM (vpodzime)
- Don't rely on selection staying selected when doing crazy things to it
  (vpodzime)
- Replace nonexisting icon with an existing one (DatetimeSpoke) (vpodzime)
- integer out of range for L format code (hamzy)
- Network spoke: use chr() instead of str() to convert dbus.Byte (#849395)
  (rvykydal)
- verify package checksums against metadata (bcl)
- use F18_PartData for hibernation flag support. (bcl)
- fix Gtk import in software.py (bcl)
- dracut: fix rd.neednet use in parse-kickstart (#849672) (wwoods)
- parse-anaconda-net: Add missing semicolon for dhclient.conf (bcl)
- anaconda-modprobe: fix .ko removal (bcl)
- Only devices that already exist may be ISO install sources (#849482).
  (clumens)
- Use python-meh's MainExceptionWindow's main_window property (vpodzime)
- dracut: fix syntax error in parse-kickstart (wwoods)
- Show fstype as "Unknown" for devices with unrecognised formatting. (dlehman)
- BTRFS magic for custom spoke. (dlehman)
- The device type of preexisting devices cannot be changed. (dlehman)
- Revert old hack that disabled btrfs in the old ui. (dlehman)
- Use correct device instance when updating selector w/ new device. (dlehman)
- Fix a traceback when clicking on the summary in custom spoke. (dlehman)
- Move device size calculation and setting into DeviceFactory. (dlehman)
- Stop pretending btrfs subvols can have a size. (dlehman)
- Fix a typo in StorageDevice._setSize. (dlehman)
- dracut: add info about special variables to README (wwoods)
- dracut: fix invalid use of 'eth0' (wwoods)
- dracut: drop upgrade-specific hack (wwoods)
- dracut: set "$netif" correctly in initqueue/online scripts (wwoods)
- dracut: fix old-style static ip=xxx gw=yyy... (wwoods)
- dracut: import anaconda-lib.sh in pre-udev hook (wwoods)
- dracut: fix set_neednet so network comes up (#849672) (wwoods)
- dracut: drop save_netinfo (wwoods)
- move anaconda-modprobe to pre-udev hook, silence modprobe errors (wwoods)
- parse-kickstart: fix crash with PXE + ks=file: (#844478) (wwoods)
- parse-kickstart: clarify/refactor Network handling (wwoods)
- Actually create default ifcfg files (#849012) (rvykydal)
- Don't fail on write of nonexisting IfcfgFile(SimpleConfigFile) (#849012,
  #849095) (rvykydal)
- If dracut left the DVD mounted, don't try to remount it (#849152). (clumens)
- Add support for most device editing functions. (dlehman)
- Various fixes, cleanups, and added logging for the custom spoke. (dlehman)
- Work around some signal handling issues in the custom spoke. (dlehman)
- Make choosing an auto-selected page after refresh slightly less fallible.
  (dlehman)
- Raise an exception if a new device ends up with size 0. (dlehman)
- Split out logic to determine container based on factory and/or device.
  (dlehman)
- Allow adding disks to a container's disk set. (dlehman)
- Allow passing a device into newDevice for adjustment. (dlehman)
- Add PartitionFactory class so partitions don't need a separate code path.
  (dlehman)
- Add a convenience method for scheduling resize actions. (dlehman)
- Return early from doKickstartStorage if there are no disks selected.
  (dlehman)
- Remove isomd5sum-static from build requires (vpodzime)
- Don't rely on having some network devices available (vpodzime)
- Enlightbox mainExceptionWindow (vpodzime)
- Put mainExceptionWindow in a WindowGroup (vpodzime)
- Bump required yum version to get the environment code. (notting)
- Add a flag so we don't get spurious 'change' events from the treeview while
  we're setting up the UI. (notting)
- Wire in the new environment logic through the UI. (notting)
- Add a local method for exposing group visibility from the comps file.
  (notting)
- Add methods to yumpayload for handling environments. (notting)
- Add some nicer wording to the column heads in the software selection UI.
  (notting)
- Rename 'description' to 'groupDescription'. (notting)
- dracut: add README (wwoods)

* Thu Aug 16 2012 Chris Lumens <clumens@redhat.com> - 18.6-1
- Remove linuxrc.s390 (dcantrell)
- Source in url-lib.sh if we don't have it (#847831) (jkeating)
- parse-kickstart: add proc_cmdline (fix init_logger()) (wwoods)
- Remove the data/bootdisk directory tree. (clumens)
- Remove duplicate boot disk setting code (#848841). (clumens)
- Force authconfig to be installed on the target system (#848803). (clumens)

* Wed Aug 15 2012 Chris Lumens <clumens@redhat.com> - 18.5-1
- Mark/unmark some strings for translation, as appropriate. (clumens)
- Save the distro label into the right variable for retranslation. (clumens)
- Add custom widget files to POTFILES.in. (clumens)
- Fix attribution on common UI code. (clumens)
- don't set armMachine in class definition (bcl)
- libudev now has a version of .1 (hamzy)
- Load anaconda-lib.sh if necessary (jkeating)
- Use shell code to work around missing basename (jkeating)
- Enable text mode once again! (jkeating)
- Update text prompt to include c for continue (jkeating)
- Don't continue if incomplete spokes exist (jkeating)
- Return a bool for timezone completed property (jkeating)
- Add a text progress hub to do the install (jkeating)
- text based storage spoke. (jkeating)
- Allow updating tmux.conf via makeupdates. (clumens)
- Prevent yum messages from showing on tty (jkeating)
- Remove unused imports from the installclasses. (clumens)
- NoSuchGroup is provided by packaging now.  yuminstall is on the way out.
  (clumens)
- Set transaction color in case of multilib install. (clumens)
- Add selinux-specific RPM macro setup. (clumens)
- Add the user-agent to urlgrabber from the old yuminstall.py. (clumens)
- Fix inheritance problems with the gui *Spoke classes. (clumens)
- Only setup python-meh when doing graphical installs (jkeating)
- Call the correct method to schedule the screen (jkeating)
- Add a missing import of os (jkeating)
- Don't display indirect spokes in the hub (jkeating)
- Revert "Remove unncessary __init__ definition. (clumens)" (jkeating)
- Honor displayMode from kickstart files (jkeating)
- Merge master into newtui (jkeating)
- Remove the base_tests file for now (jkeating)
- Remove unused import of UIObject (jkeating)
- Fix up detailederror for new common UI code (jkeating)
- Translate the base text hub class (jkeating)
- Translate the base tui class strings (jkeating)
- Remove unncessary __init__ definition. (clumens) (jkeating)
- Translate some strings in the base tui spokes classes (jkeating)
- Always use collect directly from common (jkeating)
- Add comment headers to the new files (jkeating)
- Ad source files to POTFILES.in (msivak)
- Merge remote-tracking branch 'origin/master' into newtui (msivak)
- import localization stuff and use it to translate more strings (msivak)
- finish renaming _mainloop (msivak)
- Fix naming for data attribute and move the NormalSpoke.__init__ under the
  proper class (msivak)
- Improve documentation and add licensing headers (msivak)
- Add translations to the simpleline framework (msivak)
- Add translations to Password Spoke (msivak)
- Add elementary timezone spoke (msivak)
- Pass screen args argument to prompt and input methods + fix for run-text-
  spoke (msivak)
- Merge master into newtui (msivak)
- Add automake files for TUI (msivak)
- add couple of tests and fix write method of widget (newline added unwanted
  space) (msivak)
- add couple of tests and support for them (msivak)
- add documentation and comments to TUI classes (msivak)
- Add documentation to the simpleline library for TUI (msivak)
- Add the new Summary hub and Password TUI spokes + tools to test TUI stuff
  (msivak)
- Fix bits and pieces to make TUI hub and spoke model work + example Hub and
  Password spoke (msivak)
- Create common abstract classes usable for all types of UI (msivak)
- Create the base classes for TUI Hub and Spoke model (msivak)
- Make collect and part of UserInterface setup more generic (msivak)
- Text based UI framework core (msivak)

* Mon Aug 13 2012 Chris Lumens <clumens@redhat.com> - 18.4-1
- dracut: fix inst.ks.sendmac (#826657) (wwoods)
- dracut: suppress ks errors from missing %%include (wwoods)
- dracut: add comment to run_kickstart() (wwoods)
- Remove unused writeKS methods. (clumens)
- Only show unused devices that haven't been removed/deleted. (dlehman)
- Don't unexpand already-expanded pages when trying to expand them again.
  (dlehman)
- Make parents of hidden devices appear to be leaves. (dlehman)
- Remove the right device name from the lvm filter when unhiding device.
  (dlehman)
- Take configured filesystems into account when checking package space.
  (dlehman)
- Make sure the ksdata autopart type matches the storage one. (dlehman)
- Base auto-generated name prefixes on productName, not device type. (dlehman)
- Remove shrink code that was a workaround for the old ui flow. (dlehman)
- Remove old ui progress args from devicelibs.btrfs. (dlehman)
- Make sure we allocate partitions and grow lvm as needed in kickstart.
  (dlehman)
- Streamline autopart request setup slightly. (dlehman)
- Make it possible to call setUpBootLoader safely at any time. (dlehman)
- Move setup of new partition weight arg to Storage.newPartition. (dlehman)
- Use a copy of the main Storage instance during custom partitioning. (dlehman)
- Track requested sizes of btrfs subvols. (dlehman)
- Add a method to retrieve a devicetree device by id number. (dlehman)
- Fix DiskLabel so it can be deep-copied. (dlehman)
- Add a method to produce a deep copy of a Storage instance. (dlehman)
- Fix subtraction for Size. (dlehman)
- Add support for creating device based on a top-down specification. (dlehman)
- Add size-set managers to keep a set of growable requests in sync. (dlehman)
- Add a function to estimate required disk space for an md array. (dlehman)
- Add a method to estimate disk space needs for a new logical volume. (dlehman)
- Add a convenience method for new btrfs subvols and drop subvol size args.
  (dlehman)
- Use the UEFI shim to load grub. (pjones)
- Check that Gtk.main is not already running before starting another one
  (vpodzime)
- With tmux, we no longer need to start up a shell during VNC installs.
  (clumens)
- We no longer need getkeymaps, mapshdr, or readmap. (clumens)
- Remove the last references to isysLoadKeymap. (clumens)
- remove Security class (bcl)
- replace lokkit for selinux settings (#815540) (bcl)
- tests: Add tests for new SimpleConfigFile features (bcl)
- tests: cleanup whitespace in simpleconfig_test.py (bcl)
- simpleconfig: rewrite to better support commented config files (bcl)
- If the anaconda process crashes, don't delete its window. (clumens)
- On interactive installs, default the root account to locked. (clumens)
- Make the keyboard layout test a big text area instead of a single line.
  (clumens)
- Remove our loadKeymap code from isys (vpodzime)
- Replace system-config-keyboard with our methods using ksdata.keyboard
  (vpodzime)
- A little fix of newui -> master merge (iscsi offload devices) (rvykydal)
- Require new version of python-meh (vpodzime)
- Modify kernelPackages to select the right kernel for ARM systems. (dmarlin)
- ARM: clean up the kernel selection to be consistent with the rest of the code
  (dennis)
- add command line option to set the arm platform. (dennis)
- Add support to determine the ARM processor variety and select the correct
  kernel to install. (dmarlin)
- TODO list updates. (clumens)
- Sent pot file updates to the master branch in transifex, not f17. (clumens)

* Fri Aug 03 2012 Chris Lumens <clumens@redhat.com> - 18.3-1
- New graphical user interface.
- Removed loader.

* Wed Apr 18 2012 Brian C. Lane <bcl@redhat.com> - 18.2-1
- Fixes from F17 branch
