%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo 0%{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	KDE Library for integration with the Wayland display server
Name: 		plasma-wayland-protocols
Version:	1.5.0
Release: 	1
Source0: 	http://download.kde.org/%{stable}/plasma-wayland-protocols/%{name}-%{version}.tar.xz
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildArch:	noarch

%description
KDE Library for integration with the Wayland display server.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_libdir}/cmake/PlasmaWaylandProtocols
%{_datadir}/plasma-wayland-protocols
