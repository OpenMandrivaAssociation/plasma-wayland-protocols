%undefine _debugsource_packages
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo 0%{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20231130

Summary: 	KDE Library for integration with the Wayland display server
Name: 		plasma-wayland-protocols
Version:	1.16.0
Release: 	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/plasma-wayland-protocols/-/archive/master/plasma-wayland-protocols-master.tar.bz2#/plasma-wayland-protocols-%{git}.tar.bz2
%else
Source0: 	http://download.kde.org/%{stable}/plasma-wayland-protocols/%{name}-%{version}.tar.xz
%endif
Url: 		https://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildArch:	noarch

%description
KDE Library for integration with the Wayland display server.

%files
%{_libdir}/cmake/PlasmaWaylandProtocols
%{_datadir}/plasma-wayland-protocols
