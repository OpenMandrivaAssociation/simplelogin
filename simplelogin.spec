%define date 20200825

Name:		simplelogin
Version:	0.0
Release:	%{?date:0.%{date}.}1
Source0:	https://invent.kde.org/davidedmundson/simplelogin/-/archive/master/simplelogin-master.tar.bz2
Patch0:		simplelogin-20200818-pam-session.patch
Patch1:		simplelogin-omvconfig.patch
License:	GPLv2+
Summary:	Simple autologin manager without a UI
Group:		Embedded
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(systemd)
BuildRequires:	ninja

%description
Simplelogin is an autologin-only login manager, a display manager
without the display.

It is meant primarily as a lightweight sddm replacement for
embedded devices that have only one user.

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
# Drop kwinwrapper, we get it from plasma-phone-components now
rm -f %{buildroot}%{_bindir}/kwinwrapper

%files
%{_bindir}/simplelogin
/lib/systemd/system/simplelogin.service
%{_sysconfdir}/init
%{_sysconfdir}/pam.d/simplelogin
