%define major 1
%define libname %mklibname NetworkManagerQt %{major}
%define devname %mklibname -d NetworkManagerQt
%define debug_package %{nil}

%define rname networkmanager-qt

Summary:	Qt-only wrapper for NetworkManager DBus API
Name:		libnm-qt
Version:	0.9.8.4
Release:	2
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libnm-qt
Source0:	http://download.kde.org/unstable/networkmanager-qt/%{version}/src/%{rname}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8.4
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)

%description
Qt library for NetworkManager.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt-only wrapper for NetworkManager DBus API
Group:		System/Libraries
Conflicts:	%{_lib}nm-qt0 < 1:0.9.8.3
Obsoletes:	%{_lib}nm-qt0 < 1:0.9.8.3

%description -n %{libname}
Qt library for NetworkManager.

%files -n %{libname}
%{_libdir}/libNetworkManagerQt.so.%{version}
%{_libdir}/libNetworkManagerQt.so.%{major}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Conflicts:	%{_lib}nm-qt-devel < 1:0.9.8.1
Obsoletes:	%{_lib}nm-qt-devel < 1:0.9.8.1

%description -n %{devname}
Qt libraries and header files for developing applications
that use NetworkManager.

%files -n %{devname}
%{_libdir}/pkgconfig/NetworkManagerQt.pc
%{_libdir}/libNetworkManagerQt.so
%{_includedir}/NetworkManagerQt/

#----------------------------------------------------------------------------

%prep
%setup -qn %{rname}-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

